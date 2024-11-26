import os
import numpy as np

from caso_original import gerar_interpolacoes

# Criar pasta para salvar os resultados
output_dir = "resultado_com_poucos_pontos"
os.makedirs(output_dir, exist_ok=True)

#dados com poucos pontos
x_points = np.array([0, 20, 40])  # Apenas três pontos
y_points = np.array([0, 5, 0])    # Definindo valores para manter uma curva simples e previsível

dados_com_poucos_pontos = {
    "x": x_points,
    "y": y_points
}

# Caso com poucos pontos
print("\nCaso com Poucos Pontos:")
gerar_interpolacoes(dados_com_poucos_pontos, x_value=20.5, caso_nome=output_dir)