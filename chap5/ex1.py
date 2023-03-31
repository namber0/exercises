while True:
    temperature = int(input("enter temperature: "))
    unit = input("enter temperature unit: ")

    if unit.lower() == 'c' or unit.lower() == 'celcius':
        temperature = 9/5 * temperature + 32
        break
    elif unit.lower() == 'f' or unit.lower() == 'farenheit':
        temperature = 5/9 * (temperature - 32)
        break
    else:
        print("wrong value")

print("%.2f" % temperature)