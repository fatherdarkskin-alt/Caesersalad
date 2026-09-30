
precode = input("What do you want your messsgae to be?").strip()

cypher = "abcdefghijklmnopqrstuvwxyz"

postcode= []

precodesimple = precode.lower().replace(' ', '')

for c in precodesimple :
	num = cypher.index(c) 
	i = (num + 6) % len(cypher)
	postcode.append(cypher[i])
print("".join(postcode))

	# if precode[c] == cypher[n]:
	# 	cypher.index[+5]
	# 	if cypher.index[] > 25:
	# 		cypher[-25]

