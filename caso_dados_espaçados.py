# Caso adicional 1: Dados mais espaçados
import os
import numpy as np
from caso_original import gerar_interpolacoes

output_dir = "resultados_dados_espacados"
os.makedirs(output_dir, exist_ok=True)

dados_espacados = {
    "x": np.array([0.0, 10.0, 20.0, 30.0, 40.0]),
    "y": np.array([0.0, 15.0, -5.0, 25.0, 10.0])
}

os.system('cls')
print("\nCaso Adicional 1: Dados Mais Espaçados")
gerar_interpolacoes(dados_espacados, x_value=15.0, caso_nome=output_dir)
