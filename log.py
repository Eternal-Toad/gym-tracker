from datetime import date
def calc_volume(weight, reps, sets):
    return(weight * reps * sets)
today = date.today()
print(f"today is {today}")
logs = 0
total_volume = 0
while True:
    lift = input("lift? ")
    if lift == "done":
        break
    weight = input("weight? ")
    reps = input("reps? ")
    sets = input("sets? ")
    print (lift, weight, "lb x", reps, "reps", sets, "sets")
    try:
        volume = calc_volume(int(weight), int(reps), int(sets))
    except ValueError:
        print("please type a number")
        continue
    print ("volume:", volume, "lb")
    logs = logs + 1
    total_volume = total_volume + volume
    with open("savedlifts.txt", "a") as file:
        file.write (f"{today} | {lift} | {weight}lbs x reps {reps} x sets {sets} | {volume}lbs\n")
print(f"you logged {logs} lifts today.\n")
print(f"your total volume is {total_volume}\n")
print("=== your history ===")
with open("savedlifts.txt", "r") as file:
    print(file.read())