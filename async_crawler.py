import asyncio
import aiohttp


class AsyncCrawler:
    def __init__(self, base_url, page_data, max_concurrency):
        self.base_url = base_url
        # self.base_domain # revitään beis_urlista
        self.page_data = page_data
        self.lock = asyncio.Lock()
        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(self.max_concurrency)
        self.session = aiohttp.ClientSession()
