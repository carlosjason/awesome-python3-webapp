import json,logging, inspect, functools


class APIError(Exception):
    pass

class APIValueError(APIError):
    pass 

class APIResourceNotFoundError(APIError):
    pass 

class APIPermissionError(APIError):
    pass