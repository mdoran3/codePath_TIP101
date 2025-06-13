def get_items_to_restock(products, restock_threshold):
    restock = {}
    if products == {}:
        return restock
    else:
        for key, value in products.items():
            if value < restock_threshold:
                restock[key] = value
    
    return restock
            
products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5

print(get_items_to_restock(products, restock_threshold))