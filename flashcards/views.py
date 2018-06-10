# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Deck

def home(request):
    '''
    Renders the FLASCARDS home template
    '''
    query_set = Deck.objects.all()
    context = {
        'decks':query_set
    }
    return render(request, 'flashcards/home.html', context)
