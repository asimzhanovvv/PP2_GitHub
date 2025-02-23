import re
# text = "aaa_bbb_ccc_ddd_eee!_fff."
text = "AaaBbbCccDddEee!Fff."

pattern = '[A-Z][^A-Z]*'
st2list = re.findall(pattern, text)

# casefold()

low_list = []

for i in st2list:
    i = i.casefold()
    low_list.append(i)

for i in low_list:
    print(i, end='_')