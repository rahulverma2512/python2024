import yaml
file = open("office_test_prgm_data.yaml", 'r')
data = yaml.safe_load(file)
print(data)
file.close()

ip = data["ip_add"]
key = data['key_val']
port = "443"
def sum(a,b,c):
    s = a + b + c
    return s
firewalls = ({'ip': data["ip_add"], 'key': data['key_val'], 'port': port})
print(firewalls)
for items in firewalls:
    sum(ip,key,port)
    print(sum(ip,key,port))
