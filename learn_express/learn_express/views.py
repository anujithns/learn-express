from django.shortcuts import render

from django.shortcuts import render

def home(request):
    items = [
        {'title': 'Get started', 'description': 'Start an express server in 5 minutes and sent your first request', 'price': 10},
        {'title': 'From scratch', 'description': 'Learn from scrach how express works and build a similar one', 'price': 20},
        {'title': 'Web security', 'description': 'Make your express web app resistant to attacks and make it safe', 'price': 30},
        {'title': 'Authentication', 'description': 'Add different authentication techniques to the express server', 'price': 40},
        {'title': 'WebSockets', 'description': 'Create a realtime web application with express and websockets', 'price': 50},
    ]
    context = {'items': items}
    return render(request, 'home.html', context)
