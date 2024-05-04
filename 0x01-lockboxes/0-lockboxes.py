#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """finding keys to unlock the boxes"""
    if not boxes:
        return False

    visited = set()
    visited.add(0)
    queue = [0]

    while queue:
        box_index = queue.pop(0)
        keys = boxes[box_index]
        for key in keys:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)
