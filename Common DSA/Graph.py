# https://www.youtube.com/watch?v=UyeBa0OCh2I&list=PLPbgcxheSpE3NlJ30EDpxNYU6P2Jylns8&index=13

class Graph:
    def __init__(self, edges):
        """
        It takes a list of tuples (edges) and creates a dictionary (routes) where the keys are the
        startpoints and the values are the endpoints
        
        :param edges: a list of tuples, where each tuple is a startpoint and endpoint
        """
        self.edges = edges
        self.routes = {}

        for startpoint, endpoint in self.edges:
            if startpoint in self.routes:
                self.routes[startpoint].append(endpoint)
            else:
                self.routes[startpoint] = [endpoint]

        print(self.routes)

    def get_path(self, startpoint, endpoint, path=[]):
        """
        It takes a startpoint and endpoint and returns a list of all possible paths between the two
        points.
        """
        path = path + [startpoint]

        if startpoint == endpoint:
            return [path]
        if startpoint not in self.routes:
            return []

        possible_paths = []
        for point in self.routes[startpoint]:
            if point not in path:
                new_path = self.get_path(point, endpoint, path)
                for points in new_path:
                    possible_paths.append(points)

        return possible_paths

    def get_shortest_path(self,startpoint, endpoint, path=[]):
        """
        If the startpoint is the endpoint, return the path. If the startpoint is not in the routes,
        return None. If the startpoint is in the routes, find the shortest path from the startpoint to
        the endpoint
        
        :return: The shortest path between two points.
        """
        path = path + [startpoint]

        if startpoint == endpoint:
            return path
        if startpoint not in self.routes:
            return None

        shortest_path = None
        for point in self.routes[startpoint]:
            if point not in path:
                sp = self.get_shortest_path(point,endpoint,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
                        
        return shortest_path
                   
if __name__ == "__main__" :
    routes = [
        ('mumbai','delhi'),
        ('mumbai','basti'),
        ('basti','lucknow'),
        ('basti','delhi'),
        ('delhi','basti'),
        ('delhi','london')
    ]
    graph = Graph(routes)
    # print(graph.get_path('boka','mumbai'))
    # print(graph.get_path("mumbai", "basti"))
    print(graph.get_path("mumbai", "lucknow"))
    # print(graph.get_shortest_path('mumbai', 'lucknow'))