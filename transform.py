from bertopic import BERTopic

# Sample transcript data (replace with your data)
transcript_data = [
    {'duration': 2.179, 'start': 2.46, 'text': 'foreign'},
    {'duration': 4.96, 'start': 23.18, 'text': 'ERS and you are come well to the WAN'},
    # ... more data ...
]

# Extracting texts and timestamps
texts = [segment['text'] for segment in transcript_data]
timestamps = [segment['start'] for segment in transcript_data]

# Create BERTopic model
topic_model = BERTopic()

# Fit the model and transform texts into topics
topics, _ = topic_model.fit_transform(texts)

# Create timestamps with topics
topic_timestamps = []
current_topic = topics[0]
start_time = timestamps[0]
for i, topic in enumerate(topics[1:], start=1):
    if topic != current_topic:
        end_time = timestamps[i - 1]
        topic_timestamps.append((current_topic, start_time, end_time))
        current_topic = topic
        start_time = timestamps[i]

# Add last segment
topic_timestamps.append((current_topic, start_time, timestamps[-1]))

# Print the timestamps with topics
for topic_id, start, end in topic_timestamps:
    topic_words = topic_model.get_topic(topic_id)
    print(f"Topic {topic_id} ({start} to {end}): {topic_words}")
