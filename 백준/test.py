vehicles = ['scooter\n', 'bike\n', 'car\n']
f = open('vehicles.txt', 'w')
for v in vehicles:
    f.write(v)
f.close()
f = open('vehicles.txt', 'r')
line = f.readlines()
print(line)