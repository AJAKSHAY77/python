my_disc  ={
    "name":"aksay",
    "server":"asss",
    "ram":4545534,
    "active":True
}

my_disc_2  ={
    "name":"bava",
    "server":"olol",
    "ram":0000,
    "active":False
}
# if my_disc["active"]:
# # print(my_disc.get("server"))
# # print(my_disc["name"])
#   print(my_disc["ram"])

# print(my_disc["name"])
total = [my_disc,my_disc_2]


for info in total:
   for key,value in info.items():
      if key=="active" and value==True:
         print(info)

