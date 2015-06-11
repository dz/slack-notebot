from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('foo')
def bar(message):
    message.reply('bar')
