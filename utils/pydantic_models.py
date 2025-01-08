"""
This module defines Pydantic models for structured outputs related to medical questions, triage urgency, and differential diagnosis.
Classes:
    AdditionalQuestions: A Pydantic model representing additional medical questions to ask the user based on their input.
    TriageUrgency: A Pydantic model representing the urgency of a medical case using The Manchester Triage Scale (MTS).
    DifferentialDiagnosis: A Pydantic model representing the differential diagnosis based on the user's input.
These models are used to ensure that the data related to medical questions, triage urgency, and differential diagnosis is structured and validated according to the specified fields and their constraints.
"""
from pydantic import BaseModel, Field

class AdditionalQuestions(BaseModel):
    """Medical questions to ask user based on input."""
    is_related_to_medical : bool = Field(..., title="Is Related to Medical", description="Whether the question is related to medical symptoms or not.")

    question_1 : str = Field(..., title="Question 1", description="The first most important medical question to ask to the user.")
    output_type_1 : str = Field(..., title="Output Type 1", description="The type of the output of the first question.")

    question_2 : str = Field(..., title="Question 2", description="The second most important medical question to ask to the user.")
    output_type_2 : str = Field(..., title="Output Type 2", description="The type of the output of the second question.")

    question_3 : str = Field(..., title="Question 3", description="The third most important medical question to ask to the user.")
    output_type_3 : str = Field(..., title="Output Type 3", description="The type of the output of the third question.")

    question_4 : str = Field(..., title="Question 4", description="The fourth most important medical question to ask to the user.")
    output_type_4 : str = Field(..., title="Output Type 4", description="The type of the output of the fourth question.")

    question_5 : str = Field(..., title="Question 5", description="The fifth most important medical question to ask to the user.")
    output_type_5 : str = Field(..., title="Output Type 5", description="The type of the output of the fifth question.")

    question_6 : str = Field(..., title="Question 6", description="The sixth most important medical question to ask to the user.")
    output_type_6 : str = Field(..., title="Output Type 6", description="The type of the output of the sixth question.")

    question_7 : str = Field(..., title="Question 7", description="The seventh most important medical question to ask to the user.")
    output_type_7 : str = Field(..., title="Output Type 7", description="The type of the output of the seventh question.")

    question_8 : str = Field(..., title="Question 8", description="The eighth most important medical question to ask to the user.")
    output_type_8 : str = Field(..., title="Output Type 8", description="The type of the output of the eighth question.")

    question_9 : str = Field(..., title="Question 9", description="The ninth most important medical question to ask to the user.")
    output_type_9 : str = Field(..., title="Output Type 9", description="The type of the output of the ninth question.")

    question_10 : str = Field(..., title="Question 10", description="The tenth most important medical question to ask to the user.")
    output_type_10 : str = Field(..., title="Output Type 10", description="The type of the output of the tenth question.")

class TriageUrgency(BaseModel):
    """Triage information based on input."""
    urgency : int = Field(..., title="Urgency", description="The urgency of the case using The Manchester Triage Scale (MTS).")

class DifferentialDiagnosis(BaseModel):
    """Differential diagnosis based on input."""
    disease_1 : str = Field(..., title="Disease 1", description="The most likely disease based on the input.")
    likelihood_1 : int = Field(..., title="Likelihood 1", description="The likelihood of the most likely disease.")  

    disease_2 : str = Field(..., title="Disease 2", description="The second most likely disease based on the input.")
    likelihood_2 : int = Field(..., title="Likelihood 2", description="The likelihood of the second most likely disease.")

    disease_3 : str = Field(..., title="Disease 3", description="The third most likely disease based on the input.")
    likelihood_3 : int = Field(..., title="Likelihood 3", description="The likelihood of the third most likely disease.")

    disease_4 : str = Field(..., title="Disease 4", description="The fourth most likely disease based on the input.")
    likelihood_4 : int = Field(..., title="Likelihood 4", description="The likelihood of the fourth most likely disease.")

    disease_5 : str = Field(..., title="Disease 5", description="The fifth most likely disease based on the input.")
    likelihood_5 : int = Field(..., title="Likelihood 5", description="The likelihood of the fifth most likely disease.")

    disease_6 : str = Field(..., title="Disease 6", description="The sixth most likely disease based on the input.")
    likelihood_6 : int = Field(..., title="Likelihood 6", description="The likelihood of the sixth most likely disease.")

    disease_7 : str = Field(..., title="Disease 7", description="The seventh most likely disease based on the input.")
    likelihood_7 : int = Field(..., title="Likelihood 7", description="The likelihood of the seventh most likely disease.")

    disease_8 : str = Field(..., title="Disease 8", description="The eighth most likely disease based on the input.")
    likelihood_8 : int = Field(..., title="Likelihood 8", description="The likelihood of the eighth most likely disease.")

    disease_9 : str = Field(..., title="Disease 9", description="The ninth most likely disease based on the input.")
    likelihood_9 : int = Field(..., title="Likelihood 9", description="The likelihood of the ninth most likely disease.")

    disease_10 : str = Field(..., title="Disease 10", description="The tenth most likely disease based on the input.")
    likelihood_10 : int = Field(..., title="Likelihood 10", description="The likelihood of the tenth most likely disease.")