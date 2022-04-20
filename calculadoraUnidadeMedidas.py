from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

cor1= '#3b3b3b'
cor2= '#ffffff'
cor3= '#FF8C00'
cor4= '#48b3e0'

window= Tk()
window.title('Calcular Medidas')
window.geometry('670x260')
window.config(bg=cor1)

# Frame nome app
frame_nomeApp = Frame(window, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_nomeApp.place(x=2, y=2)

# Frame opções de medidas
frame_opcoes = Frame(window, width=450, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_opcoes.place(x=2, y=54)

# Frame de operações
frame_operacoes = Frame(window, width=220, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_operacoes.place(x=454, y=2)

# estilo janela

estilo = ttk.Style(window)
estilo.theme_use('clam')

# Label para frame de nome
l_nomeApp = Label(frame_nomeApp, text='Calculadora de Unidades de Medidas', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2,fg=cor4)
l_nomeApp.place(x=50, y=10)

# configuração funcionalidade

unidades = {'massa':[{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01}, {'mg':0.001}],
            'comprimento':[{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01}, {'mm':0.001}]
            }

def mostrar_menu(i):

    unidade_de = []
    unidade_para = []
    unidade_valores = []

    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)

    c_de['values'] = unidade_de
    c_para['values'] = unidade_para

    l_unidade_nome['text'] = i

    def calcular():

        a = c_de.get()
        b = c_para.get()

        numero_para_converter = float(e_numero.get())


        if unidade_para.index(a) <= unidade_de.index(b):
            distancia = unidade_para.index(b) - unidade_de.index(a)
            resultado = numero_para_converter * (10**distancia)
            l_resultado['text'] = resultado


        else:
            distancia = unidade_de.index(a) - unidade_para.index(b)
            resultado = numero_para_converter * (10 **distancia)
            l_resultado['text'] = resultado

        if unidade_para.index(a) > unidade_de.index(b):

            if unidade_para.index(a) <= unidade_de.index(b):
                distancia =  unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter / (10**distancia)
                l_resultado['text'] = resultado


            else:
                distancia = unidade_de.index(a) - unidade_para.index(b)
                resultado = numero_para_converter / (10 ** distancia)
                l_resultado['text'] = resultado


    l_info = Label(frame_operacoes, text='Digite o número', width=16, height=2, padx=5, pady=3, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor4)
    l_info.place(x=0, y=110)


    e_numero = Entry(frame_operacoes, width=12, font=('Ivy 14 bold'), justify='center', relief=SOLID)
    e_numero.place(x=5, y=150)

    btn_Calcular = Button(frame_operacoes, command=calcular, text='Calcular', width=7, relief='raised', overrelief='ridge', anchor='nw', font=('Ivy 10 bold'), bg=cor3, fg=cor2)
    btn_Calcular.place(x=145, y=150)

    l_resultado = Label(frame_operacoes, text='', width=17, height=1, padx=0, pady=3, relief='groove', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor4)
    l_resultado.place(x=0, y=200)

# Botão massa

img_Massa = Image.open('img/massa.png')
img_Massa = img_Massa.resize((30,30), Image.ANTIALIAS)
img_Massa = ImageTk.PhotoImage(img_Massa)

btn_Massa = Button (frame_opcoes, command= lambda : mostrar_menu('massa'), text='Massa', image=img_Massa, compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Massa.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

# Botão tempo

img_Tempo = Image.open('img/tempo.png')
img_Tempo = img_Tempo.resize((30,30), Image.ANTIALIAS)
img_Tempo = ImageTk.PhotoImage(img_Tempo)

btn_Tempo = Button (frame_opcoes, command= lambda : mostrar_menu('tempo'), text='Tempo', image=img_Tempo,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Tempo.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)

# Botão Comprimento

img_Comprimento = Image.open('img/comprimento.png')
img_Comprimento = img_Comprimento.resize((30,30), Image.ANTIALIAS)
img_Comprimento = ImageTk.PhotoImage(img_Comprimento)

btn_Comprimento = Button (frame_opcoes, command= lambda : mostrar_menu('comprimento'), text='Comprimento', image=img_Comprimento,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Comprimento.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

#Botão área

img_Area = Image.open('img/area.png')
img_Area = img_Area.resize((30,30), Image.ANTIALIAS)
img_Area = ImageTk.PhotoImage(img_Area)

btn_Area = Button (frame_opcoes, command= lambda : mostrar_menu('area'), text='Área',image=img_Area,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Area.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

# Botão quantidade

img_Qtd = Image.open('img/qtd.png')
img_Qtd = img_Qtd.resize((30,30), Image.ANTIALIAS)
img_Qtd = ImageTk.PhotoImage(img_Qtd)

btn_Qtd = Button (frame_opcoes, command= lambda : mostrar_menu('quantidade'), text='Quantidade', image=img_Qtd,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Qtd.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

# Botão velocidade

img_Velocidade = Image.open('img/velocidade.png')
img_Velocidade = img_Velocidade.resize((30,30), Image.ANTIALIAS)
img_Velocidade = ImageTk.PhotoImage(img_Velocidade)

btn_Velocidade = Button (frame_opcoes, command= lambda : mostrar_menu('velocidade'), text='Velocidade', image=img_Velocidade,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Velocidade.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

# Botão temperatura

img_Temp = Image.open('img/temperatura.png')
img_Temp = img_Temp.resize((30,30), Image.ANTIALIAS)
img_Temp = ImageTk.PhotoImage(img_Temp)

btn_Temp = Button (frame_opcoes, command= lambda : mostrar_menu('tempo'), text='Tempo',image=img_Temp,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Temp.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

# Botão energia

img_Energia = Image.open('img/energia.png')
img_Energia = img_Energia.resize((30,30), Image.ANTIALIAS)
img_Energia = ImageTk.PhotoImage(img_Energia)

btn_Energia = Button (frame_opcoes, command= lambda : mostrar_menu('energia'), text='Energia', image=img_Energia,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Energia.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

# Botão pressão

img_Press = Image.open('img/pressão.png')
img_Press = img_Press.resize((30,30), Image.ANTIALIAS)
img_Press = ImageTk.PhotoImage(img_Press)

btn_Press = Button (frame_opcoes, command= lambda : mostrar_menu('pressao'), text='Pressão', image=img_Press,  compound=LEFT, width=130 ,height=50, relief='flat',overrelief='solid', anchor='nw', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
btn_Press.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)

# Frame operação

l_unidade_nome = Label(frame_operacoes, text='Unidade', width=19, height=2, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2,fg=cor4)
l_unidade_nome.place(x=0, y=0)

l_de = Label(frame_operacoes, text='De', height=1, padx=3, relief='groove', anchor='center', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
l_de.place(x=0, y=70)
c_de = ttk.Combobox(frame_operacoes, width=5, justify=('center'), font=('Ivy 11 bold'))
c_de.place(x=36, y=70)

l_para = Label(frame_operacoes, text='Para', height=1, padx=3, relief='groove', anchor='center', font=('Ivy 11 bold'), bg=cor4,fg=cor2)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_operacoes, width=5, justify=('center'), font=('Ivy 11 bold'))
c_para.place(x=145, y=70)


window.mainloop()
