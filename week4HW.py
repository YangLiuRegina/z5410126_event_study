# Code 1
def process_string(s):
    s = s.lower()
    s_base = s.split(' ')[0:]
    return s_base
name = process_string('This is my test String.')
print(name)

#code 2
prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = list (prc_dic.keys())
sorted_keys.sort()
print(sorted_keys)

