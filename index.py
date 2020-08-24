#Vous pouvez suprimer ce code c'est juste pour le test

def main():
	print("Hello World!")
	print("Langage disponibles :\n\t-Java (J)  \n\t-Python3 (PY3)")
	Langages = ["PY3", "J"]
	LangageInitial = input("Quel est le langage du programe Initial:")
	if LangageInitial.upper() not in Langages:
		print("Langage non disponible")
		exit()
	LangageFinal = input("Quel est le langage du programe Final  :")
	if LangageInitial.upper() not in Langages:
		print("Langage non disponible")
		exit()
	if LangageInitial.upper() == LangageFinal.upper():
        	print("Traduction en cours...")
        	print("Ah non, pas besoin de traduction, c'est le même langage!")
	if LangageInitial.upper() == "J" and LangageFinal.upper() == "PY3":
        	JavaToPython3()
	if LangageInitial.upper() == "PY3" and LangageFinal.upper() == "J":
        	Python3ToJava()

def JavaToPython3():
	print("Java vers Python3")
def Python3ToJava():
	print("Python3 vers Java")

if __name__ == "__main__":
	main()

