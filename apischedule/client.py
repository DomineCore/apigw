import ujson as json

from requests import Session, Request
from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response

from apischedule.models import RouteSchema
from requestrec.models import RequestRec
from resource.appman.models import AppMan
from resource.apisentry.models import ApiSentry


class ApiClient(object):
    def __init__(self,
        app:AppMan,
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
        try:
            resp = self._request(method,params,data,headers)
        except Exception as e:
            resp = "调用系统发生未知异常，请联系开发者"
            ApiSentry.objects.save_trace(
                trace_msg=str(e),
                api=self.route.api_id,
                sys=self.app.app_id
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={
                "message":resp
            })
        # 记录请求
        RequestRec.objects.save_req_resp(
            request_sys=from_sys,
            response_sys=self.app.app_id,
            method=method,
            request_message=json.dumps({
                "params":params,
                "data":data,
            }),
            response_message=resp,
            api=self.route.api_id
        )
        return HttpResponse(**resp)
