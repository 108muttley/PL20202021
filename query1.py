import re 
import collections

def query1():
    categorias = {}
    f = open('exemplo-utf8.bib')

    '''Ciclo que guarda num dicionário todas as categorias nas 'keys', e conta a quantidade de registo 
    de cada categoria no ficheiro '''
    for line in f:
        if m:= re.search(r'^@(.+){', line)  :
            categoria = m.group(1).lower()
            if categorias.get(categoria) is not None :
                value = categorias.get(categoria)
                categorias.update({categoria : value+1})
            else :
                categoria = m.group(1).lower()
                categorias.update({categoria : 1})

    ''' Escreve o título, o ano, a disciplina e os nossos nomes no html'''
    od = collections.OrderedDict(sorted(categorias.items()))
    with open('categorias.html', 'w') as res:
        res.write('<!DOCTYPE html>')
        res.write('<html>')
        res.write('<head>')
        res.write('<meta charset="UTF-8"/>')
        res.write('</head>')
        res.write('<body>')
        res.write('<h1>Pergunta 1</h1><br>')
        res.write('<h3>Trabalho TP1 -> Processamento de Linguagens</h3>')
        res.write('<h3>2020/2021</h3>')
        res.write('<h3>Autores:</h3>')
        res.write('<ul>')
        res.write('<li>Bárbara Teixeira (A89610)</li>')
        res.write('<li>Renata Teixeira (A89611)</li>')
        res.write('<li>José Henrique Monteiro (A89490)</li>')
        res.write('</ul>')
        res.write('<h2>Categorias no ficheiro "exemplo-utf8.bib" ordenadas por ordem alfabética<br>e o número de ocorrências neste ficheiro seguidamente:</h2><hr>') 
        res.write('<ul>')

        ''' Ciclo que escreve a informação do dicionário no html (Categoria : Nr de Ocorrências)'''
        for key,value in od.items() : 
            res.write('<li>{0} : {1} </l1>'.format(key,value))
        res.write('</ul>')
        res.write('</body>')
        res.write('</html>')
    f.close()