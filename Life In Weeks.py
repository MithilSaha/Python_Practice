user_age = input("What is your age?\n")
user_expected_life_age = input("What is your expected age to live?\n")
user_lifespan_in_days = ((int(user_expected_life_age)-int(user_age)) * 365)
user_lifespan_in_months = ((int(user_expected_life_age)-int(user_age)) * 12)
user_lifespan_in_weeks = ((int(user_expected_life_age)-int(user_age)) * 52)
print(f"Your life Span is {user_lifespan_in_days} days, {user_lifespan_in_weeks} weeeks and {user_lifespan_in_months} months")