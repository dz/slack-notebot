#!/usr/bin/env python
import sys
import logging
import logging.config
from slackbot import settings
from slackbot import dispatcher
from slackbot.bot import Bot

# monkey patch slackbot
def new_filter(self, msg):
    text = msg.get('text', '')
    msg['text'] = text
    return msg

dispatcher.MessageDispatcher.filter_text = new_filter

def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.DEBUG)
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
