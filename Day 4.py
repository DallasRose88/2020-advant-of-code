f = open('trial','r')

count = 0 
total = 0
for line in f:
    if ':' in line:
        if 'byr' in line:
            count += 1 
        if 'iyr' in line:
            count += 1 
        if 'eyr' in line:
            count += 1 
        if 'hgt' in line:
            count += 1 
        if 'hcl' in line:
            count += 1 
        if 'ecl' in line:
            count += 1 
        if 'pid' in line:
            count += 1
    else:
        if count == 7:
            total += 1
        count = 0 
print('Part 1 ',total)
