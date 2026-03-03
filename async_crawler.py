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
