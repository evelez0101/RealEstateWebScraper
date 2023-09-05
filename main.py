import requests
import os
import pandas as pd
from bs4 import BeautifulSoup


def scrapper(path):
    links = linkGetter()
    names = getFileNames()
    index = 0
    for link in links:
        print("\nPath: " + link)
        # URL of the website you want to scrape
        url = "https://salesweb.civilview.com" + link

        # Send a GET request to the website
        response = requests.get(url)
        print("Status: " + str(response))

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find specific elements on the page using their HTML tags, classes, or IDs
        # Here's an example of extracting all the links on the page
        table = soup.find('table', class_ = 'table table-striped')

        # Print the extracted links
        try:
            header = table.find_all("th")
        except:
            # Still skips ahead to the next name
            print(names[index] + " has no entries")
            index += 1
            continue

        # Extracts Titles
        titles = []
        for i in header:
            title = i.text
            titles.append(title)

        # Creates Table
        df = pd.DataFrame(columns = titles)
        rows = table.find_all("tr")

        # Extracts Text Here
        for i in rows[1:]:
            data = i.find_all("td")
            row = [tr.text for tr in data]
            length = len(df)
            df.loc[length] = row

        print("Successful Webpage to CSV")
        print(df)
        filename = names[index] + ".csv"
        print(filename + " created")
        index += 1
        df.to_csv(os.path.join(path, filename))
        print(f"CSV file '{filename}' added to the folder.")


def getFileNames():
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
    names = []
    for row in rows:
        # Find all the cells in the row using the HTML tag "td"
        names.append(row.text.replace("\n", ""))

    return names


def linkGetter():
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

    for row in rows:
        # Find all the cells in the row using the HTML tag "td"
        cells = row.find_all("td")

        # Extract the links from the cells
        for cell in cells:
            # Find all the links in the cell using the HTML tag "a"
            links = cell.find_all("a")

            # Print the extracted links
            for link in links:
                result.append(link["href"])

    return result


# Function to create a folder
def create_folder(folder_path):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        else:
            print(f"Folder '{folder_path}' already exists.")
    except OSError as e:
        print(f"Failed to create folder '{folder_path}'. Error: {e}")


def main():

    path = "./Houses"
    create_folder(path)
    scrapper(path)
    print("\nScrape Completed!")


if __name__ == "__main__":
    main()


