# YouTube Video Transcript Summarizer API

# ***Work in progress***

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Development](#development)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## Introduction

This is a Flask-based API that uses YouTube Transcript API and BERTopic for generating summaries and topics for YouTube videos. This project is a **work in progress**.

## Installation

To install the required dependencies, run the following command:

`bash
pip install -r requirements.tx
`

## Usage

Start the server by running:

`bash
python app.py
`

This will start the server on port 5000 by default.

## Endpoints

The current version of the API has the following endpoint:

- **GET** \`/get_transcript?video_id=<YOUTUBE_VIDEO_ID>\`

  Returns the full transcript, topics, and timestamps for the given YouTube video ID.

## Development

This project uses Python 3.x and is built on Flask. It uses BERTopic for topic modeling and the YouTube Transcript API for fetching video transcripts.

To set up a development environment, follow these steps:

1. Clone the repository
2. Install virtualenv: \`pip install virtualenv\`
3. Create a virtual environment: \`virtualenv venv\`
4. Activate the virtual environment: \`source venv/bin/activate\` (Linux) or \`.\venv\Scripts\activate\` (Windows)
5. Install dependencies: \`pip install -r requirements.txt\`
6. Run the server: \`python app.py\`

## Contributing

Feel free to open issues or PRs if you want to contribute to the project. Make sure to follow the existing code style.

## Disclaimer

This is a **work in progress** and might be subject to changes. Use at your own risk.

> **Note**: The YouTube Transcript API and YouTube are not affiliated with this project. Always respect YouTube's [Terms of Service](https://www.youtube.com/t/terms).
