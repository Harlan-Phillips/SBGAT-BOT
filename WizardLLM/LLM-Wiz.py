from typing import List, Optional, Union
from pydantic import BaseModel, Field, validator
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

class RadiationGroup(BaseModel):
    group: str = Field(description="Name of the radiation group")
    right: int = Field(description="Number of subjects for experimental group")
    grey: Optional[float] = Field(description="Total Absorbed Dose per Particle Type")
    duration: Optional[Union[int, List[int]]] = Field(default=None, description="Time Point of Sacrifice Post-Irradiation in weeks")
    gender: str = Field(description="Sex of the Subjects")
    units: str = Field(description="Total Absorbed Dose Units")
    strain: str = Field(description="Strain of the Subjects")

    @validator('duration', pre=True, always=True)
    def parse_duration(cls, v):
        if isinstance(v, str) and v == "Not Specified":
            return None
        if isinstance(v, list):
            return v[0] if v else None
        return v

class RadiationGroups(BaseModel):
    groups: List[RadiationGroup]

# Initialize the LLM model (Ollama)
model = Ollama(model="wizardlm2:7b", temperature=0)


parser = PydanticOutputParser(pydantic_object=RadiationGroups)

study = input("Paste text here: ")

prompt_text = f"""
{study}
Given the detailed description of a scientific study on the effects of radiation and specific treatments in mice, systematically extract and list the following information for each defined group in the study:
- Group name
- Number of subjects
- Total absorbed dose per particle type
- Total absorbed dose units
- Time point of sacrifice post-irradiation
- Sex of subjects
- Strain of subjects

Ensure each group from the study is represented as a separate entry in a list format. If information is not explicitly mentioned for any group, note it as 'Not Specified'.
"""

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

response = chain.invoke({"query": prompt_text})

print(response.json()) 
