import yaml,jinja2

config_file = open("test_jinja_data.yml",'r')
data = yaml.safe_load(config_file)
# print(data)
# print("vlan", data["vlans"][1])


#load jinja2 template from file
template_loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=template_loader)
template = env.get_template("testjinja.j2")
# print(template)

# render the template with the data
file = ("test_jinja_wr.conf",'w')
rendered_output = template.render(conf_vlan=data)
# file.write(rendered_output = template.render(conf_vlan=data))
print(rendered_output)

file = open("generated_conf.config","w")
file.write(template.render(conf_vlan=data))
file.close()


