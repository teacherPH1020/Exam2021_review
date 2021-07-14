from faker import Faker
import json

f = Faker()

jsn = []

for i in range(100):
    name = f.name()
    id_ = f.random_int()
    jsn.append({
        "model":"rel.student",
        "pk": i+1,
        "fields":{
            "name": name,
            "id0": id_,
        }
    })

with open("students.json","w") as f:
    f.write(json.dumps(jsn))
