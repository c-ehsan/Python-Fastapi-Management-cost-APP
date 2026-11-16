
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


class DashBoardUI:

    BASE_DIR = Path(__file__).resolve().parent

    def __init__(self, app: FastAPI, api_provider):
        self.app = app
        self.api_provider = api_provider
        self.api_provider.create_relative_routes()

        self.templates = Jinja2Templates(
            directory=self.BASE_DIR / "templates"
        )

    def setup_frontend(self):

        self.app.mount(
            "/static",
            StaticFiles(directory=self.BASE_DIR / "static"),
            name="static"
        )

        @self.app.get("/")
        async def home(request: Request):
            costs=self.api_provider.get_costs()
            return self.templates.TemplateResponse(
                request=request,
                name="index.html",
                context={"costs":costs}
            )

        @self.app.get("/expenses")
        async def expenses(request: Request):

            costs = self.api_provider.get_costs()

            return self.templates.TemplateResponse(
                request=request,
                name="expenses.html",
                context={"costs": costs}
            )
