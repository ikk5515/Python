#BOJ_1076_저항
rgb = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = rgb.index(input())
b = rgb.index(input())
c = rgb.index(input())

print(int(str(a)+str(b)) * (10 ** c))       # 리스트의 a번째 + b번째 * 10^c