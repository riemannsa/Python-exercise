#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#Write a loop that prints each of the numbers on a new line.
#Write a loop that prints each number and its square on a new line.
#Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.
#Print the product of all the numbers in the list. (product means all multiplied together)

total = 0
product=1
for xs in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print (xs)
    print(xs,",",xs**2)
    total=total+xs
    product= product * xs
print("The total is:",total)
print("The product is:",product)
