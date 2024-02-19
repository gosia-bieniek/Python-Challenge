for x in range (1,101):
    if (x % 3 ==0) & (x % 5 ==0):
        print ('FizzBuzz')
        continue
    if x % 3 ==0:
        print ('number-divisible-by-three',x,'Fizz')
        continue
    if x % 5 ==0:
        print ('number-divisible-by-five',x,'Buzz')
        continue
    print (x)