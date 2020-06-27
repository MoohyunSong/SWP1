from cgi import parse_qs
from number_template import html
import matplotlib.pyplot as plt
import os

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    try:
        a, b = int(a), int(b)
        number_sum = "%d + %d = %d" %(a,b,a+b)
        number_multi = "%d * %d = %d" %(a,b,a*b)

        f = open("/usr/local/swp1/result.txt", "w")
        f.write(number_sum)
        f.write("\n")
        f.write(number_multi)
    except:
        f = open("/usr/local/swp1/result.txt", "w")
        f.write("Please enter two numbers to calculate.")

    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])

    return [response_body]



