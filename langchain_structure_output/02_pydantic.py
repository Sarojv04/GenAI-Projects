from pydantic import BaseModel, EmailStr, Field
from typing import Optional 

class Student(BaseModel):
    #name : str
    name : str = 'Saroj'
    age : Optional[int] = None # optional argument
    email : EmailStr 
    CGPA : float = Field (gt =0, lt = 10, default = 2 , description = "A decimal value represent the CGPA of the student")

student_info = {'age' : 23, 'email': 'abc@gmail.com', 'CGPA': 9}

stu_obj = Student(**student_info)

#print(stu_obj)
print(stu_obj)