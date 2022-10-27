import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error:Creating directory.' + directory)


path = str(os.getcwd()).replace("src", "")
folderpath = (f'{path}\\res')
print(folderpath)
create_folder(folderpath)

from src import Eye
node = 'n77'
Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node)

a=1



