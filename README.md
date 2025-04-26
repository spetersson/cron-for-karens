# cron-for-karens

## Introduction

cron-for-karens is a lightweight automation toolkit designed to satisfy repetitive, bureaucratic demands without consuming valuable human attention. Focus on real engineering — let the scripts handle the illusion of productivity.

Point being that engineers want to work on engineering, and less with administrative tasks. However, given that the world consists of more roles than just engineers. We need to satisfy people who have other roles and functions in society. In most cases it's about reporting and to show that we exist.

## What this repo supports

### Slack

Slack is a fairly common tool for handling communications in a corporate environment.

#### Setup

1. Install required python packages

``` shell
pip install -r requirements.txt
```

2. You need a slack app together with a token. Check out ![Slack API: Applications | Slack](https://api.slack.com/apps) for more information.

3. Create a slack.yaml configuration file in the root directory of this repo. This will be the main configuration file for slack related automations. Check out [slack.example.yaml](slack.example.yaml) for up to date examples

``` yaml
---
slack_token: "xoxp-blabla"
slack_base_url: "https://yourspace.slack.com"
channel_for_log: DBLABLA
important_slack_reactions:
  message_lookup:
    limit: 10
    whitelist:
      - U01TBLA
      - U0ADSDS
  channels:
    - GFASDASD
    - C3412401
  reaction: "thumbsup"
```

#### Slack scripts

- [important_slack_reactions.py](important_slack_reactions.py)
  _
  This script can be used to send reactions on specific messages in specific channels. I recommend using this for humans that require specific attention and confirmations of that you are well and alive.
  _

#### Configuration options

**slack_token**

Description: _Set your Slack OAuth2 token so that the script can authenticate as your user_

Example: `slack_token: xoxp-abcdef-abcdef-abcdef-abcdef`

**slack_base_url**

Description: _Set the base url for your Slack workspace_

Example: `slack_base_url: https://iwonderwhereiwork.slack.com`

**channel_for_log**

Description: _Where to log the audits and errors. Choose your managers DM channel ID in case you want to be very verbose in your job._

Example: `channel_for_log: DBXYXYXY`

**important_slack_reactions.message_lookup.limit**

Description: _Limit on how many messages back the script shall search for and react upon._

Example: 
``` yaml
important_slack_reactions:
  message_lookup:
    limit: 10 
```

**important_slack_reactions.message_lookup.whitelist**

Description: _Define list of what users we react on, only some people demand attention. Not everyone._

Example:
  
``` yaml
important_slack_reactions:
  message_lookup:
    whitelist:
      - GFASDASD
      - C3412401
```

**important_slack_reactions.channels**

Description: _Define list of channels we shall look for messages in._

Example:

``` yaml
important_slack_reactions:
  channels:
    - GFASDASD
    - C3412401
```

**important_slack_reactions.reaction**

Description: _Define what emoji to use for reaction. Recommended is `thumbsup`, but nothing is stopping you from using `poop`._

Example:

``` yaml
important_slack_reactions:
  reaction: "thumbsup"
```

