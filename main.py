import sys
import requests


def get_html(url):
    r = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
    if r.status_code >= 400:
        raise Exception(f"Request failed: {r.status_code}: {r.reason}")
    if "text/html" not in r.headers["content-type"]:
        raise Exception(
            f"Request failed, wrong content-type: {r.headers['content-type']}"
        )
    if r.raise_for_status() is not None:
        raise r.raise_for_status()
    return r.content


def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    if len(sys.argv) == 2:
        BASE_URL = sys.argv[1]
        print(f"starting crawl of: {BASE_URL}")
        print(get_html(BASE_URL))


if __name__ == "__main__":
    main()
