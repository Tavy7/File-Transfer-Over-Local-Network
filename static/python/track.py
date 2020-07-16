from flask import request

addr = 'http://192.168.1.106:5000/'

page = request.get(addr)

print(page.content)
print(request.remote_addr)