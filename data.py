import csv
from importlib.resources import as_file
from venv import create

lista = ["Ariana", "F", "15545213", "ariana@gmail.com"]


def add_Data(listagem):
    with open('arquivos_dados.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(listagem)

#lista.append(["Ariana", "F", "15545213", "ariana@gmail.com"])
#print(lista)

def show_Data():

    contatcs_Data = []

    with open('arquivos_dados.csv') as file:
        read_csv = csv.reader(file)
        for line in read_csv:
            contatcs_Data.append(line)

    return contatcs_Data


def remove_Data(p):

    def create_New_List(create):
        with open('arquivos_dados.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(create)

        show_Data()

    new_list = []
    phone_number = p

    with open('arquivos_dados.csv') as file:
        read_csv = csv.reader(file)

        for line in read_csv:
            new_list.append(line)

            for field in line:
                if field == phone_number:
                    new_list.remove(line)
    
    create_New_List(new_list)



def refresh_Data(p):
    
    def create_New_List(create):
        with open('arquivos_dados.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(create)

            show_Data()

    new_list = []
    phone_number = p [0]

    with open('arquivos_dados.csv') as file:
        read_csv = csv.reader(file)

        for line in read_csv:
            new_list.append(line)

            for field in line:
                if field == phone_number:
                    name = p[1] 
                    gender = p[2] 
                    phone_n = p[3] 
                    email = p[4] 

                    data = [name, gender, phone_n, email]
                    index = new_list.index(line)
                    new_list[index] = data
    
    create_New_List(new_list)

#old_data = ["12345679", "Joaquina","F","0242345679","maria@gmail.com"]

#refresh_Data(old_data)

def search_data(p):

    contatcs_Data = []
    phone_number = p

    with open('arquivos_dados.csv') as file:
        read_csv = csv.reader(file)
        for line in read_csv:
            for field in line:
                if field == phone_number:
                    contatcs_Data.append(line)

    return contatcs_Data


