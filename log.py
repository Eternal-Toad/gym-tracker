lift = input("lift? ")
weight = input("weight? ")
reps = input("reps? ")
sets = input("sets? ")
print (lift, weight, "lb x", reps, "reps", sets, "sets")
volume = (int(weight) * int(reps) * int(sets))
print ("volume:", volume, "lb")
print("=== your history ===")
with open("savedlifts.txt", "a") as file:
    file.write (f"{lift} for {weight}lbs for reps {reps} and for sets {sets} for a total of {volume}lbs\n")
with open("savedlifts.txt", "r") as file:
    print(file.read())