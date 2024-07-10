# SBGAT-BOT

The SBGAT-BOT is a Python tool designed to create graphical representations of scientific experiments. It extracts data from PDFs of experimental studies and generates visual summaries of the data. The project aims to simplify the interpretation of scientific results and integrate visual analytics into machine learning workflows.

## Features

- Extracts JSON data from PDFs of experimental studies.
- Creates clear and informative visualizations representing the experimental data.
- Intended for integration with machine learning models to automate the extraction and visualization process.

## Background

NASA Ames Research Center, in collaboration with the Open Data Science community, has been at the forefront of applying machine learning to extract meaningful insights from vast amounts of research data. The SBGAT-BOT is a contribution to this endeavor, promising to streamline the process of data to decision-making in research environments.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.6 or higher
- PIL (Python Imaging Library)
- Additional Python libraries as required by the project

### Installation
```bash
# Clone the repository:
git clone https://github.com/Harlan-Phillips/LLM-Visualizer.git

# Change directory to project folder
cd SBGAT-BOT

# Install the required packages:
pip install -r requirements.txt

# Run the App
python -m streamlit run Visualizer.py

```

### Usage

After setting up the project, you can visit the web app and utilize two functionalities:

1. **Tabular Input:**
   - Upload an Excel file and click "Generate Image" to create a visual representation of the data.

2. **Manual Input:**
   - Enter the data manually into the provided fields to generate the visualization.

**Note:** The AI Image Generation tab cannot be used on the public site due to API key restrictions. To use this functionality, follow these steps:

1. Clone the repository and change the API key in `aiGenerator.py` to your own GPT-3.5 API key.
2. Install the required packages and run the Streamlit application as described above.
3. Access the AI page and input text from PDFs to generate a graphical abstract.

Link to streamlit app: https://sbgat-bot.streamlit.app/

## Demo

![Video Demo](assets/NBISCProj2.gif)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## Contact
Harlan Phillips - https://www.linkedin.com/in/harlan-phillips-950190236/

Project Link: https://github.com/Harlan-Phillips/LLM-Visualizer

## Acknowledgements
Dr. Walter Alverado
