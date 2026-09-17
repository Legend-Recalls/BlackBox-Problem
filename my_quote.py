import math


def my_quote(weight, distance, category, express=False, coupon=""):

    rounded_weight = math.ceil(weight / 0.5) * 0.5

    price = 40 * rounded_weight + 2.5 * distance

    if category == "electronics":
        price = price * 1.30

    elif category == "fragile":
        price = price + 150

    if price > 800:
        price = price * 0.90

    if coupon == "WELCOME10":
        price = price - 100

    return round(price, 2)


def quote(weight_kg, distance_km, category, express=False, coupon=""):
    """Same signature as oracle.quote()."""
    return my_quote(weight_kg, distance_km, category, express, coupon)
