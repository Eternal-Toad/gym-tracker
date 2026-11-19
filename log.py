from datetime import date
today = date.today()
print(f"today is {today}")
while True:
    lift = input("lift? ")
    if lift == "done":
        break
    weight = input("weight? ")
    reps = input("reps? ")
    sets = input("sets? ")
    print (lift, weight, "lb x", reps, "reps", sets, "sets")
    volume = (int(weight) * int(reps) * int(sets))
    print ("volume:", volume, "lb")
    with open("savedlifts.txt", "a") as file:
        file.write (f"todays date is {today} and todays lift is {lift} for {weight}lbs for reps {reps} and for sets {sets} for a total of {volume}lbs\n")
print("=== your history ===")
with open("savedlifts.txt", "r") as file:
    print(file.read())