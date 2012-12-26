#Função: Exercicio de comparação de matriz
#Autor: Raphael Ramos
#Professor: Fernando Massanori


reg= [] 
def ep2(a):
    if a == '1':
        matrix = [[0,0,1,1,0,0,1,0,1,0],[0,1,1,0,0,0,1,0,1,0],[0,0,1,1,0,0,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,1,0],[0,0,1,0,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,0,0],[0,0,1,0,0,0,1,1,1,0], [0,0,1,0,0,0,1,1,1,0]]
    elif a == '2':
        matrix = [[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]
    elif a == '3':
        matrix = [[0,1,0],[1,1,1],[0,0,0],[1,0,1]]
    elif a == '4':
        matrix = [[0,1,0,0,1,1],[1,0,0,1,0,0],[0,1,1,0,1,1],[0,1,1,1,1,1],[0,1,0,1,0,1]]
    elif a == '5':
        matrix = [[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,1],[0,1,1,1,1,1,0,1],[0,0,0,0,0,1,1,1]]
    else:
        matrix = []
        print("Errado")

    c, y, x = 0, 0, 0
    vassoura(y, x, matrix, c)
    
def vassoura(y, x, matrix, c):
    for linha in matrix:
        for item in matrix[y]: 
            if matrix[y][x] == 0:
                x+=1
            else:
                if y == 0:
                    if matrix[y][x-1] == 0:
                        c=c+1
                        matrix[y][x] = c
                        reg.append(c)
                    else:
                        matrix[y][x] = matrix[y][x-1]
                    
                else:
                    if matrix[y-1][x] == 0:
                        if matrix[y][x-1] == 0:
                            c=c+1
                            matrix[y][x] = c
                            reg.append(c)
                        else:
                            matrix[y][x] = matrix[y][x-1]
                    else:

                        if matrix[y][x-1]!=0:
                            if matrix[y][x-1] < matrix[y-1][x]:
                                matrix[y][x] = matrix[y][x-1]
                                matrix[y-1][x] = matrix[y][x]
                            else:
                                matrix[y][x] = matrix[y-1][x]
                                matrix[y][x-1] = matrix[y-1][x]
                        else:
                            matrix[y][x] = matrix[y-1][x]
                        
                    
                x+=1
        x = 0
        y+=1
    junta(matrix)


def junta(matrix):
    for i in range( len( matrix ) ):
        matriz = ''
        for j in range(len(matrix[i])):
            matriz = matriz + str( matrix[i][j] ) + ' '
        print(matriz)
    print(reg)



print("Imagem 1:\n",'''0 0 1 1 0 0 1 0 1 0
 0 1 1 0 0 0 1 0 1 0
 0 0 1 1 0 0 1 1 1 0
 0 0 0 0 0 0 0 0 0 0
 0 0 1 0 0 0 1 0 1 0
 0 0 1 0 0 1 1 1 1 1
 1 1 1 1 1 0 0 0 0 0
 0 0 1 0 0 0 1 1 1 0
 0 0 1 0 0 0 1 1 1 0
''')
print("Imagem 2:\n",'''1 0 1 0 1
 1 0 1 0 1
 1 1 1 1 1
''')
print("Imagem 3:\n",'''0 1 0
 1 1 1
 0 0 0
 1 0 1
''')
print("Imagem 4:\n",'''0 1 0 0 1 1
 1 0 0 1 0 0
 0 1 1 0 1 1
 0 1 1 1 1 1
 0 1 0 1 0 1
''')
print("Imagem 5: \n",'''0 1 1 0 0 1 1 0
 0 1 1 1 1 1 1 0
 0 0 0 0 0 0 0 0
 0 1 0 1 0 1 0 0
 0 1 0 1 0 1 0 1
 0 1 1 1 1 1 0 1
 0 0 0 0 0 1 1 1
''')
escolha = input("Escolha a imagem que deseja  testar (1, 2, 3, 4, 5): ")
ep2(escolha)


