lst = ['a', 'b', 'c', 'd',
		'e', 'f', 'g', 'h',
		'i', 'j', 'k', 'l',
		'm', 'n', 'o', 'p',
		'q', 'r', 's', 't',
		'u', 'v', 'w', 'x',
		'y', 'z']

mot = input("Enter_word:	")
chaine = str()

def iftest(chaine, mot):
	if chaine == mot:
		print("Well done!!!!")

for i_1 in lst:
	chaine = i_1
	iftest(chaine, mot)

	for i_2 in lst:
		chaine = i_1 + i_2
		iftest(chaine, mot)
		print(chaine)