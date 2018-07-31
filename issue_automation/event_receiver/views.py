from django.http.response import JsonResponse
from . import tasks


def receive_event(request):
    ret_message = {"success": False}
    method = request.method
    data = request.POST

    if method == "POST":
        tasks.handle_event.delay(data)
        ret_message['success'] = True

    return JsonResponse(ret_message)