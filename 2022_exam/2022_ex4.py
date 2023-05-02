a = '3-4i'
b = '-5+2i'

real_1 = int(a[0:1])
real_2 = int(b[0:2])
imaginary_1 = int(a[1:3])
imaginary_2 = int(b[3:4])

c = real_1*real_2 - imaginary_1*imaginary_2
d = (real_1*imaginary_2 + real_2*imaginary_1)

print(f'{c} + {d}i')

