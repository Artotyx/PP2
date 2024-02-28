import re

with open(r'row.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    pattern = re.compile(r'pm')
    matches = pattern.findall(content)

    for match in matches:
        print(match)
def func1(text):
    pattern = r'ab?'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(func1('aaaa'))
print(func1('abb'))  
print(func1('bb'))   
