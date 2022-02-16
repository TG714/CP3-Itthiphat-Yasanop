Distance = int(input("The distance in Km unit: "))
time = int(input("The time in minute unit: "))
convTimeInHr = time/60
speed = Distance/convTimeInHr
print("Avg.Speed is ",speed, "km/hr" )