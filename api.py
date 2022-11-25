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
for x in range (0,72):
    del jsonBody2[x]['SIGUN_CD']
    del jsonBody2[x]["LICENSG_DE"]
    del jsonBody2[x]["LICENSG_CANCL_DE"]
    del jsonBody2[x]["BSN_STATE_DIV_CD"]
    del jsonBody2[x]["UNITY_BSN_STATE_DIV_CD"]
    del jsonBody2[x]["UNITY_BSN_STATE_NM"]
    del jsonBody2[x]["BSN_STATE_NM"]
    del jsonBody2[x]["CLSBIZ_DE"]
    del jsonBody2[x]["SUSPNBIZ_BEGIN_DE"]
    del jsonBody2[x]["SUSPNBIZ_END_DE"]
    del jsonBody2[x]["REOPENBIZ_DE"]
    del jsonBody2[x]["LOCPLC_AR_INFO"]
    del jsonBody2[x]["X_CRDNT_VL"]
    del jsonBody2[x]["Y_CRDNT_VL"]
    del jsonBody2[x]["MEDINST_ASORTMT_NM"]
    del jsonBody2[x]["MEDSTAF_CNT"]
    del jsonBody2[x]["HOSPTLRM_CNT"]
    del jsonBody2[x]["TOT_AR"]
    del jsonBody2[x]["TREAT_SBJECT_CONT"]
    del jsonBody2[x]["APPONT_CANCL_DE"]
    del jsonBody2[x]["EASING_MEDCARE_APPONT_FORM"]
    del jsonBody2[x]["EASING_MEDCARE_CHARGE_DEPT_NM"]
    del jsonBody2[x]["SPECL_AMBLNC_CNT"]
    del jsonBody2[x]["GENRL_AMBLNC_CNT"]
    del jsonBody2[x]["TOT_EMPLY_CNT"]
    del jsonBody2[x]["RESCUPSN_CNT"]
    del jsonBody2[x]["FIRST_APPONT_DE"]
    del jsonBody2[x]["PERMISN_SICKBD_CNT"]
    del jsonBody2[x]["REFINE_ZIP_CD"]
    del jsonBody2[x]["BIZCOND_DIV_NM_INFO"]

#print(jsonBody2)
print(type(jsonBody2))
with open("./test.json",'w',encoding='utf-8')as file:
    json.dump(jsonBody2,file,indent="\t",ensure_ascii=False)

