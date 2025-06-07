filename = input("File Name: ")

if ".gif" in filename:
    print("image/gif")
elif ".png" in filename:
    print("image/png")
elif ".jpeg" in filename:
    print("image/jpeg")
elif ".png" in filename:
    print("image/png")
elif ".pdf" in filename:
    print("application/type")
elif ".zip" in filename:
    print("application/type")
elif ".txt" in filename:
    print("text/plain")
else:
    print("application/octet-stream")
