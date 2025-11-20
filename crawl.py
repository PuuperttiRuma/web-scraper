from urllib import parse

def normalize_url(input_url):
    if input_url == "":
        raise ValueError("Empty string given")

    url = parse.urlparse(input_url)

    if url.netloc == "":
        raise ValueError("Not a valid url")

    return f"{url.netloc}{url.path.rstrip("/")}"