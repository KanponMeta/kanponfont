import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class KpRequest:
    @staticmethod
    def kp_post(url, params, callback):
        """
        post请求
        :param url: 接口url
        :param params: 请求参数
        :param callback: 回调函数
        """
        if url and params and callback:
            headers = {'content-type': 'application/json'}
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            try:
                request_result = requests.post(url, json=params, headers=headers, verify=False, allow_redirects=True)
                context = request_result.text
                status = request_result.ok
                callback(status, context)
            except requests.exceptions.ConnectionError:
                callback(False, {"msg": "Connection refused"})
        else:
            callback(False, {"msg": "url or params is none"})

    @staticmethod
    def kp_get(url, params, callback):
        """
        get请求
        :param url: 接口url
        :param params: 请求参数
        :param callback: 回调函数
        """
        if url and callback:
            headers = {'content-type': 'application/json'}
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            try:
                request_result = requests.get(url, json=params, headers=headers, verify=False, allow_redirects=True)
                context = request_result.text
                status = request_result.ok
                callback(status, context)
            except requests.exceptions.ConnectionError:
                callback(False, {"msg": "Connection refused"})
        else:
            callback(False, {"msg": "url or params is none"})
