import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tabulate import tabulate

# Criar pasta para salvar os resultados
output_dir = "resultado_original"
os.makedirs(output_dir, exist_ok=True)

# Função para interpolar usando Lagrange
def lagrange_interpolation(x, y, x_value):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_value - x[j]) / (x[i] - x[j])
        result += term
    return result

# Função para gerar gráficos e calcular valores de interpolação para diferentes casos
# Função para gerar gráficos e calcular valores de interpolação para diferentes casos
def gerar_interpolacoes(dados, x_value, caso_nome):
    # Interpolação Lagrangeana
    y_value_lagrange = lagrange_interpolation(dados["x"], dados["y"], x_value)

    # Interpolação usando Splines Cúbicos
    spline = CubicSpline(dados["x"], dados["y"])
    y_value_spline = spline(x_value)

    # Imprimir os resultados em formato de tabela com cores diferentes
    resultados = [
        ["Método", "x", "y"],
        ["\033[92mInterpolação de Lagrange\033[0m", x_value, f"\033[92m{y_value_lagrange:.2f}\033[0m"],
        ["\033[94mInterpolação por Splines Cúbicos\033[0m", x_value, f"\033[94m{y_value_spline:.2f}\033[0m"]
    ]
    print("\nResultados:")
    print(tabulate(resultados, headers="firstrow", tablefmt="fancy_grid", stralign="center"))

    # Geração dos gráficos de cada método separadamente
    x_plot = np.linspace(min(dados["x"]), max(dados["x"]), 1000)
    y_plot_lagrange = [lagrange_interpolation(dados["x"], dados["y"], xi) for xi in x_plot]
    y_plot_spline = spline(x_plot)

    # Determinar os limites dos eixos x e y
    x_min, x_max = min(dados["x"]), max(dados["x"])
    y_min, y_max = min(min(y_plot_lagrange), min(y_plot_spline), min(dados["y"])), max(max(y_plot_lagrange), max(y_plot_spline), max(dados["y"]))

    # Gráfico da interpolação Lagrangeana
    plt.figure(figsize=(10, 6))
    plt.plot(dados["x"], dados["y"], 'o', label="Pontos Dados", color='black')
    plt.plot(x_plot, y_plot_lagrange, label="Interpolação Lagrangeana", color='orange', linewidth=2, antialiased=True)
    plt.scatter(dados["x"], dados["y"], color='black', antialiased=True)
    plt.scatter(x_plot, y_plot_lagrange, color='orange', s=1)
    plt.scatter(x_value, y_value_lagrange, color='red', label=f"x = {x_value}, y = {y_value_lagrange:.2f}")
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    plt.title(f"Interpolação Lagrangeana - {caso_nome}")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(caso_nome, f"interpolacao_lagrangeana_{caso_nome}.png"))
    plt.close()

    # Gráfico da interpolação por Splines Cúbicos
    plt.figure(figsize=(10, 6))
    plt.plot(dados["x"], dados["y"], 'o', label="Pontos Dados", color='black', antialiased=True)
    plt.plot(x_plot, y_plot_spline, label="Splines Cúbicos", color='blue', antialiased=True)
    plt.scatter(dados["x"], dados["y"], color='black', antialiased=True)
    plt.scatter(x_plot, y_plot_spline, color='blue', s=1)
    plt.scatter(x_value, y_value_spline, color='purple', label=f"x = {x_value}, y = {y_value_spline:.2f}")
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    plt.title(f"Interpolação por Splines Cúbicos - {caso_nome}")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(caso_nome, f"splines_cubicos_{caso_nome}.png"), dpi = 300)
    plt.close()

    # Combinação dos gráficos em um único gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(dados["x"], dados["y"], 'o', label="Pontos Dados", color='black', antialiased=True)
    plt.plot(x_plot, y_plot_lagrange, label="Interpolação Lagrangeana", color='orange', antialiased=True)
    plt.plot(x_plot, y_plot_spline, label="Splines Cúbicos", color='blue', antialiased=True)
    plt.scatter(dados["x"], dados["y"], color='black')
    plt.scatter(x_value, y_value_lagrange, color='red', label=f"Lagrange: x = {x_value}, y = {y_value_lagrange:.2f}")
    plt.scatter(x_value, y_value_spline, color='purple', label=f"Splines: x = {x_value}, y = {y_value_spline:.2f}")
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    plt.title(f"Interpolação Lagrangeana vs Splines Cúbicos - {caso_nome}")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(caso_nome, f"comparacao_interpolacoes_{caso_nome}.png"), dpi = 300)
    plt.close()

    # Análise de Erro (Ponto 1)
    pontos_validacao = np.linspace(min(dados["x"]), max(dados["x"]), 100)
    y_real = spline(pontos_validacao)  # Valores reais gerados pelas splines
    y_lagrange = [lagrange_interpolation(dados["x"], dados["y"], xi) for xi in pontos_validacao]
    mse_lagrange = mean_squared_error(y_real, y_lagrange)
    mae_lagrange = mean_absolute_error(y_real, y_lagrange)
    mse_spline = mean_squared_error(y_real, y_real)  # O spline deve coincidir com os pontos reais
    mae_spline = mean_absolute_error(y_real, y_real)

    # Mostrar erros
    erros = [
        ["Método", "MSE", "MAE"],
        ["Interpolação de Lagrange", f"{mse_lagrange:.2f}", f"{mae_lagrange:.2f}"],
        ["Splines Cúbicos", f"{mse_spline:.2f}", f"{mae_spline:.2f}"]
    ]
    print("\nAnálise de Erro:")
    print(tabulate(erros, headers="firstrow", tablefmt="fancy_grid", stralign="center"))

    # Validação Visual (Ponto 11)
    plt.figure(figsize=(10, 6))
    plt.plot(pontos_validacao, y_real, label="Valores Reais (Splines Cúbicos)", color='green', antialiased=True)
    plt.plot(pontos_validacao, y_lagrange, label="Interpolação Lagrangeana", color='orange', linestyle='--', antialiased=True)
    plt.xlabel("x (km)")
    plt.ylabel("y (km)")
    plt.title(f"Validação da Interpolação - {caso_nome}")
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(caso_nome, f"validacao_interpolacao_{caso_nome}.png"), dpi = 300)
    plt.close()

# Dados originais da tabela
dados_originais = {
    "x": np.array([0.0, 2.0, 3.0, 5.0, 10.0, 20.0, 30.0]),
    "y": np.array([0.0, 10.0, -3.0, -2.0, 20.0, 5.0, 8.0])
}

# Caso original
os.system('cls')
print("\nCaso Original:")
gerar_interpolacoes(dados_originais, x_value=8.5, caso_nome=output_dir)