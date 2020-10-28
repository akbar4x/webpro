def id_dfs(puzzle, tujuan, get_langkah):
    import itertools #digunakan untuk membuat urutan angka

    def dfs(rute, kedalaman):
        if kedalaman == 0:
            return
        if rute[-1] == tujuan:
            return rute
        for geser in get_langkah(rute[-1]):
            if geser not in rute:
                next_rute = dfs(rute + [geser], kedalaman - 1)
                if next_rute:
                    return next_rute
    #menghitung banyaknya langkah yang dilakukan
    for kedalaman in itertools.count():
        rute = dfs([puzzle], kedalaman)
        if rute:
            return rute
#menentukan batas limit solusi
def num_matrix(rows, cols, steps=20):
    import random
#membuat arrai menggunakan random
    nums = list(range(1, rows * cols)) + [0]
    tujuan = [ nums[i:i+rows] for i in range(0, len(nums), rows) ]

    get_langkah = num_gesers(rows, cols)
    puzzle = tujuan
    for steps in range(steps):
        puzzle = random.choice(get_langkah(puzzle))

    return puzzle, tujuan

def num_gesers(rows, cols):
    def get_langkah(subject):
        gesers = []
#
        zrow, zcol = next((r, c)
            for r, l in enumerate(subject)
                for c, v in enumerate(l) if v == 0)

        def swap(row, col):
            import copy
            s = copy.deepcopy(subject)
            s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
            return s

        # atas
        if zrow > 0:
            gesers.append(swap(zrow - 1, zcol))
        # kanan
        if zcol < cols - 1:
            gesers.append(swap(zrow, zcol + 1))
        # bawah
        if zrow < rows - 1:
            gesers.append(swap(zrow + 1, zcol))
        # kiri
        if zcol > 0:
            gesers.append(swap(zrow, zcol - 1))

        return gesers
    return get_langkah

puzzle, tujuan = num_matrix(4, 4)
solusi = id_dfs(puzzle, tujuan, num_gesers(4, 4))

print(solusi)
print(f'jumlah langkah : {len(solusi)}') 
