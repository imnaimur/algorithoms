import heapq
file = open('input.txt', 'r')
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
     temp[line[j]] = int(line[j+1])
   path[line[0]] = temp


dirpat.write(f"{path}\n")
output.write(f"{heuristics}\n")

def a_star(graph, heuristics, source, destination):
   pq = [[heuristics[source],0, source]]
   cost = {}
   for v in graph:
      cost[v] = float('inf')

   cost[source] = 0
   parent = {}

   while pq:
      s = heapq.heappop(pq)
      fn,acost,v = s[0],s[1],s[2]
      if v == destination:
         path = []
         while v in parent:
            path.append(v)
            v = parent[v]
         path.append(source)
         path.reverse()
         return path, cost[destination]

      for vertex, edge in graph[v].items():
         ncost = acost + edge 
         nfn = ncost + heuristics[vertex]  
            
         if nfn < cost[vertex]+heuristics[vertex]:
            cost[vertex] = ncost
            parent[vertex] = v
            heapq.heappush(pq, [nfn, ncost, vertex])

   return None, float('inf')



start_node = 'Sibiu'
goal_node = 'Bucharest'
way, distance = a_star(path, heuristics, start_node, goal_node)

print("Path",end=":")
for i in range(len(way)):
   if i != len(way) - 1:
      print(way[i],end=" --> ")
   else:
       print(way[i])

print(f"Total Distance: {distance} km")