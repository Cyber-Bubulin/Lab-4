from pprint import pprint

max_cells = 7

items = {
    'r': (25,3),
    'p': (15,2),
    'a': (15,2),
    'm': (20,2),
    'i': (5,1),
    'k': (15,1),
    'x': (20,3),
    't': (25,1), 
    'f': (15,1),
    'd': (10,1),
    's': (20,2),
    'c': (20,2)
}

points = 205

def get_cells_and_price(items):
    cells = [items[item][1] for item in items]
    price = [items[item][0] for item in items]
    return cells, price


def get_memtable(items, max_cells):
    cells, price = get_cells_and_price(items)
    n = len(price) 
    V = [[0 for a in range(max_cells+1)] for i in range(n+1)]

    for i in range(n+1):
        for a in range(max_cells+1):
            if i==0 or a==0:
                V[i][a]=0
            elif cells[i-1]<=a:
                V[i][a] = max(price[i-1]+V[i-1][a-cells[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i-1][a]
    return V, cells, price


def get_selected_items_list(items, max_cells):
    V, cells, price = get_memtable(items, max_cells)
    n = len(price)
    res = (V[n][max_cells])
    a = max_cells
    items_list = [(5, 1)]

    for i in range(n, 0, -1):
        if res <=0:
            break
        if res == V[i-1][max_cells]:
            continue
        else:
            items_list.append((price[i-1], cells[i-1]))
            res -= price[i-1]
            a -= cells[i-1]
    selected_stuff = []
    
    for search in items_list[:-1]:
        flag = 0 
        for key, price in items.items():
        
            if price == search and flag==0:
                flag+=1
                for j in range(price[1]): 
                    selected_stuff.append(key)          
    return selected_stuff
backpack = get_selected_items_list(items, max_cells)
print (backpack[:3])
print (backpack[3:6])
print (backpack[6:10])

totvalue = sum([items[item][0] for item in get_selected_items_list(items, max_cells)])
print("Итоговые очки выживания:" ,(totvalue*2)-points+15)

