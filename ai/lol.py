graf = {'A':set (['B','C']),
        'B':set (['A']),
        'C':set (['A','D','E','F']),
        'D':set (['C','G','H']),
        'E':set (['C','F','I']),
        'F':set (['C','E','K']),
        'G':set (['D','H','I']),
        'H':set (['D','G']),
        'I':set (['E','G','J']),
        'J':set (['I','L']),
        'K':set (['F','L']),
        'L':set (['K','J'])}

def bfs2 (graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue:
        jalur = queue.pop (0)
        state = jalur[-1]
        if state == tujuan:
            return jalur
        elif state not in visited:
            for cabang in graf.get (state, []):
                jalur_baru = list (jalur)
                jalur_baru.append (cabang)
                queue.append(jalur_baru)

            visited.add (state )
        ini = len (queue)
        if ini == 0:
            print("Tidak ditemukan")

print(bfs2(graf,'A','L'))
