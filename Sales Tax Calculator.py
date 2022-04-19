#Sales Tax Calculator
#Version: 1.0.1

def calc():
    x = input('Total $')
    try:
        y = float(x) * 1.0725
        y = round(y, 2)
    except:
        y = 0
    if y > 0:
        print('Total+Tax= $',y)
    else:
        print('Please enter a number')
    print(calc())
print(calc())
