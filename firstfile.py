
# print("hello")
# var= int(input("enter any value here:"))
 
# if(var>20):
#      print("value is greater than 20")
# elif (var==20):
#          print("value is equal to 20")
# else:
#      print("value is less than 20")

# Loop:/

# for i in range(0,100):
#     print(i+1)

# li = [1,2,"hello"]

# for item in li:
#     print(item)

# i=1
# while(i<100):
#     print(i)
#     i=i+1; 
# ////////////////////////basic calculation calculatior//////////////////////////////////
def calculator():

 var3="y"
 var=0
 while var3=="y":

  var = int(input("what you want to perform it\n For multiply press 1\n For divide press 2\n For Add press 3\n For subtraction press 4\n"))
  print("______________________")

  if var==1:
    print("you choose multiply")
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=a*b
    print("result:",c)

  elif var==2:
    print("you choose divide") 
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=a/b
    print("result:",c)

  elif var==3:
    print("you choose Add")
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=a+b
    print("result:",c)

  elif var==4:
     print("you choose subtraction")
     a=int(input("enter the value of a:"))
     b=int(input("enter the value of b:"))
     c=a-b
     print("result:",c)

  else:
    print("wrong input")
  
print("rest of code")  

 

calculator()
calculator()

print("______________________")






