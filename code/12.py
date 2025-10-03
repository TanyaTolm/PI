import random

def random_chiclo():
    kost = random.randint(1, 6)

    if kost == 5 or kost == 6: print("Вы победили")
    elif kost == 3 or kost == 4: return random_chiclo()
    else: print("Вы проиграли")

    print(f"Текущее значение кости равно: {kost}")

if __name__ == "__main__": random_chiclo()