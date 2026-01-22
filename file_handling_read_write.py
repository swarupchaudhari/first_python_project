try:
    with open("my file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

with open("output.txt", "w") as file:
    file.write("Data written using 'with'.\n")