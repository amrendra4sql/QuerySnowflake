async function fetchProduct() {
  const productCode = document.getElementById("productCode").value.trim();
  if (!productCode) return alert("Enter product code");

  document.getElementById("loader").style.display = "inline";
  document.getElementById("error").innerHTML = "";
  document.getElementById("result").innerHTML = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/product", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ productCode })
    });

    const data = await response.json();

    if (data.error) {
      document.getElementById("error").innerText = data.error;
      return;
    }

    if (data.length === 0) {
      document.getElementById("result").innerHTML = "<b>No product found</b>";
      return;
    }

    let table = "<table><tr>";
    for (const key in data[0]) table += `<th>${key}</th>`;
    table += "</tr>";

    data.forEach(row => {
      table += "<tr>";
      for (const key in row) table += `<td>${row[key] ?? ""}</td>`;
      table += "</tr>";
    });

    table += "</table>";
    document.getElementById("result").innerHTML = table;

  } catch (e) {
    document.getElementById("error").innerText = e;
  } finally {
    document.getElementById("loader").style.display = "none";
  }
}
