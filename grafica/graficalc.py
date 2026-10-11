import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv
import sys


load_dotenv()


def resource_path(relative_path):
    """ Retorna o caminho absoluto do arquivo, funcionando tanto no desenvolvimento quanto no .exe """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')
ID_LISTA = os.getenv('ID_LISTA')

COR_FONTE = 'white'
COR_SECUNDARIA = '#FF0188'
FONTE = 'Helvetica'
BACKGROUND_PRINCIPAL = '#0D111C'
BACKGROUND_CABECALHO = '#1E2C47'


janela = tk.Tk()
janela.title('Graficalc MD')
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.geometry('1000x700')
janela.config(bg=BACKGROUND_PRINCIPAL)


# Frame 1 -----------------------------------------------------------------------------------------------------------------------


frame_cabecalho = tk.Frame(
    janela,
    bg=BACKGROUND_CABECALHO
    )
frame_cabecalho.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky='nwe',
    ipady=10
    )
frame_cabecalho.columnconfigure(0, weight=1)
frame_cabecalho.columnconfigure(1, weight=1)


botao_sair = tk.Button(
    frame_cabecalho,
    text='Sair',
    command=janela.destroy,
    bg=COR_SECUNDARIA,
    fg=COR_FONTE,
    relief='raised',
    font=(FONTE, 15)
    )
botao_sair.grid(
    row=0,
    column=0,
    sticky='w',
    padx=30,
    pady=30
    )

label_calculadora = tk.Label(
    frame_cabecalho,
    text=' GERENCIADOR \nDE PRODUÇÃO',
    font=(FONTE, 30),
    fg=COR_FONTE,
    bg=BACKGROUND_CABECALHO
    )
label_calculadora.grid(
    row=0,
    column=0,
    rowspan=2,
    pady=20,
    padx=5,
    sticky='e'
    )

caminho_logo = resource_path('Logo md.png')
imagem_logo = tk.PhotoImage(file=caminho_logo).subsample(5, 5)

label_logo = tk.Label(
    frame_cabecalho,
    image=imagem_logo,
    bg=BACKGROUND_CABECALHO
    )

label_logo.grid(
    row=0,
    column=1,
    rowspan=2,
    sticky='w',
    padx=5
    )


def atualizar_frame():
    material = combobox_material.get()

    
    if material == 'Adesivo':
        messagebox.showinfo('', f'{material} selecionado com sucesso.')
    elif material == 'Lona':
        messagebox.showinfo('', f'{material} selecionado com sucesso.')
    elif material == '':
        messagebox.showerror('Erro', f'Selecione o material!')
        return None
    else:
        messagebox.showinfo('', f'{material} selecionado com sucesso.')

    
def calcular():
    material = combobox_material.get()

    match material:
        case 'Acrílico':
            preco_material = 1280
        case 'Acrílico Grosso':
            preco_material = 1400
        case 'Acrílico Dourado':
            preco_material = 1380
        case 'Adesivo':
            preco_material = 82
        case 'Adesivo Perfurado':
            preco_material = 100
        case 'Adesivo Transparente':
            preco_material = 100
        case 'Lona':
            preco_material = 80
        case 'MDF':
            preco_material = 390
        case 'PVC':
            preco_material = 290
        case _:
            messagebox.showerror('Erro', 'Escolha o material.')
            return None


    try:
        tamanho1 = float(entry_tamanho_1.get().replace(',', '.'))
    except:
        messagebox.showerror('Erro', 'Preencha o primeiro campo apenas com números e não o deixe vazio.')
        return None
    
    try:
        tamanho2 = float(entry_tamanho_2.get().replace(',', '.'))
    except:
        messagebox.showerror('Erro', 'Preencha o segundo campo apenas com números e não o deixe vazio.')
        return None
    
    
    acrecimo_lucro = 5
    preco = ((tamanho1 * tamanho2) * preco_material) + acrecimo_lucro
    preco = f'{preco:.2f}'.replace('.', ',')
    label_preco.config(text=f'Preço: R${preco}')


frame_calculadora = tk.Frame(janela, bg=BACKGROUND_PRINCIPAL)
frame_calculadora.grid(row=1, column=0)
frame_calculadora.columnconfigure(0, weight=1)
frame_calculadora.columnconfigure(1, weight=1)
frame_calculadora.columnconfigure(2, weight=1)


label_calculadora = tk.Label(
    frame_calculadora,
    text='Calculadora de Metro Quadrado',
    font=(FONTE, 15),
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    relief='solid',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
label_calculadora.grid(
    row=0,
    column=0,
    sticky='ew',
    ipadx=60,
    pady=35,
    columnspan=3
    )

label_material = tk.Label(
    frame_calculadora,
    text='Selecione o material:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 13)
    )
label_material.grid(
    row=1,
    column=0,
    columnspan=3
    )

materiais = ['Acrílico', 'Acrílico Grosso', 'Acrílico Dourado', 'Adesivo', 'Adesivo Perfurado', 'Adesivo Transparente', 'Lona', 'MDF', 'PVC']

style = ttk.Style()
style.theme_use('clam')

style.configure(
    'Custom.TCombobox',
    background=BACKGROUND_PRINCIPAL,
    foreground=BACKGROUND_PRINCIPAL,
    fieldbackground=BACKGROUND_PRINCIPAL,
    bordercolor=BACKGROUND_CABECALHO,
    lightcolor='black',
    darkcolor='black'
)

combobox_material = ttk.Combobox(
    frame_calculadora,
    values=materiais,
    style='Custom.TCombobox',
    state='readonly',
    font=(FONTE, 20),
    width=15
    )
combobox_material.grid(
    row=2,
    column=0,
    columnspan=3
    )
combobox_material.bind('<Return>', lambda event: atualizar_frame())

botao_escolher_material = tk.Button(
    frame_calculadora,
    text='Escolher Material',
    command=atualizar_frame,
    bg=COR_SECUNDARIA,
    fg=COR_FONTE,
    relief='raised',
    font=(FONTE, 10)
    )
botao_escolher_material.grid(
    row=3,
    column=0,
    pady=10,
    columnspan=3
    )

label_tamanhos = tk.Label(
    frame_calculadora,
    text='Digite os tamanhos (metros):',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 13)
    )
label_tamanhos.grid(
    row=4,
    column=0,
    columnspan=3
    )

def passar_para_direita(event):
    entry_tamanho_2.focus()

entry_tamanho_1 = tk.Entry(
    frame_calculadora,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 20),
    width=10,
    justify='center',
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    )
entry_tamanho_1.grid(
    row=5,
    column=0,
    sticky='e',
    )

entry_tamanho_1.bind('<Return>', passar_para_direita)

label_divisor = tk.Label(
    frame_calculadora, text='x',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 13)
    )
label_divisor.grid(
    row=5,
    column=1
    )

entry_tamanho_2 = tk.Entry(
    frame_calculadora,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 20),
    width=10,
    justify='center',
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_tamanho_2.grid(
    row=5,
    column=2
    )

entry_tamanho_2.bind('<Return>', lambda event: calcular())

label_preco = tk.Label(
    frame_calculadora,
    text='O preço aparecerá aqui.',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 13)
    )
label_preco.grid(
    row=6,
    column=0,
    columnspan=3,
    pady=20
    )

botao_calcular = tk.Button(
    frame_calculadora,
    text='Calcular',
    command=calcular,
    bg=COR_SECUNDARIA,
    fg=COR_FONTE,
    relief='raised',
    font=(FONTE, 10)
    )
botao_calcular.grid(
    row=7,
    column=0,
    columnspan=3
    )

# Frame 2 -------------------------------------------------------------------------------------------------------

def pegar_info():
    cliente = entry_cliente.get()
    if cliente == '':
        return 'erro'
    contato = entry_contato.get()
    material = entry_material.get()
    tamanho = entry_tamanhoinfo.get()
    qtde = entry_qtde.get()
    obs = entry_obs.get()
    preco = entry_precoinfo.get()

    titulo = f'{material} de {cliente}'
    descrição = f'''
        Preço: {preco}
        Contato: {contato}
        Tamanho: {tamanho}
        Quantidade: {qtde}
        Observações: {obs}
    '''

    return titulo, descrição

def criar_card(titulo, descricao):

    url = "https://api.trello.com/1/cards"

    params = {
        "key": API_KEY,
        "token": TOKEN
    }

    dados = {
        "idList": ID_LISTA,
        "name": titulo,
        "desc": descricao
    }

    resposta = requests.post(
        url,
        params=params,
        json=dados
    )

    if resposta.status_code == 200:
        
        card = resposta.json()
        card["shortUrl"]

        #print("Card criado com sucesso!")
        

    #else:
        #print("Erro ao criar card:")
        #print(resposta.text)

def limpar_pedidos():
    entry_cliente.delete(0, tk.END)
    entry_contato.delete(0, tk.END)
    entry_material.delete(0, tk.END)
    entry_tamanhoinfo.delete(0, tk.END)
    entry_qtde.delete(0, tk.END)
    entry_precoinfo.delete(0, tk.END)
    entry_obs.delete(0, tk.END)

def enviar_trello():
    if pegar_info() == 'erro':
        messagebox.showerror('Erro', 'Preencha o campo de cliente.')
        return None
    titulo, descricao = pegar_info()

    criar_card(titulo, descricao)

    messagebox.showinfo('', 'Pedido enviado para o Trello!')

    limpar_pedidos()



frame_pedido = tk.Frame(
    janela,
    bg=BACKGROUND_PRINCIPAL
    )
frame_pedido.grid(
    row=1,
    column=1,
    pady=40,
    rowspan=2
    )
frame_pedido.columnconfigure(0, weight=1)
frame_pedido.columnconfigure(1, weight=1)

label_pedido = tk.Label(
    frame_pedido,
    text='Preencha o Pedido Aqui',
    font=(FONTE, 15),
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    relief='solid',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    )
label_pedido.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky='ew',
    ipadx=60,
    pady=40
    )

label_cliente = tk.Label(
    frame_pedido,
    text='Cliente:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_cliente.grid(
    row=1,
    column=0,
    sticky='e'
    )

label_contato = tk.Label(
    frame_pedido,
    text='Contato:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_contato.grid(
    row=2,
    column=0,
    sticky='e'
    )

label_material = tk.Label(
    frame_pedido,
    text='Material:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_material.grid(
    row=3,
    column=0,
    sticky='e'
    )

label_tamanho = tk.Label(
    frame_pedido,
    text='Tamanho:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_tamanho.grid(
    row=4,
    column=0,
    sticky='e'
    )

label_qtde = tk.Label(
    frame_pedido,
    text='Quantidade:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_qtde.grid(
    row=5,
    column=0,
    sticky='e'
    )

label_precoinfo = tk.Label(
    frame_pedido,
    text='Preço:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_precoinfo.grid(
    row=6,
    column=0,
    sticky='e'
    )

label_obs = tk.Label(
    frame_pedido,
    text='Obs:',
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE,
    font=(FONTE, 15)
    )
label_obs.grid(
    row=7,
    column=0,
    sticky='e'
    )

entry_cliente = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_cliente.grid(
    row=1,
    column=1,
    sticky='w',
    pady=5
    )
entry_cliente.bind('<Return>', lambda event: entry_contato.focus() )
entry_cliente.bind('<Down>', lambda event: entry_contato.focus())

entry_contato = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_contato.grid(
    row=2,
    column=1,
    sticky='w',
    pady=5
    )
entry_contato.bind('<Return>', lambda event: entry_material.focus())
entry_contato.bind('<Up>', lambda event: entry_cliente.focus())
entry_contato.bind('<Down>', lambda event: entry_material.focus())

entry_material = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_material.grid(
    row=3,
    column=1,
    sticky='w',
    pady=5
    )
entry_material.bind('<Return>', lambda event: entry_tamanhoinfo.focus())
entry_material.bind('<Up>', lambda event: entry_contato.focus())
entry_material.bind('<Down>', lambda event: entry_tamanhoinfo.focus())

entry_tamanhoinfo = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_tamanhoinfo.grid(
    row=4,
    column=1,
    sticky='w',
    pady=5
    )
entry_tamanhoinfo.bind('<Return>', lambda event: entry_qtde.focus() )
entry_tamanhoinfo.bind('<Up>', lambda event: entry_material.focus())
entry_tamanhoinfo.bind('<Down>', lambda event: entry_qtde.focus())

entry_qtde = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_qtde.grid(
    row=5,
    column=1,
    sticky='w',
    pady=5
    )
entry_qtde.bind('<Return>', lambda event: entry_precoinfo.focus())
entry_qtde.bind('<Up>', lambda event: entry_tamanhoinfo.focus())
entry_qtde.bind('<Down>', lambda event: entry_precoinfo.focus())

entry_precoinfo = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_precoinfo.grid(
    row=6,
    column=1,
    sticky='w',
    pady=5
    )
entry_precoinfo.bind('<Return>', lambda event: entry_obs.focus())
entry_precoinfo.bind('<Up>', lambda event: entry_qtde.focus())
entry_precoinfo.bind('<Down>', lambda event: entry_obs.focus())

entry_obs = tk.Entry(
    frame_pedido,
    relief='solid',
    borderwidth=1,
    highlightthickness=1,
    highlightbackground=BACKGROUND_CABECALHO,
    highlightcolor=COR_FONTE,
    font=(FONTE, 15),
    width=15,
    insertbackground=COR_FONTE,
    bg=BACKGROUND_PRINCIPAL,
    fg=COR_FONTE
    )
entry_obs.grid(
    row=7,
    column=1,
    sticky='w',
    pady=5
    )

entry_obs.bind('<Up>', lambda event: entry_precoinfo.focus())

botao_enviar = tk.Button(
    frame_pedido,
    text='Enviar Para o Trello',
    command=enviar_trello,
    bg=COR_SECUNDARIA,
    fg=COR_FONTE,
    relief='raised',
    font=(FONTE, 10)
    )
botao_enviar.grid(
    row=8,
    column=0,
    columnspan=2,
    pady=31
    )


janela.mainloop()