print("\n".join([("Fizz"*(not i%3)+"Buzz"*(not i%5)+str(i)*(i%3!=0 and i%5!=0)) for i in range(int(input("Minimum: ")),int(input("Maximum: ")) + 1)]))
