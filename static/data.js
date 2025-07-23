function downloadCSV() {
    const table = document.getElementById("userTable");
    let csv = [];
  
    // Extract headers
    let headers = [];
    for (let th of table.querySelectorAll("thead th")) {
      headers.push(th.innerText.trim());
    }
    csv.push(headers.join(","));
  
    // Extract rows
    for (let row of table.querySelectorAll("tbody tr")) {
      let rowData = [];
      for (let cell of row.querySelectorAll("td")) {
        let text = cell.innerText.trim().replace(/,/g, ""); // remove commas in values
        rowData.push(text);
      }
      csv.push(rowData.join(","));
    }
  
    // Convert to Blob and download
    const csvContent = csv.join("\n");
    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
  
    const a = document.createElement("a");
    a.href = url;
    a.download = "userdata.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }