import requests
from bs4 import BeautifulSoup

# Fetch the web page
response = requests.get("https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)")

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Print the title of the page
print(soup.title.string)

# Find and print all the links in the page
for link in soup.find_all("a"):
    print(link.get("href"))