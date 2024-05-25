f = open('trial','r')

count = 0
count2 = 0
for line in f:
    x =line.replace('-',' ')
    m = x.replace(':','')
    split= m.split(' ')
    times = split[3].count(split[2])
    if times >= int(split[0]) and times <= int(split[1]):
        count += 1
    letter = split[2]
    a = int(split[0])-1
    b = int(split[1])-1
    t = 0
    if (split[3][a]) == letter:
        t += 1 
    if split[3][b] == letter:
        t += 1
    if t == 1:
        count2 += 1
    
print('Part 1 =',count)
print('Part 2 =', count2)
