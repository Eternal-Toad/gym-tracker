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
    try:
        volume = (int(weight) * int(reps) * int(sets))
    except ValueError:
        print("please type a number")
        continue
    print ("volume:", volume, "lb")
    with open("savedlifts.txt", "a") as file:
        file.write (f"{today} | {lift} | {weight}lbs x reps {reps} x sets {sets} | {volume}lbs\n")
print("=== your history ===")
with open("savedlifts.txt", "r") as file:
    print(file.read())