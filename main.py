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
		tmp = await client.send_message(message.channel, 'Adding Task ...')
		task = message.content[7:]
		db.addtask(task, message.author)
		await client.edit_message(tmp, 'Added task {} for user {}.'.format(task, message.author))

	elif message.content.startswith('#:mytasks'):
		tmp = await client.send_message(message.channel, 'Getting Tasks ...')
		tasksraw = db.gettasks(message.author)
		tcount = 0
		tasks = ""
		for task in tasksraw:
			count = tcount + 1
			tcount += 1
			tasks += "{}: {}\n".format(count, task[1])
			
		if len(tasks) != 0:
			await client.edit_message(tmp, 'Tasks for {}\n{} '.format(message.author,tasks))
		else:
			await client.edit_message(tmp, 'You have no tasks')
			
	elif message.content.startswith('#:deltask'):
		tmp = await client.send_message(message.channel, 'Deleting Task ...')
		task = message.content[10:]
		author = message.author
		db.deletetask(task, author)
		await client.edit_message(tmp, 'Deleted task {} from {}\'s tasks '.format(task, author))	
		
	elif message.content.startswith('!'):
		db.disconnect()
		raise SystemExit("Exited with !exit command")

client.run('Mzk5MjI4NjM4NTY3ODU4MTc3.DTOZ6Q.Svv0IT8cbq3Cw4nDyyWJfznCEJw')
