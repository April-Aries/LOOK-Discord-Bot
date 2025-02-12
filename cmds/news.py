"""
Pre-request on your Ubuntu:
$ sudo apt update
$ sudo apt install python3-pip
$ pip3 install requests beautifulsoup4
"""

import datetime
from discord.ext import commands, tasks
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

tw_tz = datetime.timezone(datetime.timedelta(hours=8))
time = datetime.time(hour=22, minute=00, tzinfo=tw_tz)

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_daily_sec_news.start()

    def cog_unload(self):
        self.load_daily_sec_news.cancel()

    def fetch_news(self):
        URL = "https://www.ithome.com.tw/users/%E5%91%A8%E5%B3%BB%E4%BD%91"
        response = requests.get(URL)
        if response.status_code != 200:
            print(f"Failed to retrieve page. Status code: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("div", class_="view-content")[1].find_all("div", class_="views-row")

        today = dt.now()

        news_list = []
        for article in articles:
            title = article.find("p", class_="title").get_text(strip=True)
            link = "https://www.ithome.com.tw" + article.find("a")["href"]
            post_time = dt.strptime(article.find("p", class_="post-at").get_text(strip=True), "%Y-%m-%d")

            if today.year == post_time.year and today.month == post_time.month and today.day == post_time.day:
                news_list.append({"title": title, "link": link})
            else:
                break
        
        return news_list

    @tasks.loop(time=time)
    async def load_daily_sec_news(self):
        news_list = self.fetch_news()
        channel = self.bot.get_channel(int(os.getenv('NEWS_CHANNEL')))
        if news_list:
            for news in news_list:
                await channel.send(f"* [{news['title']}]({news['link']})")

async def setup( bot ):
    await bot.add_cog( News( bot ) )
