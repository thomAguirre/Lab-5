#this script will sort some numbers

def getNumbers():
    numList = []
    while True:
        num = input("Enter some numbers (or text to exit)")
        if num.isdecimal():
            numList.append(num)
        else:
            break
    return numList

def sortNumbers(numbers):
    numbers.sort()
    print(numbers)

def goagain():
    again = input("Would you like to go again? [Y] or [N]")
    if again == "Y" or again == "y":
        sortNumbers(getNumbers())

if __name__ == "__main__":
    sortNumbers(getNumbers())
    goagain()