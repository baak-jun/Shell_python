import sys


def main():
    builtin_commands = {"exit","echo","type"}
    while True:
        print("$ ",end = "")
        command = input().split()
        match command[0]:
            case "exit":
                break
            case "echo":
                print(*command[1:])
                continue
            case "type":
                
                if command[1] in builtin_commands:
                    print(f"{command[1]} is a shell builtin")
                else:
                    print(f"{command[1]}: not found")
                continue
                    
        
            
        
        print(f"{''.join(command)}: command not found")

    pass


if __name__ == "__main__":
    main()
