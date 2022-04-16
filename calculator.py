from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from math import sin, cos, tan, asin, acos, atan, exp, log

"""
Простенький калькулятор на Kivy
"""

def tg(x):
	return sin(x)/cos(x)

def ctg(x):
	return cos(x)/sin(x)

def arcsin(x):
	return asin(x)

def arccos(x):
	return acos(x)

def arctg(x):
	return atan(x)

def arcctg(x):
	if x == 0:
		return p / 2
	return atan(1/x)

def ln(x):
	return log(x)/log(e)

def lb(x):
	return log(x)/log(2)

def lg(x):
	return log(x)/log(10)

e = exp(1)
p = arccos(-1)
pi = p

Config.set("graphics", "resizable","0") #запрещает увеличивать или уменьшать окно
Config.set("graphics", "width","450") 
Config.set("graphics","height","450")

class MyApp(App):

	def build(self):
		self.text_writing = TextInput(font_size = 18)

		self.button_clear = Button(text = "clear", font_size = 17, on_press=self.clear)
		self.button_result = Button(text = "result",font_size = 17, on_press=self.result)

		gridlayout = GridLayout(cols = 2,size_hint=[1,0.1])
		gridlayout.add_widget(self.button_clear)
		gridlayout.add_widget(self.button_result)

		boxlayout = BoxLayout(orientation = "vertical")
		boxlayout.add_widget(self.text_writing)
		boxlayout.add_widget(gridlayout)

		return boxlayout

	def clear(self,target):
		self.text_writing.text = ""

	def result(self,target):
		text = self.text_writing.text.replace(" ","")
		try:
			if text != "":
				text = str(eval(text))
			if text != "None":
				self.text_writing.text = text
		except:
			self.text_writing.text = "Error"


if __name__ == "__main__":
	myapp = MyApp()
	myapp.run()