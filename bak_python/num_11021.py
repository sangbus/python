num=int(input())

for i in range(1, num+1):
    num1, num2=map(int,input().split())
    print(f'Case #{i}: {num1+num2}')