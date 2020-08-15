x = 512
y = 512
v_corner = 4
v_border = x + x + (x - 2) + (x - 2) - v_corner
v_intern = (x * y) - v_border - v_corner

print(f'Pixels de canto: {v_corner}')
print(f'Pixels de borda: {v_border}')
print(f'Pixels internos: {v_intern}')

n_arestas_corner = v_corner * 3
n_arestas_border = v_border * 5
n_arestas_intern = v_intern * 8

total_vertices = x * y
total_arestas = int((n_arestas_corner + n_arestas_border + n_arestas_intern) / 2)

print('\n')
print(f'Total de vértices: {total_vertices}')
print(f'Total de arestas: {total_arestas}')
