document.addEventListener("DOMContentLoaded", () => {
  (document.querySelectorAll(".file") || []).forEach(($file) => {
    const file = $file;
    file.addEventListener("change", handleSubmit);
  });
});

function handleSubmit(event) {
  // Stop the form from reloading the page
  event.preventDefault();

  // If there's no file, do nothing
  if (!file.value.length) return;

  const selectedFile = file.files[0];
  const filenameGui = document.querySelectorAll(".file-name")[0];
  filenameGui.textContent = selectedFile.name;
  // Create a new FileReader() object
  let reader = new FileReader();
  // Read the file
  reader.readAsText(selectedFile);
  reader.onload = logFile;

  // Progress Bar
  if (document.querySelectorAll("#progress-bar").length < 1) {
    createProgressBar();
  } else {
    let progressBar = document.querySelectorAll("#progress-bar")[0];
    progressBar.removeAttribute("value");
  }
}

function increaseWidth(element) {
  element.style.width = "66%";
}

function decreaseWidth(element) {
  element.style.width = "33%";
}

function createProgressBar() {
  var progress = document.createElement("progress");
  progress.classList.add("progress", "is-small", "is-primary");
  progress.id = "progress-bar";
  progress.setAttribute("max", "100");
  progress.style.marginTop = "2.5vh";

  // progress.setAttribute("value", "0");

  var button = document.querySelectorAll("#upload-file-navbar")[0];

  var container = document.createElement("div");
  container.classList.add("progress-bar");

  container.appendChild(progress);

  button.parentNode.insertBefore(container, button);
}

function logFile(event) {
  let str = event.target.result;
  let json = JSON.parse(str);

  async function postData(data = {}) {
    let sense = document.querySelectorAll("#sensitivity")[0].value;
    const response = await fetch(
      "http://localhost:8080/v1/models/infer/" + sense,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );
    return await response.json();
  }

  postData(json).then((data) => {
    let progressBar = document.querySelectorAll("#progress-bar")[0];
    progressBar.setAttribute("value", "100");

    let clouds = document.querySelectorAll(".word-cloud");
    clouds.forEach((cloud) => {
      cloud.remove();
    });

    let i = 0;
    for (let key in data) {
      let blocks = data[key];
      blocks.forEach(function (block) {
        let theme = block["theme"];
        let answers = block["answers"];
        createBlock(i, key);
        createCloud(i, answers, theme);
        i++;
      });
    }
  });
}

function createBlock(id, sentiment) {
  let block = document.getElementById("block-" + sentiment);

  let cloudBlock = document.createElement("div");
  cloudBlock.classList.add("word-cloud");
  cloudBlock.setAttribute("id", "word-cloud" + id);
  block.appendChild(cloudBlock);
}

function createCloud(id, words, theme) {
  let config = {
    trace: true,
    spiralResolution: 0.8, //Lower = better resolution
    spiralLimit: 360 * 5,
    lineHeight: 0.8,
    xWordPadding: 0,
    yWordPadding: 0,
    font: "lato",
  };

  words = words.map(function (word) {
    return {
      word: word,
      freq: Math.floor(Math.random() * 5) + 10, // шрифт взависимости от каунта
    };
  });

  words.push({ word: theme, freq: 25 });

  words.sort(function (a, b) {
    return -1 * (a.freq - b.freq);
  });

  let cloud = document.getElementById("word-cloud" + id);
  cloud.style.position = "relative";
  cloud.style.fontFamily = config.font;

  let startPoint = {
    x: cloud.offsetWidth / 2,
    y: cloud.offsetHeight / 2,
  };

  let wordsDown = [];

  function createWordObject(word, freq) {
    let wordContainer = document.createElement("div");
    wordContainer.style.position = "absolute";
    wordContainer.style.fontSize = freq + "px";
    wordContainer.style.color = "rgb(62, 63, 64)";
    if (freq === 25) {
      wordContainer.style.fontWeight = "bold";
      // Main color
      wordContainer.style.color = "rgb(105, 113, 113)";
    }
    wordContainer.style.lineHeight = config.lineHeight;
    wordContainer.style.transform = "translateX(0%) translateY(0%)";
    wordContainer.appendChild(document.createTextNode(word));

    return wordContainer;
  }

  function placeWord(word, x, y) {
    cloud.appendChild(word);
    word.style.left = x - word.offsetWidth / 2 + "px";
    word.style.top = y - word.offsetHeight / 2 + "px";

    wordsDown.push(word.getBoundingClientRect());
  }

  function spiral(i, callback) {
    angle = config.spiralResolution * i;
    x = (1 + angle) * Math.cos(angle);
    y = (1 + angle) * Math.sin(angle);
    return callback ? callback() : null;
  }

  function intersect(word, x, y) {
    cloud.appendChild(word);

    word.style.left = x - word.offsetWidth / 2 + "px";
    word.style.top = y - word.offsetHeight / 2 + "px";

    let currentWord = word.getBoundingClientRect();

    cloud.removeChild(word);

    for (let i = 0; i < wordsDown.length; i += 1) {
      let comparisonWord = wordsDown[i];

      if (
        !(
          currentWord.right + config.xWordPadding <
            comparisonWord.left - config.xWordPadding ||
          currentWord.left - config.xWordPadding >
            comparisonWord.right + config.wXordPadding ||
          currentWord.bottom + config.yWordPadding <
            comparisonWord.top - config.yWordPadding ||
          currentWord.top - config.yWordPadding >
            comparisonWord.bottom + config.yWordPadding
        )
      ) {
        return true;
      }
    }

    return false;
  }

  (function placeWords() {
    for (let i = 0; i < words.length; i += 1) {
      let word = createWordObject(words[i].word, words[i].freq);

      for (let j = 0; j < config.spiralLimit; j++) {
        if (
          spiral(j, function () {
            if (!intersect(word, startPoint.x + x, startPoint.y + y)) {
              placeWord(word, startPoint.x + x, startPoint.y + y);
              return true;
            }
          })
        ) {
          break;
        }
      }
    }
  })();
}
