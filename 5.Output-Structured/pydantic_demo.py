from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):

    name:str = 'Vidrohi'
    age : Optional[int] = None
    email : EmailStr 
    cgpa : float = Field(gt=0 ,lt=10 , default=8.9 , description=" A decimal value repersenting the cgpa of the cgpa of the student")

new_student = {'age': '99' , 'email':'harshverma4028@gamil.com'} 

student = Student(**new_student)

student_dict = dict(student)
student_jason = student.dump_json()


print(student_dict['age'])