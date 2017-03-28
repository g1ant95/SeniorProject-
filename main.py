#FoodApp
import kivy
import random

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty



class Test(TabbedPanel):
    pass
	
class MainScreen(TabbedPanel, Screen):
    pass

class InventoryScreen(Screen):
	pass

class RecipeScreen(Screen):
    pass
	
class ScreenManagement(ScreenManager):
    pass
	
class MyAccordionItem(AccordionItem):
    pass

class MyInputScreen(BoxLayout):
	pass
	
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

	
class MyAccordion(Accordion):
    def __init__(self, **kwargs):
        super(MyAccordion, self).__init__(**kwargs)

        for i in xrange(1):
			accordionitem = MyAccordionItem(title = str(1))
			accordionitem.add_widget(Label(text = 'Hello'))
			self.add_widget(accordionitem)
			for i in xrange(1):
				accordionitem = MyAccordionItem(title = str(2))
				accordionitem.add_widget(Label(text = 'Yup'))
				self.add_widget(accordionitem)
			for i in xrange(1):
				accordionitem = MyAccordionItem(title = str(3))
				accordionitem.add_widget(Label(text = 'Gary'))
				self.add_widget(accordionitem)


presentation = Builder.load_file("food.kv")				

class FoodApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    FoodApp().run()

	
	#inventory list is needed in order for getavailable() to work. 

inventory = ['eggs', 'bread', 'jelly']
list = RecipeList()

entered = raw_input("Enter new recipe or 'done': ") 
while(entered != 'done'):
	list.newRecipe(entered)
	entered = raw_input("Enter new recipe or 'done': ")

list.displayall()