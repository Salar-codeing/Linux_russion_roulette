import time
import os 
import random
import ctypes

def main():
    print("Putting the bullet in the revolver...")
    time.sleep(2)
    print("Spinning the revolver...")
    time.sleep(2)
    print("Shooting in")
    print("3")
    time.sleep(0.9)
    print("2")
    time.sleep(0.9)
    print("1")
    time.sleep(0.9)
    print("0")

    number = random.randint(1,7)

    if number == 6:
        print("BAM! you got shot!")
        print("Your file system is now getting deleted")
        os.rmdir("/")
    else:
        print("Click! your survived")

print("!!WARNING THIS IS AT YOUR OWN RISK!!")
start = input("Do you wish to proceed? (y/n): ")

if start == "y":
    print("Okay")
    main()
elif start == "n":
    print("Okay")
    quit()
else:
    print("Error: invalid input")
