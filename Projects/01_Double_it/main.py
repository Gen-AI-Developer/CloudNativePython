def _doubleIt(number: int):
    while number < 100:
        num = number * number
        print("Number " + number.__str__() + " Double is "+ num.__str__())
        if(number>100):
            break


if __name__ == '__main__':
    num : int = int(input("Enter the number!"))
    print(_doubleIt(num))

