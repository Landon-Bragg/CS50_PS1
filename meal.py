def main():
    answer = input("What time is it? ")
    time = convert(answer)
    
    #breakfast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")
    #lunch between 12:00 and 13:00
    if time >= 12 and time <= 13:
        print("lunch time")
    #dinner between 18:00 and 19:00
    if time >= 18 and time <= 19:
        print("dinner time")
    

def convert(time):
    hour, minute = time.split(":")

    new_minute = float(minute) / 60

    return float(hour) + new_minute

if __name__ == "__main__":

    main()