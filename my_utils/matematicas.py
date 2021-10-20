# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 10:10:02 2020

@author: allan
"""
import os
import numpy as np
import matplotlib.pyplot as plt

def fibonacci_solve(n):
    fib_arr = np.array([[1,1],[1,0]], dtype=np.object)
    sequence = []
    for i in range(n + 1):
        sequence.append(np.linalg.matrix_power(fib_arr, i)[0][0])
    return sequence

def fibonacci_n(n):
    gold =  (1 + (5 ** 0.5)) / 2
    return round(((gold ** n) - ((1-gold) ** n)) / (5) ** 0.5)

def fibonacci_matrix(n):
    fib_arr = np.array([[1,1],[1,0]], dtype=np.object)
    return np.linalg.matrix_power(fib_arr, n)[0][0]

def fibonacci(message):
    n = int(message.content.split("\n")[-1].split(" ")[-1])
    resposta = []

    if n < 0:
        resposta.append("só números naturais :sweat_smile:")
    elif n == 0:
        resposta.append("zero não é natural :exploding_head:")
    elif n < 15001:
        print(message.content.split(" "))

        now = datetime.datetime.now()
        fib_n = matematicas.fibonacci_matrix(n)
        time_it = datetime.datetime.now() - now
        print(time_it)
        resposta.append("calculo exato, tempo = {}ms".format(time_it.microseconds))
        fib_n = str(fib_n)
        if len(fib_n) > 2000:
            resposta.append(fib_n[:2000])
            resposta.append(fib_n[2000:]) 
        else:
            resposta.append(fib_n)
            print(fib_n)
        n += 1

        now = datetime.datetime.now()
        fib_n = matematicas.fibonacci_n(n)
        time_it = datetime.datetime.now() - now
        print(time_it)
        resposta.append("usando float numbers, tempo = {}ms".format(time_it.microseconds))
        resposta.append(fib_n)
    else:
        resposta.append("kkkkkk, não :angry:")
    
    return resposta

def mmq(valores):
    xlista = []#x em float
    ylista = []#y em float
    
    
    titulo = valores[1]
    n = valores[2].strip()  .split(" ")[-1]
    eixo_x, eixo_y = valores[3].split()

    for a in range(int(n)):
        x, y = valores[4 + a].split()
        if "," in x or "," in y:
            virgula = True
            xlista.append(float(x.replace(',','.')))
            ylista.append(float(y.replace(',','.')))
        elif "." in x and "." in y:
            virgula = False
            xlista.append(float(x))
            ylista.append(float(y))
        else:
            print("Dados invalidos")

    sumx = 0
    vertn = 0
    sumy = 0
    alfad = 0
    alfan = 0
    xx = 0
    alfan = 0
    for i in range(0,len(xlista)):#calculo das medias
        sumx = sumx + xlista[i]
        sumy = sumy + ylista[i]
    averagex = sumx/len(xlista)
    averagey = sumy/len(ylista)
    for m in range(0,len(xlista)):
        #coef angular
        alfan = alfan + (xlista[m]-averagex)*(ylista[m])
        alfad = alfad + (xlista[m]-averagex)**2
    alfa = alfan/alfad
    beta = averagey - alfa*averagex 
    #coef linear
    for n in range(0,len(xlista)): 
        #calculo dos erros
        xx = xx + xlista[n]**2
        vertn = vertn + (alfa*xlista[n]+beta-ylista[n])**2
    vert = (vertn/(len(xlista)-2))**.5 #dispersao media do ajuste
    ialfa = vert/(alfad)**.5 #erro angular
    ibeta = vert*(xx/(len(xlista)*alfad))**.5 #erro linear

    plt.figure()
    plt.grid(True)
    plt.errorbar(xlista, ylista, yerr = vert, c = "blue", fmt = "o", zorder = 50, label = "Medidas Experimentais")
    xlinha = np.linspace(min(xlista), max(xlista), 50)
    ylinha = [x * alfa + beta for x in xlinha]
    plt.plot(xlinha, ylinha, "-r", zorder = 10, label = "Regressão Linear")
    plt.title(titulo)
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)
    plt.legend()
    save_path = os.path.join(".", "my_utils", "matematicas", str(titulo))
    plt.savefig(save_path)
    if virgula:
        resposta = ""
        resposta += "Foram inseridos:\n"
        resposta += "```||{0:^3}||  {1:^20} ||  {2:^20} ||\n".format("n",eixo_x,eixo_y)
        for a in range(0,len(xlista)):
            resposta += "||{0:^3}||  {1:^20} ||  {2:^20} ||\n".format(a+1, str(xlista[a]).replace(".",","), str(ylista[a]).replace(".",","))
        resposta += "```"
        resposta += "media dos x(xm): {}\n".format(str(averagex).replace(".",","))
        resposta += "media dos y(ym): {}\n".format(str(averagey).replace(".",","))
        resposta += "Dispersão média do ajuste: {}\n".format(str(vert).replace(".",","))
        resposta += "Σ(xi-xm) * yi = {}\n".format(str(alfan).replace(".",","))
        resposta += "Σ(xi-xm)² = {}\n".format(str(alfad).replace(".",","))
        resposta += "Σ(axi+b-yi)² = {}\n".format(str(vertn).replace(".",","))
        resposta += "Σ(xi)² = {}\n".format(str(xx).replace(".",","))
        resposta += "O coeficiente angular(a ± Δa) é: {} ± {}\n".format(str(alfa).replace(".",","),str(ialfa).replace(".",","))
        resposta += "O coeficiente linear(b ± Δb) é: {} ± {}\n".format(str(beta).replace(".",","),str(ibeta).replace(".",","))
    else:
        resposta = ""
        resposta += "Foram inseridos:\n"
        resposta += "```||{0:^3}||  {1:^20} ||  {2:^20} ||\n".format("n",eixo_x,eixo_y)
        for a in range(0,len(xlista)):
            resposta += "||{0:^3}||  {1:^20} ||  {2:^20} ||\n".format(a+1,xlista[a],ylista[a])
        resposta += "```"
        resposta += "media dos x(xm): {}\n".format( averagex)
        resposta += "media dos y(ym): {}\n".format( averagey)
        resposta += "Dispersão média do ajuste: {}\n".format(vert)
        resposta += "Σ(xi-xm)*yi = {}\n".format(alfan)
        resposta += "Σ(xi-xm)^2 = {}\n".format(alfad)
        resposta += "Σ(axi+b-yi)^2 = {}\n".format(vertn)
        resposta += "Σ(xi)^2 = {}\n".format(xx)
        resposta += "O coeficiente angular(a ± Δa) é: {} ± {}\n".format(alfa,ialfa)
        resposta += "O coeficiente linear(b ± Δb) é: {} ± {}\n".format(beta,ibeta)
    return resposta

