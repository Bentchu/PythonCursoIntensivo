from tkinter import *

'''
Coordenadas:
Sempre o topo sup esquerdo é o 0,0
Eixo y avança pra baixo com números positivos

Três pilares:
1)Gerenciador de layout
2)Widgets
3)Eventos

Três gerenciadores de layout:
1- Place
2- Pack
3- Grid
'''

janela = Tk()
janela.title("Logística VW - Contagem Cíclica - Cálculo de Uso Físico Material de Processo")
janela.geometry("600x800+200+100")
#LxA+E+T
#300x300+100+100pxls
'''janela["bg"] = "blue"'''
lb = Label(janela, text="Entre com baixas de material no período:")
lb.place(x=10, y=50)



janela.mainloop()
