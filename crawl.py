from urllib import parse
from bs4 import BeautifulSoup


def normalize_url(input_url):
    if input_url == "":
        raise ValueError("Empty string given")

    url = parse.urlparse(input_url)

    if url.netloc == "":
        raise ValueError("Not a valid url")

    return f"{url.netloc}{url.path.rstrip("/")}"


def get_h1_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.h1
    if h1 is None:
        return ""
    else:
        return h1.get_text()


def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    main = soup.find("main")
    if main is not None:
        p = main.find("p")
    else:
        p = soup.find("p")

    if p is None:
        return ""
    else:
        return p.get_text()


def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href is None:
            continue
        if bool(parse.urlparse(href).netloc):  # checks if absolute link
            links.append(href)
        else:
            joined_link = parse.urljoin(base_url, href, False)
            links.append(joined_link)
    return links
