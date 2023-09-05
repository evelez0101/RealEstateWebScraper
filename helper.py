import requests
from bs4 import BeautifulSoup

# URL of the website containing the HTML table
url = "https://salesweb.civilview.com/"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table on the page using its HTML tag, class, or ID
table = soup.find("table")

# Find all the rows in the table using the HTML tag "tr"
rows = table.find_all("tr")

# Iterate over each row and extract the links from the cells
result = []
names = []
for row in rows:
    # Find all the cells in the row using the HTML tag "td"
    names.append(row.text.replace("\n", ""))
    cells = row.find_all("td")

    # Extract the links from the cells
    for cell in cells:
        # Find all the links in the cell using the HTML tag "a"
        links = cell.find_all("a")

        # Print the extracted links
        for link in links:
            result.append(link["href"])

print(result)
print(names)
