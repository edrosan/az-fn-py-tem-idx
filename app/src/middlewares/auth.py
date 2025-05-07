import azure.functions as func
import jwt
import logging
from functools import wraps
import os

# Secret key used to decode JWT tokens, loaded from environment variables
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

def auth_jwt(f):
    """
    Decorator to protect Azure Function endpoints with JWT authentication.
    Checks for a valid Bearer token in the Authorization header of the request.
    If the token is valid, the original function is executed.
    If the token is missing, expired, or invalid, returns a 404 response.

    Args:
        f (function): The function to be protected.

    Returns:
        function: The decorated function that validates the JWT before execution.
    """
    @wraps(f)
    def decorated_function(req: func.HttpRequest, *args, **kwargs):
        # Get the Authorization header from the request
        auth_headers = req.headers.get('Authorization')

        if not auth_headers:
            logging.error('Authorization header is missing!')
            return func.HttpResponse('Not Found', status_code=404)

        # Split the header into "Bearer" and the token
        parts = auth_headers.split(" ")

        if len(parts) != 2 or parts[0] != "Bearer":
            logging.error('Invalid Authorization header format!')
            return func.HttpResponse('Not Found', status_code=404)

        token = parts[1]

        if not token:
            logging.error('Token is missing!')
            return func.HttpResponse('Not Found', status_code=404)
        try:
            # Decode the token using the secret key and HS256 algorithm
            jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            logging.error('Token has expired!')
            return func.HttpResponse('Not Found', status_code=404)

        except jwt.InvalidTokenError:
            logging.error('Invalid token!')
            return func.HttpResponse('Not Found', status_code=404)

        logging.info('Token is valid!')

        # If token is valid, execute the original function
        return f(req, *args, **kwargs)
        
    return decorated_function
