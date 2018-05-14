from django.shortcuts import render
from apps.vpp_record.models import AdminUser
from apps.common.response import ok

# Create your views here.

def vpp_login(request):
    name = request.GET['userName']
    password = request.GET['userPass']
    dict = {}
    if request.method == 'GET':
        user = AdminUser.get_user_by_name(name)
        if user.password == password:
            dict['response'] = 'success'
        else:
            dict['response'] = 'fail'

    return ok(dict)


