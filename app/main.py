import sys


def main():
    while True:
        print("$ ", end="")
        command = input()
        
        print(f"{command}: command not found", end="")

    pass


if __name__ == "__main__":
    main()
