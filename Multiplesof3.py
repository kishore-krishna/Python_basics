'''Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.'''


a=[]
def multiple(input):
    for i in range(0,input+1):
        if i%3==0:
            a.append(i)
    print(a)

multiple(20)
