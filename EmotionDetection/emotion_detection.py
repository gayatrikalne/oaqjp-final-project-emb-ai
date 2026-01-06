import requests
import json

def emotion_detector(text_to_analyze):

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = "<YOUR_WATSON_API_URL>"
    headers = {
        "Authorization": "Bearer <YOUR_API_KEY>",
        "Content-Type": "application/json"
    }

    payload = {
        "text": text_to_analyze
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = json.loads(response.text)

    emotions = response_json['emotion']['document']['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
