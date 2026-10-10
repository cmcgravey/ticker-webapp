const endpoint = "/api/ticker";

function updateClock() {
  const now = new Date();
  document.querySelector("#clock").textContent = new Intl.DateTimeFormat([], {
    hour: "2-digit", minute: "2-digit", hour12: true,
  }).format(now).replace(" ", "");
  document.querySelector("#date").textContent = new Intl.DateTimeFormat([], {
    weekday: "long", month: "long", day: "numeric", year: "numeric",
  }).format(now).toUpperCase();
}

function card(item) {
  return `<article class="card"><div class="symbol">${escapeHtml(item.symbol)}</div><div class="label">${escapeHtml(item.label)}</div><div class="quote"><span class="value">${escapeHtml(item.value)}</span><span class="change ${item.direction}">${escapeHtml(item.change)}</span></div></article>`;
}

function escapeHtml(value) {
  const node = document.createElement("span");
  node.textContent = value;
  return node.innerHTML;
}

function render(data) {
  document.querySelector("#title").textContent = data.title;
  document.querySelector("#location").textContent = data.location;
  document.querySelector("#weather").textContent = data.weather;
  document.querySelector("#footer-message").textContent = data.footer_message;
  document.querySelector("#watchlist").innerHTML = data.watchlist.map(card).join("");
  const headlines = data.headlines.map((headline) => `<span class="headline">${escapeHtml(headline)}</span>`).join("");
  document.querySelector("#headline-track").innerHTML = headlines + headlines;
}

async function loadTicker() {
  try {
    const response = await fetch(endpoint, { cache: "no-store" });
    if (!response.ok) throw new Error(`API returned ${response.status}`);
    render(await response.json());
  } catch (error) {
    console.error("Unable to load ticker content", error);
    document.querySelector("#footer-message").textContent = "WAITING FOR TICKER SERVICE";
  }
}

updateClock();
setInterval(updateClock, 1000);
loadTicker();
setInterval(loadTicker, 5 * 60 * 1000);
