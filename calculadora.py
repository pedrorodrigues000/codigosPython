from tkinter import ttk
from tkinter import *

# cores a serem usadas

cor1 = '#1e1f1e'  # preto
cor2 = '#feffff'  # branco
cor3 = '#38576b'  # azul carregado
cor4 = '#ECEFF1'  # cizenta
cor5 = '#FFAB40'  # laranja

window = Tk()  # inicia a janela
window.title('Calculadora')  # nomeia a janela
window.geometry('240x313')  # define as medidas de tamanho
window.config(bg=cor1)  # define o background da janela

#  criando os frames (divisões)

frame_tela = Frame(window, width=280, height=50, bg=cor3)  # divisão para o visor principal
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(window, width=280, height=308, bg=cor1)  # divisão para o corpo da calculadora
frame_corpo.grid(row=1, column=0)

# variável

todos_valores = ''
valor_texto = StringVar()

# criando função

def entrar_valor(event):

    global todos_valores
    todos_valores = todos_valores + str(event)

    # passando valor para o label
    valor_texto.set(todos_valores)

# função calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# função limpar tela

def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# criando label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e',
                  justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# criando botões

btn1 = Button(frame_corpo, command=limpar, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn1.place(x=0, y=0)

btn2 = Button(frame_corpo, command=lambda: entrar_valor('%'), text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn2.place(x=120, y=0)

btn3 = Button(frame_corpo, command=lambda: entrar_valor('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn3.place(x=180, y=0)

btn4 = Button(frame_corpo, command=lambda: entrar_valor('7'),text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn4.place(x=0, y=53)

btn5 = Button(frame_corpo, command=lambda: entrar_valor('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn5.place(x=60, y=53)

btn6 = Button(frame_corpo, command=lambda: entrar_valor('9'),text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn6.place(x=120, y=53)

btn7 = Button(frame_corpo, command=lambda: entrar_valor('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn7.place(x=180, y=53)

btn8 = Button(frame_corpo, command=lambda: entrar_valor('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn8.place(x=0, y=105)

btn9 = Button(frame_corpo, command=lambda: entrar_valor('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn9.place(x=60, y=105)

btn10 = Button(frame_corpo, command=lambda: entrar_valor('6'),text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn10.place(x=120, y=105)

btn11 = Button(frame_corpo, command=lambda: entrar_valor('-'),text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn11.place(x=180, y=105)

btn12 = Button(frame_corpo, command=lambda: entrar_valor('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn12.place(x=0, y=157)

btn13 = Button(frame_corpo, command=lambda: entrar_valor('2'),text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn13.place(x=60, y=157)

btn14 = Button(frame_corpo, command=lambda: entrar_valor('3'),text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn14.place(x=120, y=157)

btn15 = Button(frame_corpo, command=lambda: entrar_valor('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn15.place(x=180, y=157)

btn16 = Button(frame_corpo, command=lambda: entrar_valor('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn16.place(x=0, y=209)

btn17 = Button(frame_corpo, command=lambda: entrar_valor('.'), text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn17.place(x=120, y=209)

btn18 = Button(frame_corpo, command=calcular, text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn18.place(x=180, y=209)


window.mainloop()
