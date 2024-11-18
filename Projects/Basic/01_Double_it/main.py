def _double_it():
        number = int(input("Enter a number: "))
        while number < 10000:
            numb = number * 2;
            print(str(number) +" Double is :" + str(numb))
            if numb==10000:
                break
            number = numb 
_double_it()