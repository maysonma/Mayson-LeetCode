"""
s1, s2 = {}
s1.add(start)
s2.add(end)
step = 0
while s1 and s2:
	step += 1
	swap(s1, s2)
	s = {}
	for node in s1:
		new_nodes = expand(node)
		if any(new_nodes) in s2: return step + 1
		s.append(new_nodes)
	s1 = s
return NOT_FOUND
"""
