from httplib import HTTPConnection

request_body = b"<?xml version='1.0'?>\n<methodCall>\n<methodName>myfunction</methodName>\n<params>\n<param>\n<value><int>2</int></value>\n</param>\n<param>\n<value><int>3</int></value>\n</param>\n</params>\n</methodCall>\n"

print "request"
print request_body

connection = HTTPConnection('localhost:8000')
connection.putrequest('POST', '/RPC2')
connection.putheader('Content-Type', 'text/xml')
connection.putheader('User-Agent', 'Python-xmlrpc/3.5')
connection.putheader("Content-Length", str(len(request_body)))
connection.endheaders(request_body)


print "response"
print(connection.getresponse().read())