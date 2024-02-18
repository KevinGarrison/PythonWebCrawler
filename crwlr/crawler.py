import requests
from bs4 import BeautifulSoup


def web_crawler(main_url: str, sub_urls: list, element: str, attr_name: list) -> dict:
    """
    :param main_url: main url for the web page
    :param sub_urls: list of sub urls for subpages for scraping
    :param element: html element
    :param attr_name: list containing attribute name and value
    :return: Dictionary containing the content
    """
    content_dict = {}

    try:
        for index, sub_url in enumerate(sub_urls, start=1):
            page = main_url + "/" + sub_url
            # Make a GET request
            r = requests.get(page)

            # Check if status code is 200
            if r.status_code == 200:
                print('Request ' + str(index) + ' successful')
                soup = BeautifulSoup(r.text, "html.parser")

                # Find the element based on the attribute name and value
                element_name = soup.find(element, itemprop=attr_name[0])
                print(element_name)
                element_description = soup.find(element, itemprop=attr_name[1])
                # Add to the dictionary
                if element_name and element_description:
                    content_dict['bike_' + str(index)] = ('bike name:' + element_name.text + 'bike description:'
                                                          + element_description.text)
            else:
                print('Request ' + str(index) + ' failed with status code:', r.status_code)

    except requests.exceptions.RequestException as e:
        print('Error making request:', e)

    return content_dict
