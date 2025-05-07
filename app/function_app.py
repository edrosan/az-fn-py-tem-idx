import azure.functions as func
import logging
import json

from src.middlewares.auth import auth_jwt

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="hello_word", methods=["GET"])
@auth_jwt
def hello_word(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Hello World function processed a request.')

    print("Hello world from Azure Functions!")

    response = {
        "success": True,
        "message": "Hello world from Azure Functions!"
    }

    return func.HttpResponse(
        json.dumps(response),
        mimetype="application/json",
        status_code=200
    )
