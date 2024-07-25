import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа


# Функція для обчислення інтегралу методом Монте-Карло
def mc_integral(a, b, num_samples=10000):
    # Генерація випадкових точок
    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, f(b), num_samples)

    # Оцінка кількості точок під кривою
    points_under_curve = np.sum(y <= f(x))
    area_ratio = points_under_curve / num_samples

    # Оцінка площі під кривою
    total_area = (b - a) * f(b)
    return total_area * area_ratio


# Основна частина програми
if __name__ == "__main__":
    # Обчислення числового інтегралу
    numerical_integral, numerical_error = sci.quad(f, a, b)
    print(f"Числовий інтеграл: {numerical_integral} з помилкою {numerical_error}")

    # Перевірка результатів для різної кількості точок
    num_samples = [100, 1000, 10000, 100000, 1000000]
    for sample in num_samples:
        mc_result = mc_integral(a, b, num_samples=sample)
        print(f"Monte Carlo інтеграл ({sample} точок): {mc_result}")

    # Побудова графіка
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
    plt.grid()
    plt.show()
