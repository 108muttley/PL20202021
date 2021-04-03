import query1 as a
import query2 as b
import query3 as c 
import query4 as d

def main() : 
    query = input('Insira o número da query que pretende executar (1 a 4) ou "EXIT" se pretender sair:')
    query = query.lower()
    if query == '1' : 
        a.query1()
        main()
    elif query == '2' :
        b.query2()
        main()
    elif query == '3' :
        c.query3()
        main()
    elif query == '4' : 
        d.query4()
        main()
    elif query == "exit" :
        pass
    else : 
        print('Input incorreto, insira um número de 1 a 4 para identificar a query que pretende executar ou "EXIT" se pretender sair ')
        main()
main()



