from expand import expand
import heapq 


def a_star_search (dis_map, time_map, start, end):
    # chase all passed nodes for the shortest path
    def create_path(start, end, prev_nodes):
        # create an empty path for later
        path = []
        # start chasing from the end point
        curr_node = end

        # start looking for passed nodes until at start point
        while curr_node != start:
            path = [curr_node] + path
            curr_node = prev_nodes[curr_node]
        
        # full path containing all passed nodes
        return [start] + path
    
    # track every node's total costs and distance cost
    f_val = {node : float('inf') for node in dis_map}
    g_val = {node : float('inf') for node in dis_map}
    # set f(n) and g(n) values for the start point
    # though the start point does have value for 
    # f(n) and g(n), but it will not affect the result
    # so instead set it as 0
    f_val[start] = 0
    g_val[start] = 0
    
    # track every node's previous node
    prev_nodes = {node : None for node in dis_map}
    prev_nodes[start] = start
    
    # track the order of entering the queue
    track_order = 0
    h_val = 0
    visit = set()
    # to break the tie
    queue = [(0, h_val, track_order, start)]
    while queue:
        curr_f_val, curr_h_val, enter_order, curr_node = heapq.heappop(queue)

        if curr_node == end:
            return create_path(start, end, prev_nodes)
        
        # no expansion on expanded node
        if curr_node not in visit:
            for next_node in expand(curr_node, time_map):
                track_order += 1 
                h_val = dis_map[next_node][end]
                # get g value for next node
                curr_g_val = g_val[curr_node] + time_map[curr_node][next_node]
                if curr_g_val < g_val[next_node]:
                    # update next node's g value
                    g_val[next_node] = curr_g_val
                    # update next node's f value
                    f_val[next_node] = curr_g_val + h_val
                    # record previous path
                    prev_nodes[next_node] = curr_node
                    # add next node into queue with total cost, h value and order of entering the queue
                    heapq.heappush(queue, (f_val[next_node], h_val, track_order, next_node))
            # add new expanded node
            visit.add(curr_node)
    return print(f'No path found between {start} and {end}')


def depth_first_search(time_map, start, end):
    path = []
    path.append([start])
 
    if start == end:
        return path[0]
    while path:
        curr_way = path.pop()
        curr_node = curr_way[-1]
        if  curr_node == end:
            return curr_way
        for connection in expand(curr_node, time_map):
                # record new path
                new_way = curr_way+[connection]
                # add new path into path
                path.append(new_way)
    return print(f'No path found between {start} and {end}')


def breadth_first_search(time_map, start, end):
    from collections import deque
    
    visit = set()
    path = deque()
    path.append([start])
 
    if start == end:
        return path[0]
    while path:
        curr_way = path.popleft()
        curr_node = curr_way[-1]
        if  curr_node == end:
            return curr_way
        # no expansion on expanded node
        if curr_node not in visit:
            for connection in expand(curr_node, time_map):
                if connection not in visit:
                    # record new path
                    new_way = curr_way+[connection]
                    # add new path into path
                    path.append(new_way)
            # add new expanded node
            visit.add(curr_node)
    return print(f'No path found between {start} and {end}')	
