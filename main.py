import kprequest


def kp_request_data(status, context):
    if status is True:
        print(context)
    else:
        print("出错了")


if __name__ == '__main__':

    url = 'http://127.0.0.1:8080/userinfo'

    # 注意这里必须以json字符串构造数据
    data = {
        "user": "kanpon"
    }
    kprequest.KpRequest.kp_get(url=url, params=data, callback=kp_request_data)
