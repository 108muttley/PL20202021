import re 

f = open('exemplo-utf8.bib')
f2 = open('new.dot' , 'w')

autor = input ("Enter author :")
print(autor)
autores = {autor : []}

blocos = re.split('\n\n' , f.read())
a = re.compile(r'(?i)author *= *({{|{|")([^}"]+)(}}|}|"),')
for bloco in blocos :
    if ma:= a.search(bloco) :
        au = re.split(r'[\n\t ]and[\n\t ]', ma.group(2) )
        au = [i.strip(' \n\t') for i in au]
        au = [re.sub('(.+),(.+)', '\2 \1', i) for i in au]
        print(au)
        if autor in au : 
            for e in au :
                
                print(e + '\n\n\n\n')
                if e != autor and e not in autores[autor] :
                    autores[autor].append(e)
print(autores)

f2.write('graph{\n')
for elem in autores[autor] :
    f2.write('\t"{0}" -- "{1}"\n'.format(autor,elem))
f2.write('}')
f.close()
f2.close()

