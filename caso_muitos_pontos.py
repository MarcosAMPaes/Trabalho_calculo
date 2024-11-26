import os
import numpy as np

from caso_original import gerar_interpolacoes

# Criar pasta para salvar os resultados
output_dir = "resultado_com_muitos_pontos_definidos"
os.makedirs(output_dir, exist_ok=True)

# Gerar dados com pontos de 0.5 em 0.5 no intervalo de 0 a 20
x_points = np.sort(np.random.choice(np.arange(0, 20.5, 0.5), size=25, replace=False))  # Pontos x irregulares
y_points = 5 * np.sin(x_points / 3) + 2 * (x_points / 5) + np.random.normal(scale=2.0, size=len(x_points))  # Função + ruído

dados_com_muitos_pontos = {
    "x": x_points,
    "y": y_points
}

# Caso com muitos pontos
print("\nCaso com Muitos Pontos Definidos:")
gerar_interpolacoes(dados_com_muitos_pontos, x_value=15.5, caso_nome=output_dir)