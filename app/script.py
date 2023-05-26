import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the movie data
table = soup.find("table", class_="chart full-width")

# Find all rows (movies) in the table except the header row and limit to 10 records
rows = table.find_all("tr")[1:11]

with open("top_movies.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Rating", "Summary"])


    # Iterate over the rows to extract movie data
    for row in rows:
        # Extract the movie title
        title_column = row.find("td", class_="titleColumn")
        title = title_column.a.text.strip()

        # Extract the movie rating
        rating_column = row.find("td", class_="ratingColumn")
        rating = rating_column.strong.text.strip()

        # Extract the movie summary
         # Extract the movie summary with error handling
        summary_column = row.find("td", class_="watchlistColumn")
        summary_element = summary_column.find("span", class_="secondaryInfo")
        summary = summary_element.text.strip() if summary_element else "N/A"

        # Write the movie data to the CSV file
        writer.writerow([title, rating, summary])

# Print a message when the scraping is complete
print("Scraping completed. Data saved in top_movies.csv.")