### Variation of ip address checker
##Variation one with more print statement
# ip = input("enter your ip :")
# ip = ip.split(".")
# if len(ip) == 4 and int(ip[0]) != 0:
#     for item in ip:
#         if int(item) > 0 and int(item) <= 255:
#             print("all octates are valid")
#         else:
#             print("invalid octates")
# else:
#     print("invalid IP")  

# #Variation  with less  print statement and flag value = false

# ip = input("enter your ip :")
# ip = ip.split(".")
# flag = False
# if len(ip) == 4 and int(ip[0]) != 0:
#     for item in ip:
#         if int(item) > 0 and int(item) <= 255:
#             flag = True
#     if flag == True:
#         print("IP with valid octates")
#     else:
#             print("invalid octates")
# else:
#     print("invalid IP")

#Variation  with less  print statement and flag value = true

ip = input("enter your ip :")
ip = ip.split(".")
flag = True
if len(ip) == 4 and int(ip[0]) != 0:
    for item in ip:
        if not (int(item) >= 0 and int(item) <= 255):
            flag = False
            break
    if flag == True:
        print("IP with valid octates")
    else:
            print("invalid octates")
else:
    print("invalid IP")