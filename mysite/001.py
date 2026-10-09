# import requests
#
# # 1. 准备请求参数
# url = "https://httpbin.org/get"
# # 查询参数
# params = {"name": "test", "age": 20}
# # 请求头
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
# # cookies
# cookies = {"token": "abc123xyz"}
#
# # 2. 发送GET请求
# # verify=False 关闭ssl证书校验；timeout设置超时时间，单位秒
# resp = requests.get(
#     url=url,
#     params=params,
#     headers=headers,
#     cookies=cookies,
#     verify=False,
#     timeout=10
# )
#
# # 3. 打印结果
# print("状态码：", resp.status_code)
# print("响应头：", resp.headers)
# print("响应内容：", resp.text)


import requests

# 1. 创建会话对象，保持登录状态
sess = requests.Session()

# 2. 一次性定义请求头：User-Agent、Referer、Cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "_uuid=B125DEB5-351D-EF95-67C8-793A8ACE10510F10655infoc; buvid_fp=3d7e4f6e0132c6ea0da0ba3d5c6e2192; buvid3=AEA11CBD-27A7-79A7-2CDE-463B8FB4037128492infoc; b_nut=1790559910; buvid4=406906E1-CF16-3775-7D00-D7A3DF140B2G28492-026092809-23B5r1G5EPrcus1ktsN7SQ%3D%3D; SESSDATA=961ea7d4%2C1806111989%2C627d1%2A92CjAwNbsNXkv12Ntr-0nFnLwim0uNWS8-IxH_ozF774GfHRzeF27xxoFWWtAzKq9JUz4SVllYYlFaRGVkMFFUaFFGc3hWQ210bG5vWUdWQlZ2ZTlCdFpIQUNIVTEtd1dNM0lPX0VUUG9pRkh0TVRsLW9IZEtEejlKZDkzQ01sa1J0QVRWZmllY0h3IIEC; bili_jct=78e1e48e7b81e08c5b76ec68097ff903; DedeUserID=481078183; DedeUserID__ckMd5=2b59559386786b1a; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTA4MTkxOTEsImlhdCI6MTc5MDU1OTkzMSwicGx0IjotMX0.5R_rvI7QZycme_33Q0Aa7t5IE3wn4FtXyBv-RnqJ7Is; bili_ticket_expires=1790819131; home_feed_column=5; browser_resolution=1494-1156; CURRENT_FNVAL=2000; b_lsid=0D026E4F_1A0E5B19E5F; sid=6vpzelic"
}

# 把请求头一次性更新到会话中，后面所有get自动带上
sess.headers.update(headers)

# -------- 三个接口依次请求 --------
# 接口1：验证登录
url1 = "https://api.bilibili.com/x/web-interface/nav"
resp1 = sess.get(url1)
print("【接口1 登录验证结果】")
print(resp1.json())

# 接口2：获取基础信息
url2 = "https://api.bilibili.com/x/space/myinfo"
resp2 = sess.get(url2)
print("\n【接口2 个人基础信息】")
print(resp2.json())

# 接口3：获取关注/粉丝数，把你的UID替换进链接
my_uid = "481078183"
url3 = f"https://api.bilibili.com/x/relation/stat?vmid={my_uid}"
resp3 = sess.get(url3)
print("\n【接口3 粉丝&关注数据】")
print(resp3.json())