import re
from telethon import TelegramClient, events
import ahocorasick

# API
api_id = 'api_id'
api_hash = 'api_hash'
phone = 'phone_number'

source_channels = ['@first_channel', '@second_channel']
target_channel = '@you_channel'
keywords = ['first', 'second', 'example', 'word']  # Replace your keywords for filters

client = TelegramClient('NewsIt', api_id, api_hash)

async def main():
    """
    Main asynchronous function to start the Telegram client and process new messages.

    **This version of the script emphasizes message filtering by keywords, utilizing the Aho-Corasick algorithm for optimized searching.**

    The function performs the following actions:
    1. Starts the Telegram client with the provided API ID, API Hash, and phone number.
    2. Retrieves information about the target channel for message forwarding.
    3. Initializes the Aho-Corasick automaton for efficient keyword searching within messages.
    4. Sets up an event handler for new messages from the specified source channels.
    5. Runs the client until disconnected, waiting for new messages.
    """
    await client.start(phone=lambda: input('Введите код: '))
    target = await client.get_entity(target_channel)

    automaton = ahocorasick.Automaton()
    for keyword in keywords:
        automaton.add_word(keyword, keyword)
    automaton.make_automaton()

    @client.on(events.NewMessage(chats=source_channels))
    async def new_message_handler(event):
        """
        Event handler for new messages arriving from the specified source channels.

        **To optimize keyword searching, the Aho-Corasick algorithm is employed.**
        Messages are forwarded to the target channel only if they contain at least one of the predefined keywords.

        Args:
            event: The NewMessage event object, containing information about the new message.
        """
        message = event.message
        text = message.text
        media = message.media
        entities = message.entities # get entities message

        if text:
            # Searching for keywords in text using the Aho-Corasick machine
            found_keywords = list(automaton.iter(text.lower())) # Convert text to lowercase for case-insensitive search

            if found_keywords: # If at least one occurrence of the keyword is found
                try:
                    if media:
                        # Sending a message with entities to save premium emoji
                        await client.send_message(target, text, file=media, formatting_entities=entities)
                    else:
                        await client.send_message(target, text, formatting_entities=entities)
                except Exception as e:
                    print(f"Error sending message: {e}")
            else:
                print("The message does not contain keywords and will not be sent.")
        else:
            print("The message does not contain text.")


    print("Starting...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
