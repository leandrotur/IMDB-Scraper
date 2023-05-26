
from bs4 import BeautifulSoup
import requests
import re
from app.model.utils import get_page_content


class IMDB:
    def __init__(self, URL: str):
        self.URL = URL

    def getTopMovies(self):
        movies_list = []
        url = f"{self.URL}chart/top/?ref_=nv_mv_250"
        # Send a GET request to the URL
        response = requests.get(url)
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the table containing the movie data
        table = soup.find("table", class_="chart full-width")
        # Find all rows (movies) in the table except the header row and limit to 10 records
        rows = table.find_all("tr")[1:11]
        # Iterate over the rows to extract movie data
        for row in rows:
            response = {}
            # Extract the movie title
            title_column = row.find("td", class_="titleColumn")
            title = title_column.a.text.strip()
            # Extract the movie rating
            rating_column = row.find("td", class_="ratingColumn")
            rating = rating_column.strong.text.strip()
            movie_url = row.find("a")["href"]
            # Extract the title ID from the URL using regular expressions
            title_id = re.search(r"/title/([a-zA-Z0-9]+)/", movie_url).group(1)
            summary = self.getSummaryByTitleId(title_id)
            response["Title"] = title
            response["Rating"] = rating
            response["Summary"] = summary
            movies_list.append(response)
        return movies_list

    def getSummaryByTitleId(self, title_id):
        url = f"{self.URL}title/{title_id}/"
        page = get_page_content(url)
        soup = BeautifulSoup(page, 'html.parser')
        summary_p_element = soup.find('p', attrs={'data-testid': 'plot'})
        # Extract the content
        summary_text = summary_p_element.text.strip()
        return summary_text
