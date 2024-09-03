bgp_commands = {'neighbor': 'neighbor {} remote-as {}',
					'nexthop' : 'neighbor {} nexthop-self',
					'updatesource': 'neighbor {} updatesource loopback 1',
					'policy-in' : 'neighbor {} route-map {} in',
					'policy-out' : 'neighbor {} route-map {} out'
					}
neighborlist = [ {'remote_ip': '1.1.1.1',
					'asn' :'100',
					'policy-in': 'NETG1',
					'policy-out': 'INDIA1'
				  },{'remote_ip': '2.2.2.2',
					'asn' : '200',
					'policy-in': 'NETG2',
					'policy-out': 'INDIA2'
				  },{'remote_ip': '3.3.3.3',
					'asn' : '300',
					'policy-in': 'NETG3',
					'policy-out': 'INDIA3'
				  },{'remote_ip': '4.4.4.4',
					'asn' : '400',
					'policy-in': 'NETG4',
					'policy-out': 'INDIA4'
				  }
				  
				]
#creating a file to write config : 'w : write' ; 'a:append'
config_file = open("bgp_config.config", 'w')
config_file.write("Router bgp 100" +'\n')
for data in neighborlist:
    config_file.write(bgp_commands["neighbor"].format(data["remote_ip"], data["asn"]) +'\n')
    config_file.write(bgp_commands["nexthop"].format(data["remote_ip"]) +'\n')
    config_file.write(bgp_commands["updatesource"].format(data["remote_ip"]) +'\n')
    config_file.write(bgp_commands["policy-in"].format(data["remote_ip"], data["policy-in"]) +'\n')
    config_file.write(bgp_commands["policy-out"].format(data["remote_ip"], data["policy-out"]) +'\n')
config_file.close()

#reading from a file and printing first output to terminal

read_bgpconfig = open("bgp_config.config" , 'r')
output_file = read_bgpconfig.readline()
print(output_file)
read_bgpconfig.close()

#reading from a file and printing using readlines
read_bgpconfig = open("bgp_config.config" , 'r')
output_file = read_bgpconfig.readlines()
print(output_file)

#reading from a file and printing using readlines using for loop
read_bgpconfig = open("bgp_config.config" , 'r')
for data in read_bgpconfig.readlines():
    print(data.rstrip('\n'))

    
    
