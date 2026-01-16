async function runAISearch() {
    const query = document.getElementById("query").value.trim();
    if (!query) return alert("Enter your question");

    const resultDiv = document.getElementById("aiResult");
    resultDiv.innerHTML = "Thinking...";

    try {
        const response = await fetch("http://127.0.0.1:8000/api/ai-query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: query })  // original
        });

        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<span style="color:red;">Error: ${data.error}</span>`;
            return;
        }

        // original behavior: just print JSON nicely
        resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;

    } catch (err) {
        console.error(err);
        resultDiv.innerHTML = `<span style="color:red;">Failed to fetch data from backend.</span>`;
    }
}
