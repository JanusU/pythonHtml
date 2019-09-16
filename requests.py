# Create an application that asks for an url. 
# Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page. 
# when done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).

# You will have to use the requests module, the OS module and the subprocesses module for this taks. 

from urllib.request import urlopen
import subprocess

url = str(input("FEED ME A WEBSITE NOM NOM :"))

html = urlopen(url).read().decode('utf-8')

f = open("html-copy.html","w")
f.write(html)
f.close

subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","\"new html\""])
subprocess.run(["git","push"])
subprocess.run("janusu")

