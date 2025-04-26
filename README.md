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

