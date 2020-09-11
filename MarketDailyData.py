import json

import requests


def gettoken(client_id ,client_secret):
    url ='http://webapi.cninfo.com.cn/api-cloud-platform/oauth2/token'
    response = requests.post(url=url, data={'grant_type':'client_credentials','client_id':client_id,'client_secret':client_secret})
    print(response.text)
    responsedict =json.loads(response.text)
    token =responsedict["access_token"]
    return token

def apipost(scode,token):
    #url = "http://webapi.cninfo.com.cn/api/stock/p_stock2401"
    url="http://webapi.cninfo.com.cn/api/index/p_index2905"
    data = {"scode": scode, "access_token": token,"sdate":"2020-09-10","edate":"2020-09-10"}
    response = requests.post(url=url,data=data)
    print(response.text)
    responsedict =json.loads(response.text)
    resultcode =responsedict["resultcode"]
    print(responsedict["resultmsg"], responsedict["resultcode"])
    if responsedict["resultmsg"] == "success" and len(responsedict["records"]) >= 1:
        print(responsedict["records"])
    else:
        print('no data')
    return resultcode


if __name__ == "__main__":
    client_id, client_secret = "8VIcrh4Pn1Ableq6elEcdSNRmKVqjuiA", "tFyzmCT8oSQK4NCC0cu94aqwRlxew3JB"
    token =gettoken(client_id ,client_secret)
    list=['000001']
    for scode in list:
        resultcode =apipost(scode ,token)  # 以http post方法获取数据
        if resultcode==405:  # token失效，重新获取
            token =gettoken(client_id ,client_secret)
            apipost(scode,token)#post请求
