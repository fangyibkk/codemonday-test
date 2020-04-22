var log = (...args) => {
  console.log("[LOGGING script.js]", args);
};

// Update counnt
var setCountElement = (data) => {
  log("Response data:", data);
  count = parseInt(data.count);
  log("Global count", count);
  document.getElementById("display-count").innerHTML = count;
};

// Binding with button
var getURL = function (url, inc) {
  if (count + inc < 0) {
    return;
  } else {
    fetch(`${url}/${count + inc}`)
      .then((response) => response.json())
      .then(setCountElement);
  }
};

// Main program start here
count = null;
fetch("/api/count")
  .then((response) => response.json())
  .then(setCountElement);
