#!/usr/bin/env python3

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import yaml

def load_config(config_path='slack.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def react_on_message(client, config, channel, emoji, timestamp, text):
    try:
        client.reactions_add(
            channel=channel,
            name=emoji,
            timestamp=timestamp
        )
        log_text = f"I reacted with :{emoji}: on message: {text} in channel: {config['slack_base_url']}/archives/{channel}"
    except SlackApiError as e:
        error = e.response['error']
        print(f"error: {error}")
        if error == "already_reacted":
            log_text = f"I already reacted with :{emoji}: on message: {text} in channel: {config['slack_base_url']}/archives/{channel}"
        else:
            log_text = f"Failed to react with :{emoji}: on message: {text} due to error: {error}"

    client.chat_postMessage(channel=config['channel_for_log'], text=log_text)

def get_message(client, config):
    channels = config['important_slack_reactions']['channels']
    limit = config['important_slack_reactions']['message_lookup']['limit']
    reaction = config['important_slack_reactions']['reaction']
    whitelist = config.get('important_slack_reactions', {}).get('message_lookup', {}).get('whitelist')

    for channel in channels:
        try:
            messages = client.conversations_history(channel=channel, limit=limit)
            for message in messages['messages']:
                user = message.get('user')
                text = message.get('text')
                timestamp = message.get('ts')

                # Ignore messages that does not contain following fields
                if not user or not text or not timestamp:
                    continue

                # Use whitelist if defined else we will just process latest messages based on what
                # is defined as a limit
                if whitelist:
                    if user in whitelist:
                        react_on_message(client, config, channel, reaction, timestamp, text)
                else:
                    react_on_message(client, config, channel, reaction, timestamp, text)

        except SlackApiError as e:
            print(f"Error: {e.response['error']}")

if __name__ == "__main__":
    config = load_config()
    client = WebClient(token=config['slack_token'])
    get_message(client, config)
