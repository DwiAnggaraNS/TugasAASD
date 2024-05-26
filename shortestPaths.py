import heapq
from collections import deque

# Fungsi untuk baca data
def convertDataToGraph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        N = int(lines[0].strip().split()[0])
        M = int(lines[0].strip().split()[1])
        edges = []
        for line in lines[1:M+1]:
            u, v, w = map(int, line.strip().split())
            edges.append((u, v, w))
        S = int(lines[M+1].strip())
    return N, M, edges, S

# Fungsi untuk nomor 1
def dijkstraAlgo(N, edges, S):
    graph = {i: [] for i in range(1, N+1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    distances = {i: float('inf') for i in range(1, N+1)}
    distances[S] = 0
    pq = [(0, S)]
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        if current_distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return distances

# Fungsi untuk nomor 2
def findPathWithExactDistance(N, edges, S, target_distance):
    # Inisiasi graf
    graph = {i: [] for i in range(1, N+1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dfs(current, distance, path):
        if distance == target_distance:
            return path
        if distance > target_distance:
            return None
        
        for neighbor, weight in graph[current]:
            if all(neighbor != vertex for vertex, _ in path):  # Menghindari pengunjungan vertex yg sama 2 kali
                result = dfs(neighbor, distance + weight, path + [(neighbor, distance + weight)])
                if result:
                    return result
        return None
    
    # Mulai pencarian dari vertex S
    result_path = dfs(S, 0, [(S, 0)])
    if result_path:
        return result_path
    else:
        return None

def format_path(path):
    return ' -> '.join(f"{vertex}({distance})" for vertex, distance in path)

# Fungsi untuk nomor 3
def bfs_with_distance(N, edges, S):
    graph = {i: [] for i in range(1, N+1)}
    for u, v, _ in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    distances = {i: float('inf') for i in range(1, N+1)}
    distances[S] = 0
    queue = deque([S])
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if distances[v] == float('inf'):
                distances[v] = distances[u] + 1
                queue.append(v)
    
    return distances

def main():
    N, M, edges, S = convertDataToGraph('D:\Analisis Algoritma dan Struktur Data\AASD\data.txt')
    
    # 1. Vertex dengan Jarak Terpendek Tertinggi dari S
    distances = dijkstraAlgo(N, edges, S)
    furthest_vertex = max(distances, key=distances.get)
    max_distance = distances[furthest_vertex]
    print(f"1. Vertex dengan jarak terpendek tertinggi dari S: {furthest_vertex} dengan jarak {max_distance}")
    print()
    
    # 2. Vertex dengan Jarak 2024 dari S
    path = findPathWithExactDistance(N, edges, S, 2024)
    if path:
        last_vertex = path[-1][0]
        print(f"Vertex: {last_vertex}")
        formatted_path = format_path(path)
        print(f"Path yang ditempuh: {formatted_path}")
    else:
        print("Tidak ada path yang memiliki jarak 2024 dari S")
    print()
    
    # 3. Vertex Terjauh dari S (mengabaikan bobot edge)
    unweighted_distances = bfs_with_distance(N, edges, S)
    max_unweighted_distance = max(unweighted_distances.values())
    furthest_vertices_unweighted = [v for v, d in unweighted_distances.items() if d == max_unweighted_distance]
    print(f"3. Vertex yang terjauh dari S (mengabaikan bobot): {furthest_vertices_unweighted} dengan jarak {max_unweighted_distance}")

if __name__ == "__main__":
    main()
