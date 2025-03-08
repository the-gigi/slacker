# Slacker

Use Slack as a hub to manage AI apps

## Using Slack programmatically

Slack has an RPC-style API that allows you to interact with it programmatically. You can use it to
send messages, create channels, and more. There are API groups:

- [Web API](https://docs.slack.dev/apis/web-api/): Querying information and enact changes in a Slack
  workspace.
- [Event API](https://docs.slack.dev/apis/events-api/) Build apps and bots that respond to
  activities in Slack.

But, using the API directly can be cumbersome. You have to deal with HTTP requests, JSON payloads,
authentication, retries, rate limiting and pagination.

It's better to use a library that abstracts all these details and access Slack in a more idiomatic
way.

Enter [Bolt](https://tools.slack.dev/bolt-python/).

I followed the docs to generate the Slacker app, generated Bot Oauth tokeninstalled it to the #bot-playground workspace. I created a new app in Slack and installed it in my

## Python setup

Let's create a Python virtual environment and install the required packages:

```shell
python -m venv venv
source venv/bin/activate
```

# Reference

https://docs.slack.dev/
https://api.slack.com/apps