mes = input()

if mes.count(":-)") == 0 and mes.count(":-(") == 0:
    print("none")
elif mes.count(":-)") == mes.count(":-("):
    print("unsure")
elif mes.count(":-)") > mes.count(":-("):
    print("happy")
else:
    print("sad")