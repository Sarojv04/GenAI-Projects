from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated, Optional, Literal
from pydantic import BaseModel, Field 

load_dotenv()

model = ChatOpenAI()

#Schema for data format

class Review(BaseModel):
    key_themes : list[str] = Field(description ="write down main key themes discussed in the review")
    summary : str = Field (description = "A brief summary of the review ")
    sentiment : Literal["Pos","Neg", "Nul"] = Field(description = "Return sentimemt of the review either negative positive or neutral")
    pros : Optional[list[str]]= Field(description ="write down all the pros inside the review", default=None)
    cons : Optional[list[str]] = Field(description ="write down all the cons mentioned in the review",default=None)


structure_model_data = model.with_structured_output(Review)

result = structure_model_data.invoke("The iPhone 16 delivers excellent performance with the powerful A18 chip, making everyday tasks, gaming, and multitasking feel smooth and responsive. Its 48MP camera captures sharp, vibrant photos, while the improved ultra wide lens and Camera Control button enhance the photography experience. Battery life comfortably lasts a full day for most users, and the premium design feels comfortable to hold. The only notable drawback is the 60Hz display, but overall it's an excellent choice for anyone looking for a reliable flagship smartphone.")

print(result)
