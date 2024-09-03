bgp_commands = {'neighbor': 'neighbor {} remote-as {}',
					'nexthop' : 'neighbor {} nexthop-self',
					'updatesource': 'neighbor {} updatesource loopback 1',
					'policy-in' : 'neighbor {} route-map {} in',
					'policy-out' : 'neighbor {} route-map {} out'
					}
command_data = [ {'remote_ip': '1.1.1.1',
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

# for data in command_data:
	# print(data)
	# print(bgp_commands["neighbor"].format(data["remote_ip"],data["asn"]))
	# print(bgp_commands["nexthop"].format(data["remote_ip"]))
	# print(bgp_commands["updatesource"].format(data["remote_ip"]))
	# print(bgp_commands["policy-in"].format(data["remote_ip"],data["policy-in"]))
	# print(bgp_commands["policy-out"].format(data["remote_ip"],data['policy-out']))

#creating a file to write config : 'w : write' ; 'a:append' , 'r' : read
# import yaml
# config_file = open("dict_06_04_bgp_config_data.yml", 'r')
# command_data = yaml.safe_load(config_file)
# config_file.close()
config_file = open("bgp_config.config", 'w')
# # print("Router bgp 100")
config_file.write("Router bgp 100" +'\n')
for data in command_data:
	config_file.write(bgp_commands["neighbor"].format(data["remote_ip"], data["asn"]) +'\n')
	config_file.write(bgp_commands["nexthop"].format(data["remote_ip"]) +'\n')
	config_file.write(bgp_commands["updatesource"].format(data["remote_ip"]) +'\n')
	config_file.write(bgp_commands["policy-in"].format(data["remote_ip"], data["policy-in"]) +'\n')
	config_file.write(bgp_commands["policy-out"].format(data["remote_ip"], data["policy-out"]) +'\n')
config_file.close()

#import yaml data file



# #reading from a file and printing output to terminal

read_bgpconfig = open("bgp_config.config" , 'r')

# 
for line in read_bgpconfig.readlines():
	output_file = read_bgpconfig.readlines()
	# print(output_file)
	print(line.rstrip('\n'))
read_bgpconfig.close()


         
             
    


