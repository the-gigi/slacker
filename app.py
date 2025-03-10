import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app_token = os.environ.get("SLACKER_APP_TOKEN")
bot_token = os.environ.get("SLACKER_BOT_TOKEN")
# Initializes your app with your bot token and socket mode handler
app = App(token=bot_token)


# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://tools.slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()