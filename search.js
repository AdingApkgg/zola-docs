function debounce(func, wait) {
  var timeout;

  return function () {
    var context = this;
    var args = arguments;
    clearTimeout(timeout);

    timeout = setTimeout(function () {
      timeout = null;
      func.apply(context, args);
    }, wait);
  };
}

function makeTeaser(body, terms) {
  var TEASER_MAX_WORDS = 30;
  var stemmedTerms = terms.map(function (w) {
    return w.toLowerCase();
  });
  var termFound = false;
  var index = 0;
  var weighted = []; // contains elements of ["word", weight, index_in_document]

  // split in sentences, then words
  var sentences = body.toLowerCase().split(". ");

  for (var i in sentences) {
    var words = sentences[i].split(" ");
    var value = 8;

    for (var j in words) {
      var word = words[j];

      if (word.length > 0) {
        for (var k in stemmedTerms) {
          if (word.includes(stemmedTerms[k])) {
            value = 40;
            termFound = true;
          }
        }
        weighted.push([word, value, index]);
        value = 2;
      }

      index += word.length;
      index += 1; // ' ' or '.' if last word in sentence
    }

    index += 1; // because we split at a two-char boundary '. '
  }

  if (weighted.length === 0) {
    return body;
  }

  var windowWeights = [];
  var windowSize = Math.min(weighted.length, TEASER_MAX_WORDS);
  // We add a window with all the weights first
  var curSum = 0;
  for (var i = 0; i < windowSize; i++) {
    curSum += weighted[i][1];
  }
  windowWeights.push(curSum);

  for (var i = 0; i < weighted.length - windowSize; i++) {
    curSum -= weighted[i][1];
    curSum += weighted[i + windowSize][1];
    windowWeights.push(curSum);
  }

  // If we didn't find the term, just pick the first window
  var maxSumIndex = 0;
  if (termFound) {
    var maxFound = 0;
    // backwards
    for (var i = windowWeights.length - 1; i >= 0; i--) {
      if (windowWeights[i] > maxFound) {
        maxFound = windowWeights[i];
        maxSumIndex = i;
      }
    }
  }

  var teaser = [];
  var startIndex = weighted[maxSumIndex][2];
  for (var i = maxSumIndex; i < maxSumIndex + windowSize; i++) {
    var word = weighted[i];
    if (startIndex < word[2]) {
      // missing text from index to start of `word`
      teaser.push(body.substring(startIndex, word[2]));
      startIndex = word[2];
    }

    // add <em/> around search terms
    if (word[1] === 40) {
      teaser.push("<b>");
    }
    startIndex = word[2] + word[0].length;
    teaser.push(body.substring(word[2], startIndex));

    if (word[1] === 40) {
      teaser.push("</b>");
    }
  }
  teaser.push("…");
  return teaser.join("");
}

function formatSearchResultItem(item, terms) {
  return '<div class="search-results__item">'
  + `<a href="${item.url}">${item.title}</a>`
  + `<div>${makeTeaser(item.body, terms)}</div>`
  + '</div>';
}

var fuse;
var options = {
  includeScore: true,
  includeMatches: true,
  ignoreLocation: true,
  keys: [
    { name: "title", weight: 0.8 },
    { name: "body", weight: 0.5 },
  ],
};

var initIndex = async function () {
  if (fuse === undefined) {
    try {
      const response = await fetch("/search_index.zh.json");
      if (response.ok) {
        const data = await response.json();
        fuse = new Fuse(data, options);
      }
    } catch (e) {
      console.error("Failed to load search index", e);
    }
  }
  return fuse;
}

function initSearch() {
  var $searchInput = document.getElementById("search");
  var $searchResults = document.querySelector(".search-results");
  var $searchResultsItems = document.querySelector(".search-results__items");
  var MAX_ITEMS = 50;
  
  if (!$searchInput || !$searchResults || !$searchResultsItems) {
      return;
  }

  if ($searchInput.dataset.searchBound === "true") {
    return;
  }
  $searchInput.dataset.searchBound = "true";

  $searchInput.addEventListener("keyup", debounce(async function() {
    var term = $searchInput.value.trim();
    if (term === "") {
      $searchResults.style.display = "none";
      return;
    }

    var fuseInstance = await initIndex();
    if (!fuseInstance) return;

    var results = fuseInstance.search(term);
    
    $searchResults.style.display = results.length > 0 ? "block" : "none";
    $searchResultsItems.innerHTML = "";

    if (results.length > 0) {
      // Collect all terms from matches for highlighting
      // Or just use the search term
      var terms = term.split(" ");
      
      for (var i = 0; i < Math.min(results.length, MAX_ITEMS); i++) {
        var item = document.createElement("li");
        // results[i].item contains the document
        item.innerHTML = formatSearchResultItem(results[i].item, terms);
        $searchResultsItems.appendChild(item);
      }
    }
  }, 150));
}

initSearch();
document.addEventListener("turbo:load", initSearch);
document.addEventListener("turbo:before-cache", function() {
    var $searchResults = document.querySelector(".search-results");
    var $searchInput = document.getElementById("search");
    if ($searchResults) $searchResults.style.display = "none";
    if ($searchInput) $searchInput.value = "";
});
