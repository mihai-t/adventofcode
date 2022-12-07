import os
from copy import copy


def is_conn(st, en, edges):
    return (st, en) in edges or (en, st) in edges


paths = []
paths_p2 = []


def get_unique_paths(node, visited, all_nodes, edges):
    global paths
    visited.append(node)
    if node == 'end':
        paths.append(visited)
    else:
        for n in all_nodes:
            if n in visited and n.islower():
                continue
            if not is_conn(node, n, edges):
                continue
            get_unique_paths(n, copy(visited), all_nodes, edges)


def is_small_cave_twice(visited):
    count = {}
    for v in visited:
        if v.islower():
            count[v] = count.get(v, 0) + 1
    maxx = max(count.values())
    return maxx > 1


def get_unique_paths_p2(node, visited, all_nodes, edges):
    global paths_p2
    visited.append(node)
    if node == 'end':
        paths_p2.append(visited)
    else:
        for n in all_nodes:
            if n == 'start' or not is_conn(node, n, edges):
                continue

            if n.islower() and n in visited and is_small_cave_twice(visited):
                continue

            get_unique_paths_p2(n, copy(visited), all_nodes, edges)


if __name__ == '__main__':
    with open(os.path.join('inputs', 'day12.txt'), 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip(), lines))
        edges = list(map(lambda x: x.split('-'), lines))
        edges = set(map(lambda x: (x[0], x[1]), edges))
        all_nodes = set(sum(edges, ()))
    get_unique_paths('start', [], all_nodes, edges)
    print(len(paths))
    get_unique_paths_p2('start', [], all_nodes, edges)
    print(len(paths_p2))
