isExpensive = True #boolean variable

while isExpensive == True:
    x = bool(input(" Is the health care still expensive?(True/False)"))

    if x == True:
        print ("Continuing loop")
        continue

    else:
        break
                   