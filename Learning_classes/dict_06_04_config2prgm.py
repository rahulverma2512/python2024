# commands = {"intf": "Gig0/1",
# 		    'speed': '1000',
# 			'duplex': 'full',
#             'desc': 'switchport'}

# import yaml
# config_file = open("int_config.yaml","r")
# commands = yaml.safe_load(config_file)
# # print(commands)
# config_file.close()

# config_file = open("int_config_wr.yaml","w")
# yaml.dump(commands,config_file)


import json
config_file = open("int_config.json","r")
commands = json.load(config_file)

# config_file = open("int_config_wr.json","w")
# json.dump(commands,config_file,indent=4)

configtempl = {"intf": "interface {}",
               'desc':'description {}',
			    'speed': 'speed {}',
				'duplex': 'duplex {}'
			  }

# for k,v in commands.items():
# 	print(k,v)
conf_file = open("intf_config.config",'w')
for k, v in configtempl.items():
# #     # print(v)
	# print(configtempl[k].format(commands[k]))
	conf_file.write(configtempl[k].format(commands[k]) +'\n')
conf_file.close()

# open_to_read = open("intf_config.config",'r')
# output = open_to_read.readline()
# print(output)
# open_to_read.close()

# open_to_read = open("intf_config.config",'r')
# for line in open_to_read.readlines():
# 	print(line.rstrip('\n'))
# open_to_read.close()

# open_to_read = open("intf_config.config",'r')
# for line in open_to_read.readlines():
# 	print(line)
# open_to_read.close()

# open_to_read = open("intf_config.config",'r')
# output = open_to_read.readlines()
# print(output)
# open_to_read.close()
