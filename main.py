import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix = '!')

# Function to get War Thunder news
def get_warthunder_news():
    news_url = 'https://warthunder.com/en/news'
    news_page = requests.get(news_url)
    news_page_content = news_page.content
    news_page_content = news_page_content.decode()
    news_start = news_page_content.find('<div class="b-main-content__text">')
    news_end = news_page_content.find('<div class="b-main-content__more">')
    news = news_page_content[news_start:news_end]
    return news

# Event for when bot is ready
@bot.event
async def on_ready():
    print('Bot is ready.')

# Command for getting War Thunder news
@bot.command()
async def news(ctx):
    news = get_warthunder_news()
    await ctx.send(news)

# Command for getting War Thunder tank information
@bot.command()
async def tank(ctx, tank_name):
    tank_url = f'https://wiki.warthunder.com/{tank_name}'
    await ctx.send(tank_url)

bot.run('YOUR_BOT_TOKEN')
