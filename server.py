from bertopic import BERTopic
from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from collections import Counter
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

app = Flask(__name__)
CORS(app)


def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join([word for word in text.split()
                    if word.lower() not in stopwords.words('english')])
    return text


def format_seconds_to_timestamp(seconds):
    mins, sec = divmod(int(seconds), 60)
    return f"[{mins}:{sec:02}]"


@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

    texts = [preprocess_text(segment['text']) for segment in transcript_data]
    timestamps = [segment['start'] for segment in transcript_data]

    combined_texts = [' '.join(texts[i:i+10])
                      for i in range(0, len(texts), 10)]

    vectorizer_model = CountVectorizer(ngram_range=(1, 2))
    topic_model = BERTopic(top_n_words=5, min_topic_size=2,
                           vectorizer_model=vectorizer_model)
    topics, _ = topic_model.fit_transform(combined_texts)

    topic_representations = pd.DataFrame(topic_model.get_topic_info())
    column_name = 'Words' if 'Words' in topic_representations.columns else 'Representation'

    topic_freq = Counter(topics)
    top_n_topics = [item[0]
                    for item in topic_freq.most_common(5) if item[0] != -1]

    topic_timestamps = []
    formatted_timestamps = []
    current_topic = topics[0] if topics[0] in top_n_topics else None
    start_time = timestamps[0]

    for i, topic in enumerate(topics[1:], start=1):
        if topic in top_n_topics:
            if topic != current_topic:
                if current_topic is not None:
                    end_time = timestamps[i - 1]
                    N = 3
                    representative_words = topic_representations.loc[
                        topic_representations['Topic'] == current_topic, column_name].values[0]
                    if isinstance(representative_words, str):
                        representative_words = representative_words.split(", ")[
                            :N]
                    else:
                        representative_words = representative_words[:N]

                    topic_label = " ".join(representative_words)
                    topic_timestamps.append(
                        (topic_label, start_time, end_time))
                    formatted_timestamps.append(
                        f"{format_seconds_to_timestamp(start_time)} {topic_label}")

                current_topic = topic
                start_time = timestamps[i]

    if current_topic is not None:
        end_time = timestamps[-1]
        N = 3
        representative_words = topic_representations.loc[topic_representations['Topic']
                                                         == current_topic, column_name].values[0]
        if isinstance(representative_words, str):
            representative_words = representative_words.split(", ")[:N]
        else:
            representative_words = representative_words[:N]

        topic_label = " ".join(representative_words)
        topic_timestamps.append((topic_label, start_time, end_time))
        formatted_timestamps.append(
            f"{format_seconds_to_timestamp(start_time)} {topic_label}")

    response = {
        'transcript': transcript_data,
        'topic_timestamps': topic_timestamps,
        'formatted_timestamps': formatted_timestamps
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
