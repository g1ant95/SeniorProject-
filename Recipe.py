class Recipe:
	availableNum = 0
	requiredNum = 0
	percent = 0
	
	def __init__(self,name):
		
		self.ingredients = []
		self.name = name
		counter = 1
		entered = raw_input("Enter ingredient number " + str(counter) + " or 'done': ")
		while(entered != 'done'):
			self.ingredients.append(entered)
			counter += 1
			entered = raw_input("Enter ingredient number " + str(counter) + " or 'done': ")
		self.getrequiredNum()
		self.getavailableNum()
		
#sets the requiredNum variable
	def getrequiredNum(self):
		self.requiredNum = len(self.ingredients)
		print(self.requiredNum)
		
#gets the number of ingredients required to make recipe that user has in inventory
	def getavailableNum(self):
		for i in xrange(0,len(self.ingredients)):
			for j in xrange(0,len(inventory)):
				if self.ingredients[i] == inventory[j]:
					self.availableNum += 1
		self.percent = float(self.availableNum)/float(self.requiredNum)
		print(self.availableNum)
		print(self.percent)
	def display(self):
		print "Recipe Name: " + self.name
		print "Ingredient List: "
		print self.ingredients
		print "Number of Ingredients: " + str(len(self.ingredients))
		print "Percent of Ingredients Available: " + str(self.percent)
		
		
class RecipeList():
	def __init__(self):
		self.recipes = []
	
	def newRecipe(self, name):
		new = Recipe(name)
		self.recipes.append(new)
		
	def sort(self): 
		for i in xrange(0,len(self.recipes) - 1):
			for j in xrange(0, len(self.recipes)):
				if self.recipes[j].percent < self.recipes[j+1]: 
					temp = self.recipes[j]
					self.recipes[j] = self.recipes[j+1]
					self.recipes[j+1] = temp
		
	def displayall(self):
		print "Recipe List"
		print "Number of Recipes: " + str(len(self.recipes))
		for items in self.recipes:
			items.display()


		
#MAIN###################################################################################				

#inventory list is needed in order for getavailable() to work. 

inventory = ['eggs', 'bread', 'jelly']
list = RecipeList()

entered = raw_input("Enter new recipe or 'done': ") 
while(entered != 'done'):
	list.newRecipe(entered)
	entered = raw_input("Enter new recipe or 'done': ")

list.displayall()


	
	
	

