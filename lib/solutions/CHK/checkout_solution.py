# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> str:
    store_items = {"A": 50, "B": 30, "C": 20, "D": 15}
    return store_items.get(skus, -1)

