import networkx as nx
import matplotlib.pyplot as plt

# Membuat graph
G = nx.DiGraph()

# Menambahkan node (entitas) dan atribut
G.add_node("Tiket", atribut="deskripsi, acara, tanggal, harga")
G.add_node("Agen", atribut="nama, nomor telepon")
G.add_node("Loket", atribut="alamat, nomor telepon")
G.add_node("Internet", atribut="URL")

# Menambahkan hubungan saling eksklusif
G.add_edge("Tiket", "Agen", label="eks")
G.add_edge("Tiket", "Loket", label="eks")
G.add_edge("Tiket", "Internet", label="eks")  # "eks" menunjukkan eksklusif

# Menggambar graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Diagram Entitas dengan Hubungan Saling Eksklusif")
plt.show()