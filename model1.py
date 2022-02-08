from typing import Optional, List
from uuid import UUID, uuid4 #an id in databases and systems 
from pydantic import BaseModel #BASEMODEL declares the data model as a class
from enum import Enum

class Gender(str,Enum): #ENUM communicates a limited set of values (male,female)
    male="male"
    female ='female'


class Role(str,Enum): #Making the user have multiple roles
    admin='admin'   
    user= 'user' 
    student='student'


class User(BaseModel) :#Declaring the data model 
    id: Optional[UUID] =uuid4()
    first_name:str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
      

class UserUpdateRequest(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    middle_name: Optional[str]
    roles: Optional[list[Role]]