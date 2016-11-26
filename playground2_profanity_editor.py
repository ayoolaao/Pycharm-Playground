
def read_text():
    quotes = open("/Users/ayoolaao/Downloads/movie_quotes.txt")
    contents = quotes.read()
    print (contents)
    quotes.close()

read_text()