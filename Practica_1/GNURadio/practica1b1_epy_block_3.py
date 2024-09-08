"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self): 
        gr.sync_block.__init__(
            self,
            name='e_Average', # se mostrará en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x = input_items[0] # Señal de entrada.
        y0 = output_items[0] # Señal acumulada

# Calcula la suma acumulativa y luego divide por el índice + 1 para el promedio
        cumsum_x = np.cumsum(x)
        y0[:] = cumsum_x / (np.arange(len(x)) + 1)


        return len(output_items[0]) # Retorna el tamaño del buffer de salida
