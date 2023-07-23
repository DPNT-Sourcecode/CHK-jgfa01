# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> str:
    store_items = {"A": [50, 3, 130], "B": [30, 2, 45], "C": [20], "D": [15]}
    static_skus = ("A", "B", "C")
    if skus not in static_skus:
        return -1

    skus_counter_dict = {}
    for sku in skus:
        skus_counter_dict[sku] = skus_counter_dict.get(sku, 0) + 1
    total_cost = 0
    for sku, sku_list in enumerate(store_items):
        if len(store_items.get(str)) > 1:
            discounted_items = skus_counter_dict[sku] // sku_list[0]
            remaining_items = skus_counter_dict[sku] % sku_list[0]
            final_cost = sku_list[2] * discounted_items + sku_list[0] * remaining_items
            total_cost = +final_cost
        else:
            total_cost += sku_list[0]

    return total_cost

