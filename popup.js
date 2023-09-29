document.addEventListener("DOMContentLoaded", () => {
  // Retrieve saved state
  chrome.storage.local.get("extensionState").then((data) => {
    const state = data.extensionState || "on";
    document.getElementById(state).checked = true;
  });

  // Handle radio button changes
  document
    .querySelectorAll('input[name="toggleExtension"]')
    .forEach((radio) => {
      radio.addEventListener("change", (event) => {
        const newState = event.target.value;
        // Save the new state
        chrome.storage.local.set({ extensionState: newState });
        // Optionally, send a message to content.js to notify about the state change
        chrome.tabs
          .query({ active: true, currentWindow: true })
          .then((tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, { extensionState: newState });
            console.log(
              "Youtube Timestamps extension state changed to",
              newState
            );
          });
      });
    });

  // Handle other actions, like the "Create Timestamps" button
  document.getElementById("createTimestamps").addEventListener("click", () => {
    // Add code to handle timestamp creation
  });
});
