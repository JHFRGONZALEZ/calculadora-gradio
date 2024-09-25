import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
from PIL import Image

def calcular_mru(v, t_max):
    t = np.linspace(0, t_max, 100)
    x = v * t
    return t, x, np.full_like(t, v), np.zeros_like(t)

def calcular_mruv(v0, a, t_max):
    t = np.linspace(0, t_max, 100)
    x = v0 * t + 0.5 * a * t**2
    v = v0 + a * t
    return t, x, v, np.full_like(t, a)

def graficar(tipo_movimiento, v0, v, a, t_max):
    plt.figure(figsize=(15, 10))
    
    # Título específico según el tipo de movimiento
    if tipo_movimiento == "mru":
        plt.suptitle("Calculadora gráfica de Movimiento Rectilíneo Uniforme (MRU)", fontsize=16, fontweight='bold')
    elif tipo_movimiento == "mruv":
        plt.suptitle("Calculadora gráfica de Movimiento Rectilíneo Uniforme Variado (MRUV)", fontsize=16, fontweight='bold')
    
    if tipo_movimiento == "mru":
        t, x, v, a = calcular_mru(v, t_max)
        plt.subplot(3, 1, 1)
        plt.title("Posición vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Posición (m)")
        plt.plot(t, x, color='blue')
        plt.grid()

        plt.subplot(3, 1, 2)
        plt.title("Velocidad vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Velocidad (m/s)")
        plt.plot(t, v, color='orange')
        plt.grid()

        plt.subplot(3, 1, 3)
        plt.title("Aceleración vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Aceleración (m/s²)")
        plt.plot(t, a, color='green')
        plt.grid()

    elif tipo_movimiento == "mruv":
        t, x, v, a = calcular_mruv(v0, a, t_max)
        plt.subplot(3, 1, 1)
        plt.title("Posición vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Posición (m)")
        plt.plot(t, x, color='blue')
        plt.grid()

        plt.subplot(3, 1, 2)
        plt.title("Velocidad vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Velocidad (m/s)")
        plt.plot(t, v, color='orange')
        plt.grid()

        plt.subplot(3, 1, 3)
        plt.title("Aceleración vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Aceleración (m/s²)")
        plt.plot(t, a, color='green')
        plt.grid()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Ajustar para no superponer el título
    plt.savefig('plot.png')  # Guardar la figura
    plt.close()  # Cerrar la figura
    return Image.open('plot.png')  # Cargar y retornar la imagen

# Interfaz de Gradio
inputs = [
    gr.Dropdown(["mru", "mruv"], label="Tipo de Movimiento"),
    gr.Number(label="Velocidad Inicial (m/s)", value=0),
    gr.Number(label="Velocidad (m/s)", value=0),
    gr.Number(label="Aceleración (m/s²)", value=0),
    gr.Number(label="Tiempo Máximo (s)", value=10)
]

output = gr.Image()  # Salida como imagen

# Añadir título a la interfaz
gr.Interface(fn=graficar, inputs=inputs, outputs=output, 
             title="Calculadora gráfica de Movimiento Rectilíneo UNAD CIP DOSQUEBRADAS", 
             description="Una herramienta para calcular y graficar los movimientos rectilíneos uniformes y uniformemente variados.").launch()

