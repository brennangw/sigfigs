n = 503
print(int(n//10))
"""
int(input("int:"))
"""
mag = 10
magC = 1


while (n//mag != 0):
    mag = int(mag * 10)
    magC += 1
else:
    print("int(mag/10): " + str(int(mag/10)))
    print("magC: " + str(magC))


for place in range(magC,0,-1):
    print("place is" + str(place))
    for d in range (9,0,-1):
        print("d is " + str(d))
        print(d*10**(place-1))
        print("n//(d*10**place-1) = " + str(n//(d*10**(place-1))))
        if int(n//(d*10**(place-1))) == 1:
            print("THIS DIGIT IS: " + str(d))
            break
    else:
        print("THIS DIGIT IS: 0")
"""
get the number of places using n//10*x 
for each digit subtract each possible digit in that tens place to find the first that when // 10*x gives 
"""