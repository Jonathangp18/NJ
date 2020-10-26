import os, requests, uuid
#from pprint import pprint
def cogn(_com):
    subscription_key = "10ed6ba7b3d4497096beabf32a4c9d39"
    endpoint = "https://nrrecluters.cognitiveservices.azure.com/"
    sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"
    documents = {"documents": [
        {"id": "1", "language": "es",
            "text": _com }
        ]}

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentimientos = response.json()
    #pprint(sentimientos)
    axx = sentimientos['documents'][0]['confidenceScores']['positive']
    print(axx)
    return axx