#!/usr/bin/env python3
import cgi, os

list = cgi.parse_qsl(qs) #returns a list of tuples
nome = list[0][1] #returns the value of the first tuple

print("Content-type: text/html")
print()
print("<html><head><title>Exemplo GET</title></head><body>")
for key in os.environ:
    print(key + "'" + os.environ[key] + "'<br>")

print("nome = '" + nome + "'<br>")
print("</body></html>")