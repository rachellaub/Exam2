#!/usr/bin/env python3
"""
Python Task 5
Common words
"""


def main():
    """
    Test your module
    """
    input_file_1 = input("Enter the name of a file: ")
    input_file_2 = input("Enter the name of a file: ")

    #open input 1
    input1 = open(input_file_1, mode='rt', encoding='utf-8')
    #open input 2
    input2 = open(input_file_2, mode='rt', encoding='utf-8')
    print("The words that are common to both files.")

    series1 = []
    series2 = []
    for line in input1:
        #strip the \n character
        ser1 = line.strip()
        series1.append(ser1)
        for lines in input2:
            #strip the \n character
            ser2 = lines.strip()
            series2.append(ser2)
            if series1 == series2:
                print(series1)


    input1.close()
    input2.close()

if __name__ == "__main__":
    main()
    exit(0)
