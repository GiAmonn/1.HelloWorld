def main():
    textinput = convert(input("What time is it?: "))
    if textinput >= 7 and textinput <=8:
        print("breakfast time")
    elif textinput >= 12 and textinput <=13:
        print ("lunch time")
    elif textinput >= 18 and textinput <=19:
        print ("dinner time")

def convert(time):
    hours, minutes = time.split(":")    
    minc = float(hours) + float(minutes)/60
    return minc

main()