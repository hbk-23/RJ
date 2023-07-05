import json

def sum(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum

def value(file):
    cnt = 0
    max = 0
    with open(file, "r") as f:
        data = json.load(f)
    min = data[0]['price']
    for i in data:
        if i["name"] == "jacket":
            cnt = cnt + 1
            if max < i["price"]:
                max = i["price"]
            if min > i["price"]:
                min = i["price"]
    
    
    print(cnt)
    print(max)
    print(min)
    

value("catalog.json")