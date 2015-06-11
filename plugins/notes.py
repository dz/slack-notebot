from slackbot.bot import respond_to
from slackbot.bot import listen_to
from itertools import chain
import re

AT_USER_MATCHER = re.compile(r'(\<@(\w+)\>)')

NoteStore = {}

def start_taking(userid):
    NoteStore[userid] = []

def stop_taking(userid, client):
    notes = NoteStore.pop(userid, [])
    users = client.users
    user_ids = list(chain.from_iterable([get_user_ids(note) for note in notes]))
    import pdb; pdb.set_trace()
    return "\n".join(replace_user_ids(note, users) for note in notes)

def add_note(userid, note):
    NoteStore[userid].append(note)

def get_user(message):
    return message.body['user']

def get_text(message):
    return message.body['text']

def user_is_taking_notes(userid):
    return userid in NoteStore

def get_user_ids(text):
    return [m[1] for m in AT_USER_MATCHER.findall(text)]

def replace_user_ids(text):
    pass

@respond_to('start')
def start_notes(message):
    userid = get_user(message)
    text = get_text(message)
    if user_is_taking_notes(userid):
        add_note(userid, text)
    else:
        message.reply('*Starting notes*')
        message.reply('(Type `finished` to stop taking notes)')
        start_taking(userid)

@respond_to('finished')
def finish_notes(message):
    userid = get_user(message)
    text = get_text(message)
    if user_is_taking_notes(userid):
        notes = stop_taking(userid, message._client)
        message.reply("```%s```" % notes)
    else:
        message.reply('Error. Type `start` to start taking notes')

@respond_to('(.*)')
def take_notes(message, something):
    userid = get_user(message)
    text = get_text(message)
    if text == "finished" or text == "start":
        return
    if user_is_taking_notes(userid):
        add_note(userid, text)
    else:
        message.reply('Error. Type `start` to start taking notes')
