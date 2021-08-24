#Python Program To Swap Two Variables

x = 20
y = 50

#Create A Temporary Variables And Swap The Values

temp = x
x = y
y = temp

print('The Value of x After Swapping: {}'.format(x))
print('The Value of y After Swapping: {}'.format(y))

#Also We Have Another Way To Swap Two Variables

#Here Is The Result

x = 15
y = 20

x,y = y,x

print('After Swapping x is {}'.format(x))
print('After Swapping x is {}'.format(y))


print('Here !!!')