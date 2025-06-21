import pickle
import os

class Graph:
    def __init__(self, file_path="graph.pkl"):
        self.file_path = file_path
        self.graph = self.load_graph()

    def add_edge(self, user, friend):
        user, friend = user.lower(), friend.lower()
        self.graph.setdefault(user, [])
        self.graph.setdefault(friend, [])
        if friend not in self.graph[user]:
            self.graph[user].append(friend)
        if user not in self.graph[friend]:
            self.graph[friend].append(user)
        self.save_graph()

    def remove_edge(self, user, friend):
        user, friend = user.lower(), friend.lower()
        if friend in self.graph.get(user, []):
            self.graph[user].remove(friend)
        if user in self.graph.get(friend, []):
            self.graph[friend].remove(user)
        self.save_graph()

    def get_graph(self):
        return self.graph

    def save_graph(self):
        with open(self.file_path, "wb") as f:
            pickle.dump(self.graph, f)

    def load_graph(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                return pickle.load(f)
        return {}
