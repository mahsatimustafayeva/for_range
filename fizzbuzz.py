#1#-dən 30-a qədər ədədləri çap edin. 3-ə bölünənlərin yerinə 
#“Fizz”, 5-ə bölünənlərin yerinə “Buzz”, hər ikisinə 
##bölünənlərin yerinə “FizzBuzz” yazılsın.

for i in range(1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)