import http.server
import socketserver
import urllib.parse

# Simple handler to process HTTP requests
class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters from the URL
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Check if 'num1' and 'num2' are provided
        if 'num1' in query_params and 'num2' in query_params:
            try:
                num1 = float(query_params['num1'][0])
                num2 = float(query_params['num2'][0])
                result = num1 + num2
                response = f"The sum of {num1} and {num2} is: {result}"
            except ValueError:
                response = "Please provide valid numbers."
        else:
            response = "Please provide 'num1' and 'num2' in the URL parameters."

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())

# Set the server port and host
PORT = 8080
HOST = "0.0.0.0"  # Makes it accessible from any device on the local network

# Start the HTTP server
with socketserver.TCPServer((HOST, PORT), SimpleHandler) as httpd:
    print(f"Serving at {HOST}:{PORT}...")
    httpd.serve_forever()

