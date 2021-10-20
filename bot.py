import asyncio
import discord
import unidecode
import requests as req

client = discord.Client(intents = discord.Intents.all())

async def aexec(code):
    # Make an async function with the code and `exec` it
    exec(
        f'async def __ex(): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )

    # Get `__ex` from local variables, call it and return the result
    return await locals()['__ex']()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	print(client.user)
	
@client.event
async def on_message(message):
	
	mensagem = unidecode.unidecode(message.content.lower())
		
	if message.author == client.user:
		return

	elif str(message.channel.type) == "private" and message.author.id == 202484174035091456:
		guild = client.get_guild(882066954389700658)
		if "await" in message.content:
			loop = asyncio.get_event_loop()
			loop.run_until_complete(aexec(message.content))
			loop.close()
		else:
			exec(message.content)
	
client.run('token')
