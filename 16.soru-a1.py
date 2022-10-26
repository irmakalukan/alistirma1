n = int(input("bir sayı giriniz= "))
def asalmi(n):
    for i in range(2,n):
        if n%i==0:
            return False
        print("sayı asal")
        return True

print(asalmi(n))
