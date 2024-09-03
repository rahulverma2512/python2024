commands_data = [{"intf": "Gig0/1",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   },
           {"intf": "Gig0/2",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   },
           {"intf": "Gig0/3",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   }]


configtempl = {"intf": "interface {}",
               'desc':'description {}',
			    'speed': 'speed {}',
				'duplex': 'duplex {}'}

for data in commands_data:
	for k,v in configtempl.items():
	# print(data)
		print(configtempl[k].format(data[k]))



    