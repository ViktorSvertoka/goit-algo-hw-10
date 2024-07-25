import pulp

# Створення проблеми лінійного програмування
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Змінні для кількості вироблених напоїв
x = pulp.LpVariable("Lemonade", lowBound=0, cat="Continuous")  # Кількість лимонаду
y = pulp.LpVariable(
    "FruitJuice", lowBound=0, cat="Continuous"
)  # Кількість фруктового соку

# Обмеження на ресурси
model += 2 * x + y <= 100, "Water"  # Обмеження на воду
model += 1 * x <= 50, "Sugar"  # Обмеження на цукор
model += 1 * x <= 30, "LemonJuice"  # Обмеження на лимонний сік
model += 2 * y <= 40, "FruitPuree"  # Обмеження на фруктове пюре

# Функція цілі - максимізація кількості вироблених напоїв
model += x + y, "TotalProducts"

# Розв'язання проблеми
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {pulp.value(x)}")
print(f"FruitJuice: {pulp.value(y)}")
print(f"Total Products: {pulp.value(model.objective)}")
