# File to get a list of 5 letter english words

import requests

url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
page = requests.get(url)

if page.status_code == 200:
    print("page access status okay")
    words = page.text

    with open("dictionary.txt", "w+") as f:
        f.write(words.rstrip('\n'))

else:
    print("Could not access page. Code: {} for {}".format(page.status_code, url))