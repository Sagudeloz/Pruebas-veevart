"""
Prueba realizada por: Santiago Agudelo



Ejemplos usados:
#https://www.askpython.com/python/examples/knapsack-problem-dynamic-programming
#https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
"""
#
def knapsack (max_weight, items):
    num_items = len(items)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        item_weight, item_value = items[i - 1]
        for j in range(1, max_weight + 1):
            if item_weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_weight] +  item_value)
            else:
                dp[i][j] = dp[i - 1][j]
    #devuelve el valor total, los items tomados y los items no tomados
    taken_items = []
    j = max_weight
    for i in range(num_items, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            taken_items.append(items[i - 1])
            j -= items[i - 1][0]

    not_taken_items = [item for item in items if item not in taken_items]

    return dp[num_items][max_weight], taken_items, not_taken_items

#lsita de items que se "pueden" llevar
items = [(2, 3), (3, 4), (4, 5), (5, 6)]
#peso maximo que soporta la mochila
max_weight = 8

#llamado a la funcion para imprimir los resultados
total_value, taken_items, not_taken_items = knapsack(max_weight, items)
print(f"Total value: {total_value}")
print(f"Taken items: {taken_items}")
print(f"Not taken items: {not_taken_items}")
