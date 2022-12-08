import PySimpleGUI as sg

usuario = ['francimar']
senha = ['1']

def tela_inicial():
    layout = [
        [sg.Text('\n\n\t\t\t\tAGENDA\t\t',text_color='black')],
        [sg.Text('\n\n')],
        [sg.Button('login',size=(15,2),button_color='blue')], 
        [sg.Button('cadastro',size=(15,2),button_color='blue')],
        [sg.Button('configuração',button_color='blue',size=(15,2))]
        ]
    return sg.Window('AGENDA', layout=layout, finalize=True, size=(600, 400))


def tela_login():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - LOGIN\t\t',text_color='black')],
        [sg.Text('\n\n')],
        [sg.Text('usuário',text_colsizeor='black')],
        [sg.Input(key='usuarioL')],
        [sg.Text('senha',text_color='black')],
        [sg.Input(key='senhaL', password_char='*')],
        [sg.Text('', key='msgL',text_color='black')],
        [sg.Button('LOGIN',size=(15,2),button_color='blue'), sg.Button('CADASTRAR',size=(15,2),button_color='blue')],
        [sg.Button('voltar',size=(15,2),button_color='blue')]
    ]
    return sg.Window('AGENDA-LOGIN',layout=layout,finalize=True,size=(600,400))

def tela_cadastro():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - CADASTRO\t\t',text_color='black')],
        [sg.Text('\n\n')],
        [sg.Text('usuário',text_color='black')],
        [sg.Input(key='usuarioC')],
        [sg.Text('senha',text_color='black')],
        [sg.Input(key='senhaC', password_char='*')],
        [sg.Text('confirmar senha',text_color='black')],
        [sg.Input(key='Consenha', password_char='*')],
        [sg.Text('', key='msgC',text_color='black')],
        [sg.Button('CADASTRAR',size=(15,2),button_color='blue')]
    ]
    return sg.Window('AGENDA-CADASTRO', layout=layout, finalize=True, size=(600, 400))


def tela_usuario():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - USUÁRIO\t\t',text_color='black')],
        [sg.Text('\n\n')],
        [sg.Text('', key='msgUsuario',text_color='black')]
        ]
    return sg.Window('AGENDA-USUÁRIO', layout=layout, finalize=True, size=(600, 400))

telaInicial, TelaLogin, telaCadastro, telaAgenda, telaUsuario,telaConfiguracao = tela_inicial(
), None, None, None, None, None

while True:

    window, eventos, valores = sg.read_all_windows()

    if eventos == sg.WIN_CLOSED:
        break
    if window == telaInicial and eventos == 'login':
        TelaLogin = tela_login()
        telaInicial.hide()
    if window == telaInicial and eventos == 'cadastro':
        telaCadastro = tela_cadastro()
        telaInicial.hide()
    if window == TelaLogin and eventos == 'voltar':
        TelaLogin.hide()
        telaInicial.un_hide()
    if window == TelaLogin and eventos == 'CADASTRAR':
        telaCadastro = tela_cadastro()
        TelaLogin.hide()

    if window == TelaLogin and eventos == 'LOGIN':

        if valores['usuarioL'] == '' or valores['senhaL'] == '' or valores['usuarioL']==' ' or valores['senhaL'] == ' ':
            window['msgL'].update('todos os campos devem ser preenchidos')
        else:
            for i in range(0, len(usuario)):
                if valores['usuarioL'] == usuario[i] and valores['senhaL'] == senha[i]:
                    telaUsuario = tela_usuario()
                    TelaLogin.hide()
                else:
                    window['msgL'].update('usuário ou senha incorreto!')

    if window == telaCadastro and eventos == 'CADASTRAR':
        if valores['usuarioC'] == '' or valores['senhaC'] == '' or valores['Consenha'] == '':
            window['msgC'].update('todos os campos devem ser preenchidos')
        elif valores['senhaC'] != valores['Consenha']:
            window['msgC'].update('as senhas devem ser iguais')
        else:
            for i in range(0, len(usuario)):
                if valores['usuarioC'] == usuario[i]:
                    window['msgC'].update('nome de usuário já existe')
                else:
                    usuario.append(valores['usuarioC'])
                    senha.append(valores['senhaC'])
                    telaCadastro.hide()
                    telaInicial.un_hide()
