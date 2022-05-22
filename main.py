
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from unicodedata import name

from data import *


#cores


co0 = "#f0f3f5"  # Preta
cor_cinza = "#f0f3f5"  # cizenta / grey
cor_branca = "#feffff"  # branca
cor_preta = "#38576b"  # preta / black
cor_para_letra = "#403d3d"   # letra
cor_azul = "#6f9fbd"  # azul
cor_vermelha = "#ef5350"   # vermelha
cor_verde = "#93cd95"   # verde


#janela

janela = Tk()
janela.title("")
janela.geometry('500x450')
janela.configure(background=cor_cinza)
janela.resizable(width = FALSE, height = FALSE)


estilo = Style(janela)
estilo.theme_use("clam")


frame_top = Frame(janela, width = 500, height = 50, bg = cor_preta, relief="flat")
frame_top.grid(row = 0, column = 0, pady = 1, padx = 0, sticky = NSEW)


frame_bottom = Frame(janela, width = 500, height = 150, bg = cor_cinza, relief="flat")
frame_bottom.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW)


frame_table = Frame(janela, width = 500, height = 248, bg = cor_branca, relief="groove")
frame_table.grid(row = 2, column = 0, pady = 1, padx = 0, sticky = NSEW)


global tree

def import_Data_And_Show():

    global tree

    list_header = ["Nome", "Sexo" , "Telefone" , "Email"]
    dados =  show_Data()
    tree = ttk.Treeview(frame_table, selectmode = "extended", columns=list_header, show="headings")
    tree.grid(column=0, row= 0, stick="nsew")
    #scroll_vertical.grid(column=1, row= 0, stick="ns")
    #scroll_horizontal.grid(column=0, row= 0, stick="ew")

    hd = ["nw","nw", "nw", "nw","nw"]
    h = [120, 50, 80, 120, 200]
    n = 0

    #cabeçalho

    tree.heading(0, text= "Nome", anchor=NW)
    tree.heading(1, text= "Sexo", anchor=NW)
    tree.heading(2, text= "Telefone", anchor=NW)
    tree.heading(3, text= "Email", anchor=NW)

    tree.column(0, width=100, anchor="nw")
    tree.column(1, width=50, anchor="nw")
    tree.column(2, width=100, anchor="nw")
    tree.column(3, width=250, anchor="nw")

    for item in dados:
        tree.insert('', 'end', values=item)
        
#tabela


import_Data_And_Show()

label_name = Label(frame_top, text="Contatos", anchor= NE, font=("Times 20 bold"), bg=cor_preta, fg=cor_cinza)
label_name.place(x=5, y=5)
label_line = Label(frame_top, text="", width=500, anchor= NE, font=("Times 1"), bg=cor_branca, fg=cor_cinza)
label_line.place(x=0, y=45)


def add_Contact():
    name = entry_nome.get()
    gender = comboBox_gender.get()
    number = entry_contactNumber.get()
    email = entry_email.get()

    data_entry = [name, gender, number, email]

    if name == "" or gender == "" or number == "" or email == "":
        messagebox.showwarning("Dados", "Preencha todos os campos para prosseguir!")

    else:
        add_Data(data_entry)
        messagebox.showinfo("Dados", "Novo contato adicionado com sucesso!")

        entry_nome.delete(0, "end")
        comboBox_gender.delete(0, "end")
        entry_contactNumber.delete(0, "end")
        entry_email.delete(0, "end")

        #label_check.destroy()

        show_Data()
        import_Data_And_Show()


def refresh ():
    try:
        tree_dados = tree.focus()
        tree_dictionary = tree.item(tree_dados)
        tree_list  = tree_dictionary["values"]

        name =  tree_list[0]
        gender =  tree_list[1]
        number =  str(tree_list[2])
        email =  tree_list[3]


        entry_nome.insert(0, name)
        comboBox_gender.insert(0, gender)
        entry_contactNumber.insert(0, number)
        entry_email.insert(0, email)

        

        def check():
            name = entry_nome.get()
            gender = comboBox_gender.get()
            new_number = entry_contactNumber.get()
            email = entry_email.get()

            data_entry = [number,name, gender, new_number, email]

            refresh_Data(data_entry)
            
            messagebox.showinfo("Dados", "Agenda atualizada com sucesso!")

            entry_nome.delete(0, "end")
            comboBox_gender.delete(0, "end")
            entry_contactNumber.delete(0, "end")
            entry_email.delete(0, "end")

            label_check.destroy()

            show_Data()
            import_Data_And_Show()

        label_check = Button(frame_bottom, command= check, text="Confirmar", width=8, font=("Ivy 8 bold"), bg=cor_cinza, fg=cor_para_letra, relief= RAISED, overrelief= RIDGE)
        label_check.place(x=300, y=110)

    except:
        messagebox.showwarning("Dados", "Selecione uma informação na agenda para continuar")

    
def remove():
    try:
        tree_dados = tree.focus()
        tree_dictionary = tree.item(tree_dados)
        tree_list  = tree_dictionary["values"]

        phone = str(tree_list[2])

        remove_Data(phone)

        messagebox.showinfo("Dados", "Contato apagado com sucesso!")
        show_Data()
        

        for widget in frame_table.winfo_children():
            widget.destroy()
        

    except:
        messagebox.showwarning("Dados", "Selecione uma informação na agenda para continuar")

    import_Data_And_Show()
    
     
def search():
    phone_number = entry_search.get()

    data = search_data(phone_number)

    tree.delete(*tree.get_children())


    for items in data:
        tree.insert("", "end", values = items)

    entry_search.delete(0,"end")


    

label_name = Label(frame_bottom, text="Nome     :", anchor= NW, font=("Ivy 10"), bg=cor_cinza, fg=cor_para_letra)
label_name.place(x=10, y=25)
entry_nome = Entry(frame_bottom, width=25, justify="left", relief=FLAT, font=('', 10), highlightthickness=1)
entry_nome.place(x=80,y=20)


label_gender = Label(frame_bottom, text="Sexo   :" , anchor= NW , font=("Ivy 10") ,  bg=cor_cinza, fg=cor_para_letra)
label_gender.place(x=10, y=55)
comboBox_gender = Combobox(frame_bottom, width=27)
comboBox_gender ["value"] = ( '' , 'F' , 'M')
comboBox_gender.place(x=80,y=55)


label_contactNumber = Label(frame_bottom, text="Telefone  :", anchor= NW, font=("Ivy 10"), bg=cor_cinza, fg=cor_para_letra)
label_contactNumber.place(x=10, y=85)
entry_contactNumber = Entry(frame_bottom, width=25, justify="left", relief=FLAT, font=('', 10), highlightthickness=1)
entry_contactNumber.place(x=80,y=85)


label_email = Label(frame_bottom, text="Email     :", anchor= NW, font=("Ivy 10"), bg=cor_cinza, fg=cor_para_letra)
label_email.place(x=10, y=115)
entry_email = Entry(frame_bottom, width=25, justify="left", relief=FLAT, font=('', 10), highlightthickness=1)
entry_email.place(x=80,y=115)


label_search = Button(frame_bottom, command=search, text="Buscar", font=("Ivy 8 bold"), bg=cor_azul, fg=cor_branca, relief= RAISED, overrelief= RIDGE)
label_search.place(x=299, y=20)
entry_search = Entry(frame_bottom, width=17, justify="left", relief=FLAT, font=('', 11), highlightthickness=1)
entry_search.place(x=347,y=21)


label_data = Button(frame_bottom, command= import_Data_And_Show, text="Ver contatos", width=10, font=("Ivy 8 bold"), bg=cor_azul, fg=cor_branca, relief= RAISED, overrelief= RIDGE)
label_data.place(x=299, y=50)

label_add = Button(frame_bottom, command= add_Contact, text="Adicionar", width=10, font=("Ivy 8 bold"), bg=cor_verde, fg=cor_branca, relief= RAISED, overrelief= RIDGE)
label_add.place(x=410, y=50)

label_refresh = Button(frame_bottom, command= refresh, text="Editar", width=10, font=("Ivy 8 bold") ,  bg=cor_azul, fg=cor_branca, relief= RAISED, overrelief= RIDGE)
label_refresh.place(x=410, y=80)

label_delete = Button(frame_bottom, command= remove, text="Deletar", width=10, font=("Ivy 8 bold") ,  bg=cor_vermelha, fg=cor_branca, relief= RAISED, overrelief= RIDGE)
label_delete.place(x=410, y=110)


#global tree

def import_Data_And_Show():

    global tree

    list_header = ["Nome", "Sexo" , "Telefone" , "Email"]

    dados =  show_Data()

    tree = ttk.Treeview(frame_table, selectmode = "extended", columns=list_header, show="headings")

    tree.grid(column=0, row= 0, stick="nsew")
    #scroll_vertical.grid(column=1, row= 0, stick="ns")
    #scroll_horizontal.grid(column=0, row= 0, stick="ew")

    hd = ["nw","nw", "nw", "nw","nw"]
    h = [120, 50, 80, 120, 200]
    n = 0

    #cabeçalho

    tree.heading(0, text= "Nome", anchor=NW)
    tree.heading(1, text= "Sexo", anchor=NW)
    tree.heading(2, text= "Telefone", anchor=NW)
    tree.heading(3, text= "Email", anchor=NW)

    tree.column(0, width=100, anchor="nw")
    tree.column(1, width=50, anchor="nw")
    tree.column(2, width=100, anchor="nw")
    tree.column(3, width=250, anchor="nw")

    for item in dados:
        tree.insert('', 'end', values=item)
#tabela


import_Data_And_Show()


janela.mainloop()