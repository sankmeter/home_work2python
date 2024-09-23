last1 = int(input( "введіть 5 значне число ")) #наприклад 12345
number1 = last1 % 10
number2 = (last1 % 100) // 10
number3 = (last1 % 1000)  // 100
number4 = (last1 % 10000) // 1000
number5 = (last1 % 100000) // 10000
print(number1, number2, number3, number4, number5, sep='')