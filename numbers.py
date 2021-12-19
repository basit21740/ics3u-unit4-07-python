#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# This program prints all numbers from 1000 to 2000 skiping a line every 5
# numbers


def main():
    # This function prints all numbers from 1000 to 2000 skiping a line
    # every 5 numbers
    for output in range(1000, 2000 + 1):
        if output % 5 == 0:
            print()
        print(output, end=" ")
    print("\nDone.")


if __name__ == "__main__":
    main()