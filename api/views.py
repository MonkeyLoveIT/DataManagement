from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from api.models import MysqlTest


# Create your views here.
def test(request):
    data = MysqlTest.objects.using('mysqldb').all().values()
    print(list(data))
    return JsonResponse({'data': list(data)})
