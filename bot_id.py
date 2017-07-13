import os 
from slackclient import SlackClient

def get_bot_id(api_token, bot_name):
    BOT_NAME = bot_name
    slack_client = SlackClient(api_token)
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                return user.get('id') 
        return None
    else:
        return None