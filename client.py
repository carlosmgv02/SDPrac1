import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:4000/')
proxy.add_user('carlos', 'mart')
proxy.add_user('aliagas', 'calvo')
proxy.add_user('molina', 'romani')
print('EL PROGRAMA FUNCIONA: ')
print(proxy.get_users())
print(proxy.delete_user('carlos'))
print(proxy.get_users())
print("pollita")
proxy.bondia()
