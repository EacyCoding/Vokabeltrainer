import random
class Entry:
	def __init__(self, german, other):
		self.german = german
		self.other = other

vocabulary = [Entry("hallo", "hello")]
	
def vocab_input():
  lang = input("Welche Sprache möchtest du lernen?").capitalize()
	while True:
		german = input("Deutsches Wort: ")
		other = input(f"{lang}es Wort: ")
		if german == "#fertig" or other == "#fertig":
			return
		vocabulary.append(Entry(german, other)
		
def test():
	while True:
		i = random.randint(0,len(vocabulary)-1)
		other = input(f"{lang}e Übersetzung von " + vocabulary[i].german + ": ")
		if other == "#fertig":
			return
		if vocabulary[i].other == other:
			print("Richtig!")
		else:
			print("Leider falsch. Richtige Antwort: " + vocabulary[i].other)
			
def print_all():
	for word in vocabulary:
		print(vocabulary.german + " - " + eintrag.vocabulary)

while True:
	order = input("Befehl: ").lower()
	if order == "eingabe":
		vocab_input()
	elif order == "abfrage":
		test()
	elif order == "beenden":
		break
	elif order == "ausgabe":
		print_all()
	else:
		print("Kein bekannter Befehl. Befehle: eingabe, abfrage, ausgabe oder beenden")
