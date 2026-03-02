import sys
from crawl import crawl_page


def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    BASE_URL = sys.argv[1]
    print(f"starting crawl of: {BASE_URL}")
    page_data = crawl_page(BASE_URL)
    if page_data is not None:
        print(f"Found {len(page_data.keys())} pages.")
        for page in page_data:
            print(page_data[page])


if __name__ == "__main__":
    main()
