import datetime

API_DATA_PATH = '/api/data'
LOGIN_DATA_PATH = '/login/data'

class AccessGatewayFilter:
    def filter(self, request):
        if request['path'] == API_DATA_PATH and request['method'] == 'GET':
            return True
        elif request['path'] == API_DATA_PATH and request['method'] == 'POST':
            return True
        elif request['path'] == LOGIN_DATA_PATH and request['method'] == 'GET':
            return True
        elif request['path'] == LOGIN_DATA_PATH and request['method'] == 'POST':
            return True
        elif request['path'] == '/abc' and request['method'] == 'POST':
            if 'headers' in request and 'Authorization' in request['headers']:
                user = request['headers']['Authorization']['user']
                jwt = request['headers']['Authorization']['jwt']
                if user['level'] == 5 and jwt == 'user1' + str(datetime.date.today()):
                    return True
                elif user['level'] == 3 and jwt == 'user1' + str(datetime.date.today() - datetime.timedelta(days=365)):
                    return False
                elif user['level'] == 1 and jwt == 'user1' + str(datetime.date.today()):
                    return None
                else:
                    return True
        else:
            return True

    def is_start_with(self, request_uri):
        if request_uri.startswith(API_DATA_PATH) or request_uri.startswith(LOGIN_DATA_PATH):
            return True
        else:
            return False

    def get_jwt_user(self, request):
        if 'headers' in request and 'Authorization' in request['headers']:
            jwt = request['headers']['Authorization']['jwt']
            if jwt.endswith(str(datetime.date.today())):
                return jwt.split(str(datetime.date.today()))[0]
            else:
                return None
        else:
            return None