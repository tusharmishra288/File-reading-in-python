
import json
with open("realEstate_trans.json","r+") as y:
    data=y.read()
    m=json.loads(data)
    n=json.dumps(data)
    with open("output/realEstate_trans.json","w+") as y:
        y.write(json.dumps(m))
        for i in range(10):
            print(m[i])

    
            
    