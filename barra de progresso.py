from tkinter import *
from tkinter.ttk import *
import time

""" 
    step by step:
    Definir uma função para começar o carregamento da barra de progresso.
        Na função:
            - A quantidade de tarefas.
            - Um contador 
            - Acrescentador para barra de progresso
            - Velocidade do Download = velocidade / tarefas x 100
            - Retardador para o progresso da barra
            - Iterador de porcentagem
            - Iterador de texto
            - Atualizador de janela

        Escopo global:
            - Variável " Janela " para TK()
            - Variável para porcentagem em str.
            - Variável para texto em str.
            - Variável para barra de progresso.
                *Empacotar com largura da barra
            - Variável para rótulo de porcentagem.
                *Empacotar a variável.
            - Variável para rótulo de texto.
            - Variável para botão de Download.
                *Empacotar o botão de Download.
            - Chamada da " Janela "


"""
def start():
    tasks = 100 # exemplo de quantia de tarefas.
    counter = 0 # contador do looping while.
    speed = 1
    while counter < tasks:
        speedDownload = (speed / tasks) * 100
        time.sleep(0.05) # retarda a atualização da barra de progresso.
        bar['value'] += speedDownload # contador do progresso da barra.

        counter += speed # limitador do contador. 

        percentCounter = int((counter/tasks) * 100) # variável para contabilizar do progresso da percentual.
        tasksCounter = str(counter) + "/" + str(tasks) # variável para contabilizar o progresso das tarefas.

        percent.set(str(percentCounter) + "%") #interador do carregamento em porcentagem.
        text.set(tasksCounter + " Tasks completed!") #iteração da quantidade de tarefas.
        window.update_idletasks() #interação da barra de porcentagem por looping.

window = Tk()

percent = StringVar() # atualizara a iteração percentual por strings.
text = StringVar() # atualizara a iteranção sequencial por strings.
bar = Progressbar(window, orient=HORIZONTAL, length=100) #barra de progresso.
bar.pack(pady=10) #largura do eixo Y da janela.
percentLabel = Label(window, textvariable=percent).pack() #atualização percentual da barra de progresso.
taskLabel = Label(window, textvariable=text).pack() 
button = Button(window, text="Download", command=start).pack() #botão de download.

window.mainloop()