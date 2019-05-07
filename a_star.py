from ast import literal_eval

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    dists, heuristic = get_content();
    city = start, 0;
    nearest_neighbor = city, heuristic[start];

    already_visited = [];
    already_visited.append(nearest_neighbor)

    a_star_alg(already_visited, goal, dists, heuristic);
  
def get_content():
    r = open("dists.py", "r");
    content = literal_eval(r.read());
    return content['dists'], content['heuristic'];
    
def a_star_alg(already_visited, goal, dists, heuristic):
    city, dist_calc = already_visited[0];
    name, dist = city;

    print(already_visited[0]);
    if (name == goal):
        return;
    
    already_visited.remove(already_visited[0]);
    
    for neighbor in dists[name]:
        f = dist + calc_function(neighbor, heuristic);
        child = neighbor[0], dist + neighbor[1];
        child_city = child, f;
        already_visited.append(child_city);
        
    already_visited.sort(key=sorted_list);

    return a_star_alg(already_visited, goal, dists, heuristic);
 
def calc_function(neighbor, heuristic):
    city, dist = neighbor;
    return dist + heuristic[city];

    
def sorted_list(s):
    return s[-1]


a_star("Lugoj");