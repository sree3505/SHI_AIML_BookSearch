// Attach event listeners to buttons
document.getElementById('getBooks').addEventListener('click', searchBooks);

// Function to call the search API (GET with query parameters)
async function searchBooks() {
    const title = document.getElementById('search_text').value;
    const url = `http://127.0.0.1:5000/api/books/${encodeURIComponent(title)}?limit=20`;
    // Clear previous content
    const container = document.getElementById('dataGrid');
    const errorMsg = document.getElementById('errorMsg');
    container.innerHTML = '';
    errorMsg.textContent = '';
    try {
        const response = await fetch(url);
        const data = await response.json();
        displayDataGrid(data, container);
    } catch (error) {
        errorMsg.textContent = `Error: ${error.message}`;
    }
}

function displayDataGrid(data, container) {
    // Create a table
    const table = document.createElement('table');
    table.className += "striped";
    // Create table header
    const tableHead = document.createElement('thead');
    const headerRow = document.createElement('tr');


    const headers = Object.keys(data[0]); // Get keys from the first object
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });
    tableHead.appendChild(headerRow);
    table.appendChild(tableHead);
    // Create table rows
    const tableBody = document.createElement('tbody');
    data.forEach(item => {
        const row = document.createElement('tr');
        headers.forEach(key => {
            const cell = document.createElement('td');
            cell.textContent = item[key];
            row.appendChild(cell);
        });
        tableBody.appendChild(row);
    });
    // Append the table body to table
    table.appendChild(tableBody);
    // Append the table to the container
    container.appendChild(table);
}