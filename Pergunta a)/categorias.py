import re 
import collections
categorias = {}
f = open('exemplo-utf8.bib')
for line in f:
    if m:= re.search(r'^@(.+){', line)  :
        if categorias.get(m.group(1)) is not None :
            value = categorias.get(m.group(1))
            categorias.update({m.group(1) : value+1})
        else :
            categorias.update({m.group(1) : 1})


od = collections.OrderedDict(sorted(categorias.items(), key=lambda i: i[0].lower()))
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
    
    for key,value in od.items() : 
        res.write('<li>{0} : {1} </l1>'.format(key,value))
    res.write('</ul>')
    res.write('</body>')
    res.write('</html>')


f.close()