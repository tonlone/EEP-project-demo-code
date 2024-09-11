from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'precheck/index.html')

@csrf_exempt
def check_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Process the data here
        # For now, we'll just return a success message
        return JsonResponse({'status': 'success', 'message': 'Payment check completed successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})