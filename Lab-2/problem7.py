li=[{"name":"cup","price":250,"quantity":4},{"name":"clock","price":500,"quantity":1},{"name":"bread","price":80,"quantity":3},{"name":"cerial","price":120,"quantity":5}]
total=0
for x in li:
    total+=(x["price"]*x["quantity"])
print("before discount",total)
if total>=2000:
    total-=total*(10/100)
    print("after discount:",total)
else:
    print("no discount applied")