import os
import shutil

def PATH():
    return "/folder_managment"

def create_directory(folder_name):
    if os.path.exists(folder_name) is False:
        os.mkdir(folder_name)
    else:
        return False
    
def remove_directory(folder_name):
    if os.path.exists(folder_name) is True:
        while x != str("y") and x != str("n"):
            x = input ("Are you sure Y/n: ")
        if x == "y":
            shutil.rmtree(folder_name)
        else:
            return False
    else:
        return False

def edit_directory(folder_name, new_name):
    if os.path.exists(folder_name) is True:
        os.rename(folder_name, new_name)
    else:
        return False
    
def tree():
    if not os.path.isdir(PATH()):
        return False
    for root, dirs, files in os.walk(sciezka):
        print(f'Katalog: {root}')
        for dir in dirs:
            print(f'    Podkatalog: {dir}')
        for file in files:
            print(f'    Plik: {file}')


def main():
    while True:
        choice = input("Podaj opcje mały kurwiu: ")
        if choice = ('1'):
            x = input("Podaj nazwe katalogu do utworzeniu: ")
            while create_directory(x) is False:
                print ("Katalog o takiej nazwie już istnieje")
                x = input("Podaj nazwe katalogu do utworzeniu: ")





if __name__ == "__main__":
    main()




cos = os.path.exists("folder_name")
print (cos)