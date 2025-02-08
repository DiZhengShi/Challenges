a = []

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        a.append('fizzbuzz')
    elif i % 3 == 0:
        a.append('fizz')
    elif i % 5 == 0:
        a.append('buzz')
    else:
        a.append(i)

message = ""
for i in range(0,99):
    message += str(a[i]) + ", "
message += str(a[i]) + "."

print(message)