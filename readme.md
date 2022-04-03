

这是python前端用来发送post/get请求

使用说明：
1. 安装requirements.txt

`conda install -r requirements.txt`
2. 进入main.py
3. 修改url
如果有域名,以testdata.kanpon.com为例

`url = https://testdata.kanpon.com/userinfo
`
3. kp_request_data()

这是回调函数 ，请求返回的数据在这里处理
4.执行main.py
`python main.py`