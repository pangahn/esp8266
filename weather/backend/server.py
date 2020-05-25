from http.server import BaseHTTPRequestHandler
from http.server import HTTPStatus
import json
import time
import os


class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length).decode('utf-8')
        form = json.loads(data)
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        form['time'] = time_str
        print('{}: T1: {:3.1f}C, T2: {:3.2f}C, H: {:3.1f} %, P: {:d}Pa'.format(
            time_str, form['t1'], form['t2'], form['h'], form['p']))
        writer(form)


def writer(form):
    file_name = 'data.csv'
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write('time,t1,t2,humidity,p\n')
            print('Create success.')
    with open(file_name, 'a') as f:
        f.write('{},{},{},{},{}\n'.format(form['time'], form['t1'], form['t2'], form['h'], form['p']))
        print('Write success.')


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 1111), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()