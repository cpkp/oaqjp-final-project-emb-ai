import requests  # To make the POST request
import json      # To format the response into a dictionary

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Send POST request
    response = requests.post(url, json=myobj, headers=header)

    # Handle error for blank/invalid input
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert response to dictionary
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']

    # Determine the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the final formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    