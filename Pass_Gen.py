import random

up_l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_l= up_l.lower()
digits='0123456789'
symbols="()[]{}.,:;-_\\|?+*# "

upper,lower,nums,symns= True,True,True,True

all=""

if upper:
    all+=up_l
if lower:
    all+=low_l
if nums:
    all+=digits
if symns:
    all+=symbols

length=40;
amount=10;

for x in range(amount):
    password=" ".join(random.sample(all, length))
    print(password)