# LLM Visualizer

The LLM Visualizer is a Python tool designed to create graphical representations of scientific experiments. It extracts data from PDFs of experimental studies and generates visual summaries of the data. The project aims to simplify the interpretation of scientific results and integrate visual analytics into machine learning workflows.

## Features

- Extracts JSON data from PDFs of experimental studies.
- Creates clear and informative visualizations representing the experimental data.
- Intended for integration with machine learning models to automate the extraction and visualization process.

## Background

NASA Ames Research Center, in collaboration with the Open Data Science community, has been at the forefront of applying machine learning to extract meaningful insights from vast amounts of research data. The LLM Visualizer is a contribution to this endeavor, promising to streamline the process of data to decision-making in research environments.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.6 or higher
- PIL (Python Imaging Library)
- Additional Python libraries as required by the project

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Harlan-Phillips/LLM-Visualizer.git

Install the required packages:
pip install -r requirements.txt

python -m streamlit run <filename.py>
```
### Usage

After setting up the project, you can run the script visualizer.py to start generating visualizations from your data.
```
from visualizer import create_visualization

# Example data input
data = { ... }

create_visualization(data)
```
Link to streamlit app: https://llm-visualizer.streamlit.app/
## Demo

![Video Demo](assets/NBISCProj2.gif)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## Contact
Harlan Phillips - https://www.linkedin.com/in/harlan-phillips-950190236/

Project Link: https://github.com/Harlan-Phillips/LLM-Visualizer

## Acknowledgements
Dr. Walter Alverado
