from bs4 import BeautifulSoup
import requests
from datetime import date


def get_links(url):

    # Get url result
    result = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(result.content, "html.parser")

    # Getting today's date
    current_date = (date.today()).strftime('%m-%d-%Y')

    # Find the <main> element on the page
    main_element = soup.find("main")

    # Find all <span> tags within the <main> element
    a_tags = main_element.find_all("a", href=True)

    # Opening and naming file
    f = open(f"news.txt {current_date}", "w")

    # Write content into txt file
    for num, tag in enumerate(a_tags):
        f.write(f"""
        Story {num + 1}
        ------------------"
        {tag.text.strip()}
        {tag['href']}
                """)
    f.close()

