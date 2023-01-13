"""
    1.5 How many years older will you be 1.00 gigaseconds from now
"""

# TODO: What is a gigasecond
# TODO: Convert the gigasecond to years from now


def output_gigasecond_years_from_now(now):
    now += 1e+9 / (3600*24*365)
    return now

print("This program takes your age as user input and returns how old that person will be a gigasecond from now")
age = int(input("Enter your age in years: "))

giga_age = output_gigasecond_years_from_now(age)
print(f"You will be {giga_age} years old a giga second from now.")