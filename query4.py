import re 

def query4() : 
    f = open('exemplo-utf8.bib')
    f2 = open('new.dot' , 'w') #Ficheiro dot para fazer o grafo
    autor = input ("Enter author :") #Guarda o autor escolhido pelo utilizador 
    autores = {autor : []}
    blocos = re.split('\n\n' , f.read()) # Divide o ficheiro em registos 

    a = re.compile(r'(?i)author *= *({{|{|")([^}"]+)(}}|}|"),') 

    #ciclo que associa ao autor escolhido os autores com quem trabalhou
    for bloco in blocos :
        if ma:= a.search(bloco) :
            au = re.split(r'[\n\t ]and[\n\t ]', ma.group(2) )
            if autor in au : 
                for e in au :
                    res = re.sub('[ \n\t]+' , ' ', e.strip())
                    if re.search(',' , res) : 
                        m = re.findall('(.+),(.+)', res)
                        (p,snd) = m[0]
                        res = re.sub(r'[^,]+', f'{snd}', res)
                        res = re.sub(r',(.+)', f' {p}', res)
                    if res != autor and res not in autores[autor] :
                        autores[autor].append(res)
    if(len(autores[autor]) == 0) :
        print(f'Autor \"{autor}\" não existe na base de dados ou não costuma publicar com nenhum dos autores nesta base de dados.\n Grafo vazio. \n  ')

    #Escreve o grafo num ficheiro .dot
    else:
        f2.write('graph{\n')
        for elem in autores[autor] :
            f2.write('\t"{0}" -- "{1}"\n'.format(autor,elem))
            
        f2.write('}')

    f.close()
    f2.close()

