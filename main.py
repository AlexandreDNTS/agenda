import PySimpleGUI as sg


def tela_inicial():
    layout = [
        [sg.Text('\n\n\t\tAGENDA\t\t')],
        [sg.Text('\n\n')],
        [sg.Button('login'), sg.Button('cadastro')]
    ]
    return sg.Window('AGENDA', layout=layout, finalize=True)


def tela_login():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - LOGIN\t\t')],
        [sg.Text('\n\n')],
        [sg.Text('usuário')],
        [sg.Input(key='usuarioL')],
        [sg.Text('senha')],
        [sg.Input(key='senhaL')],
        [sg.Text('', key='msg')],
        [sg.Button('LOGIN')]
    ]
    return sg.Window('AGENDA-LOGIN', layout=layout, finalize=True)


def tela_cadastro():
    layout = [
        [sg.Text('\n\n\t\tAGENDA - CADASTRO\t\t')],
        [sg.Text('\n\n')],
        [sg.Text('usuário')],
        [sg.Input(key='usuarioC')],
        [sg.Text('senha')],
        [sg.Input(key='senhaC')],
        [sg.Text('confirmar senha')],
        [sg.Input(key='Csenha')],
        [sg.Text('', key='msgC')],
        [sg.Button('CADASTRAR')]
    ]
    return sg.Window('AGENDA-CADASTRO', layout=layout, finalize=True)


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
