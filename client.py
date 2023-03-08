import xmlrpc.client
proxy= xmlrpc.client.ServerProxy("http://localhost:4000/")
result = proxy.add_user('carlos','mart')
print('EL PROGRAMA FUNCIONA: ', result)
print(proxy.get_users())
print(proxy.delete('molina'))
print(proxy.get_users())