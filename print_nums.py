#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 31, 2021
# This program lists all numbers from 1000 to 2000 and puts a new line only
# every 5 numbers


# main function
def main():
    # sets counter to zero so that python doesnt commplain
    # about undefined variables
    counter = 0
    # for each number in the range do the code in the for loop
    for each in range(1000, 2001):
        # print each number and dont go to the next line
        print(each, end=" ")
        # add to the counter
        counter = counter + 1
        # when the counter reaches 5 go to the next line then reset
        # the counter to 0
        if(counter == 5):
            print("")
            counter = 0


if __name__ == "__main__":
    main()
