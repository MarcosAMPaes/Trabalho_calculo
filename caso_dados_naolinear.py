# Caso adicional 3: Dados não lineares
import os
import numpy as np
from caso_original import gerar_interpolacoes

output_dir = "resultados_nao_lineares"
os.makedirs(output_dir, exist_ok=True)


dados_nao_lineares = {
    "x": np.array([0.0, 1.0, 4.0, 9.0, 16.0, 25.0]),
    "y": np.array([0.0, 1.0, 8.0, 27.0, 64.0, 125.0])
}

os.system('cls')
print("\nCaso Adicional 3: Dados Não Lineares")
gerar_interpolacoes(dados_nao_lineares, x_value=10.0, caso_nome=output_dir)