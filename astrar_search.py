file = open('input.txt','r')
output = open('output.txt', 'w')

heutistic = {}
actual_distance = {}

for i in file:
   line = file.readline().split()
   for j in range(0,len(line),2):
      heutistic[line[j]] = line[j+1]

print(heutistic)
         