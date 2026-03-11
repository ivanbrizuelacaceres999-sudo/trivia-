print('BIENVENIDO A TRIVIA ABURRIDA.COM ')
puntos=0
nombre= input('Ingrese su nombre')
print('el planeta es redondo ?')
if input('SI/NO') == 'SI':
    puntos = puntos+1
print('las sandias son redondas ?')
if input('SI/NO') == 'NO':
    puntos = puntos+1
print('Santa clos existe ?')
if input('SI/NO') == 'SI':
    puntos = puntos+1
print('Cerro es mejor q olimpia ?')
if input('SI/NO') == 'NO':
    puntos = puntos+1
print(f'terminas la encuentas {nombre} hiciste {puntos}')