from django.shortcuts import render

def home(request):
    '''
    Renders home page
    :param request:
    :return:
    '''
    context = {} # an empty dictionary
    return render(request, 'home.html', context)