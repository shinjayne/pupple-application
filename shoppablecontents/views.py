from django.shortcuts import render

def test_contents(request):
    return render(request, 'shoppablecontents/test_contents.html')