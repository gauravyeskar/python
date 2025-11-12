# W.A.P.P.which will obtain internal informations about the files such as file_name, file_mode, readability,writeability, and closeability.
try:
    with open("stud3.data","w+") as fp:
        print("-"*20)
        print("File Opened in Write mode. ")
        print("-"*20)
        print(f"File name: {fp.name}")
        print(f"File Opening Mode: {fp.mode}")
        print(f"Is this file readable: {fp.readable()}")
        print(f"Is this file writable: {fp.writable()}")
        print(f"Is this file Closed: {fp.closed}")
        print("-"*20)
    print("With open() as")
    print(f"Is closed: {fp.closed}")

except FileExistsError:
    print("File already exists.")