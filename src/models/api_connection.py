import requests
from typing import Any


EXCEPTIONS = requests.exceptions


class Books:
    def __init__(self, key):
        self.key = key
        self.books = []

    def fetch(self, url: str) -> requests.Response:
        """Sends a request to a Google Books API endpoint

        Args:
            url (str): Google Books API endpoint

        Returns:
            requests.Response: JSON object
        """

        try:
            res: requests.Response = requests.get(url)
        except EXCEPTIONS.RequestException as e:
            raise Exception("OOPS! Something went wrong with the API endpoint.")
        else:
            return res

    def search(self, by: str, query: str):
        """Searches Google Books API

        Args:
            by (string): searches by intitle, inauthor, or inpublisher
            query (string): provides descriptive search result for by
        """
        url: str = f"https://www.googleapis.com/books/v1/volumes?q=search+{by}:{query}&key={self.key}"
        try:
            json_data = self.fetch(url).json()
        except EXCEPTIONS.JSONDecodeError:
            print("Couldn't decode the text to JSON")
        else:
            return json_data

    def book_info(self, book):
        try:
            items = book["items"]
        except KeyError as e:
            print(f"Key does not exist {e}")
        else:
            for i in range(len(items) - 1):
                title: str = book["items"][i]["volumeInfo"]["title"]
                description: str = book["items"][i]["volumeInfo"]["description"]

                self.books.append({"title": title, "description": description})
            return self.books


books = Books("AIzaSyDZ2V1Fg4OKirlxvrX0ETSjcymqLXOLbdQ")

data = books.search("intitle", "harry potter")


print(data)
