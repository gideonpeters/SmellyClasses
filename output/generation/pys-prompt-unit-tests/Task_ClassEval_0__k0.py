import datetime

class AccessGatewayFilter:
    def filter(self, request):
        if request['path'] in ['/api/data', '/login/data']:
            return True
        elif request['path'] == '/abc' and request['method'] == 'POST':
            if 'headers' in request and 'Authorization' in request['headers']:
                user = request['headers']['Authorization']['user']
                jwt = request['headers']['Authorization']['jwt']
                if user['level'] >= 3 and jwt.endswith(str(datetime.date.today())):
                    return True
        return False

    def is_start_with(self, request_uri):
        if request_uri.startswith('/api') or request_uri.startswith('/login'):
            return True
        return False

    def get_jwt_user(self, request):
        if 'headers' in request and 'Authorization' in request['headers']:
            jwt = request['headers']['Authorization']['jwt']
            if jwt.endswith(str(datetime.date.today())):
                return request['headers']['Authorization']['user']['name']
        return None
