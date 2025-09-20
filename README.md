# EX01 Developing a Simple Webserver
## Date:08/09/2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
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
```

## OUTPUT:
![alt text](<Screenshot 2025-09-16 190341.png>)

![alt text](<Screenshot 2025-09-16 181159.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
