
from autoModules import *
auto_modules('beautifulsoup4')
auto_modules('webbrowser')
auto_modules('requests')
auto_modules('re')
from bs4 import BeautifulSoup
from sys import exit
import requests
import re 
import webbrowser
import os

try :
	if os.name == 'nt' :
		os.system('cls')
	else :
		os.sytem('clear')
except :
	print('Error in clear screen !')

print("""
######################################################


      ___           ___                               
     /\__\         /\__\                      ___     
    /:/  /        /:/ _/_       ___          /\  \    
   /:/  /        /:/ /\__\     /\__\         \:\  \   
  /:/  /  ___   /:/ /:/ _/_   /:/__/          \:\  \  
 /:/__/  /\__\ /:/_/:/ /\__\ /::\  \      ___  \:\__\ 
 \:\  \ /:/  / \:\/:/ /:/  / \/\:\  \__  /\  \ |:|  | 
  \:\  /:/  /   \::/_/:/  /   ~~\:\/\__\ \:\  \|:|  | 
   \:\/:/  /     \:\/:/  /       \::/  /  \:\__|:|__| 
    \::/  /       \::/  /        /:/  /    \::::/__/  
     \/__/         \/__/         \/__/      ~~~~      


######################################################
""")

question = input('Type any question/subject/word : ')

words = question.split(' ')

url = "https://github.com/search?o=desc&q="+'+'.join(words)+"&s=stars&type=Repositories" # Creating the link
print(url)

################################## GETTING LINKS #############################################
mylist=[]
i=0
# try :
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('a', class_='v-align-middle')

for item in items :
	mylist.append("https://github.com"+item['href'])
	i+=1
	if i == 10 : # if you want more or less results just change the "10" 
		break
# except :
# print('Error !')
################################################# CHOICES #################################

print("""WHAT YOU WANNA DO WITH THE DATA :
	     1) Save them to a .txt file.
	     2) Open search results in browser.
	     3) Print them.
	     4) Exit """)

choices = [1,2,3,4]

while 1:
	choice = int(input('>'))
	if choice in choices:
		break
###########################################################################################
if choice == 1 :
	with open('Result_s.txt', 'w') as f:
		for item in mylist:
			f.write(item+'\n')
			f.write('')
	try :
		os.startfile(str(re.escape(os.getcwd())+'\\Result_s.txt')) #Pop up the Result_s.txt file
		""" i used the getcwd() method to get the current work directory 
			and added the file name to it, then i used the re.escape() method to replace
			single backslashes with double backslashes """

	except:
		print("error")

if choice == 2 :
	for item in mylist :
		webbrowser.open(item)
		"""this open all search results in the browser"""

if choice == 3 :
	for item in mylist :
		print(item+'\n')

if choice == 4 : 
	exit()

#############################################################################################

