for resistance in range(1, 11):
    for voltage in [12, 5, 3.3]:
        print("%.2f" % (voltage / resistance), end=" ")
    print()
