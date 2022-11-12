import requests
import xml.etree.ElementTree as ET



try:
    url = "https://openapi.gg.go.kr/GgHosptlM?Key=d6d4ac4e2c084ba78dc472e893d68e77&SIGUN_NM=시흥시"
    r = requests.get(url)
    print(r.text)
except:
    print("Invalid URL or some error occured while making the GET request to the specified URL")
    