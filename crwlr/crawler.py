import requests
from bs4 import BeautifulSoup
import time

def web_crawler(main_url: str, sub_urls: list, element: str, attr_name: list) -> list:
    """
    :param main_url: main url for the web page
    :param sub_urls: list of sub urls for subpages for scraping
    :param element: html element
    :param attr_name: list containing attribute name and value
    :return: Dictionary containing the content
    """
    names = []
    descriptions = []
    content = []

    try:
        for index, sub_url in enumerate(sub_urls, start=1):
            page = main_url + "/" + sub_url
            # Make a GET request
            r = requests.get(page)
            time.sleep(0.5)
            # Check if status code is 200
            if r.status_code == 200:
                print('Request ' + str(index) + ' successful')
                soup = BeautifulSoup(r.text, "lxml")
                # Find the element based on the attribute name and value
                names.extend([element.get_text(strip=True) for element in soup.find_all(element, itemprop=attr_name[0])])
                descriptions.extend([element.get_text(strip=True) for element in soup.find_all(element, itemprop=attr_name[1])])
            else:
                print('Request ' + str(index) + ' failed with status code:', r.status_code)

        content.append(names)
        content.append(descriptions)

    except requests.exceptions.RequestException as e:
        print('Error making request:', e)

    return content
