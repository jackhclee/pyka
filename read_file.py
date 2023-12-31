import json

content = ""
if __name__ == "__main__":
    with open("pretty.json", "r", encoding="utf-8") as file:
        jObj = json.load(file)
        # jObj = json.loads("".join(file.readlines()))
        print(jObj["name"] + str(jObj["price"]) + ' ')
        jObj["name"] = "London"
        print(json.dumps(jObj))

   


