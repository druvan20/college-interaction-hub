// scripts.js

// This file is reserved for additional JavaScript that might be needed
// for non-React related functionality. Most logic will be in React components.

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/service-worker.js").then(
      (registration) => {
        console.log(
          "ServiceWorker registration successful with scope: ",
          registration.scope
        );
      },
      (error) => {
        console.error("ServiceWorker registration failed: ", error);
      }
    );
  });
}
