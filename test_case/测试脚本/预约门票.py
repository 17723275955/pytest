import requests
import time
import demjson
yq='boNa84IbEs6JCA0NMWu+VkRwXzq5OLVpRDuxp59BvSqvrDN4vcNgHLoNbD2Xw/6Y'
url=f'https://pcticket.chnmuseum.cn/prod-api/pool/getBlock?nonce={yq}&platform=1&docType=1'
headers={'Content-Type':'application/json;charset=UTF-8',
         'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbl91c2VyX25hbWUiOiIuIiwibG9naW5fZXhwaXJlZF90aW1lIjoxNjg4MTE1MjUxMDIxLCJsb2dpbl91c2VyX2lkIjo4NTIxOTE2LCJsb2dpbl91c2VyX2tleSI6Ijg1MjE5MTY6MzY2YjY2YWMtMGU1NS00NTlmLWE4ZDgtNzExNzhiOWIzODUzIiwibG9naW5fdXNlcl9hY2NvdW50Ijoid3hwYjI3c2M2NmtubDBtZzJ0In0.VdjzsGtu6vTwnTWgRynG1m8dLHyGinfu-mWDQzEED1I'


}
session=requests.session()
res2=session.get(url=url,headers=headers)
token=demjson.decode(res2.text)

while True:
    time.sleep(2)
    print(res2.content.decode(),time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # if res.content.decode()['msg']!='预约已满':
    #     break

