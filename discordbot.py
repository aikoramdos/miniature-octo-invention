from discord.ext import commands
from os import getenv
import traceback

import smtplib
from email.message import EmailMessage


bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    # Open the plain text file whose name is in textfile for reading.
    print "test!!"
    msg = EmailMessage()
    msg.set_content("test")

    msg['Subject'] = 'test message'
    msg['From'] = "test@example.jp"
    msg['To'] = "65108" + "@" + "aikogakuen.net"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    
    


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)

