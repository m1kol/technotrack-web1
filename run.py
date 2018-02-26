# -*- coding: utf-8 -*-
import socket
import os

def get_response(request):
    print request
    request_lines = request.split('\n')
    request_type = request_lines[0].split(' ')

    if request_type[1] == '/':
        u_a_start = request.find("User-Agent")
        if u_a_start == -1:
            return "Hello mister!\nSorry, but we have been unable to identify you."
        str = request[u_a_start:]
        u_a_end = str.find('\n')
        if u_a_end == -1:
            return "Hello mister!\nSorry, but we have been unable to identify you."

        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n" \
               "<html>\n<head><title>/</title></head>\n<body>\n" \
               "<p>Hello mister!</p>\n<p>You are: " + str[12:u_a_end] + "</p>\n</body></html>"

    elif request_type[1] == "/test/":
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n" \
               "<html>\n<head><title>/test/</title></head>\n<body>\n" \
               "<p>" + request + "</p>\n</body></html>"

    elif request_type[1] == '/media/':
        files_list = os.listdir("/home/mkolesov/technotrack-web1-spring-2018/lesson1/files")
        files_string = ''
        for file in files_list:
            files_string = files_string + file + ', \n'

        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n" \
               "<html>\n<head><title>/media/</title></head>\n<body>\n" \
               "<p>" + files_string + "</p>\n</body></html>"
    elif request_type[1].find("/media/") != -1 and request_type[1].rfind('/') != len(request_type[1]):
        file_start = request_type[1].rfind('/')
        file_name = request_type[1][file_start:]
        path_name = "/home/mkolesov/technotrack-web1-spring-2018/lesson1/files" + file_name
        try:
            file_object = open(path_name,'r')
        except IOError:
            return "HTTP/1.1 404 Not found\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n" \
               "<html>\n<head><title>404 Not found</title></head>\n<body>\n" \
               "<center>File not found</center>\n</body></html>"
        buff = file_object.read()

        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n" + buff

    else:
        return "HTTP/1.1 404 Not found\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n" \
               "<html>\n<head><title>404 Not found</title></head>\n<body>\n" \
               "<center>Not found</center>\n</body></html>"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #
server_socket.listen(0)  #

print 'Started'
while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #
        request_string = client_socket.recv(2048)  #
        client_socket.send(get_response(request_string))  #
        client_socket.close()
    except KeyboardInterrupt:  #
        print 'Stopped'
        server_socket.close()  #
        exit()


