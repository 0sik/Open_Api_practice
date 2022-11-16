import requests
import json
import xmltodict

apiUrl = "https://openapi.gg.go.kr/GgHosptlM?Key=d6d4ac4e2c084ba78dc472e893d68e77&SIGUN_NM=시흥시"
req = requests.get(apiUrl)

xpars = xmltodict.parse(req.text)

jsonDump = json.dumps(xpars)

jsonBody = json.loads(jsonDump)



keys = [key for key in jsonBody['GgHosptlM']]
print (keys)
print(jsonBody ['GgHosptlM']['row'][0]['REFINE_WGS84_LAT'])