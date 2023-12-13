import os

if __name__ == '__main__':
    print("Welcome to robospeaker 1.0")
    while True:
            x = input("Enter what you want to say ")
            if x == "q":
                break
            command = f"say {x}"
            os.system(command)


