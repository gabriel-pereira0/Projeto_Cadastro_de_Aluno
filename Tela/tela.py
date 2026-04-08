# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import Image, ImageTk

# Calendario TK
from tkcalendar import DateEntry, Calendar
from datetime import datetime

import sys
import os

# Adiciona a pasta raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_registros.sistema_de_registro import *




#cores
co0 = "#020202"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#f70804"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando Janela

janela = Tk()
janela.title("Sistema de Registro")
janela.geometry("970x590")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)
janela.attributes("-alpha",0.9)

Style = Style(janela)
Style.theme_use("clam")
Style.configure("Treeview",
                background=co1,
                foreground=co0,
                rowheight=25,
                fieldbackground=co1)

# Frame Logo
frame_logo = Frame(janela, width=690, height=55, bg=co0, relief=RAISED)
frame_logo.grid(row=0, column=0, pady=1, padx=10, sticky=NSEW, columnspan=5)

# Frame Botões
frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Frame Detalhes
frame_detalhes = Frame(janela, width=690, height=100, bg=co2, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

# Frame Tabela
frame_tabela = Frame(janela, width=690, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Trabalhando no Frame Logo

global imagem, iamgem_string, l_imagem

app_logo = Image.open("Icons/logo.png")
app_logo = app_logo.resize((50, 50))
app_logo= ImageTk.PhotoImage(app_logo) 
app_lg = Label(frame_logo, image=app_logo, text=" Sistema de Registro ", width=800, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=("Ivy 20 bold"), bg=co0, fg=co1)
app_lg.place(x=0, y=0)

# Abrindo uma imagem padrão
imagem = Image.open("Icons/logo.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, width=130, height=130, bg=co2, relief=SOLID)
l_imagem.place(x=550, y=10)

# Criando funções para CRUD 

#função adicionar
from datetime import datetime
from tkinter import messagebox
from PIL import Image

def adicionar_aluno():
    global imagem, imagem_string, l_imagem
    
    # Obtendo os dados dos campos
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    sexo = c_genero.get()

    # Captura a data do widget sem sobrescrevê-lo
    nascimento_data = data_nascimento.get_date()
    nascimento_formatado = nascimento_data.strftime('%d/%m/%Y')

    endereco = e_endereco.get()
    curso = c_curso.get()
    picture = imagem_string

    # Verificando se os campos obrigatórios estão preenchidos
    if nome == "" or email == "" or telefone == "" or sexo == "" or nascimento_formatado == "" or endereco == "" or curso == "" or picture == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    estudante = (nome, email, telefone, sexo, nascimento_formatado, endereco, curso, picture)
    sistema_de_registro.inserir_registro(estudante)
    messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
    
    # Limpando os campos após adicionar
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_genero.set("")  # limpa seleção
    data_nascimento.set_date(datetime.now().date())  # define data atual
    e_endereco.delete(0, END)  # corrigido: era .get()
    c_curso.set("")  # limpa seleção
    imagem_original = Image.open("Icons/logo.png")
    imagem_redimensionada = imagem_original.resize((130, 130))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

    # Atualiza o Label com a imagem
    l_imagem.config(image=imagem_tk)
    l_imagem.image = imagem_tk  # ESSENCIAL: mantém referência viva

    mostrar_alunos()

# Função Procurar Aluno
def procurar_aluno():
    from PIL import Image, ImageTk
    global imagem, imagem_string, l_imagem

    try:
        # Obtendo ID do aluno
        id_aluno = int(e_procurar.get())
    except ValueError:
        messagebox.showerror("Erro", "ID do aluno inválido.")
        return
    
     # Limpando os campos
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_genero.set("")  # limpa seleção
    data_nascimento.set_date(datetime.now().date())  # define data atual
    e_endereco.delete(0, END)  # corrigido: era .get()
    c_curso.set("")  # limpa seleção

    # Inserindo dados nos campos
    dados = sistema_de_registro.Procurar_registro(id_aluno)
    e_nome.insert(0, dados[1])
    e_email.insert(0, dados[2])
    e_telefone.insert(0, dados[3])
    c_genero.set(dados[4])
    data_nascimento.set_date(dados[5])
    e_endereco.insert(0, dados[6])
    c_curso.set(dados[7])
    imagem_string = dados[8]
    imagem_pil = Image.open(imagem_string)
    imagem_pil = imagem_pil.resize((130, 130))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    l_imagem = Label(frame_detalhes, image=imagem_tk, width=130, height=130, bg=co2, relief=SOLID)
    l_imagem.image = imagem_tk  # ESSENCIAL: mantém referência viva
    l_imagem.place(x=550, y=10)
   
# Função Atualizar Aluno   
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk

def atualizar_aluno():
    global imagem, imagem_string, l_imagem

    try:
        # Obtendo ID do aluno
        id_aluno = int(e_procurar.get())
    except ValueError:
        messagebox.showerror("Erro", "ID do aluno inválido.")
        return

    # Obtendo os dados dos campos
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    sexo = c_genero.get()

    # Captura a data do widget sem sobrescrevê-lo
    nascimento_data = data_nascimento.get_date()
    nascimento_formatado = nascimento_data.strftime('%d/%m/%Y')

    endereco = e_endereco.get()
    curso = c_curso.get()
    picture = imagem_string

    # Verificando se os campos obrigatórios estão preenchidos
    if not all([nome, email, telefone, sexo, nascimento_formatado, endereco, curso, picture]):
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    estudante = (nome, email, telefone, sexo, nascimento_formatado, endereco, curso, picture, id_aluno)
    sistema_de_registro.Atualizar_registro(estudante)
    messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")

    # Limpando os campos após atualizar
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_genero.set("")
    data_nascimento.set_date(datetime.now().date())
    e_endereco.delete(0, END)
    c_curso.set("")

    # Restaurando imagem padrão
    imagem_original = Image.open("Icons/logo.png")
    imagem_redimensionada = imagem_original.resize((130, 130))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

    l_imagem.config(image=imagem_tk)
    l_imagem.image = imagem_tk  # mantém referência viva

    mostrar_alunos()

# Deletar Aluno
def deletar_aluno():
    global imagem, imagem_string, l_imagem

    try:
        # Obtendo ID do aluno
        id_aluno = int(e_procurar.get())
    except ValueError:
        messagebox.showerror("Erro", "ID do aluno inválido.")
        return

    sistema_de_registro.Deletar_registro(id_aluno)
    messagebox.showinfo("Sucesso", "Aluno exluído com sucesso!")

    # Limpando os campos após atualizar
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_telefone.delete(0, END)
    c_genero.set("")
    data_nascimento.set_date(datetime.now().date())
    e_endereco.delete(0, END)
    c_curso.set("")
    e_procurar.delete(0, END)

    # Restaurando imagem padrão
    imagem_original = Image.open("Icons/logo.png")
    imagem_redimensionada = imagem_original.resize((130, 130))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
    l_imagem.config(image=imagem_tk)
    l_imagem.image = imagem_tk  # mantém referência viva

    mostrar_alunos()


# Criando campos de entrada Nome
l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief=SOLID)
e_nome.place(x=7, y=40)

# Criando campos de entrada email
l_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left', relief=SOLID)
e_email.place(x=7, y=100)

# Criando campos de entrada Telefone
l_telefone = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_telefone.place(x=4, y=130)
e_telefone = Entry(frame_detalhes, width=15, justify='left', relief=SOLID)
e_telefone.place(x=7, y=160)

# Criando campos de entrada Sexo
l_genero = Label(frame_detalhes, text="Genero *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_genero.place(x=127, y=130)
c_genero = Combobox(frame_detalhes, width=7, justify='center', font=("Ivy 8 bold"))
c_genero['values'] = ('M', 'F', 'N/A')
c_genero.place(x=130, y=160)
c_genero.current(0)

# Criando campos de entrada Data de Nascimento
l_dt_nascimento = Label(frame_detalhes, text="Data de Nascimento *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_dt_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_detalhes, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='dd/mm/yyyy')
data_nascimento.place(x=224, y=40)

# Criando campos de entrada Telefone
l_endereco = Label(frame_detalhes, text="Endereço *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_detalhes, width=45, justify='left', relief=SOLID)
e_endereco.place(x=224, y=100)

# Criando campos de entrada Curso
cursos = ['Administração', 'Análise e Desenvolvimento de Sistemas', 'Arquitetura e Urbanismo', 'Biomedicina',
          'Ciência da Computação', 'Ciências Contábeis', 'Design de Interiores', 'Direito', 'Educação Física',
          'Engenharia Civil', 'Engenharia de Alimentos', 'Engenharia de Produção', 'Estética e Cosmética', 'Farmácia',
          'Fisioterapia', 'Jornalismo', 'Medicina', 'Medicina Veterinária', 'Nutrição', 'Odontologia', 'Psicologia', 'Publicidade e Propaganda',
          'Recursos Humanos', 'Relações Internacionais', 'Sistemas para Internet', 'Tecnologia em Gestão Comercial', 'Tecnologia em Gestão de Recursos Humanos',
          'Tecnologia em Marketing', 'Tecnologia em Processos Gerenciais', 'Tecnologia em Redes de Computadores', 'Tecnologia em Segurança da Informação']
l_curso = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co0)
l_curso.place(x=220, y=130)
c_curso = Combobox(frame_detalhes, width=42, justify='center', font=("Ivy 8 bold"))
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)
c_curso.current(0)

# Função para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem_string = fd.askopenfilename(initialdir="/", title="Selecione uma Imagem", filetypes=(("Arquivos PNG", "*.png"), ("Arquivos JPG", "*.jpg"), ("Todos os Arquivos", "*.*")))
    imagem = Image.open(imagem_string)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, width=130, height=130, bg=co2, relief=SOLID)
    l_imagem.place(x=550, y=10)
    b_imagem['text'] = "Alterar Foto".upper()

# Botão para escolher imagem
b_imagem = Button(frame_detalhes, command=escolher_imagem, text="Carregar Foto".upper(), width=21, compound='center', anchor='center', bg=co1, fg=co0 , font=("Ivy 7 bold"), relief=RAISED, overrelief=RIDGE)
b_imagem.place(x=550, y=160)

# Tabela Alunos
def mostrar_alunos():
    # Criando a tabela
    list_header = ['ID','Nome', 'Email', 'Telefone', 'Sexo', 'Data de Nascimento', 'Endereço', 'Curso']

    # Visualizando todos os Alunos
    df_list = sistema_de_registro.Todos_registros()
    tree_alunos = Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
    # Scrollbar Vertical
    vsb = Scrollbar(frame_tabela, orient="vertical", command=tree_alunos)
    # Scrollbar Horizontal
    hsb = Scrollbar(frame_tabela, orient="horizontal", command=tree_alunos)

    tree_alunos.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_alunos.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(1, weight=12)

    hd=["nw","nw","nw","center","center","center","center","center","center",]
    h=[35,160,150,75,35,125,150,200,240]
    n=0
    
    for col in list_header:
        tree_alunos.heading(col, text=col.title(), anchor=NW)
        # ajustando a coluna
        tree_alunos.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in df_list:
        tree_alunos.insert('', 'end', values=item)

# Procurar Aluno
frame_procurar = Frame(frame_botoes, width=40, height=50, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno [Insira o ID]", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co0)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center', relief=SOLID, font=("Ivy 10 bold"))
e_procurar.grid(row=1, column=0, pady=10, padx=10, sticky=NSEW)

b_procurar = Button(frame_procurar, command=procurar_aluno, text="Procurar".upper(), width=9, compound='center', anchor='center', bg=co1, fg=co0 , font=("Ivy 7 bold"), relief=RAISED, overrelief=RIDGE)
b_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botões  Menu Lateral

app_img_adicionar = Image.open("Icons/adicionar.png")
app_img_adicionar = app_img_adicionar.resize((25, 25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar_aluno, image=app_img_adicionar, text=" Adicionar Aluno", width=100, compound=LEFT, bg=co1, fg=co0 , font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open("Icons/atualizar.png")
app_img_atualizar = app_img_atualizar.resize((25, 25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar_aluno, image=app_img_atualizar, text=" Atualizar Aluno", width=100, compound=LEFT, bg=co1, fg=co0 , font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open("Icons/deletar.png")
app_img_deletar = app_img_deletar.resize((25, 25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar_aluno, image=app_img_deletar, text=" Apagar Aluno", width=100, compound=LEFT, bg=co1, fg=co0 , font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# linha separatoria

l_linha = Label(frame_botoes, text="h", width=1, height=123, bg=co1, fg=co0 , font=("Ivy 1"), relief=GROOVE, anchor=NW)
l_linha.place(x=260, y=15)



# Chamando a função para mostrar alunos
mostrar_alunos()

janela.mainloop()
