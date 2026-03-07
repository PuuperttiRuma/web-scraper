import asyncio
import aiohttp


class AsyncCrawler:
    def __init__(self, base_url, base_domain, page_data, max_concurrency):
        self.base_url = base_url
        self.base_domain = base_domain
        self.page_data = page_data
        self.lock = asyncio.Lock()
        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(self.max_concurrency)
        self.session

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def add_page_visit(self, normalized_url):
        async with self.lock:
            if normalized_url in self.page_data.keys():
                return True
            else:
                return False

    async def get_html(self, url):
        async with self.session.get(
            url, headers={"User-Agent": "BootCrawler/1.0"}
        ) as r:
            if r.status >= 400:
                raise Exception(f"Request failed: {r.status}: {r.reason}")
            if "text/html" not in r.headers["content-type"]:
                raise Exception(
                    f"Request failed, wrong content-type: {r.headers['content-type']}"
                )
            r.raise_for_status()
            return r.content


def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = str(base_url)
    if page_data is None:
        page_data = {}

    if parse.urlparse(current_url).hostname != parse.urlparse(base_url).hostname:
        # print("Page outside of domain")
        return

    normalized_url = normalize_url(current_url)
    if normalized_url in page_data.keys():
        return page_data

    print(f"Crawling {normalized_url}")
    try:
        html = get_html(current_url)
        page_data[normalized_url] = extract_page_data(html, current_url)
        # print(page_data.keys())
        for link in page_data[normalized_url]["outgoing_links"]:
            crawl_page(base_url, link, page_data)
    except Exception as e:
        print(f"{e}")
    return page_data
