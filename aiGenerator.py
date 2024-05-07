import json
from typing import List, Optional, Union
from langchain_openai import ChatOpenAI
import pandas as pd

def generate_df(info):
    def generate_json(study):
        model = ChatOpenAI(api_key='you-api-key', temperature=0)
        ans = ''
        with open('Example.txt') as f:
            ans = f.read()
        context_example = ''
        with open('Context.txt') as f:
            context_example = f.read()

        prompt_text = f"""
        Example 1.
        Context: {context_example}
        Question: Given the detailed description of a scientific study on the effects of radiation and specific treatments in mice, systematically extract and list the following information for each defined group in the study:
        - Group name
        - Beam Type
        - Number of subjects
        - Total absorbed dose per particle type
        - Total absorbed dose units
        - Time point of sacrifice post-irradiation
        - Sex of subjects
        - Strain of subjects (something like: C57BL/6)

        Ensure each group from the study is represented as a separate entry in a list format. If information is not explicitly mentioned for any group, note it as 'N/A'. Convert to json
        Answer: {ans}

        Context: {study}
        Question: Given the detailed description of a scientific study on the effects of radiation and specific treatments in mice, systematically extract and list the following information for each defined group in the study:
        - Group name
        - Beam Type
        - Number of subjects
        - Total absorbed dose per particle type
        - Total absorbed dose units
        - Time point of sacrifice post-irradiation
        - Sex of subjects
        - Strain of subjects (something like: C57BL/6)

        Ensure each group from the study is represented as a separate entry in a list format. If information is not explicitly mentioned for any group, note it as 'N/A'. Convert to Json
        Answer:
        """

        response = model.invoke(prompt_text)
        return response.json()


    
    json_data = generate_json(info)

    print(json_data)
    json_dict = json.loads(json_data)
    # Now extract content assuming json_dict is properly parsed and structured
    data = json.loads(json_dict['content'])  # Parse the 'content' string into an actual JSON object
    df = pd.DataFrame(data)
    return df