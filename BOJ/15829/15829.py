l = int(input())
string = input()
result = 0

for i in range(l):
  result += ((ord(string[i]) - 96) * (31 ** i)) % 1234567891
  
print(result % 1234567891)
