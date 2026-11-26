#import libraries and create global variables 
from pydantic import BaseModel ,Field , ConfigDict
#hint: to request infos like post , put,delete we must use Costschema for send client data ofcourse to get_response  for client like get(with internal item),search , get all costs we must use Response_models like Cost Response Schema and etc,...

#Base Schema
class BaseSchema(BaseModel):
    model_config=ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )
    
#CostBaseSchema

class BaseCostSchema(BaseSchema):
    amount:float=Field(description="Your Amount:")


#Request Schema
class CostSchema(BaseCostSchema):
    description:str=Field(description="Your Product Name:")

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



