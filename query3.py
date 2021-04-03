import re 
import json
from remove_accents import remove_accents

def query3() : 
    dicRegisto ={}
    dicAuxiliar = {}
    lista = []
    f = open('exemplo-utf8.bib')
    blocos = re.split('\n\n' , f.read()) #Divide o ficheiro nos vários registos

    cc = re.compile(r'@(.+){(.+),\n') #ER para obter a Categoria e Chave de Citação
    er = re.compile(r'(\w+\s*)=\s*("((.|\n)+?)"|({({((.|\n)+?)}((.|\n)*?))})|{((.|\n)*?)}|((.|\n)+?)),?(\n| )') #ER que obtém todos as outras linhas 

    for bloco in blocos:
        if m:= cc.search(bloco) : #obtém categoria e Chave de Citação 
            categoria = m.group(1)
            chave = m.group(2)
            categoria = remove_accents(categoria)
            chave = remove_accents(chave)
            dicRegisto = {}
            dicAuxiliar = {}
            dicAuxiliar['Key'] = chave

        if ma:= er.findall(bloco): #Obtem os campos e o conteúdo desse campo
            for (a,b,c,d,e,g,h,i,j,k,l,m,n,o,p) in ma :
                print(ma)
                a = a.strip()
                a = remove_accents(a)     
                if c :                      # Se depois do igual vierem aspas o terceiro grupo não é vazio
                    c = c.strip()
                    c = re.sub(r'[\n\t ]+' , r' ',c)
                    c = remove_accents(c)
                    dicAuxiliar[a] = c
                elif l :                    # Se depois do igual vier uma chaveta, o décimo primeiro grupo não é vazio
                    l = l.strip()
                    l = re.sub(r'[\n\t ]+' , r' ',l)
                    l = remove_accents(l)
                    dicAuxiliar[a] = l
                elif n :                    # Se depois do igual não vier nada, o terceiro grupo não é vazio
                    n = n.strip()
                    n = re.sub(r'[\n\t ]+' , r' ',n)
                    n = remove_accents(n)
                    dicAuxiliar[a] = n
                    
                elif g :                    # Se depois do igual vierem 2 chavetas, o grupo 6 não é vazio
                    if j :                  
                        g = g.strip()
                        g = re.sub(r'[\n\t ]+' , r' ',g)
                        g = remove_accents(g)
                        dicAuxiliar[a] = g
                    else :                     
                        h = h.strip()
                        h = re.sub(r'[\n\t ]+' , r'',h)
                        h = remove_accents(h)
                        dicAuxiliar[a] = h
                else :
                    dicAuxiliar[a] = ""
        dicRegisto[categoria]= dicAuxiliar #Associa a categoria ao registo e guarda no dicionário
        lista.append(dicRegisto)    #Guarda cada dicionário (com categoria) numa lista
        with open('teste.json' , 'w' ) as fout : 
            json.dump(lista, fout ,indent=4)  #Guarda toda a informação da lista num ficheiro do tipo file.json

    f.close()