# __author__ = 'tusharmakkar08'

import json

import requests

SENTIMENT_ANALYSIS_ENDPOINT = 'http://text-processing.com/api/sentiment/'


def find_sentiment(text_to_analyse):
    """
    :param text_to_analyse: Any test you want to analyse
    :return: 2 elements:
            1. The net label eg: pos, neg, neutral as a string
            2. The probability vector as a dictionary
                e.g: {'pos': 0.757939138722773, 'neg': 0.24206086127722704, 'neutral': 0.26175572807072145}
    """
    request_data = "text=" + text_to_analyse
    result = json.loads(requests.post(SENTIMENT_ANALYSIS_ENDPOINT, request_data).content.decode('utf-8'))
    return result["label"], result["probability"]
