from unittest.mock import MagicMock


class MockApp(object):
    def __init__(self, **kwargs):
        self.app_id = kwargs.get("app_id","app_id")
        self.app_sk = kwargs.get("app_sk","app_sk")
        self.name = kwargs.get("name","name")
        self.host = kwargs.get("host","host")


class MockRoute(object):
    def __init__(self, **kwargs):
        self.api_id = kwargs.get("api_id","api_id")
        self.origin_url = kwargs.get("origin_url","origin_url")
        self.apigw_url = kwargs.get("apigw_url","apigw_url")
        self.from_sys = kwargs.get("from_sys","from_sys")
        self.name = kwargs.get("name","name")
