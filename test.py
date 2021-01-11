lists = "DL","MH","TN","HP","HR","PB"
number_plates_DL = "DL ABC 9874","DL ERT 3243"
number_plates_MH = "MH WDC 2312","MH DFG 6587"
number_plates_PB = "PB EDF 4543","PB HJT 3455"
number_plates_TN = "TN SFD 4352","TN ESF 2434"
number_plates_HP = "HP DFG 3241","HP ASD 9808"
number_plates_HR = "HR SDF 3242","HR SEF 9222"

number_plates = ""
plate = input("PLEASE ENTER THE CODE OF THE CITY.")
#print(number_plates)

if plate == "DL":
    number_plates = number_plates_DL
if plate == "MH":
    number_plates = number_plates_MH
if plate == "TN":
    number_plates = number_plates_TN
if plate == "HP":
    number_plates = number_plates_HP
if plate == "HR":
    number_plates = number_plates_HR
if plate == "PB":
    number_plates = number_plates_PB


def num_inp():

    u = input("WHICH NUMBER PLATE YOU WANT TO SEE ?")
    if u in number_plates:
        print("YOU ENTERED -",u)
    elif u == "show all" or u == "SHOW ALL" or u == "Show all" or u == "show All":
        print(number_plates)
    else:
        print("NOTHING FOUND LIKE THIS, FOR THIS CITY.")



if plate == 'DL':
    print("OKAY SO IN",lists[0])
    num_inp()

if plate == "MH":
    print("OKAY SO IN",lists[1])
    num_inp()

if plate == "TN":
    print("OKAY SO IN",lists[2])
    num_inp()

if plate == "HP":
    print("OKAY SO IN",lists[3])
    num_inp()

if plate == "HR":
    print("OKAY SO IN",lists[4])
    num_inp()

if plate == "PB":
    print("OKAY SO IN",lists[5])
    num_inp()
