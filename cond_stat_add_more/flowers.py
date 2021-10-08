hrisantems_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()
bucket = 0
if season == "Spring" or season == "Summer":
    hrisantems_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
    bucket_price = hrisantems_price * hrisantems_count + roses_price * roses_count + tulips_price * tulips_count
    bucket = hrisantems_count + roses_count + tulips_count
    if holiday == "No":
        bucket_price = bucket_price
        if tulips_count > 7:
            bucket_price -= 0.05 * bucket_price
        if bucket > 20:
            bucket_price -= 0.2 * bucket_price
    elif holiday == "Y":
        bucket_price += bucket_price * 0.15
        if tulips_count > 7:
            bucket_price -= 0.05 * bucket_price
        if bucket > 20:
            bucket_price -= 0.2 * bucket_price
if season == "Autumn" or season == "Winter":
    hrisantems_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    bucket_price = hrisantems_price * hrisantems_count + roses_price * roses_count + tulips_price * tulips_count
    bucket = hrisantems_count + roses_count + tulips_count
    if holiday == "N":
        bucket_price = bucket_price
        bucket = hrisantems_count + roses_count + tulips_count
        if roses_count >= 10 and season == "Winter":
            bucket_price -= 0.1 * bucket_price
        if bucket > 20:
            bucket_price -= 0.2 * bucket_price
    elif holiday == "Y":
        bucket_price += bucket_price * 0.15
        if roses_count >= 10 and season == "Winter":
            bucket_price -= 0.1 * bucket_price
        if bucket > 20:
            bucket_price -= 0.2 * bucket_price
print(f"{(bucket_price + 2):.2f}")

