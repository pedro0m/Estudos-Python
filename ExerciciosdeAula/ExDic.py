filme = {
    'Titulo': 'Carros 2',
    'Diretor': 'John Lasseter',
    'Ano de Lançamento': '2011'
}

filme['Ano de lançamento'] = input('Insira um novo ano de lançamento: ')
novo = input('Insira novo campo: ')
filme[novo] = 'Animação'
print(filme)