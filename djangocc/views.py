from django.shortcuts import render

def home(request):
    '''
    Renders home page
    :param request:
    :return:
    '''
    # a dictionary with the keyword to be passed on as dictionary to the template for rendering
    context = {

    }
    return render(request, 'home.html', context)