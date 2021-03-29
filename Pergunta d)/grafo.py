import re 

f = open('exemplo-utf8.bib')
f2 = open('new.dot' , 'w')

f2.write('graph autores { \n\t a -- b; \n\t b -- c; \n\t a --c;\n} ' )

f.close()
f2.close()

