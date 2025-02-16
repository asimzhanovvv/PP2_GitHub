import json



json_file = 'sample-data.json'
with open(json_file, 'r') as file:
    data = json.load(file)



print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")


for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")