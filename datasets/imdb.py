import urllib.request
url = "https://raw.githubusercontent.com/Ankit152/IMDB-sentiment-analysis/master/IMDB-Dataset.csv"
urllib.request.urlretrieve(url, "imdb.csv")