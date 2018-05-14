from django.http import JsonResponse, HttpResponse


def ok(data=None):
    response = JsonResponse({
        'result': {
            'success': True,
            'code': 0,
            'msg': '',
            'displaymsg': '',
        },
        'data': data if data else {}
    })

    response = set_headers(response)
    return response

def set_headers(response):
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers' + \
                                               ',Access-Control-Allow-Methods' + \
                                               ',Access-Control-Allow-Origin' + \
                                               ',Authorization' + \
                                               ',Content-Type' + \
                                               ',Crossdomain'
    response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, PATCH, OPTIONS'
    response['Access-Control-Allow-Credentials'] = True
    return response



