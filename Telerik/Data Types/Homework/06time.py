d = int(input())
h = int(input())
m = int(input())
s = int(input())

d_convert = d * 86400
h_convert = h * 3600
m_convert = m * 60

total = d_convert + h_convert + m_convert + s

print(total)