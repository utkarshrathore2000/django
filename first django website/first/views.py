from django.http import HttpResponse
def func(request):
    return HttpResponse(f"hello world \t utkarsh loves rashi \t utkarsh loves python")
def rashi(request):
    return HttpResponse('''<h1> utkarsh </h1> <a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'>django code with harry</a> <br>
    <a href='https://www.instagram.com/?hl=en'>\n instagram</a> 
    <br>
    <a href='https://www.google.com'> \n google </a> ''')
def pythonn(request):
    return HttpResponse('utkarsh loves python')
def removepunc(request):
    return HttpResponse('remove punc')
def removespace(request):
    return HttpResponse('remove space')
def capitalfirst(request):
    return HttpResponse('capital first')
def charcount(request):
    return HttpResponse('character count')

