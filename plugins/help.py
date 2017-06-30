from slackbot.bot import respond_to

@respond_to('help')
def help(message):
    message.reply('help')
