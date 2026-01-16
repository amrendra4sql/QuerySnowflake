async function loadPage(page) {
  const content = document.getElementById("content");
  content.innerHTML = "⏳ Loading...";

  try {
    const response = await fetch(`pages/${page}.html`);
    const html = await response.text();
    content.innerHTML = html;

    // Load corresponding JS dynamically
    const script = document.createElement("script");
    script.src = `js/${page}.js`;
    script.defer = true;
    document.body.appendChild(script);

  } catch (e) {
    content.innerHTML = "❌ Failed to load page";
  }
}
