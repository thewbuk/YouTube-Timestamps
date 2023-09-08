if (window.location.pathname === "/watch") {
  console.log("YouTube video detected:", window.location.href);

  const videoId = new URLSearchParams(window.location.search).get("v");
  fetchCaptions(videoId);
}

function fetchCaptions(videoId) {
  fetch(`http://localhost:5000/get_transcript?video_id=${videoId}`)
    .then((response) => response.json())
    .then((data) => {
      console.log("Transcript:", data.transcript);
      console.log("Topic Timestamps:", data.topic_timestamps);
      console.log(data.formatted_timestamps);
    })
    .catch((error) => {
      console.log("Error fetching captions:", error);
    });
}
