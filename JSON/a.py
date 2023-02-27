import json
jsondata = open("sample-data.json").read()
json_object = json.loads(jsondata)
print("=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
for i in range(3):
    attributes = json_object["imdata"][i]["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    speed = attributes.get('speed')
    mtu = attributes.get('mtu')
    descr = attributes.get('descr')
    print("{0:50} {1:20} {2:9} {3:6}".format(dn,descr,speed,mtu))