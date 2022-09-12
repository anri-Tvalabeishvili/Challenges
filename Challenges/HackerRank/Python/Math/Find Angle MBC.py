# Enter your code here. Read input from STDIN. Print output to STDOUT
import math as m
AB = int(input())
BC = int(input())

hypotenuse = m.hypot(AB,BC)

MC = hypotenuse / 2 

ACB = (m.acos(BC/hypotenuse))

MB = m.sqrt(pow(BC,2) + pow(MC,2) - m.cos(ACB)*BC*MC*2 )

MBC = int(round((m.degrees(m.asin(m.sin(ACB)*MC/MB))),0))

print(str(MBC) + "\u00B0")