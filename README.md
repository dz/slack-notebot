# Slack Notebot

A meeting notes bot to help take and distribute notes.

### Starting the bot

Create Slack Bot API token at: [https://my.slack.com/services/new/bot](https://my.slack.com/services/new/bot) (See [https://api.slack.com/bot-users](https://api.slack.com/bot-users) for additional info)

Run `bot.py` with the `SLACK_API_TOKEN` environment variable set:

``bash
$ SLACK_API_TOKEN='xxxxxxx' python bot.py
``

### Using the bot

Private message the bot with the words `start`.

Start typing meeting notes.  Users that are `@mentioned` will be remembered and sent a transcript of the notes at the end of the session.

Type `finished` to end the notes session.

This is what a typical notes session might look like:

![http://i.imgur.com/J4X65Sv.png](http://i.imgur.com/J4X65Sv.png)

### Warnings

The bot just stores incoming meeting notes messages unencrypted into memory. Buy beware.
