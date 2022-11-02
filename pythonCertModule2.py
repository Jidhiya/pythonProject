x = float(input("Enter value for x: "))
y = (1/(x+1/(x+1/(x+1/x))))
print("y =", y)




hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour = (hour + dura//60 + (mins+ dura%60)//60)%24
mins = (mins+ dura%60)%60
print(hour,":",mins,sep="")



