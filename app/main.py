import sys


def main():
    while True:
        print("$ ",end = "")
        command = input().split()
        match command[0]:
            case "exit":
                break
            case "echo":
                print(*command[1:])
                continue
        
            
        
        print(f"{"".join(command)}: command not found")

    pass


if __name__ == "__main__":
    main()
