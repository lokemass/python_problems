# pip install pyfiglet
import pyfiglet

import math

ascii_banner = pyfiglet.figlet_format("Fast module ")
print(ascii_banner )
print("				-by lokemass")
print("Fast modulo ")
'''step by step aproch '''
base= int(input('enter base value'))
expo= int(input("enter exponent value"))
mod= int(input("enter mod value"))
i=1
while(i<expo):
	print(base,"^",i,"=",(base**i),"mod",mod)
	print("=", ((base**i))%mod)
	i=i*2
print(base,"^",expo,"=",(base**expo,"mod",mod))
print("=", ((base**expo))%mod)
