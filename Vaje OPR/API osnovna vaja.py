import requests

base_url = "https://api.agify.io"

#for index (enumerate)
"""
print(list(enumerate(imena)))
for i, ime in enumerate(imena):
    print(i, ime)
"""
i = 0
A = 0
call = requests.get(base_url, params={"name[i]": ["Maj", "Žiga", "Bor", "Rok"]}).json()
new = []

for i in range(len(call)):
    if age[i] > A: 
        A = age[i]
        new.append(call["name[i]"])

