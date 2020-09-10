sym = { 
        '!' : '1',
        '@' : '2', 
        '#' : '3', 
        '$' : '4', 
        '%' : '5', 
        '^' : '6', 
        '&' : '7',
        '*' : '8', 
        '(' : '9', 
        ')' : '0' 
        }
ans = ""
cipher = "%@$%%#%$$#$f$e_&b_%(#0%%%f$$#!$$%f%$$*#!%#&d"
for i in cipher:
    try:
        ans += sym[i] 
    except:
        if i!="_":
            ans += i
print(bytes.fromhex(ans).decode("ascii"))
