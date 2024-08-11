def CalcularMedia(aluno,n1,n2,n3):
    media=(n1+n2+n3)/3
    DicMedia.update({aluno:media})

DicAlunos={}
DicMedia={}
notas=[]
NumDigitar=int(input("Deseja cadastrar quantos alunos: "))
for  i in range(1,NumDigitar+1):
    nome=input("Digite nome do aluno: ").upper()
    nota1 = float(input("Digite nota 1: "))
    nota2 = float(input("Digite nota 2: "))
    nota3 = float(input("Digite nota 3: "))
    print()
    CalcularMedia(nome,nota1,nota2,nota3) 
    
    notas=[nota1,nota2,nota3] 
    DicAlunos.update({nome:notas})
print("Dicionario de notas: ",DicAlunos,"\nDicionario de médias: ",DicMedia,"\n")