from collections import deque
file = open('input.txt','r')
output = open('output.txt', 'w')
dirpat = open('ditpath.txt', 'w')

heuristics = {}
path = {}
n = 20

for i in range(n):
   temp = {}
   line = file.readline().split()
   heuristics[line[0]] = int(line[1])
   for j in range(2,len(line),2):
     temp[line[j]] = line[j+1]
   path[line[0]] = temp

# dirpat.write(f"{path}")

# for i,j in heuristics.items():
#    output.write(f"{i}: {j}\n")
# output.write(f"{heuristics}")
def dfs(path,root,goal):
   visited = set()
   q = deque([root])
   while q:
      v = q.popleft()
      visited.add(v)
      if v == goal:   
         return v
      else:
         for i in path.values():
            for j in i:
               if j not in visited:
                  q.append(j)
   print(visited)
      

dfs(path,"Arad","Sibiu")


# print(heuristics)