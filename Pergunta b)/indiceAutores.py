import re
import collections

def remove_accents(raw_text):
    raw_text = re.sub(u"[àáâãäå]", 'a', raw_text)
    raw_text = re.sub(u"[èéêë]", 'e', raw_text)
    raw_text = re.sub(u"[ìíîï]", 'i', raw_text)
    raw_text = re.sub(u"[òóôõö]", 'o', raw_text)
    raw_text = re.sub(u"[ùúûü]", 'u', raw_text)
    raw_text = re.sub(u"[ýÿ]", 'y', raw_text)
    raw_text = re.sub(u"[ß]", 'ss', raw_text)
    raw_text = re.sub(u"[ñ]", 'n', raw_text)
    raw_text = re.sub(u"[\~\\'\^]", '', raw_text)
    return raw_text


f = open('exemplo-utf8.bib')
blocos = re.split('\n\n' , f.read())
'''for bloco in blocos:
    print(bloco + '\n')'''
    
dictt = {}
c = re.compile(r'@(.+){(.+),')
a = re.compile(r'(?i:author) *= *({{|{|")([^}"]+)(}}|}|"),')

for bloco in blocos:
    if m:= c.search(bloco) :
        cc = m.group(2)
    if ma:= a.search(bloco) :
        au = re.split(r'[\n\t ]and[\n\t ]', ma.group(2) )
        #print(au)

        #au = [re.sub('(.+),(.+)', '\2 \1', i) for i in au]
        #print(au)
        
        for e in au:
            if re.search(',' , e) : 
                #print(e)
                #e = re.sub('([A-Za-z\. ])+,([A-Za-z\. ])+ ', '\2 \1', e)
                m = re.findall('(.+),(.+)', e)
                (p,f2) = m[0]
                e = re.sub(r'[^,]+', f'{f2}', e)
                e = re.sub(r',(.+)', f' {p}', e)
            res = re.sub('[ \n\t]+' , ' ', e.strip())
            res = remove_accents(res)
            if res in dictt and cc not in dictt[res]:
                dictt[res].append(cc)
            elif res not in dictt :
                dictt[res] = [cc]


for i in sorted(dictt):
    print(i + ": ",dictt[i])



f.close()