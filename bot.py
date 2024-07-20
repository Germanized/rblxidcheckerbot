import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import asyncio
import time


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


items_status = {}


CHANNEL_ID = PUTURCHANNELIDHERE # Replace with your channel ID

def check_catalog_ids(catalog_ids):
    on_sale_ids = []

    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    for catalog_id in catalog_ids:
        try:
            url = f"https://www.roblox.com/catalog/{catalog_id}"
            driver.get(url)
            time.sleep(2)  # Wait for the page to load and redirect if necessary

            buy_button = driver.find_elements(By.CLASS_NAME, "shopping-cart-buy-button")
            buy_button_alt = driver.find_elements(By.CLASS_NAME, "PurchaseButton")

            if buy_button or buy_button_alt:
                on_sale_ids.append(catalog_id)
        except Exception as e:
            print(f"Failed to retrieve data for Catalog ID {catalog_id}. Error: {str(e)}")

    driver.quit()
    return on_sale_ids

async def check_items_status():
    while True:
        catalog_ids = list(items_status.keys())
        on_sale_ids = check_catalog_ids(catalog_ids)

        for item_id in items_status.keys():
            current_status = "🟢 On Sale" if item_id in on_sale_ids else "🔴 Off Sale"
            
            if items_status[item_id] != current_status:
                items_status[item_id] = current_status
                alert_message = f"[alert] Catalog ID {item_id} is now {current_status}!"
                await bot.get_channel(CHANNEL_ID).send(alert_message)

        await asyncio.sleep(10)  # Check every 10 seconds

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    bot.loop.create_task(check_items_status())

@bot.command()
async def addid(ctx, item_id: int):
    items_status[item_id] = "Checking..."
    await ctx.send(f"Catalog ID {item_id} has been added to the watchlist.")

@bot.command()
async def removeid(ctx, item_id: int):
    if item_id in items_status:
        del items_status[item_id]
        await ctx.send(f"Catalog ID {item_id} has been removed from the watchlist.")
    else:
        await ctx.send(f"Catalog ID {item_id} was not found in the watchlist.")

@bot.command()
async def status(ctx):
    if not items_status:
        await ctx.send("No items are currently being monitored.")
        return

    status_message = "Current status of monitored items:\n"
    for item_id, status in items_status.items():
        status_message += f"Catalog ID {item_id}: {status}\n"

    await ctx.send(status_message)

@bot.command()
async def credits(ctx):
    await ctx.send("Credits to Marcelo. Visit my socials at guns.lol/pronhubstar")

# Run the bot with your token
bot.run('PUTYOURBOTTOKENHERE')  # Replace with your bot token
