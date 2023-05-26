
from app.model.imdb import IMDB
import csv

def main():
    url = "https://www.imdb.com/"
    imdb = IMDB(url)
    data = imdb.getTopMovies()
    fieldnames = ["Title", "Rating", "Summary"]

# Specify the path and name of the output CSV file
    filename = "top_movies.csv"

    # Write the data to the CSV file
    with open(filename, "w", newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write the rows


if __name__ == '__main__':
    main()