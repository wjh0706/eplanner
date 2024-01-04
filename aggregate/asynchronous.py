import asyncio
import aiohttp
import logging
urls={"auth":"http://ec2-3-91-67-221.compute-1.amazonaws.com/api/auth/user"
      ,
      "user":"http://ec2-18-118-30-126.us-east-2.compute.amazonaws.com:8012/",
      "event":"https://eplanner-event-mircro.wl.r.appspot.com/"}

logging.basicConfig(filename='asynchronous_fetch_urls.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
async def fetch(session, url):
    print("Calling URL = ", url)
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                logging.info(f"Content of {url}: {content}")
            else:
                logging.error(f"Failed to fetch {url}. Status code: {response.status}")
    except aiohttp.ClientError as e:
        logging.error(f"Error fetching {url}: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch(session, urls[each])) for each in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(type(response))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())