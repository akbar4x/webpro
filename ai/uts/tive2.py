def id_dfs(puzzle, goal, get_moves):
    import itertools

    def dfs(route, depth):
        if depth == 0:
            return
        if route[-1] == goal:
            return route
        for move in get_moves(route[-1]):
            if move not in route:
                next_route = dfs(route + [move], depth - 1)
                if next_route:
                    return next_route

    for depth in itertools.count():
        route = dfs([puzzle], depth)
        if route:
            return route

def str_matrix(rows, cols, steps=25):
    import random, string

    goal = string.ascii_lowercase[:rows * cols - 1] + '*'

    get_moves = str_moves(rows, cols)
    puzzle = goal
    for steps in range(steps):
        puzzle = random.choice(get_moves(puzzle))

    return puzzle, goal


def str_moves(rows, cols):
    def get_moves(subject):
        moves = []

        zero = subject.index('*')
        zrow = zero // cols
        zcol = zero % cols

        def swap(idx):
            s = list(subject)
            s[zero], s[idx] = s[idx], s[zero]
            return ''.join(s)

        # north
        if zrow > 0:
            moves.append(swap(zero - cols))
        # east
        if zcol < cols - 1:
            moves.append(swap(zero + 1))
        # south
        if zrow < rows - 1:
            moves.append(swap(zero + cols))
        # west
        if zcol > 0:
            moves.append(swap(zero - 1))

        return moves
    return get_moves

puzzle, goal = str_matrix(3, 3) # (aebhg*dfc, abcdefgh*)
solution = id_dfs(puzzle, goal, str_moves(3, 3))
print(solution)
print(len(solution)) # 12

