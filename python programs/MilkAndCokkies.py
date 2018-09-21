t = int(input("enter the number of test cases"))
while t!=0:
  n = int(input("enter the number of min limak spend"))
  while(n!=0):
    food = input("limak had")
    if food == "cookies" and food == "milk":
      boolean = True
    elif food == "cookies" and food == "cookies":
      boolean = False
    elif food == "milk" and food == "milk":
      boolean = True
    elif food == "milk" and food == "cookies":
      boolean = False
    else:
      boolean = False
    n=n-1
  t=t-1
  print(boolean)
