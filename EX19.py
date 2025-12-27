grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

A = 0
B = 0
C = 0
below_70 = 0

for g in grades:
    if g >= 90:
        A += 1
    elif g >= 80:
        B += 1
    elif g >= 70:
        C += 1
    else:
        below_70 += 1

print("A grade:", A)
print("B grade:", B)
print("C grade:", C)
print("Below 70:", below_70)
