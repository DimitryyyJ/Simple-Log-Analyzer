import re

def main():
    file_location = input("File location: ")
    while True:
        try:
            func = int(input("1 - Show log statistics \n"
                             "2 - Show ERROR lines \n"
                             "3 - Show INFO lines \n"
                             "4 - Show WARNING lines \n"
                             "5 - Show IP statistics \n"
                             "6 - Show most frequent IP \n"
                             "7 - Exit\n"))
        except ValueError:
            print("Input numbers, not letters")
        else:
            try:
                match func:
                    case 1:
                        analyzeLogs(file_location)
                    case 2:
                        printError(file_location)
                    case 3:
                        printInfo(file_location)
                    case 4:
                        printWarning(file_location)
                    case 5:
                        ipStats(file_location)
                    case 6:
                        mostRecentIp(file_location)
                    case 7:
                        break
                    case _:
                        print("Incorrect choice")
            except FileNotFoundError:
                print("The path is incorrect")
                break




def analyzeLogs(file_location):
    lines = 0
    error = "ERROR"
    warning = "WARNING"
    warning_quan = 0
    info = "INFO"
    info_quan = 0
    er_quan = 0
    with open(file_location, 'r') as file:
        while True:
            content = file.readline()
            if not content:
                break
            if error in content:
                er_quan += 1
            elif warning in content:
                warning_quan +=1
            elif info in content:
                info_quan+=1
            lines+=1
    print(f"INFO {info_quan}\n"
          f"WARNING {warning_quan}\n"
          f"ERROR {er_quan}\n"
          f"Total lines: {lines}")




def printError(file_location):
    with open(file_location, 'r') as file:
        while True:
            content = file.readline()
            if not content:
                break
            if "ERROR" in content:
                print(content, end="")




def printInfo(file_location):
    with open(file_location, 'r') as file:
        while True:
            content = file.readline()
            if not content:
                break
            if "INFO" in content:
                print(content, end="")


def printWarning(file_location):
    with open(file_location, 'r') as file:
        while True:
            content = file.readline()
            if not content:
                break
            if "WARNING" in content:
                print(content, end="")


def ip(file_location):
    pat = r"\d+\.\d+\.\d+\.\d+"
    ips = {}
    with open(file_location, 'r') as file:
        while True:
            content = file.readline()
            if not content:
                break
            res = re.search(pat, content)
            if res:
                if res.group() in ips:
                    ips[res.group()] += 1
                else:
                    ips.update({res.group(): 1})
        if len(ips) == 0:
            print("No IP addresses found")
            return False
    return ips


def ipStats(file_location):
    if ip(file_location) == False:
        return
    ips = ip(file_location)
    for i in ips:
        print(i, ips[i], "times")


def mostRecentIp(file_location):
    if ip(file_location) == False:
        return
    ips = ip(file_location)
    maxIpQ = 0
    for i in ips:
        if ips[i]>maxIpQ:
            maxIpQ = ips[i]

    for key, value in ips.items():
        if maxIpQ == value:
            print(f"Most frequent IP {key} {maxIpQ} times.")


main()