# Codeniacs FLL Taskbot

import discord
import asyncio
from db import dp as db

client = discord.Client()

db = db.db()
db.connect('Taskbot.sqlite3')
db.cursor()
db.createtasktable()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name="Prefix: '#:'"))

@client.event
async def on_message(message):
	if message.content.startswith('#:task'):
		task = message.content[7:]
		tmp = await client.send_message(message.channel, 'Adding Task ...')
		await client.edit_message(tmp, 'Added task {} for user {}.'.format(task, message.author))

	elif message.content.startswith('#:mytasks'):
		tmp = await client.send_message(message.channel, 'Getting Tasks ...')
		tasksraw = db.gettasks(message.author)
		tcount = 0
		tasks = []
		for task in tasksraw:
			count = tcount + 1
			tcount += 1
			name = task[1]
			tasks += "{} : {}".format(count, name)
			
			
		await client.edit_message(tmp, 'Your tasks\n {} '.format(tasks))
		
	elif message.content.startswith('!exit'):
		db.disconnect()
		raise SystemExit("Exited with !exit command")

client.run('Mzk5MjI4NjM4NTY3ODU4MTc3.DTOZ6Q.Svv0IT8cbq3Cw4nDyyWJfznCEJw')
