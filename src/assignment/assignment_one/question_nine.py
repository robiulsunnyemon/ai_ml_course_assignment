"""
Question: 9
Ask the user for:Principal(P),Rate(R),Time(T).Convert all to float and compute simple interest:
formula: SI=(P∗R∗T)/100
"""

p=float(input("Enter principal: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter the time: "))

si=(p*r*t)/100
print(si)