

name = input("Gib deinen Namen ein: ")
print("Dein Name ist: "+ name+".")

input_string = input("Gib deine Noten mit einem Leerzeichen unterteilt ein: ")
print("Du hast, " + input_string, "eingegeben.")

grades= input_string.split()

for i in range(len(grades)):
    grades[i] = float(grades[i])

average_grade = sum(grades) / len(grades)

print("Durchschnitt = "+ str(average_grade))