text = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ']
l = []

for i in text:
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))
''.join(l)
print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

print([i for i in range(10) if i % 2 == 0])
