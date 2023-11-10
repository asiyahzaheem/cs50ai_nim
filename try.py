q = {('hi', 'bye'): 3, ('to', 'a'): 1, ('hi', 'damn'): 4}
vals = []
for key in q.keys():
    if key[0] == 'hi':
        vals.append(q[key])
print(vals)
print(max(vals))