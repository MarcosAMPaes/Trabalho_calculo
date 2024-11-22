# Caso adicional 2: Dados mais concentrados
import os
import numpy as np
from caso_original import gerar_interpolacoes

output_dir = "resultados_dados_concentrados"
os.makedirs(output_dir, exist_ok=True)

dados_concentrados = {
    "x": np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0]),
    "y": np.array([0.0, 3.0, 1.0, 4.0, 2.0, 5.0])
}

os.system('cls')
print("\nCaso Adicional 2: Dados Mais Concentrados")
gerar_interpolacoes(dados_concentrados, x_value=2.5, caso_nome=output_dir)