import os, requests, uuid
from pprint import pprint
import pandas as pd

def cogn(_com):
    print("al servicio cognituve")
    subscription_key = "10ed6ba7b3d4497096beabf32a4c9d39"
    endpoint = "https://nrrecluters.cognitiveservices.azure.com/"
    language_url = endpoint + "/text/analytics/v3.0/languages"
    print("creedenciales")
    documents = {"documents": [
    {"id": "1", "text": _com }
    
    ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    print("headers")
    response = requests.post(language_url, headers=headers, json=documents)
    _languages = response.json()
     
    pprint(_languages)
    axx = _languages['documents'][0]['detectedLanguage']['name']
    print("ahi vamos de nuevo")
    print(axx)

    if axx == "English":
        _axxx= "en"

    if axx == "Spanish":
        _axxx= "es"

    if axx == "French":
        _axxx= "fr"

###########################################
 
    sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"
    documents = {"documents": [
        {"id": "1", "language": _axxx,
            "text": _com }
        ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentimientos = response.json()
    pprint(sentimientos)
    axx = sentimientos['documents'][0]['confidenceScores']['positive']
    print(axx)

##############################################################
    subscription_key = "10ed6ba7b3d4497096beabf32a4c9d39"
    endpoint = "https://nrrecluters.cognitiveservices.azure.com/"
    keyphrases_url = endpoint + "/text/analytics/v3.0/keyphrases"

    documents2 = {"documents": [
    {"id": "1", "language": _axxx,
        "text": _com }
    ]}
    headers2 = {"Ocp-Apim-Subscription-Key": subscription_key}
    response2 = requests.post(keyphrases_url, headers=headers2, json=documents2)
    key2 = response2.json()
    pprint(key2 )
    wa= key2['documents'][0]['keyPhrases']
    s="'"
    r=""
    q="["
    qq="]"
    was=str(wa)
    texto=was.replace(s,r)
    wal=texto.replace(q,r)
    w=wal.replace(qq,r)
    print(w)



    return (axx, w)