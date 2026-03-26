data = [1,2,3,4,5,0,0,0]

print(min(data), max(data), sum(data))

print("----------------------")

for x in data:
    print(x)

print("----------------------")

for n, x in enumerate(data):
    print(n,x)

print("----------------------")

for n in range(len(data)):
    print(data[n])

