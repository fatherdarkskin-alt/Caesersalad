
choice = input("Do you want to encrypt or decrypt E/D")
precode = input("What do you want your messsgae to be?").strip()
simplechoice = choice.strip().lower()
cypher = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

postcode= []

if choice == "e":
	for c in precode :

		if c not in cypher:
			postcode.append(c)
		else:
			num = cypher.index(c) 
			i = num + 6
			if i > 51:
				i -=  51
			postcode.append(cypher[i])
	print("".join(postcode))

if choice == "d":
	for c in precode :

		if c not in cypher:
			postcode.append(c)
		else:
			num = cypher.index(c) 
			i = num - 6
			if i > 51:
				i -=  51
			postcode.append(cypher[i])
	print("".join(postcode))
