## TUTORIAL HERE: https://drive.google.com/file/d/1kknfskqebQRSzwreWG798Efy2D4tOJQl/view?usp=sharing
# Roblox Catalog Sale Notifier Bot

This Discord bot monitors the sale status of Roblox catalog items and alerts you when their status changes. It uses Selenium to scrape the catalog pages and checks for item availability every 10 seconds. (can be changed)

## Features

- **Monitor Items:** Add Roblox catalog item IDs to the watchlist and get notified when their sale status changes.
- **Status Updates:** Receive updates in the specified Discord channel when items go on sale or are taken off sale.
- **Commands:**
  - `/addid <item_id>` - Add a Roblox catalog item ID to the watchlist.
  - `/removeid <item_id>` - Remove a Roblox catalog item ID from the watchlist.
  - `/status` - Get the current status of all monitored items.
  - `/credits` - View credits for the bot creator.

## Setup

1. **Install Dependencies:**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install discord.py selenium webdriver-manager
   ```
## Configure the Bot

- **Replace** `PUTYOURCHANNELIDHERE` with your Discord channel ID where notifications will be sent.
- **Replace** `PUTYOURBOTTOKENHERE` with your Discord bot token.

## Run the Bot

Save the script as `bot.py` and run it:

```bash
python bot.py
```
## Credits

- **Bot Creator:** Marcelo
- **Socials:** [guns.lol/pronhubstar](https://guns.lol/pronhubstar)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
