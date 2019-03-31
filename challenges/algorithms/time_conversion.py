t = input().strip()
h, m, s = map(int, t[:-2].split(':'))
p = t[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))
