sum = 541489.48
payment = 2736.95
i =7
year = 1

for i in range(126):
    sum = sum * 1.003675 - payment
    if i >= 5:    
        year =1 + (i+6)/12        
    if  (i+6)%12 == 0:
        print("year %d, balance  %.2f"%(year-1, sum))        
    i = i + 1
    
    