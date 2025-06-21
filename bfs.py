from collections import deque

def bfs(graph, start_user):
    visited = set()
    queue = deque()
    suggestions = []

    queue.append(start_user)
    visited.add(start_user)

    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                suggestions.append(neighbor)
                queue.append(neighbor)
    return suggestions
