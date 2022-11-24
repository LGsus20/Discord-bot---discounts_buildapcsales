import discord
import random
import reddit_scrapping
#import time

TOKEN = #Need to include token 
MINUTES_AGO = 60

client = discord.Client()

@client.event
async def on_ready():
    print("USER ID: {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #print(f'{username}: {user_message} ({channel})')

    if message.channel.name == 'descuentos-juegosgratis':
     #discount section
        if (user_message.lower() == 'discount') or (user_message.lower() == 'discounts'):
            for every_message in reddit_scrapping.last_deal():
                if (every_message[2] < MINUTES_AGO):
                    i = 0
                    for element in every_message:
                        i = i + 1
                        if i == 3:
                            i = 0
                            await message.channel.send(f'Publicado hace {element} minutos')
                        else:
                            await message.channel.send(element)
     #randomizer
        elif user_message.lower() == '!random':
            response = f'Random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return

client.run(TOKEN)
