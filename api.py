import requests
import json
import xmltodict

apiUrl = "https://openapi.gg.go.kr/GgHosptlM?Key=d6d4ac4e2c084ba78dc472e893d68e77&SIGUN_NM=시흥시"
#request받기
req = requests.get(apiUrl)

#xml형식으로 받기
xpars = xmltodict.parse(req.text)

#xml json(str) 형식으로 받기
jsonDump = json.dumps(xpars)
print(type(jsonDump))

#json(str)을 json(dict)형식으로 받기
jsonBody = json.loads(jsonDump)
print(type(jsonBody))
jsonBody2 = jsonBody ['GgHosptlM']['row']
print(type(jsonBody2))
for x in range (0,74):
    jsonBody(x)[x]
print(jsonBody2)
#jsonBody3 = dict(jsonBody2)
#print(type(jsonBody3))
#print(jsonBody3)

def deletefun (x):
    del jsonBody(x)["SIGUN_CD"]
    del jsonBody(x)["LICENSG_DE"]
    del jsonBody(x)["LICENSG_CANCL_DE"]
    del jsonBody(x)["BSN_STATE_DIV_CD"]
    del jsonBody(x)["UNITY_BSN_STATE_DIV_CD"]
    del jsonBody(x)["UNITY_BSN_STATE_NM"]
    del jsonBody(x)["BSN_STATE_NM"]
    del jsonBody(x)["CLSBIZ_DE"]
    del jsonBody(x)["SUSPNBIZ_BEGIN_DE"]
    del jsonBody(x)["SUSPNBIZ_END_DE"]
    del jsonBody(x)["REOPENBIZ_DE"]
    del jsonBody(x)["LOCPLC_AR_INFO"]
    del jsonBody(x)["X_CRDNT_VL"]
    del jsonBody(x)["Y_CRDNT_VL"]
    del jsonBody(x)["MEDINST_ASORTMT_NM"]
    del jsonBody(x)["MEDSTAF_CNT"]
    del jsonBody(x)["HOSPTLRM_CNT"]
    del jsonBody(x)["TOT_AR"]
    del jsonBody(x)["TREAT_SBJECT_CONT"]
    del jsonBody(x)["APPONT_CANCL_DE"]
    del jsonBody(x)["EASING_MEDCARE_APPONT_FORM"]
    del jsonBody(x)["EASING_MEDCARE_CHARGE_DEPT_NM"]
    del jsonBody(x)["SPECL_AMBLNC_CNT"]
    del jsonBody(x)["GENRL_AMBLNC_CNT"]
    del jsonBody(x)["TOT_EMPLY_CNT"]
    del jsonBody(x)["RESCUPSN_CNT"]
    del jsonBody(x)["FIRST_APPONT_DE"]
    del jsonBody(x)["PERMISN_SICKBD_CNT"]
    del jsonBody(x)["REFINE_ZIP_CD"]
    del jsonBody(x)["BIZCOND_DIV_NM_INFO"]
