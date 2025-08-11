inventario = [
    {"producto": "camisa", "precio": 25900, "stock": "11"},
    {"producto": "pantalón", "precio": 39900, "stock": "23"},
]

inventario.append({"producto": "abrigo", "precio": 50000, "stock": "2"}),

inventario[0]["stock"] = int(inventario[0]["stock"]);
inventario[1]["stock"] = int(inventario[1]["stock"]);
inventario[2]["stock"] = int(inventario[2]["stock"]);

inventario[0]["precio"] = inventario[0]["precio"] + 10000;
inventario[1]["precio"] = inventario[1]["precio"] + 10000;
inventario[2]["precio"] = inventario[2]["precio"] + 10000;

A = inventario[0];
B = inventario[1];
C = inventario[2];

print(f"Hay {A['stock']} unidades del producto {A['producto']}. Su precio por unidad es de {A['precio']} pesos.");
print(f"Hay {B['stock']} unidades del producto {B['producto']}. Su precio por unidad es de {B['precio']} pesos.");
print(f"Hay {C['stock']} unidades del producto {C['producto']}. Su precio por unidad es de {C['precio']} pesos.");
