#import libraries and create global variables
from fastapi import FastAPI,status,HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from .data import DataLoader
import random
import uvicorn

class FastApiProvider:
    def __init__(self,data):
        self.app=FastAPI()
        self.__data=data
        self.__loader=DataLoader()


    def create_relative_routes(self):
        #GET METHODS
        @self.app.get("/costs")
        def get_all_costs():
            if self.__data:
                return JSONResponse(content=self.__data,status_code=status.HTTP_200_OK)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        @self.app.get("/costs/{item_id}")
        def get_cost_item_id(item_id:int):
            print(self.__data)
            for item in self.__data:
                print(item)
                if item["id"]==item_id:
                    return JSONResponse(content=item,status_code=status.HTTP_200_OK)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{item_id} was not found")
        @self.app.post("/costs")
        def post_new_item(description:str,amount:float):
            new_items={"id":random.randint(1,1000),"description":description,"amount":amount,"Authority":str(uuid4())}
            if new_items:
                self.__data.append(new_items)
                self.__loader.save_data(self.__data)
                return JSONResponse(content=new_items,status_code=status.HTTP_201_CREATED)
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

        @self.app.put("/costs/{item_id}")
        def update_item(item_id:int,new_description:str,new_amount:float):
            for item in self.__data:
                if item["id"]==item_id:
                    item["description"]=new_description
                    item["amount"]=new_amount
                    self.__loader.save_data(self.__data)

                    return JSONResponse(content=item , status_code=status.HTTP_200_OK)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        @self.app.delete("/costs/{item_id}")
        def delete_item(item_id:int):
            for item in self.__data:
                if item["id"]==item_id:
                    self.__data.remove(item)
                    self.__loader.save_data(self.__data)
                    return JSONResponse(content=item , status_code=status.HTTP_204_NO_CONTENT)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        
        
        
        
        

    def run(self):
        uvicorn.run(app=self.app,host="0.0.0.0",port=5000)
if __name__=="__main__":
    data=DataLoader().load_data()
    fastapi=FastApiProvider(data)
    fastapi.create_relative_routes()
    fastapi.run()
