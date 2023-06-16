from bs4 import BeautifulSoup
import requests
from datetime import date


def get_links(url):
    # Get url result
    result = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(result.content, "html.parser")

    # Find the <main> element on the page
    main_element = soup.find("main")

    # Create new variable headlines which finds the h2 elements on the page
    headlines = main_element.find_all('h2')

    # Opening and naming file
    f = open(f"NBA News.txt", "w")

    for num,topic in enumerate(headlines):
        # Check if an <a> tag exists within the <h2> tag
        if topic.find('a'):
            # Retrieve the href link using the 'a' tag within the 'h2' tag
            link = topic.find('a')['href']

            # Retrieve the text content of the 'h2' tag
            text = topic.get_text()

            # Begin writing to file
            f.write(f"""
                   STORY {num + 1}: {text}
                   LINK: {link}
                   ------------------------------------------------------
                 """)
        #  'TypeError: 'NoneType' object is not subscriptable' error will pop up if no href link is found so we need to handle error
        else:
            f.write(f"""
            STORY {num + 1}: {text}
            LINK: No link found for this story.
            ------------------------------------------------------
            """)


