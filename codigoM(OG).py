import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import pygame

temperaturas = []
limite_inferior = 0
limite_superior = 0
ventana_advertencia = None  # Variable global para la ventana emergente

def recibir_temperatura():
    temperatura = random.randint(10, 40)
    temperaturas.append(temperatura)
    etiqueta_temperatura.config(text=f'Temperatura: {temperatura}°C')
    if temperatura < limite_inferior or temperatura > limite_superior:
        mostrar_advertencia()
        reproducir_sonido()
    
    # Actualizar el gráfico en tiempo real
    plt.plot(temperaturas, 'b-')
    plt.xlabel('Muestras')
    plt.ylabel('Temperatura (°C)')
    plt.title('Gráfico de Temperatura')
    plt.draw()
    
    # Programar la próxima recepción de temperatura después de 5 segundos
    ventana.after(5000, recibir_temperatura)

def establecer_limites():
    global limite_inferior, limite_superior, ventana_advertencia
    limite_inferior = entrada_limite_inferior.get()
    limite_superior = entrada_limite_superior.get()
    
    if not limite_inferior or not limite_superior:
        ventana_advertencia = tk.Toplevel(ventana)
        ventana_advertencia.title('Advertencia')
        ventana_advertencia.grab_set()  # Bloquear la ventana principal
        mensaje = tk.Label(ventana_advertencia, text='Debe ingresar los límites de temperatura.')
        mensaje.pack()
        reproducir_sonido()
    else:
        limite_inferior = int(limite_inferior)
        limite_superior = int(limite_superior)
        etiqueta_limite_inferior.config(text=f'Límite inferior: {limite_inferior}°C')
        etiqueta_limite_superior.config(text=f'Límite superior: {limite_superior}°C')

def mostrar_advertencia():
    ventana_advertencia = tk.Toplevel(ventana)
    ventana_advertencia.title('Advertencia')
    ventana_advertencia.grab_set()  # Bloquear la ventana principal
    mensaje = tk.Label(ventana_advertencia, text='¡La temperatura está fuera de los límites establecidos!')
    mensaje.pack()

def reproducir_sonido():
    pygame.mixer.init()
    pygame.mixer.music.load('ERRSFX.mp3')
    pygame.mixer.music.play()

def generar_grafico():
    plt.ion()  # Habilitar el modo interactivo de Matplotlib
    plt.style.use('bmh')
    plt.plot(temperaturas, 'b-')
    plt.xlabel('Muestras')
    plt.ylabel('Temperatura (°C)')
    plt.title('Gráfico de Temperatura')
    plt.show()

ventana = tk.Tk()
ventana.title('Lectura de temperatura')
ventana.geometry('500x250')

style = ttk.Style()
style.theme_use('clam')

contenedor_principal = tk.Frame(ventana)
contenedor_principal.pack(pady=10)

marco_temperatura = tk.LabelFrame(contenedor_principal, text='Temperatura', padx=20, pady=10)
marco_temperatura.pack(side='left', padx=10)

etiqueta_temperatura = tk.Label(marco_temperatura, text='Temperatura: ')
etiqueta_temperatura.pack()

marco_limites = tk.LabelFrame(contenedor_principal, text='Límites', padx=20, pady=10)
marco_limites.pack(side='left', padx=10)

etiqueta_limite_inferior = tk.Label(marco_limites, text='Límite inferior: ')
etiqueta_limite_inferior.pack()
etiqueta_limite_superior = tk.Label(marco_limites, text='Límite superior: ')
etiqueta_limite_superior.pack()

entrada_limite_inferior = ttk.Entry(marco_limites)
entrada_limite_inferior.pack()
entrada_limite_superior = ttk.Entry(marco_limites)
entrada_limite_superior.pack()

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)

boton_establecer_limites = ttk.Button(marco_botones, text='Establecer límites', command=establecer_limites)
boton_establecer_limites.pack(side='left', padx=5)

boton_generar_grafico = ttk.Button(marco_botones, text='Generar gráfico', command=generar_grafico)
boton_generar_grafico.pack(side='left', padx=5)

ventana.after(5000, recibir_temperatura)  # Iniciar la recepción automática después de 5 segundos

ventana.mainloop()