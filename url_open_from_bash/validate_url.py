





import sys


if __name__ == "__main__":

    args = sys.argv
    if len(args) == 2:
        url = args[1]
        if url.startswith("https://") or url.startswith("http://"):
            items = url.split("/") # 3 items
            items = [item for item in items if item != ""]

            domain_name_extension = items[1]
            if domain_name_extension.__contains__("."):
                print("yes")
            # https | domain name + extension | any url parameters
        else:
            print("no")




