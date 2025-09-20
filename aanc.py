rom http.server import HTTPServer, BaseHTTPRequestHandler
content ="""
<html>
    <head>
        <title>
        </title>
    </head>
    <body>
        <h1 align="center">DEVICE SPECIFICATION(Aancy)</h1>
        <table border="5" cellpadings="10"cellspacing="10"</table>
            <td>SI NO</td>
            <td>DEVICE SPECIFICATION</td>
            <td>TYPE</td>

        <tr>
            <td>1</td>
            <td>device name</td>
            <td>TMP215-75</td>
        </tr>
        <tr>
            <td>2</td>
            <td>proceessor</td>
            <td>pr</td>
        </tr>
        <tr>
            <td>3</td>
            <td>installed ram</td>
            <td>16.0 gb (15.5 gb usable)
        </td>
        <tr>
            <td>4</td>
            <td>product id</td>
            <td>00456677</td>
        </tr>
        <tr>
            <td>5</td>
            <td>system type</td>
            <td>reduced</td>
        </tr>

    </tr>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
