"""
Flask server for Emotion Detection Application.
This module provides web endpoints to analyze emotions in text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as analyze_emotion

app = Flask(__name__)


@app.route('/')
def home():
    """
    Render the home page.
    
    Returns:
        str: Rendered HTML template for index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    """
    Analyze emotions from user-provided text.
    
    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = analyze_emotion(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
