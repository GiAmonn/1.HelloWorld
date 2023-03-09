fileformat = input("Input fila name: ").lower()
filetype = fileformat[fileformat.find("."):]
match filetype:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")