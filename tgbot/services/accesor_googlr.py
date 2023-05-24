import asyncio
from requests_html import AsyncHTMLSession


class Google_accessor:
    def __init__(self, url='https://www.google.com/search?q='):
        self.url = url
        self.session = None


    def setup(self) -> None:
        self.session = AsyncHTMLSession()


    async def get_response(self, item: str):
        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        response = await self.session.get(self.url + item, headers=headers)
        return response

async def main():
    session = Google_accessor()
    session.setup()
    r = await session.get_response(item='привет')
    print(r.html)
    r = str(r.html)
    with open('1.html', 'w') as file:
        file.write(r)


if __name__ == '__main__':
    asyncio.run(main())