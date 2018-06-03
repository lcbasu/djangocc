from django.shortcuts import render

def home(request):
    '''
    Renders home page
    :param request:
    :return:
    '''
    message = "Hope and necessity. They should the pillar of your future endeavours."
    random_message_var = "Hello world!"

    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # a dictionary with the keyword  'greeting_message' mapping to the variable 'message' defined above
    # and other variables as well
    context = {
        'greeting_message': message,
        'random_message': random_message_var,
        'weekday_list': days_of_week,
    } # to be passed on as dictionary to the template for rendering
    return render(request, 'home.html', context)