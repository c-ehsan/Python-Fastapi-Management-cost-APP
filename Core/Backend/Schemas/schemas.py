#import libraries and create global variables 
from pydantic import BaseModel ,Field , ConfigDict

#Base Schema
class BaseSchema(BaseModel):
    model_config=ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )
    
#CostBaseSchema

class BaseCostSchema(BaseSchema):
    amount:float



class CostResponseSchema(BaseSchema):
    id:int=Field(description="Your ID:")
    description:str=Field(description="Your Product Name:")
    amount:float=Field(description="Your Amount:")
    Authority:str=Field(description="Your Authority:")



class APIResponseSchema(BaseSchema):
    success:bool
    message:str

class CostListResponseSchema(BaseSchema):
    success:bool
    message:str
    data:list[CostResponseSchema]



