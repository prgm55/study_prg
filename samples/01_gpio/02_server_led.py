# coding:utf-8
import cgi
import pigpio
# python2の場合
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
# python3の場合
#from http.server import HTTPServer
#from http.server import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/serial':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                    environ={'REQUEST_METHOD': 'POST'})
            code = form['code'].value
            print(code)

            if code == "ON":
                # 指定したピンをON状態にする
                pi.write(PIN, True)
            elif code == "OFF":
                # 指定したピンをOFF状態にする
                pi.write(PIN, False)

            self.send_response(100)
            self.send_header('Content-type', 'text/html')
            return
        return self.do_GET()

# pigpio初期化
pi = pigpio.pi()

PIN = 17
# 指定したピンを出力モードに設定
pi.set_mode(PIN, pigpio.OUTPUT)
# 指定したピンをOFF状態にする
pi.write(PIN, False)

port = 8081
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)
httpd.serve_forever()
