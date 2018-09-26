kg1,jq1 = eval(raw_input(">>"))
kg2,jq2 = eval(raw_input(">>"))
dj1 = jq1/kg1
dj2 = jq2/kg2
if dj1 > dj2:
    print("Package 2 has the better price")
else:
    print("Package 1 has the better price")
