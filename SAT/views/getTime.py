from django.http import HttpResponse, JsonResponse


def getTime(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    response = JsonResponse({1:'a', 2:'b', 3:''}, safe=False)
    return HttpResponse(response)