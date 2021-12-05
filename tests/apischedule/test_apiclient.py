from django.test import TestCase
from unittest.mock import patch,MagicMock

from apischedule.client import ApiClient
from tests.test_settings import MockApp,MockRoute

MOCK_REQUESTREC_SAVE_REQ_RESP = "requestrec.models.RequestRec.objects.save_req_resp"

class TestApiClient(TestCase):

    def test_url(self):
        app = MockApp()
        route = MockRoute()
        client = ApiClient(app,route)
        test_url = "host/origin_url"
        self.assertEqual(client.url,test_url)

    def test_request_success(self):
        with patch(MOCK_REQUESTREC_SAVE_REQ_RESP,MagicMock(return_value=None)) as mocked:
            app = MockApp(host="http://www.baidu.com/")
            route = MockRoute(origin_url="")
            client = ApiClient(app,route)
            resp = client.request(
                'get',
                {},
                {},
                {},
                'testapp'
            )
            mocked.assert_called_once()