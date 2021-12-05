from rest_framework.decorators import api_view

from apischedule.decorators import path_validator
from apischedule.client import ApiClient

@api_view(['GET','POST'])
@path_validator
def api_bouncer(request,app,route):
    client = ApiClient(app,route)
    method = request.method
    params = request.query_params
    data = request.data
    headers = request.headers
    return client.request(method,params,data,headers)
