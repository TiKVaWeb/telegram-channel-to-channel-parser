from telethon import TelegramClient, events

# API
api_id = 'api_id'
api_hash = 'api_hash'
phone = 'phone_number'

source_channels = ['@test1', '@test2']
target_channel = '@my_channel'

client = TelegramClient('session_name', api_id, api_hash)


async def main():
    await client.start(phone=lambda: input('telegram_code: '))

    # We get the entity of the target channel
    target = await client.get_entity(target_channel)

    @client.on(events.NewMessage(chats=source_channels))
    async def new_message_handler(event):
        message = event.message
        text = message.text
        media = message.media

        try:
            if media:  # If the message contains media
                await client.send_message(target, text, file=media)
            else:  # If the message is text only
                await client.send_message(target, text)

            print("Message sent successfully.")
        except Exception as e:
            print(f"Error sending message: {e}")

    print("Start...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
