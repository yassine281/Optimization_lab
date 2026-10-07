import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.optimizers import dichotomy, fibonacci_search
from core.test_functions import f_test, f_1, f_2, f_3, f_4, f_5

st.set_page_config(page_title="1D Optimization (Вариант 8)", layout="wide")
st.title("Лабораторная работа №1: Одномерная безусловная оптимизация")
st.subheader("Вариант 8 (Дихотомия и Фибоначчи)")

functions_dict = {
    "Тестовая: f(x) = (x-1)^2": f_test,
    "Учебная 1: f(x) = 4x^3 - 8x^2 - 11x + 5": f_1,
    "Учебная 2: f(x) = x + 3/x^2": f_2,
    "Учебная 3: f(x) = (x+2.5)^4 - x^2": f_3,
    "Учебная 4: f(x) = -sin(x) - sin(3x)/3": f_4,
    "Учебная 5: f(x) = -2sin(x) - sin(2x) - 2sin(3x)/3": f_5
}

st.sidebar.header("Параметры")
selected_func_name = st.sidebar.selectbox("Выберите функцию", list(functions_dict.keys()))
selected_func = functions_dict[selected_func_name]

a = st.sidebar.number_input("Левая граница (a)", value=0.0)
b = st.sidebar.number_input("Правая граница (b)", value=10.0)
eps = st.sidebar.number_input("Точность (eps)", value=0.01, format="%.4f")

if st.sidebar.button("Выполнить оптимизацию "):

    x_d, f_d, it_d, fev_d, hist_d = dichotomy(selected_func, a, b, eps)
    x_f, f_f, it_f, fev_f, hist_f = fibonacci_search(selected_func, a, b, eps)

    res_df = pd.DataFrame({
        "Метод": ["Дихотомия", "Фибоначчи"],
        "x*": [x_d, x_f],
        "f(x*)": [f_d, f_f],
        "Итерации ": [it_d, it_f],
        "Вычисления f(x)": [fev_d, fev_f]
    })
    st.table(res_df)


    fig, ax = plt.subplots(figsize=(10, 6))


    if selected_func == f_2 and a <= 0 <= b:
        x_vals = np.linspace(a, b, 500)
        x_vals = x_vals[np.abs(x_vals) > 0.05]
    else:
        x_vals = np.linspace(a, b, 500)

    y_vals = [selected_func(x) for x in x_vals]
    ax.plot(x_vals, y_vals, label=selected_func_name, color='black', linewidth=1.5)

    d_x = [h[3] for h in hist_d]
    d_y = [h[4] for h in hist_d]
    ax.scatter(d_x, d_y, color='red', label="Итерации (Дихотомия)", zorder=5)

    f_x = [h[3] for h in hist_f]
    f_y = [h[4] for h in hist_f]
    ax.scatter(f_x, f_y, color='blue', marker='x', label="Итерации (Фибоначчи)", zorder=5)

    ax.set_title("График с полученными точками минимума")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

    st.pyplot(fig)