T = {i for i in range(101, 251) if i % 3 == 0}

T = T - {i for i in T if i % 6 == 0}

print("\nМножина T після вилучення чисел, які діляться на 6:")
print(T)
