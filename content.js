if (window.location.pathname === "/watch") {
  console.log("YouTube video detected:", window.location.href);

  const videoId = new URLSearchParams(window.location.search).get("v");
  fetchCaptions(videoId);
}

function fetchCaptions(videoId) {
  fetch(`http://localhost:5000/get_transcript?video_id=${videoId}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // This is the transcript
    })
    .catch((error) => {
      console.log("Error fetching captions:", error);
    });
}
