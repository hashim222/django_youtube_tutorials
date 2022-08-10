from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, 'home.html')


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html')


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4567, 8910]
    }
    return render(request, 'about.html', my_context)


def social_view(request, *args, **kwargs):
    return render(request, 'social.html')
