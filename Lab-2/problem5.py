st={"name":"ratin","id":24,"department":"cse","cgpa":3.75}
for key,value in st.items():
    print(key,value)
if st["cgpa"]>=2.50:
    print("good standing")
else:
    print("academic warning")
