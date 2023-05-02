a = '2-3i'
b = '-5+4i'

real_1 = int(a[0:1])
real_2 = int(b[0:2])
imaginary_1 = int(a[1:3])
imaginary_2 = int(b[3:4])


c = real_1+real_2 
d = imaginary_2 +imaginary_1
print(f'{c}+{d}i')

c = real_1-real_2
d = imaginary_1 - imaginary_2
print(f'{c}{d}i')

#약간 애매한게 d 의 값이 음수면 그대로 양수면 +를 붙이는게 나을수도 있음

