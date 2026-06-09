value = 250

match value:
    case value if value  > 500:
        print("buy good food")
    case value if value > 200:
        print("buy normal food")
    case _:
        print("no food")