import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from image import generate_image
from imageN import generate_images



col1, col2 = st.columns([5, 1])  # Adjust the ratio as needed
with col2:
    st.image('icon_folder/nbisc_logo.png', width=100)


def set_background_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, .55), rgba(0, 0, 0, .55)), url({url});
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* Targeting the HTML elements directly for demonstration */
        h1, .title {
            color: #ffffff; /* White text color */
            text-shadow: 0 0 10px #00a1ff, 0 0 20px #00a1ff, 0 0 30px #00a1f7; /* Light Blue glow */
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )

def process_excel(uploaded_file):
    df = pd.read_excel(uploaded_file)
    # Define the columns of interest with exact names
    columns_of_interest = [
        'Radiation beam type  (Acute)', 
        'Number of subjects for experimental group',
        'Total absorbed dose per particle type  (Acute)', 
        'Total absorbed dose units  (Acute)',
        '****Time point of sacrifice post-irradiation',
        'Sex',
        'Strain',
        'PI Institution',
        'PI name'
    ]

    # Filter DataFrame based on columns of interest
    df_filtered = df[columns_of_interest]

    # Clean column names to ensure they match expected values
    df_filtered.columns = df_filtered.columns.str.strip()

    # Use .loc to avoid SettingWithCopyWarning and ensure correct data types
    df_filtered.loc[:, 'Number of subjects for experimental group'] = df_filtered['Number of subjects for experimental group'].astype(int)

    # Group by 'Radiation beam type (Acute)' and select the top two groups based on 'Number of subjects for experimental group'
    top_groups = df_filtered.groupby('Radiation beam type  (Acute)').apply(
        lambda x: x.nlargest(2, 'Number of subjects for experimental group')
    ).reset_index(drop=True)
    return top_groups

with col1:
    
    set_background_image('https://imgur.com/7RfzRz4.jpg')
    
    # Example of using inline styling for semi-transparent background on a specific text block
    apply_custom_styles()
    
    st.title("Welcome to NBISC Visualizer!")
    st.markdown("Please enter info to get started and generate your graphical abstract!")
    # ... Insert the rest of your content that should be inside the semi-transparent box here ...
    bool_form = st.sidebar.selectbox(
    'Do you have an excel datasheet of the experiment?',
    options=[True, False],
    index=0  
    )
    if bool_form:
        uploaded_file = st.file_uploader("Upload Excel Sheet", type=['xlsx'])
        experiment_title = st.text_input('Experiment Title:', key='experiment_title')
        if uploaded_file is not None:
            # Read the uploaded Excel file
            top_groups = process_excel(uploaded_file)
            st.write("Top Groups by Radiation Beam Type:")
            st.dataframe(top_groups)
        
            group_data = []
            if top_groups is not None:  # Ensure top_groups is not empty
                strain = top_groups.iloc[0]['Strain']
                institution = top_groups.iloc[0]['PI Institution']
                pi_name = top_groups.iloc[0]['PI name']
                for index, row in top_groups.iterrows():
                    group_info = {
                        'group': row['Radiation beam type  (Acute)'],
                        'left': 0,  # Assuming 0 is a placeholder
                        'right': row['Number of subjects for experimental group'],
                        'grey': row['Total absorbed dose per particle type  (Acute)'],
                        'duration': row['****Time point of sacrifice post-irradiation'],
                        'gender': row['Sex'],
                        'units': row['Total absorbed dose units  (Acute)']
                    }
                    group_data.append(group_info)

        if st.button('Generate Image'):
            # Cast types as necessary within the group processing
            total_mice = 0
            for group in group_data:
                group['left'] = int(group['left'])
                group['right'] = int(group['right'])
                group['grey'] = float(group['grey'])
                group['duration'] = int(group['duration'])
                total_mice += group['right']

            print(group_data)
            image_path = generate_images(group_data, total_mice, strain, experiment_title, institution, pi_name)
            st.image(image_path, caption='Generated Image')
        
    else:
        animal_type = st.sidebar.selectbox(
        'What species are your subjects?',
        options=['mice', 'pig'],
        index=0  
        )
        
        experiment_location = st.sidebar.selectbox(
            'Where were the subjects irradiated?',
            options=['Lawrence Berkeley National Laboratory', 'Other'],
            index=0  
        )
    
        number_of_groups = st.sidebar.selectbox(
            'How many groups do you have?',
            options=['1', '2', '3', '4', '5', '6'],
            index=0  
        )
        
        number_of_groups = int(number_of_groups)
        
        experiment_title = st.text_input('Experiment Title:', key='experiment_title')
        
        group_data = []
        for i in range(number_of_groups):
            st.text(f'Group {i+1} Info')
            group_info = {
                'group': st.text_input(f'Group Number:', key=f'group_{i+1}_number'),
                'beam': st.text_input(f'Beam Element', key=f'group_{i+1}_beam'),
                'left': st.text_input(f'Subject # Start', key=f'group_{i+1}_min'),
                'right': st.text_input(f'Subject # End', key=f'group_{i+1}_max'),
                'grey': st.text_input(f'Dose of Group (cGy)', key=f'group_{i+1}_grey'),
                'duration': st.text_input(f'Duration of Group (weeks)', key=f'group_{i+1}_duration')
            }
            group_data.append(group_info)
        
            st.text(' ')
            
        if st.button('Generate Image'):
            for group in group_data:
                group['left'] = int(group['left'])
                group['beam'] = f"{group['beam']}"
                group['right'] = int(group['right'])
                group['grey'] = float(group['grey'])
                group['duration'] = f"{group['duration']} weeks"
        
        
            image_path = generate_image(group_data, animal_type, experiment_title)
            st.image(image_path, caption='Generated Image')
