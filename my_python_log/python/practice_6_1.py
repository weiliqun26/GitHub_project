River_Country = {"nile": "egypt", "amazon": "brazil", "yangtze": "china"}
for river, country in River_Country.items():
    print(f"The {river.title()} runs though {country.title()}.")

for river in River_Country.keys():
    print(river.title())

for country in River_Country.values():
    print(country.title())
