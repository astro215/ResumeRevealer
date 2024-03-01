from typing import List, Dict, Union
from langchain_core.pydantic_v1 import BaseModel, Field


class ResumeStructure(BaseModel):
    education: List[Dict[str, str]] = Field(description="List of dictionaries containing 'university' and 'CGPA'")
    work: List[Dict[str, Union[str, List[str]]]] = Field(description="List of dictionaries containing "
                                                                     "'organization', 'location', 'position', "
                                                                     "'duration', 'standardized_job_title', "
                                                                     "and 'predicted_skills'")
    projects: List[Dict[str, Union[str, List[str]]]] = Field(description="List of dictionaries containing "
                                                                         "'project_name', 'start_date', 'end_date', "
                                                                         "'description', and 'predicted_skills'")
    skills: Dict[str, List[str]] = Field(description="Dictionary containing 'technical' and 'non_technical' skills")
    career_trajectory: str = Field(description="String representing the career progression of the candidate")
