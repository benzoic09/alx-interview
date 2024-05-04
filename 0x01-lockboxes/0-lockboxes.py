#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """finding keys to unlock the boxes"""
    if not boxes:
        return False

    visited = set()
    queue = boxes[0]

    visited.add(0)
    while queue:
        key = queue.pop(0)
        if key < len(boxes) and key not in visited:
            queue.extend(boxes[key])
            visited.add(key)

    return len(visited) == len(boxes)
