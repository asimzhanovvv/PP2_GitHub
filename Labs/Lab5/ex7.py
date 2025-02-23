import re
text = "aaa_bbb_ccc_ddd_eee!_fff."
# text = "AaaBbbCccDddEee!Fff."

pattern = '_'

st2list = re.split('_', text)

cap_list = []

for i in st2list:
    i = i.capitalize()
    cap_list.append(i)

for i in cap_list:
    print(i, end='')