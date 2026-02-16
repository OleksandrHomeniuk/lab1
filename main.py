from collections import deque

# Початковий стан
start = (0, 7, 8,
         4, 5, 6,
         1, 2, 3)

# Цільовий стан
finish = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Порядок рухів: вниз, вліво, вправо, вверх
moves = {
    0: [3, 1],
    1: [4, 0, 2],
    2: [5, 1],
    3: [6, 4, 0],
    4: [7, 3, 5, 1],
    5: [8, 4, 2],
    6: [7, 3],
    7: [6, 8, 4],
    8: [7, 5]
}

# Функція для виводу стану 3х3
def print_state(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()

def bfs(start, finish):
    queue = deque()
    queue.append((start, [], 0))  # (стан, шлях, глибина)

    visited = set() # вже відвідані стани
    visited.add(start)

    generated_states = 0 # скільки всього станів згенеровано
    rejected_states = 0 # скільки відкинуто
    step = 0 # номер кроку

    max_queue_size = 1  # нова змінна

    while queue:
        # КРОКИ ВИВОДЯТЬСЯ ПОСЛІДОВНО
        input("--> Enter")

        # Беремо перший елемент з черги
        state, path, depth = queue.popleft()

        print("\n Крок", step)
        print("Глибина:", depth)
        print("Поточний стан:")
        print_state(state)
        step += 1

        if state == finish:
            return {
                "solution": path + [state],
                "depth": depth,
                "generated": generated_states,
                "stored": len(visited),
                "rejected": rejected_states
                "max_queue": max_queue_size
            }

        zero_index = state.index(0) # Знаходимо позицію порожньої клітинки

        # Генеруємо всі можливі нові стани
        for move in moves[zero_index]:
            generated_states += 1

            # Створюємо новий стан (міняємо місцями 0 і сусідній елемент)
            new_state = list(state)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            new_state = tuple(new_state)

            print("  Згенеровано стан:")
            print_state(new_state)

            if new_state not in visited:
                print("--Додано в чергу\n")
                visited.add(new_state)
                queue.append((new_state, path + [state], depth + 1))
                # оновлюємо максимум
                max_queue_size = max(max_queue_size, len(queue))
            else:
                print("--Відкинуто\n")
                rejected_states += 1

    return {
        "solution": None,
        "depth": None,
        "generated": generated_states,
        "stored": len(visited),
        "rejected": rejected_states
    }


# Запуск
result = bfs(start, finish)

if result["solution"]:
    print("\nРозв’язок знайдено")
    print("Глибина:", result["depth"])
    print("\nПослідовність станів:\n")

    for step in result["solution"]:
        print_state(step)
else:
    print("\nРозв’язок не знайдено")

print("Згенеровано станів:", result["generated"])
print("Занесено в базу:", result["stored"])
print("Відкинуто станів:", result["rejected"])
print("Максимальний розмір черги:", result["max_queue"])
