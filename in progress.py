f = open('trial','r')

count = 0 
total = 0
for line in f:
    if ':' in line:
        m = line.replace(':',' ')
        split = m.split(' ')
        if 'byr' in line:
            place = split.index('byr') 
            if int(split[place+1]) >= 1920 and int(split[place+1]) <= 2002:
                count += 1
        if 'iyr' in line:
            place = split.index('iyr') 
            if int(split[place+1]) >= 2010 and int(split[place+1]) <= 2020:
                count += 1
        if 'eyr' in line:
            place = split.index('eyr') 
            if int(split[place+1]) >= 2020 and int(split[place+1]) <= 2030:
                count += 1 
        if 'hgt' in line:
            count += 1 
        if 'hcl' in line:
            print('yes')
            b = split.index ('hcl') 
            if len(split[b + 1]) == 8:
                place = line.index ('hcl')
                print(line[place+4])
                if line[place + 4] == '#':
                    print('yes yes')
                    x = 5 
                    times = 0 
                    while x <11:
                        if line[place + x] == 'f':
                            times += 1
                        if line[place + x] == 'e':
                            times += 1
                        if line[place + x] == 'd':
                            times += 1
                        if line[place + x] == 'c':
                            times += 1
                        if line[place + x] == 'b':
                            times += 1
                        if line[place + x] == 'a':
                            times += 1
                        if line[place + x].isdigit ():
	                        times += 1
                        x += 1 
                    if times == 6:
                        count += 1
        if 'ecl' in line:
            c = 0
            if 'amb' in line:
                c += 1 
            if 'blu' in line:
                c += 1 
            if 'brn' in line:
                c += 1 
            if 'gry' in line:
                c += 1 
            if 'grn' in line:
                c += 1 
            if 'hzl' in line:
                c += 1 
            if 'oth' in line:
                c += 1 
            if c == 1:
                count += 1
        if 'pid' in line:
            place = split.index('pid') 
            if len(split[place+1]) == 9 and split[place+1].isdigit():
                count += 1
        if count >= 1:
            print(line)
            print(count)
    else:
        if count == 7:
            print(line)
            total += 1
        count = 0 
print('Part 2 ',total)
