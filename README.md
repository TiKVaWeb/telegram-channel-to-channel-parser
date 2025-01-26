# Telegram post's scraper
Telegram Parser is a Python script designed to automatically forward messages from one or more Telegram channels to a different channel. It allows you to automatically gather news or updates from various sources and publish them in your Telegram channel.

## Content
- [Technologies](#Technologies)
- [Usage](#Usage)
- [Installation](#Installation-and-launch)
- [Contacts](#Contacts)

## Technologies
- **[Python 3.9+](https://www.python.org/)**
- **[Telethon](https://docs.telethon.dev/en/stable/)**
- **[ahocorasick](https://pypi.org/project/pyahocorasick/)**
- **[re](https://docs.python.org/3/library/re.html)**
  
## Usage
The script forwards messages from specified Telegram channels to a specified target channel, hiding the source of the messages.

## Settings
1. Create an application in Telegram API to get ***api_id*** and ***api_hash***.
2. Subscribe to the channels from which you want to parse messages.
3. Add your account to the channel where messages will be sent, with publishing rights.

If you are using a [KeywordTelegramForwarder.py](https://github.com/TiKVaWeb/telegram-keyword-filter-forwarder/blob/main/KeywordTelegramForwarder.py):
1.  **Define your keywords:**  Edit the `keywords` list in the script to include words relevant to the content you want to forward.
2.  **Case-insensitive search:** Keyword matching is case-insensitive, meaning "Keyword", "keywords", and "KEYWORD" will all be matched.

## Installation and launch
1. Install dependencies:
   `pip install telethon pyahocorasick`
3. Set up the script:
   * Provide your API data: api_id, api_hash and phone number.
   * Add links to source channels in source_channels.
   * Specify the target channel in target_channel.
4. Run the script:
   `python script.py`

## Contacts
* ___Author:___ *Bogomolov N.O.*
* ___Email:___ *fortunaandrak@gmail.com*
* ___Telegram:___ *@thebiggestblackcock*

   [![support me](https://camo.githubusercontent.com/0b448aabee402aaf7b3b256ae471e7dc66bcf174fad7d6bb52b27138b2364e47/68747470733a2f2f7777772e6275796d6561636f666665652e636f6d2f6173736574732f696d672f637573746f6d5f696d616765732f6f72616e67655f696d672e706e67)](https://www.donationalerts.com/r/tikva_web)
