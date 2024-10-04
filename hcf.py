#Write a python program to find HCF or GCD.

num1 = int(input("enter num1 here:"))
num2 = int(input("enter num2 here:"))
def compute_hcf(x,y):
    if x>y:
       smaller = y
    else:
        smaller = x
    for i in range (1,smaller+1):
        if(x%i==0) and (y%i==0):
          HCF = i
            
        
    return HCF 
print ("the HCF is",compute_hcf(num1,num2))           




  
  
    