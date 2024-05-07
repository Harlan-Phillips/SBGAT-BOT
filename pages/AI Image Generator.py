import streamlit as st
from aiGenerator import generate_df
from imageAI import generate_images

st.set_page_config(
    page_title="LLM Interpreter",
    page_icon="🤖",
)

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


set_background_image('https://imgur.com/7RfzRz4.jpg')
    
# Example of using inline styling for semi-transparent background on a specific text block
apply_custom_styles()

st.title("Welcome to your AI Visualizer!")
experiment_title = st.text_input('Experiment Title:', key='experiment_title')
st.markdown("Please enter the experiemnt's info to get started and generate your graphical abstract!")

user_input = st.text_area("Enter your text here:", height=300)

if st.button('Generate Image'):
    df = generate_df(user_input)
    st.dataframe(df)
    group_data = []
    if df is not None:
        strain = df.iloc[1]['Strain of Subjects']
        for index, row in df.iterrows():
            group_info = {
                'group': row['Group Name'],
                'beam': row['Beam Type'],
                'grey': row['Total Absorbed Dose per Particle Type'],
                'duration': row['Time Point of Sacrifice Post-Irradiation'],
                'gender': row['Sex of Subjects'],
                'units': row['Total Absorbed Dose Units']
            }
            group_data.append(group_info)
        for group in group_data:
            if group['grey'] != 'N/A':
                group['grey'] = float(group['grey'])
            elif group['grey'] == 'N/A':
                group['grey'] = 0.0
        image_path = generate_images(group_data, strain, experiment_title)
        st.image(image_path, caption='Generated Image')

