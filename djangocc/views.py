from django.shortcuts import render

def home(request):
    '''
    Renders home page
    :param request:
    :return:
    '''
    message = "Hope and necessity. They should the pillar of your future endeavours."
    random_message_var = "Hello world!"

    # a dictionary with the keyword  'greeting_message' mapping to the variable 'message' defined above
    # and other variables as well
    context = {
        'greeting_message': message,
        'random_message':random_message_var
    } # to be passed on as dictionary to the template for rendering
    return render(request, 'home.html', context)