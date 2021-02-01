"""
Program to count vowels, consonant, digits and special characters in string.
"""
def space_remover(s):
    l = s.split()
    s = " ".join(l)
    return s

def count_chars(st):
    vow_count = 0
    const_count = 0
    special_count = 0
    number_count = 0
    vow = "aeiou"
    st = space_remover(st)
    st = st.lower()
    for c in st:
        if 'a' <= c <= 'z':
            if c in vow:
                vow_count += 1
            else:
                const_count += 1
        elif c.isdigit():
            number_count += 1
        else:
            if c != " ":
                special_count += 1
    return [vow_count,const_count,number_count,special_count]

s = "GFG       is       a2 2  go12od     we22892bsite *@*@% 828282"
r = count_chars(s)
print("vowel count:{}".format(r[0]))
print("consonant count:{}".format(r[1]))
print("digit count:{}".format(r[2]))
print("special character count:{}".format(r[3]))




