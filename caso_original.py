# Dados originais da tabela
import os

import numpy as np
from interpolar import gerar_interpolacoes

# Criar pasta para salvar os resultados
output_dir = "resultado_original"
os.makedirs(output_dir, exist_ok=True)

dados_originais = {
    "x": np.array([0.0, 2.0, 3.0, 5.0, 10.0, 20.0, 30.0]),
    "y": np.array([0.0, 10.0, -3.0, -2.0, 20.0, 5.0, 8.0])
}

# Caso original
os.system('cls')
print("\nCaso Original:")
gerar_interpolacoes(dados_originais, x_value=8.5, caso_nome=output_dir)