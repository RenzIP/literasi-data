# List
A = ["Komputer", "meja", "kursi", "papan tulis"]
A.insert(2, [100, 200, 300])
A[2].insert(1, ["a", "b", "c", "d"])
A.insert(6, "keyboard")
A[2][1].insert(4, "e")
print (A)
print (A[2][0])
print (A[2][1][3])
A.remove("meja")
A[1].remove(300)
A[1][2] = 1000
print (A)