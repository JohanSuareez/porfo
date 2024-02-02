
def fib_finder(x=input("What is the number that you want: ")):
    fib_nums=[]
    for i in range(35):
        if i ==0 or i==1 :
            fib_nums.append(i)
        else:
            fib_nums.append(fib_nums[i-2]+fib_nums[i-1])
    print(fib_nums)
    if int(x) in fib_nums:
        location = fib_nums.index(int(x))
        print (f'The number is the position {location + 1} in the Fibonacci  sequence')

    elif int(x) not in fib_nums:
        print ("The number is not part of the sequence so try again")

fib_finder()

