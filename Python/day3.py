# dt = {
#     "name" : "Mohan",
#     'branch': "cse",
#     "year": 2,
#     "year" : 3,
#     "class" : ["one","two","three"],
#     "Year" : ("1","2","3"),
#     "set" : {True,"hello",1}
# }

# print(dt)
# print(type(dt))
# print(len(dt))

# thisdt = dict(name= "john",section = "4",year= "4" )
# print(thisdt)
# print(type(thisdt))


# print(dt["model"])
# print(dt.get("model"))
# print(dt.keys())
# print(dt.values())

# dt = {
#     "brand":"ford",
#     "model": "GT",
#     "year": 1919
    
# }
# print(dt.items())
# x= dt.update({"model":"audi"})
# print(x)

# print(dt.pop("model"))
# print(dt)



# dt = {'dt1':{"name":"ram"},
#       'dt2':{"name2":"mohan"}}

# # print(dt)
# print(dt['dt2']["name2"])


# a = 200 
# b = 33 
# if b>a:
#     print("b is greater than a ")
# elif a==b:
#     print("it is equal")
# else:
#     print("a is greater then b")

# if a>b: print("a is greater then b")


# a = 2
# b = 330


# print("a") if a>b else print("b")


# a = 330 
# b = 330

# print("A") if a>b else print("equal") if a==b else print("b")


# a = 200
# b  = 33
# c = 500
# if a>b and c>a:
#     print("both conditions are true")

# a = 33
# b = 200
# if not a>b:
#     print("a is not greater then b")


# x = 41 
# if x>10:
#     print("above ten"),
#     pass
#     if x>20:
        
#         print("above 20"),
#     else:
#         print("but not above 20")
    
 

# x = int(input("enter number:"))
# y = int(input("enter number:"))
# if x==y:
#     print("cond is true")
# else:
#     print("cond is not true")


# x = input("enter alphabet:")
# if x=="a" or x=="e"



# for x in "mango":
#     print(x)

# fruits= ["apple","mango","cherry"]
# for x in fruits:
#     print(x) 


# fruits= ["apple","mango","cherry"]
# for x in fruits:
#     print(x)
#     if x == "mango":
#         break

# fruits= ["apple","mango","cherry"]
# for x in fruits:
#     print(x)
#     if x == "mango":
#         continue


# for x in range(6):
#     print(x)


# for x in range(2,10):
#     print(x)

# for x in range(6):
#     print(x)
# else:
#     print("finished")

# for x in range(6):
#     if x==3: break
#     print(x)
# else:
#     print("finish")




# dt = {
#     "name" : "Mohan",
#     'branch': "cse",
#     "year": 2,
#     "year" : 3,
#     "class" : ["one","two","three"],
#     "Year" : ("1","2","3"),
#     "set" : {True,"hello",1}
# }


# for x in dt:
#     print(dt[x])

# for x in dt.keys():
#     print(x)


# for x in dt.values():
#     print(x)


# for x , y in dt.items():
#     print(x, y)

# y = int(input("enter number:"))
# for i in range(1,11):
#     print(f"{y} * {i} = {y*i}")


# fruits = ["apple","mango","cherry"]
# for index, fruits in enumerate(fruits):
#     print(index,fruits)