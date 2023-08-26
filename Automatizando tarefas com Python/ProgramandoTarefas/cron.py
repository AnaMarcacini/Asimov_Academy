import os

def organize_folder():
    types = ['jpg', 'zip']
    ## pasta dowloads
    # base_path = os.path.expanduser('~')
    # path = os.path.join(base_path, 'Downloads')

    # path = os.getcwd()

    
    base_path = os.path.expanduser('~')
    path = os.path.join(base_path, '/home/anahelena/GITs/Asimov_Academy/Automatizando tarefas com Python/ProgramandoTarefas')
    cwd = os.chdir(path)

    full_list = os.listdir(cwd)
    for type_ in types:
        if type_ not in os.listdir():
            os.mkdir(type_)

    for file in full_list:
        for type_ in types:
            if '.' + type_ in file:
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, type_, file)

                os.replace(old_path, new_path)
    
if __name__ == '__main__':

    organize_folder()

