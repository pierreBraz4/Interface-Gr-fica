import customtkinter as ctk

# Configuração de aparência
ctk.set_appearance_mode('dark')  # Modos: 'dark', 'light', 'system'

# Criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuário é "jhonatan" e a senha "123456"
    if usuario == 'jhonatan' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

# Criação da janela principal
app = ctk.CTk()  # Alterado de CTK para CTk
app.title('Sistema de Login')
app.geometry('300x300')

# Criação dos campos
# Label para o usuário
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady=10)

# Entrada de texto para o usuário
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

# Label para a senha
label_senha = ctk.CTkLabel(app, text='Senha:')  # Corrigido o nome da variável
label_senha.pack(pady=10)

# Entrada de texto para a senha
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# Botão de login
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

# Campo de feedback para o login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()