# Created by Eacy with much love and effort! Hope you like it <3

import random
import os
from colorama import Fore, Style

class Entry:
	def __init__(self, german, other):
		self.german = german
		self.other = other		

vocabulary = []

def vocab_input():
	while True:
		german = input("Deutsches Wort: ").lower().capitalize()
		if german != "#back":
			other = input(f"{lang}es Wort: ").lower()
		# Quit instantly if '#back' is entered
		while german != "#back" and other != "#back":
			# Append words to vocabulary list
			vocabulary.append(Entry(german, other))
			german = input("Deutsches Wort: ").lower().capitalize()
			if german != "#back":
				other = input(f"{lang}es Wort: ").lower()
		else:
			return
		
def test():
	while True:
		# Choose random word out of vocabulary list
		i = random.randint(0, len(vocabulary)-1)
		# Other language to German
		if i%2 == 0:
			searched_word = input(f"{lang}e Übersetzung von {vocabulary[i].german}:")
			if searched_word == "#back":
				return
			if searched_word == vocabulary[i].other:
				print("Richtig!")
			else:
				print(f"Leider falsch. Richtige Antwort: {vocabulary[i].other}")
		# German to other language
		else:
			searched_word = input(f"Deutsche Übersetzung von {vocabulary[i].other}:")
			if searched_word == "#back":
				return
			if searched_word == vocabulary[i].german:
				print("Richtig!")
			else:
				print(f"Leider falsch. Richtige Antwort: {vocabulary[i].german}")
		
			
def print_all():
	print(f"{Fore.GREEN}Vokabeln:{Style.RESET_ALL}"
	f"\nDeutsch - {lang}\n")
	for word in vocabulary:
		print(f"{word.german} - {word.other}")

def load_vocab():
	with open('vocabulary.txt', 'r') as f:
		content = [line.strip('\n') for line in f]
		f.close()
		for wpair in content:
			vocabulary.append(Entry(wpair.split(" - ")[0], wpair.split(" - ")[1]))

def write_file():
	for word in vocabulary:
		f.write(f"{word.german} - {word.other}\n")
	f.close()

def search_vocab_file(path, extension):
    """ 
       extension with leading point, for example: ".png"
    """
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == extension:
                yield os.path.join(root, filename)
# Main		
if __name__ == '__main__':
	file_list = list(search_vocab_file('.', '.txt'))
	if len(file_list) >= 1:
		load = input("Es liegt eine gespeicherte Vokabelliste vor, willst du sie laden? \n>>").lower()
		if load == "ja":
			load_vocab()
		elif load == "nein":
			pass
		else:
			print("Unbekannte Eingabe. Bitte antworte mit ja oder nein.")

	lang = input("Welche Sprache möchtest du lernen?\n>>").lower().capitalize()

	while True:
		order = input("****************************************************************************************************"
		"\nDu kannst eine Vokabelliste anlegen, dich in beide Sprachen abfragen, oder die Vokabelliste ausgeben lassen."
		f"\nBEFEHLLISTE: '{Fore.GREEN}eingabe{Style.RESET_ALL}', '{Fore.GREEN}abfrage{Style.RESET_ALL}', '{Fore.GREEN}ausgabe{Style.RESET_ALL}', '{Fore.GREEN}beenden{Style.RESET_ALL}'."
		f"\nDu kannst jederzeit mit '{Fore.GREEN}#back{Style.RESET_ALL}' zum Menü zurückkehren."
		"\n****************************************************************************************************"
		"\nWas willst du tun? Befehl: \n>>").lower()
		if order == "eingabe":
			vocab_input()
		elif order == "abfrage":
			test()
		elif order == "beenden":
			while True:
				inp = input("Willst du die Vokabelliste speichern? \n>>").lower()
				# Speichern 
				if inp == "ja":
					try:
						with open("vocabulary.txt", "x") as f:
							write_file()
						print("Quit.")
						quit()
					# File already exists
					except:
						user = input("Es existiert bereits eine Vokabelliste, willst du sie überschreiben? \n>>").lower()
						# Overwrite old file 
						if user == "ja":
							with open("vocabulary.txt", "w") as f:
								write_file()
							print("Quit.")
							quit()
						# Create new one with other filename
						elif user == "nein":
							while True:
								filename = str(input("Gib einen Dateinamen an.(z.B.filename.txt) \n>>").lower())
								if filename != "#back":
									with open(filename, "w") as f:
										write_file()
									print("Quit.")
									quit()
								else:
									break
						else:
							print("Unbekannte Eingabe.\n")
				# Nicht Speichern
				elif inp == "nein":
					print("OK, bis zum nächsten Mal!")
					quit()
				else:
					print("Unbekannte Eingabe. Bitte antworte mit ja oder nein.")
		elif order == "ausgabe":
			print_all()
		else:
			print(f"Kein bekannter Befehl. \nBEFEHLLISTE: '{Fore.GREEN}eingabe{Style.RESET_ALL}', '{Fore.GREEN}abfrage{Style.RESET_ALL}', '{Fore.GREEN}ausgabe{Style.RESET_ALL}', '{Fore.GREEN}beenden{Style.RESET_ALL}'.")
