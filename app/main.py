import sys
import shutil
import subprocess


def main():
    builtin_commands = {"exit","echo","type"}
    while True:
        print("$ ",end = "")
        command = input()
        if command=="":
            continue
        elif command=="exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            elif path := shutil.which(command[5:]):
                print(f"{command[5:]} is {path}")
            else:
                print(f"{command[5:]}: not found")                    
        
            
        
        else:
            print(f"{''.join(command)}: command not found")

    pass


if __name__ == "__main__":
    main()
