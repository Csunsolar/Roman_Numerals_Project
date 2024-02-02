rndict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

r_numerals = input("Type in Roman Numerals Here: ")


if 1 < len(r_numerals) <= 4:
    x, y = [0, 1]
    for q in range(len(r_numerals)-1):
        enumerate(r_numerals)
        if rndict.get(r_numerals[x]) >= rndict.get(r_numerals[y]):
            addition = True
            x += 1
            y += 1
        else:
            addition = False
elif len(r_numerals) > 4:
    print("invalid")
else:    
    addition = True

if addition == True:
    r_list = []
    for a in r_numerals:
       r_list.append(rndict.get(a))
    print(sum(r_list))

print(addition)
#printing bool




       


