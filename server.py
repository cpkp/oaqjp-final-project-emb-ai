"""
Flask web server for emotion detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Handles the /emotionDetector endpoint.

    Returns:
        str: A formatted string containing emotion scores or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is None or response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")


@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
