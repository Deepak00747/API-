from rest_framework.response import Response
from rest_framework.decorators import api_view

def DPfact(N):
    arr = {}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
        arr[N] = 1
    else:
        factorial = N * DPfact(N - 1)
        arr[N] = factorial
    return factorial
 
def error_log(code, msg):
    return Response({
            "code": code,
            "msg": msg
    })

@api_view(['GET'])
def getData(request):

    num = request.GET.get('fact', '')

    if not num:
        return error_log(500,"Factorial Number not specified")

    num = int(num)

    if (num > 956):
        return error_log(500,"The Entered Value is too High")

    if (num < 0):
        return error_log(500,"The Entered Value is too Low")

    anss = DPfact(num)
    data = {'code': 200, 'FactNumber': num, 'FactValue': anss }
    return Response(data)
