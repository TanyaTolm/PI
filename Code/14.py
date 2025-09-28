a = "THE HOUSE IS UGLY. END"
count = 0
flag = False
g = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in range (len(g)):
    for j in range(len(a)):
        if g[i] == a[j]:
            count += 1

if ((a.startswith("THE") and a.endswith("END")) or
    (a.startswith("The") and a.endswith("end"))):
    print("Строка начинается с The и заканчивается end")

if "UGLY" in a:
    a = a.replace("UGLY", "beauty")
    print(f"В предложении заменены все ugly на beauty: {a}")


print(f"Длина строки равна {len(a)}")
print(f"Предложение в нижнем регистре: {a.lower()}")
print(f"Количество гласных в предложении: {count}")

