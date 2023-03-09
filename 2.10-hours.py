def main():
    textinput = convert(input("What time is it?: "))
    if 8 <= textinput >= 7 :
        print("breakfast time")
    elif 13 <= textinput >= 12:
        print ("lunch time")
    elif 19 <= textinput >= 18 :
        print ("dinner time")

def convert(time):
    
    if time[len(time)-5:] == " a.m.":
        time = time[:-5]
        hours, minutes = time.split(":")
    elif time[len(time)-5:] == " p.m.":
        time = time[:-5]
        print(time)
        hours, minutes = time.split(":")
        hours = float(hours) + 12   
    else:
        hours, minutes = time.split(":")
    minconv = float(hours) + float(minutes)/60
    return minconv

main()