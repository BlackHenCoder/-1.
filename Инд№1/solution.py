python
# ============================================
# КУРСОВАЯ РАБОТА: ЗАДАЧА ПРО КУБИКИ (Вариант 3)
# ============================================

def get_input():
    """Запрашивает у пользователя число N."""
    n = int(input("Введите количество очков первого игрока: "))
    return n

def find_min_second_score(n: int) -> int:
    """Находит минимальную сумму очков второго игрока."""
    min_cubes = (n + 5) // 6
    return 7 * min_cubes - n

def find_max_second_score(n: int) -> int:
    """Находит максимальную сумму очков второго игрока."""
    return 7 * n - n

def display_result(min_score: int, max_score: int):
    """Выводит результат в консоль."""
    print(f"Минимальное: {min_score}, Максимальное: {max_score}")

def main():
    """Главная функция программы."""
    n = get_input()
    min_res = find_min_second_score(n)
    max_res = find_max_second_score(n)
    display_result(min_res, max_res)

# ============================================
# ПРОСТЫЕ ТЕСТЫ (БЕЗ ЗАВИСАНИЙ)
# ============================================

def run_tests():
    """Запускает все тесты и показывает результат."""
    print("\n" + "=" * 50)
    print("ЗАПУСК ТЕСТОВ")
    print("=" * 50)
    
    all_passed = True
    test_count = 0
    
    tests_min = [
        (1, 6, "n=1 → минимум 6"),
        (2, 5, "n=2 → минимум 5"),
        (6, 1, "n=6 → минимум 1"),
        (7, 7, "n=7 → минимум 7"),
    ]
    
    for n, expected, description in tests_min:
        result = find_min_second_score(n)
        if result == expected:
            print(f"✅ {description}: {result} → ОК")
        else:
            print(f"❌ {description}: ожидалось {expected}, получено {result}")
            all_passed = False
        test_count += 1
    
    tests_max = [
        (2, 12, "n=2 → максимум 12"),
        (36, 216, "n=36 → максимум 216"),
        (1, 6, "n=1 → максимум 6"),
        (10, 60, "n=10 → максимум 60"),
    ]
    
    for n, expected, description in tests_max:
        result = find_max_second_score(n)
        if result == expected:
            print(f"✅ {description}: {result} → ОК")
        else:
            print(f"❌ {description}: ожидалось {expected}, получено {result}")
            all_passed = False
        test_count += 1
    
    print("\n" + "=" * 50)
    if all_passed:
        print(f"✅ ВСЕ {test_count} ТЕСТОВ ПРОЙДЕНЫ!")
    else:
        print("❌ ЕСТЬ ОШИБКИ!")
    print("=" * 50)
    
    return all_passed

# ============================================
# ЗАПУСК
# ============================================

print("=" * 50)
print("ВЫБЕРИ РЕЖИМ:")
print("1 - Запустить программу")
print("2 - Запустить тесты")
print("=" * 50)

choice = input("Введите 1 или 2: ")

if choice == "1":
    main()
else:
    run_tests()