def main():
    textinput = convert(input("What time is it?: "))
    if textinput >= 7 and textinput <=8:
        print("breakfast time")
    elif textinput >= 12 and textinput <=13:
        print ("lunch time")
    elif textinput >= 18 and textinput <=19:
        print ("dinner time")

def convert(time):
    
    if time[len(time)-5:] == " a.m.":
        time = time[:-5]
        hours, minutes = time.split(":")
    elif time[len(time)-5:] == " p.m.":
        time = time[:-5]
        hours, minutes = time.split(":")
        hours = float(hours) + 12   
    else:
        hours, minutes = time.split(":")
    minconv = float(hours) + float(minutes)/60
    return minconv

main()