import sys


def main():
    while True:
        print("$ ",end = "")
        command = input()
        if command =="exit":
            break
        
        print(f"{command}: command not found")

    pass


if __name__ == "__main__":
    main()
