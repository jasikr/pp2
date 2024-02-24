import json

with open('C:\\Users\\Evrika\\Desktop\\\\lab4\\json\\sample-data.json', "r") as file:
    data = json.load(file)


vihod = data.get('imdata', [])

print("Interface Status")
print("=" * 79)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50,"-" * 19," ------"," " "------")

target_id = ["eth1/33", "eth1/34", "eth1/35"]

for vhod in vihod:
    l1physif = vhod.get('l1PhysIf', {}).get('attributes', {})
    
    id_value = l1physif.get('id', '')
    if id_value in target_id:
        dn = l1physif.get('dn', '')
        description = l1physif.get('descr', '')
        speed = l1physif.get('speed', '')
        mtu = l1physif.get('mtu', '')

        print("{:<50} {:<21} {:<8} {:<6}".format(dn, description, speed, mtu))