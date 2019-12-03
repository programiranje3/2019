"""Web crawling and scraping
"""

import requests
from bs4 import BeautifulSoup

from woodstock.util import utility

BASE_URL = 'https://www.imdb.com/'


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed
    response = requests.get(url, allow_redirects=False)
    # Get text from the Response object
    response_text = response.text
    # Create and return the corresponding BeautifulSoup object from the response text; use 'html.parser'
    return BeautifulSoup(response_text, 'html.parser')


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    url_chunks = start_url.split('&page=')
    return ''.join(url_chunks) + '&page=' + str(page)


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    """

    return get_soup(get_specific_page(start_url, page))


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """

    page = 1
    while page <= max_pages:
        yield get_next_soup(url, page)
        page += 1


def get_m_info(start_url: str, max_pages=1):
    """
    Returns structured information about movies from a multi-page IMDb movie list.
    :param start_url: the url of the starting page of a multi-page IMDb movie list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the movies from a multi-page IMDb movie list
    Creates and uses the following data:
    - h3_list - a list of all 'h3' tags from multiple IMDb pages
                (each 'h3' tag contains: movie title, year of release, and (relative) link to the movie's IMDb page)
    - poster_list - a list of all relevant 'div' tags from multiple IMDb pages
                    (each such a 'div' tag contains the link to the poster of the corresponding movie)
    - info_list - a list of 3-tuples of information about each movie from h3_list
    - poster_link_list - a list of links to the posters of the movies from poster_list
    - complete_list - a list of 4-tuples of information about each movie from h3_list and poster_list
    """

    h3_list = []
    poster_list = []
    next_soup = crawl(start_url, max_pages)
    while True:
        try:
            s = next(next_soup)
            h3_list.extend(s('h3'))
            h3_list.pop(len(h3_list) - 1)
            poster_list.extend(s('div', {'class': "lister-item-image ribbonize"}))
            # pass
        except StopIteration:
            break
    info_list = []
    for h3 in h3_list:
        title = h3.a.text
        link = BASE_URL + h3.a['href'].lstrip('/')
        year = h3.a.find_next_sibling().text.lstrip('(').rstrip(')')
        info_t = title, link, year
        info_list.append(info_t)
    poster_link_list = []
    for p in poster_list:
        poster_link_list.append(p.a.img['loadlate'])
    complete_list = []
    for i, p in zip(info_list, poster_link_list):
        title, link, year = i
        complete_t = title, link, year, p
        complete_list.append(complete_t)
    return complete_list


if __name__ == "__main__":

    # Test get_soup()
    start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
                'mode=detail&page=1&sort=moviemeter,asc'
    soup = get_soup(start_url)
    print(soup)
    print()

    # Write BeautifulSoup info to an HTML file (using write_text(str(<soup>), encoding='utf-8', errors='replace')
    f = utility.get_data_dir() / 'IMDb_soup_rnr.html'
    f.write_text(str(soup), encoding='utf-8', errors='replace')
    print()

    # Demonstrate <soup>.find_all('<tag_name>') for 'h3' - attribute h3.text
    # print(soup.find_all('h3'))
    print(soup('h3'))
    print()
    print(soup.find('h3').text)
    print(soup.h3)
    print(soup.h3.text)
    print()

    # Demonstrate <soup>.find_all('<tag_name>') for 'div' (filter ResultSet with <{'class': "<class name>"}), 'h3',...
    print(soup('div', {'class': "lister-item-image ribbonize"}))
    print(soup('img'))
    print(type(soup('img')[0]))
    print(soup('img')[0]['loadlate'])
    print()

    # Demonstrate attribute h3.find('<subtag>'), h3.find('<subtag>').text, h3.find('<subtag>').get('<attribute>')
    h3 = soup.find('h3')
    # h3 = soup.h3          # equivalent to the previous line
    print(h3.find('a').text)
    # print(h3.a.text)      # equivalent to the previous line
    print(h3.a.string)
    print(h3.find('a').get('href'))
    print(h3.a.get('href'))
    print()

    # Demonstrate attribute h3.find('<subtag>'), filtered with <{'class': "<class name>"}
    h3_tags = soup('h3')
    h3_tags.pop(len(h3_tags)-1)
    for h3 in h3_tags:
        print(h3.find('span', {'class': "lister-item-year text-muted unbold"}))
        print(h3.find('span', {'class': "lister-item-year text-muted unbold"}).get('class'))
        print(h3.find('span', {'class': "lister-item-year text-muted unbold"}).text)
        print(h3.find('span', {'class': "lister-item-year text-muted unbold"}).text.lstrip('(').rstrip(')'))
    print()

    # Demonstrate shorthand notation (e.g., h3.find('<tag>').text is equivalent to h3.<tag>.text),
    # h3.<tag>.find_next_siblings() and h3.<tag>.string
    h3 = soup.h3
    print(h3)
    print(h3.span.find_next_siblings())
    print(h3.a.find_next_sibling())
    print(h3.a.find_next_sibling().string)
    print()

    # Test get_specific_page()
    print(get_specific_page(start_url, 3))
    print()

    # Test get_next_soup()
    print(get_next_soup(start_url, 2))
    print()

    # Test crawl()
    next_soup = crawl(start_url, 2)
    # print(next(next_soup)('h3'))
    # print(next(next_soup)('h3'))
    # print(next(next_soup)('h3'))
    while True:
        try:
            print(next(next_soup)('h3'))
        except StopIteration:
            break
    print()

    # Test get_m_info()
    for m in get_m_info(start_url, 2):
        print(m)
    print()


