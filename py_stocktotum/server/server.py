from types import SimpleNamespace

import sanic
import sanic.response
from jinja2 import Environment, FileSystemLoader


def create_server() -> sanic.Sanic[sanic.Config, SimpleNamespace]:
    app = sanic.Sanic("stocktotum")
    env = Environment(loader=FileSystemLoader("public"))

    @app.get("/")
    async def index(request: sanic.Request) -> sanic.response.BaseHTTPResponse:
        template = env.get_template("index.html")
        html_content = template.render(title="Home Page", content="Hello, World!")
        return sanic.response.html(html_content)

    return app
