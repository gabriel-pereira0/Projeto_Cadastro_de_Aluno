import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self, db_name='registro.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS registro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                sexo TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                endereco TEXT NOT NULL,
                curso TEXT NOT NULL,
                picture text NOT NULL
            )
        ''')
        self.conn.commit()

    def inserir_registro(self, registro):
        try:
            self.cursor.execute('INSERT INTO registro (nome, email, telefone, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)', registro)
            self.conn.commit()
            # Mostrando mensagem de sucesso
            messagebox.showinfo("Sucesso", "Registro inserido com sucesso!")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao inserir registro: {e}")

    def Todos_registros(self):
            self.cursor.execute('SELECT * FROM registro')
            dados = self.cursor.fetchall()
            return dados
    def Procurar_registro(self, id):
            self.cursor.execute('SELECT * FROM registro WHERE id = ?', (id,))
            dados = self.cursor.fetchone()
            return dados

    def Atualizar_registro(self, novo_registro, ):
            if len(novo_registro) != 9:
                messagebox.showerror("Erro", f"Número de valores incorreto! Esperado 9, recebido {len(novo_registro)}")
                return
            query = '''UPDATE registro SET nome = ?, email = ?, telefone = ?, sexo = ?, data_nascimento = ?, endereco = ?, curso = ?, picture = ? WHERE id = ?'''
            self.cursor.execute(query, novo_registro)
            self.conn.commit()
            messagebox.showinfo("Sucesso", f"Registro ID:{novo_registro[8]}, atualizado com sucesso!")

    def Deletar_registro(self, id):
            self.cursor.execute('DELETE FROM registro WHERE id = ?', (id,))
            self.conn.commit()
            messagebox.showinfo("Sucesso", f"Registro ID:{id}, deletado com sucesso!")

# criando uma instanacia da classe SistemaDeRegistro
sistema_de_registro = SistemaDeRegistro()

#Informacoes para registro
#estudante = ('Karen', 'karen@gmail.com', '12345', 'F', '01/01/1998', 'Cambe-PR', 'Odontologia', 'keren.jpg')
# Inserindo um registro
#sistema_de_registro.inserir_registro(estudante)

#Ver os registros
#todos_registros = sistema_de_registro.Todos_registros()

#Procurar um registro
#aluno = sistema_de_registro.Procurar_registro(2) # ADICIONAR CONDIÇÃO PARA VERIFICAR SE O ID EXISTE

#Atualizar um registro
#estudante = ('Karen', 'karen@gmail.com', '654321', 'F', '01/01/1998', 'Cambe-PR', 'Odontologia', 'keren.jpg', 2)  # O último valor é o ID do registro a ser atualizado
#aluno_atualizado = sistema_de_registro.Atualizar_registro(estudante)

#Deletar um registro
#sistema_de_registro.Deletar_registro(2) # ADICIONAR CONDIÇÃO PARA VERIFICAR SE O ID EXISTE