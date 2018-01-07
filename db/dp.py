import sqlite3 as s

class db():
	attributes = {
		'db': "",
		'cursor': "",
		}

	def connect(self, dbname):
		self.attributes['db'] = s.connect(dbname)
		
	def disconnect(self, ):
		self.attributes['db'].close()
		
	def cursor(self, ):
		self.attributes['cursor'] = self.attributes['db'].cursor()

	def createtasktable(self, ):
		try:
			query = "CREATE TABLE tasks(id INTEGER PRIMARY KEY, task TEXT, author TEXT)"
			self.attributes['cursor'].execute(query)
			self.attributes['db'].commit()
		except:
			print("Table already exists")

	def addtask(self, task, author):
		try:
			query = "INSERT INTO tasks(task, author) VALUES(?,?)"
			self.attributes['cursor'].execute(query, (task, author))
			self.attributes['db'].commit()
		except:
			print("Error: Can not add task to database")
			return False

	def deletetask(self, task, author):
		try:
			query = "DELETE FROM tasks WHERE task = ? AND author = ?"
			self.attributes['cursor'].execute(query, (task, author))
			self.attributes['db'].commit()
		except:
			print("Error: Can not delete task {}".format(task))
			return False

	def gettasks(self, author):
		try:
			query = "SELECT task WHERE author=?"
			self.attributes['cursor'].execute(query, (author))
			return self.attributes['cursor'].fetchall()
		except:
			print("Error: Can not get tasks for user {}".format(author))
			return False