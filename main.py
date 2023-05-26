
from app.model.imdb import IMDB


def main():
    url = "https://www.imdb.com/"
    imdb = IMDB(url)
    get_totals = imdb.getTopMovies()
    print(get_totals)


if __name__ == '__main__':
    main()