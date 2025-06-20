from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    a = 10
    b = 0
 
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    
if __name__ == "__main__":
    main()
