import json

with open ('task1_d.json','r', encoding = "utf-8") as file:
    raw_data = file.read()
    replacements = {
        ":id=>": '"id":',
        ":title=>": '"title":',
        ":author=>": '"author":',
        ":genre=>": '"genre":',
        ":publisher=>": '"publisher":',
        ":year=>": '"year":',
        ":price=>": '"price":'
    }
    clean_data = raw_data
    for old, new in replacements.items():
        clean_data = clean_data.replace(old, new)
    correct_data = json.loads(clean_data)
    # print(correct_data)
# print(type(correct_data_dict))
    data_for_db = []
    for book in correct_data:
        raw_price = book.get("price","0")
        if "$" in raw_price:
            currency = "$"
            price = raw_price.replace('$','')
        elif "€" in raw_price:
            currency = "€"
            price = raw_price.replace('€','')
        else:
            currency = "$"
            price = raw_price.replace('$','')
        # converting to tuple
        data_for_db.append((str(book.get("id")),book.get("title"),book.get("author"), book.get("genre"), book.get("publisher"), book.get("year"), price,  currency))
    # print(data_for_db)
