
# coding: utf-8

# In[26]:

last_index = 0

def gen_successors(node):
    global last_index
    graph = {'S':'ABD','A':'BCE','B':'CDEG','C':'E','D':'EG','E':'G'}
    node_id = node[1]
    level = node[3]
    ret = []
    for c in graph[node[0]]:
        ret += [(c,last_index+1,node[1],node[3]+1)]
        last_index += 1
    return ret
    
def is_goal(node):
    return node[0] == 'G'

def insert_all(node,fringe):
    children = gen_successors(node)
    for child in children:
        fringe[0:0] = [child] # fringe.append(child)
    print(fringe)

def show_result(g):
    current_node = g
    parent_index = current_node[1]
    while True:
        print(current_node[0],end=' ')
        parent_index = current_node[2]
        if parent_index == -1:
            break
        current_node = visited_node[parent_index]

def dfs(start_node,limited_level):
    global last_index
    last_index = 0
    fringe = [start_node]
    print(fringe)
    visited_node = {}
    while True:
        if len(fringe) == 0:
            print('Not Found')
            break
        front = fringe[0]
        visited_node[front[1]] = front
        fringe = fringe[1:]
        if is_goal(front):
            show_result(front)
            return True
        if front[3] == limited_level:
            continue
        insert_all(front,fringe)

for i in range(100):
    print('Limit at level '+str(i))
    if dfs(('S',0,-1,0),i):
        break


# In[ ]:



