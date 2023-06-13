my_dict={"1":3, "2":2, "3":5}
items=my_dict.items()
result=sorted(items, key=lambda x: x[1])
print(result)