# noinspection PyUnusedLocal
# skus = unicode string

store_items = {"A": [50, 3, 130], "B": [30, 2, 45], "C": [20], "D": [15]}


def calculate_price(
    sku: str, d_cost: int, d_count: int, r_cost, occurrence: int
) -> int:
    if len(store_items.get(str)) == 1:
        return store_items.get(str)
    discounted_items = occurrence // d_count
    remaining_items = occurrence % d_count
    final_cost = d_cost * discounted_items + r_cost * remaining_items
    return final_cost


def checkout(skus: str) -> str:
    static_skus = ("A", "B", "C")
    if skus not in static_skus:
        return -1

    skus_counter_dict = {}
    for sku in skus:
        skus_counter_dict[sku] = skus_counter_dict.get(sku, 0) + 1
    total_cost = 0
    for sku, sku_list in enumerate(store_items):
        if len(store_items.get(str)) > 1:
            current_cost = calculate_price(
                sku, sku_list[2], sku_list[1], sku_list[0], skus_counter_dict[sku]
            )

            total_cost = +current_cost
        else:
            total_cost += sku_list[0]

    return total_cost


