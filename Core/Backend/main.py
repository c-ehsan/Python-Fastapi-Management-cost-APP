#import libraries and create global variables
from .fastapi_routes_provider import FastApiProvider
from .data import DataLoader
from Core.Frontend.dashboard import DashBoardUI
from .data import DataLoader


class MainApp:
    def __init__(self):
        data=DataLoader().load_data()
        self.fastapi=FastApiProvider(data)
        self.fastapi.create_relative_routes()
        

        ui=DashBoardUI(app=self.fastapi.app,api_provider=self.fastapi)

        ui.setup_frontend()
    def run(self):
        self.fastapi.run()


if __name__=="__main__":
    app=MainApp()
    app.run()




