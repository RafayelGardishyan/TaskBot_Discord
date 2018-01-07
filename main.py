import discord
import asyncio
from db import dp as db

client = discord.Client()

db = db.db()
db.connect('Taskbot.sqlite3')

db.createtasktable()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('#:task'):
		task = message.content[7:]
		db.addtask(task, message.author)
		tmp = await client.send_message(message.channel, 'Adding Task ...')
		await client.edit_message(tmp, 'Added task {} for user {}.'.format(task, message.author))

	elif message.content.startswith('#:mytasks'):
		tmp = await client.send_message(message.channel, 'Getting Tasks ...')
		tasks = db.gettasks(message.author)
		await client.edit_message(tmp, 'Your tasks\n {} '.format(tasks))
		
	elif message.content.startswith('!exit'):
		db.disconnect()
		raise SystemExit("Exited with !exit command")

client.run('token')
