import time


string = "HelloWORLD"


print(str.capitalize(string))
print(string.count('OR'))
print(string.find('l'))
print(string.isdigit())
print(string.isalpha())


list = ['my', 'name', 'is', 'Aditya', 'Suman']
j = " | "
teams = "Hello,is,a,world,my,friend"


print(j.join(list))
print(teams.split(','))


# tuple value can't be changed
tupul1 = (13, "ok0", "myfrnd")


print(tupul1[1])
tup_len = len(tupul1)

x = 0
while x < tup_len:
    print (tupul1[x])
    x +=1

print(tupul1[0:2])

digits = (12,58,84,900,27)

print('max:', max(digits))


dict = {"name": "aditya suman",
        "Roll": "1601ME01",
        "Money": 89500,
        "address": "home",
        "College": "IIT"}

dict['name'] = "ADITYA SUMAN"

print(dict)
print(dict['name'])


localtime = time.localtime(time.time())
print(localtime)

formatted_time = time.asctime(localtime)
print(formatted_time)


