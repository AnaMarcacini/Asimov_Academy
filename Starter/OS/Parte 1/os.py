import os

os.getcwd()

os.listdir()
os.listdir('/home/anahelena/Curso Python/')
#os.chdir()
diretorioAtual = os.getcwd()
os.chdir('/home/anahelena/Curso Python/')
print(os.getcwd())

os.chdir(diretorioAtual)
print(os.getcwd())

os.mkdir('Pasta2')
os.rename('teste.txt','teste2.txt')
os.rename('Pasta2','Pasta')
os.mkdir('Pasta2')
os.mkdir('Pasta3')
os.mkdir('Pasta4')


os.rename('Pasta','Pasta2/Pasta')
os.rename('Pasta2/Pasta','Pasta')

os.remove('teste.csv')
os.rmdir('Pasta4')

cmd = 'date'
os.system(cmd)