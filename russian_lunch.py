import os
import time
from slackclient import SlackClient
from bot_id import *
import sys
from interaction import *

def main():
    # print command line arguments
    api_token, bot_name = sys.argv[1:]
    BOT_ID = get_bot_id(api_token, bot_name)
    slack_client = SlackClient(api_token)
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read(), BOT_ID)
            if command and channel:
                handle_command(command, channel, slack_client)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

if __name__ == "__main__":
    main()
    