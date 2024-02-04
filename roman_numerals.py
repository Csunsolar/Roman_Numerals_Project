rn_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

rn_response = input("Type in Roman Numerals Here: ")
addition = ""
add_list = []
sub_list = []
enumerate(rn_response)

#check to make sure that length of roman numeral is valid
if 1 < len(rn_response) <= 7:
    x, y = [0, 1]
    for q in range(len(rn_response)-1):
        if y <= len(rn_response) and rn_dict.get(rn_response[x]) >= rn_dict.get(rn_response[y]):
            addition = True
            add_list.append(rn_dict.get(rn_response[x]))
            x += 1
            y += 1
            if x == len(rn_response) - 1:
                add_list.append(rn_dict.get(rn_response[x]))
                break
        elif y < len(rn_response):
            #gets the difference between the smaller roman numeral and the larger roman numeral
            addition = True
            z = rn_dict.get(rn_response[y]) - rn_dict.get(rn_response[x])
            sub_list.append(z)
            x += 2
            y += 2
        else:
            break
       
elif len(rn_response) > 7:
    print("Invalid. Roman Numerals can only be 7 characters long")
else:    
    print(rn_dict.get(rn_response))

if addition == True:
    answer = sum(add_list) + sum(sub_list)
    print(answer)