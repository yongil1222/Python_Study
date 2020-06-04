count = 0
sum = 0

while count < 1000 :
    if(count%3 == 0) :
        sum += count
    count += 1
print("Sum of multiples of 3 from 0 to 1000 is %d" %sum)

count = 0
while count < 5 :
    for i in range(0, count+1) :
        print("*", end = " ")
    print('')
    count += 1