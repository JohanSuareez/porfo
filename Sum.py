# Print the consecutive summation of the integer given
def sumation(x):
    count=0
    count1=0
    for i in range(x):
        print(f'This is the natural number {count} and the previous number is {count1} lastly this is the submation {count+count1}')
        count1=count+count1
        count=count+1
sumation(10)
