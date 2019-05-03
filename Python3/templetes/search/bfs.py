"""
q.push(start)
step = 0
while q:
	step += 1
	size = len(q)
	for i in range(size):
		node = q.popleft()
		new_nodes = expand(node)
		if goal in new_nodes:
			return step + 1
		q.extend(new_nodes)
return NOT_FOUND
"""
