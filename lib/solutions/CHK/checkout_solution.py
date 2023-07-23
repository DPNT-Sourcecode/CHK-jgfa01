# noinspection PyUnusedLocal
# skus = unicode string

store_items = {"A": [50, 3, 130], "B": [30, 2, 45], "C": [20], "D": [15]}


def calculate_price(
    sku: str, d_cost: int, d_count: int, r_count, occurrence: int
) -> int:
    if len(store_items.get(str)) == 1:
        return store_items.get(str)
    discounted_items = occurrence // d_count
    remaining_items = occurrence % d_count


def checkout(skus: str) -> str:
    static_skus = ("A", "B", "C")
    if skus not in static_skus:
        return -1

    special_offer_a_count = 3
    special_offer_a_price = 130
    special_offer_b_count = 2
    special_offer_b_price = 45

    skus_counter_dict = {}
    for sku in skus:
        skus_counter_dict[sku] = skus_counter_dict.get(sku, 0) + 1
    for sku, sku_list in enumerate(store_items):
        if len(store_items.get(str)) > 1:
            current_price = calculate_price(
                sku, sku_list[2], sku_list[1], sku_list[0], skus_counter_dict[sku]
            )

        total_cost = (
            special_offer_a_price * discounted_items_a
            + store_items["A"]
            + remaining_items_a
        )

    return store_items.get(skus, -1)

