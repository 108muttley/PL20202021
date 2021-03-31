import re
import remove_accents as function

f = open('exemplo-utf8.bib')
blocos = re.split('\n\n' , f.read())    
dictt = {}
c = re.compile(r'@(.+){(.+),')
a = re.compile(r'(?i:author) *= *({{|{|")([^}"]+)(}}|}|"),')

for bloco in blocos:
    if m:= c.search(bloco) :
        cc = m.group(2)
    if ma:= a.search(bloco) :
        au = re.split(r'[\n\t ]and[\n\t ]', ma.group(2) )
        
        for e in au:
            if re.search(',' , e) : 
                m = re.findall('(.+),(.+)', e)
                (p,f2) = m[0]
                e = re.sub(r'[^,]+', f'{f2}', e)
                e = re.sub(r',(.+)', f' {p}', e)
            res = re.sub('[ \n\t]+' , ' ', e.strip())
            res = function.remove_accents(res)
            if res in dictt and cc not in dictt[res]:
                dictt[res].append(cc)
            elif res not in dictt :
                dictt[res] = [cc]

for i in sorted(dictt):
    print(i + ": ",dictt[i])

f.close()