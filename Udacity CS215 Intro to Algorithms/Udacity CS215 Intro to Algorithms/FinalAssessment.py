from heap import *
from operator import itemgetter
from collections import defaultdict
from math import log, exp

def reform_graph(G):
	new_graph = defaultdict(dict)
	for node in G:
		for neighbor in G[node]:
			new_graph[node][neighbor] = log(G[node][neighbor]) * -1
	return new_graph

def maximize_probability_of_favor(G, v1, v2):

	def _count_edges():
		return sum([len(G[v]) for v in G])

	G = reform_graph(G)

	node_num = len(G.keys())
	edge_num = _count_edges()

	if edge_num * log(node_num) <= node_num ** 2:
		dist_dict = dijkstra_heap(G, v1)
	else:
		dist_dict = dijkstra_list(G, v1)

	path = []
	node = v2
	while True:
		path += [node]
		if node == v1:
			break
		_, node = dist_dict[path[-1]]

	path = list(reversed(path))
	prob_log = dist_dict[v2][0] * -1

	return path, exp(prob_log)


def dijkstra_heap(G, a):

	first_entry = (0, a, None)
	heap = [first_entry]

	location = {first_entry:0}
	dist_so_far = {a:first_entry}
	final_dist = {}
	while len(dist_so_far) > 0:
		dist, node, parent = heappopmin(heap, location)
		# lock it down!
		final_dist[node] = (dist, parent)
		del dist_so_far[node]
		for x in G[node]:
			if x in final_dist:
				continue
			new_dist = G[node][x] + final_dist[node][0]
			new_entry = (new_dist, x, node)
			if x not in dist_so_far:
				# add to the heap
				insert_heap(heap, new_entry, location)
				dist_so_far[x] = new_entry
			elif new_entry < dist_so_far[x]:
				# update heap
				decrease_val(heap, location, dist_so_far[x], new_entry)
				dist_so_far[x] = new_entry
	return final_dist


def dijkstra_list(G, a):
	dist_so_far = {a:(0, None)} #keep track of the parent node
	final_dist = {}
	while len(final_dist) < len(G):
		node, entry = min(dist_so_far.items(), key=itemgetter(1))
		# lock it down!
		final_dist[node] = entry
		del dist_so_far[node]
		for x in G[node]:
			if x in final_dist:
				continue
			new_dist = G[node][x] + final_dist[node][0]
			new_entry = (new_dist, node)
			if x not in dist_so_far:
				dist_so_far[x] = new_entry
			elif new_entry < dist_so_far[x]:
				dist_so_far[x] = new_entry
	return final_dist

# Test

def test():
	G = {'a':{'b':.9, 'e':.5},
		 'b':{'c':.9},
		 'c':{'d':.01},
		 'd':{},
		 'e':{'f':.5},
		 'f':{'d':.5}}
	path, prob = maximize_probability_of_favor(G, 'a', 'd')
	assert path == ['a', 'e', 'f', 'd']
	assert abs(prob - .5 * .5 * .5) < 0.001

if __name__ == '__main__':
	test()
	print "Test passes"