import queue


def forward_and_back(target):
    q = queue.Queue()
    q.put((0, 1, 0))
    while not q:
        pos, delta, depth = q.get()
        j1 = pos + delta
        j2 = pos - delta
        if target == j1 or target == j2:
            return depth
        else:
            q.put((j1, delta + 1, depth + 1))
            q.put((j2, delta + 1, depth + 1))