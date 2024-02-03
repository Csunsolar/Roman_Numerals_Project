rndict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

r_numerals = input("Type in Roman Numerals Here: ")
addition = ""

#check to make sure that length of roman numeral is valid
if 1 < len(r_numerals) <= 7:
    x, y = [0, 1]
    for q in range(len(r_numerals)-1):
        enumerate(r_numerals)
        if rndict.get(r_numerals[x]) >= rndict.get(r_numerals[y]):
            addition = True
            x += 1
            y += 1
        else:
            addition = False
            #gets the difference between the smaller roman numeral and the larger roman numeral
            z = rndict.get(r_numerals[x+1]) - rndict.get(r_numerals[x])
            x += 1
            y += 1
            for q in range(len(r_numerals)-1):
                if rndict.get(r_numerals[x]) >= rndict.get(r_numerals[y]):
                    x += 1
                    y += 1            
elif len(r_numerals) > 7:
    print("Invalid. Roman Numerals can only be 7 characters long")
else:    
    addition = True

#makes list of dict values for each character of r_numerals
r_list = []
for a in r_numerals:
   r_list.append(rndict.get(a))

if addition == True:
    print(sum(r_list))
elif addition == False:
    print(sum(r_list[:x]) + z)




       


