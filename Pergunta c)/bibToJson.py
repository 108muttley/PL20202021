import re 
import json

dic ={}

f = open('exemplo-utf8.bib')

blocos = re.split('\n\n' , f.read())
'''for bloco in blocos:
    print(bloco + '\n')'''

cc = re.compile(r'@(.+){(.+),\n')
er = re.compile(r'(\w+ *)= *((.|\n)+?)(}|}}|"| +),?\n')

for bloco in blocos:
    if m:= cc.search(bloco) :
        cat = m.group(1)
        ccita = m.group(2)
        print(cat)
        print(ccita)
    if ma:= er.findall(bloco):
        print(ma)


f.close()