from django.shortcuts import render
from quotes.models import Quotes
from random import choice


def get_random_quote_parsed():
    try:
        all_quotes = Quotes.objects.all() # Toma todas las citas
        if all_quotes:
            random_quote = choice(all_quotes).quote_text.split('-')
            return random_quote
        else:
            return None
    except Quotes.DoesNotExist:
        return None
    
def homepage(request):  # Your homepage view function
  # ... your homepage logic ...
  quote = get_random_quote_parsed()
  context = { 'random_quote': quote}
  return render(request, 'homepage.html', context)
