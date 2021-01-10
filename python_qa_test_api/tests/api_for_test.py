import requests


def get_status_code(url):
    return requests.get("https://" + url).status_code


print(get_status_code("www.hackthebox.eu"))
print(get_status_code("www.google.com"))

# интерфейс iterator for itareble object
inter = iter(["alexis", "lukaku", "martinez"])
print(inter.__next__())
print(inter.__next__())


# work files
with open("interteam.txt", "w+") as files:
    files.write(inter.__next__())
    files.close()


f = open("interteam.txt", 'r')
print(f"Запись в файлу ->> {f.read()}")
print()
