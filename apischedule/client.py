import ujson as json

from requests import Session, Request
from django.shortcuts import HttpResponse

from apischedule.models import RouteSchema
from requestrec.models import RequestRec
from resource.app.models import App


class ApiClient(object):
    def __init__(self,
        app:App,
        route:RouteSchema,
        ):
        self.route = route
        self.app = app
    
    @property
    def url(self):
        return self.app.host.rstrip('/') + '/' + self.route.origin_url.lstrip('/')

    def _request(self,method,params,data,headers):
        _session = Session()
        _req = Request(
            method,
            self.url,
            params,
            data,
            headers
        )
        _pre_req = _session.prepare_request(_req)
        _response = _session.send(_pre_req)
        content_type = _response.headers.get('content-type', 'text/html')

        return dict(
            content=_response.content,
            content_type=content_type,
            status=_response.status_code,
        )
    
    def request(self,method,params,data, headers,from_sys):
        resp = self._request(method,params,data,headers)
        # 记录请求
        RequestRec.objects.save_req_resp(
            request_sys=from_sys,
            response_sys=self.app.app_id,
            method=method,
            request_message=json.dumps({
                "params":params,
                "data":data,
                "headers":headers
            }),
            response_message=resp,
            api=self.route.api_id
        )
        return HttpResponse(**resp)
