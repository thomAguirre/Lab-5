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

if __name__ == "__main__":
    sortNumbers(getNumbers())