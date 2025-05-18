def calculate_steps(kilos_to_lose, target_days):
    calories_in_one_kilo = 7700
    calories_to_burn = kilos_to_lose * calories_in_one_kilo
    calories_per_day = calories_to_burn / target_days
    return round(calories_per_day / 0.04, 0)