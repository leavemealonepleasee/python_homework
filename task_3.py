country_capitals = {
    "USA": "Washington, D.C.",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo",
"UK": "London"
}

country = input("input country name: " )
capital = country_capitals.get(country)
if capital:
    print(f"the capital of {country} is {capital}.")
else:
    print("error")