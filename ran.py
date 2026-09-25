import os
import platform


def banner():
    os.system("clear")
    print("""
╔══════════════════════════════╗
║          MY TOOL             ║
║        Version 1.0           ║
╚══════════════════════════════╝
""")


def main():
    while True:
        banner()

        print("""
[1] Say Hello
[2] About
[3] System Info
[0] Exit
""")

        choice = input("Select an option: ")

        if choice == "1":
            print("\nHello! Welcome to MyTool.")
            input("\nPress Enter to continue...")

        elif choice == "2":
            print("\nMyTool - Version 1.0")
            print("My first Python/GitHub project.")
            input("\nPress Enter to continue...")

        elif choice == "3":
            print("\nSystem Information")
            print("System:", platform.system())
            print("Machine:", platform.machine())
            print("Python:", platform.python_version())
            input("\nPress Enter to continue...")

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
