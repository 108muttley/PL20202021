import re 

f = open('exemplo-utf8.bib')
f2 = open('new.dot' , 'w')

autor = input ("Enter author :")
#print(autor)

autores = {autor : []}

blocos = re.split('\n\n' , f.read())
a = re.compile(r'(?i)author *= *({{|{|")([^}"]+)(}}|}|"),')
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

print(autores[autor])
f2.write('graph{\n')
for elem in autores[autor] :
    f2.write('\t"{0}" -- "{1}"\n'.format(autor,elem))
f2.write('}')
f.close()
f2.close()

