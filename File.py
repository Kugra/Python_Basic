__author__ = 'aluno01'


#O modo pode ser 'r' para ler, 'w' para escrever, 'a' para abrir um arquivo para adicionar dados
arquivo = open('meuArquivo.txt','a', encoding='utf-8')
print('Nome do arquivo: ',arquivo.name)
print('Tipo de encodamento: ',arquivo.encoding)
print('Modo RAW: ',arquivo.mode)

#Abre o arquivo
arquivo = open('meuArquivo.txt')

#lê arquivo e printa o que há em cada linha
for line in arquivo:
    print(line.rstrip())

#fecha o arquivo
arquivo.close()

#adicionar texto
arquivo = open('meuArquivo.txt','a')
arquivo.write("Escrever ou não escrever?\nEis a questão!")
arquivo.close()

''' Comentado por que é apenas uma amostra, caso queira utilizar é só retirar as aspas triplas
#Leitura e escrita simultanea

arqIn = open('meuArquivo.txt')
arqOut = open('meuArquivo.txt','a')
i = 1
for line in arqIn:
    print(line.rstrip())
    arqOut.write(str(i)+": "+line)
    i+=1
arqIn.close()
arqOut.close()

'''

#apenas uma boa pratica
with open('meuArquivo.txt','r') as file:
    lerDados = file.read()
    print(lerDados)
file.closed