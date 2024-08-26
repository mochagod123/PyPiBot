from bs4 import BeautifulSoup
import aiohttp
import os

async def pypiurl(key: str, numb: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://pypi.org/search/?q={key}') as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                link = soup.find_all('a', class_="package-snippet")[numb]
                return f"https://pypi.org{link["href"]}"
    except:
        return "Error."
        
async def pypititle(key: str, numb: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://pypi.org/search/?q={key}') as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                title = soup.find_all('span', class_="package-snippet__name")[numb]
                return f"{title.get_text()}"
    except:
        return "Error."