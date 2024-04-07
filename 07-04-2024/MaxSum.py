num = list(map(int, input("Enter the elements : ").split()))
num.sort(reverse=True)
n = int(input("Enter n's value : "))
print(f"Maximum possible sum : {sum(num[:n])}")
