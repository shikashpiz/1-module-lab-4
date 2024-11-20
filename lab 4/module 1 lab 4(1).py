# TODO решите задачу
import json

def task(son)-> float:
    with open("input.json", 'r') as file:
        dannue = json.load(file)
    sum_vsex = sum(item["score"] * item["weight"] for item in dannue if "score" in item and "weight" in item)
    return round(sum_vsex, 3)


son = "input.json"

gotovo = task(son)
print(gotovo)
