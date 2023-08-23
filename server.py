from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return jsonify(transcript)

if __name__ == "__main__":
    app.run(port=5000)
