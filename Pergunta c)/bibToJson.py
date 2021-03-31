import re 
import json
from remove_accents import remove_accents

dicRegisto ={}
dicAuxiliar = {}
lista = []
f = open('exemplo-utf8.bib')
blocos = re.split('\n\n' , f.read()) #Divide o ficheiro nos vários registos

cc = re.compile(r'@(.+){(.+),\n') #ER para obter a Categoria e Chave de Citação
er = re.compile(r'(\w+ *)= *(("((.|\n)+?)(",?))|(\{(\{((.|\n)+?)\}((.|\n)*?))\}),?|({((.|\n)+?)(},?))|((.|\n)+?),?)(\n| )') #ER que obtém todos as outras linhas 

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
        for (a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s,t) in ma :
            
            a = a.strip()
            a = remove_accents(a)     #Guarda o registo sem categoria num dicionário
            if d : 
                d = d.strip()
                d = re.sub(r'[\n\t ]+' , r' ',d)
                d = remove_accents(d)
                dicAuxiliar[a] = d
            elif i :
                i = i.strip()
                i = re.sub(r'[\n\t ]+' , r' ',i)
                i = remove_accents(i)
                dicAuxiliar[a] = i
            elif o :
                o = o.strip()
                o = re.sub(r'[\n\t ]+' , r' ',o)
                o = remove_accents(o)
                dicAuxiliar[a] = o
                
            elif r :
                if re.search(r'^{}$', r) :
                    dicAuxiliar[a] = ""
                else :
                    r = r.strip()
                    r = re.sub(r'[\n\t ]+' , r'',r)
                    r = remove_accents(r)
                    dicAuxiliar[a] = r
    dicRegisto[categoria]= dicAuxiliar#Associa a categoria ao registo e guarda no dicionário
    lista.append(dicRegisto)    #Guarda cada dicionário (com categoria) numa lista
    with open('teste.json' , 'w' ) as fout : 
        json.dump(lista, fout ,indent=4)  #Guarda toda a informação da lista num ficheiro do tipo file.json

f.close()