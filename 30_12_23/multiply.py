text = [[4, 3, 8, ], [8, 3, 4, ], [6, 1, 8, ]]
r = 3
m = []
for i in range(r):
        m.append([int(x) for x in text[i]])
for i in m:
        print (i)