#import libraries and create global variables
from fastapi import FastAPI,status,HTTPException , Path , Query
from fastapi.responses import JSONResponse
from uuid import uuid4
from .data import DataLoader
from typing import Optional
from Core.Backend.Schemas.schemas  import BaseCostSchema  , CostResponseSchema, CostListResponseSchema , CostSchema

import random
import uvicorn

class FastApiProvider:
    def __init__(self,data):
        self.app=FastAPI()
        self.__data=data
        self.__loader=DataLoader()



    def get_costs(self):
        return self.__data




    def create_relative_routes(self):

        # GET METHODS
        @self.app.get("/costs",response_model=CostListResponseSchema)
        def get_all_costs():
            if self.__data:
                return {
                    "success":True,
                    "message":"Costs Retrieved successfully",
                    "data":self.__data

                }
            return {
                "success":False,
                "message":"Couldnt Retreived Costs",
                "data":[]
            }


        @self.app.get("/search_costs",response_model=CostListResponseSchema)
        def search_item(q:Optional[str]=Query(
                            None,
                            title="Search Method",
                            description="this endpoint just for search(filters) your products",
                            max_length=50,
                            pattern="^[^0-9]*$"
                
                        )):
                        result=[item for item in self.__data  if item["description"]==q]

                
                        if result:
                            return{
                                    "success":True,
                                    "message":"Your choosen field Returns successfully",
                                    "data":result
                
                                }
    
                        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{q} Was not found")


        

        @self.app.get("/costs/{item_id}",response_model=CostResponseSchema)
        def get_cost_item_id(item_id:int=Path(title="Get Product:",description="this endpoint get id and returns infos...")):
            for item in self.__data:
                print(item)
                if item["id"]==item_id:
                    return item
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{item_id} was not found")

         
     
        @self.app.post("/costs",response_model=CostResponseSchema)
        def post_new_item(cost:CostSchema):
            new_items={"id":random.randint(1,1000),"description":cost.description,"amount":cost.amount,"Authority":str(uuid4())}
            if new_items:
                self.__data.append(new_items)
                self.__loader.save_data(self.__data)
                return new_items

            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)



        @self.app.put("/costs/{item_id}",response_model=CostResponseSchema)
        def update_item(item_id:int,cost:CostSchema):
            for item in self.__data:
                if item["id"]==item_id:
                    item["description"]=cost.description
                    item["amount"]=cost.amount
                    self.__loader.save_data(self.__data)

                    return item
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


        @self.app.delete("/costs/{item_id}",response_model=CostResponseSchema)
        def delete_item(item_id:int):
            for item in self.__data:
                if item["id"]==item_id:
                    self.__data.remove(item)
                    self.__loader.save_data(self.__data)
                    return item 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        




    def run(self):
        uvicorn.run(app=self.app,host="0.0.0.0",port=5000)


