import PySimpleGUI as sg


def tela_inicial():
    layout = [
        [sg.Text('\n\n\t\tAGENDA\t\t')],
        [sg.Text('\n\n')],
        [sg.Button('login'), sg.Button('cadastro')]
    ]
    return sg.Window('AGENDA', layout=layout, finalize=True, size=(600, 400))


def tela_login():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - LOGIN\t\t')],
        [sg.Text('\n\n')],
        [sg.Text('usuário')],
        [sg.Input(key='usuarioL')],
        [sg.Text('senha')],
        [sg.Input(key='senhaL')],
        [sg.Text('', key='msgL')],
        [sg.Button('LOGIN')]
    ]
    return sg.Window('AGENDA-LOGIN', layout=layout, finalize=True, size=(600, 400))


def tela_cadastro():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - CADASTRO\t\t')],
        [sg.Text('\n\n')],
        [sg.Text('usuário')],
        [sg.Input(key='usuarioC')],
        [sg.Text('senha')],
        [sg.Input(key='senhaC')],
        [sg.Text('confirmar senha')],
        [sg.Input(key='Consenha')],
        [sg.Text('', key='msgC')],
        [sg.Button('CADASTRAR')]
    ]
    return sg.Window('AGENDA-CADASTRO', layout=layout, finalize=True, size=(600, 400))


telaInicial, TelaLogin, telaCadastro = tela_inicial(), None, None

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

    # validações

    if window == TelaLogin and eventos == 'LOGIN':
        if valores['usuarioL'] == '' or valores['senhaL'] == '':
            window['msgL'].update('todos os campos devem ser preenchidos')
        else:
            window['msgL'].update('')
    if window == telaCadastro and eventos == 'CADASTRAR':
        if valores['usuarioC'] == '' or valores['senhaC'] == '' or valores['Consenha'] == '':
            window['msgC'].update('todos os campos devem ser preenchidos')
        elif valores['senhaC'] != valores['Consenha']:
            window['msgC'].update('as senhas devem ser iguais')
        else:
            window['msgC'].update('')
