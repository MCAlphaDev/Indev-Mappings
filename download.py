import requests, os

OBJECT = 'in-20100128-2304'

url = 'https://archive.org/download/Minecraft-JE-Indev/' + OBJECT + '/' + OBJECT + '.jar'

try:
    os.mkdir("./minecraft")
except FileExistsError:
    print("I see this ain't your first rodeo")

print("Downloading Minecraft")
myfile = requests.get(url)

print("Saving Minecraft Jar")
with open("./minecraft/" + OBJECT + ".jar", 'wb') as file:
    file.write(myfile.content)
