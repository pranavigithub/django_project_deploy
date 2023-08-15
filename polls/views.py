from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.views.generic.base import TemplateView

def home(request):
    return HttpResponse("""I am in Django project ----
    polls.views.home(function)----->(add to url)polls.url ---<poll.urls> need to be include in the <mysite.urls>
    """)

def html_render(request):
    messages.add_message(request, messages.INFO, "HelloWorld.")
    messages.debug(request, "%s SQL statements were executed." %100)
    messages.info(request, "Three credits remain in your account.")
    messages.success(request, "profile details updated.")
    messages.warning(request, "Your account expires in three days.")
    messages.error(request, "Document deleted.")
    my_data={
        "list":["Python", "Django", "selinium"],
        "python":["2.7","3.8","3.10"],
        "django":["2.3.1", "4.1.2"],
        "user" :{
            "first_name": "praveen",
            "last_name":"Kumar",
            "email":"praveen@gmail.com"
        }
    }

    my_users=[
        {"first_name": "pradeep", "last_name":"kumar", "salary":12345678, "email":"pradeep@gmail.com", "dob":datetime(1994,4,23,5,30,30) },
        {"first_name": "praveen", "last_name":"kumar", "salary":12345678, "email":"praveen@gmail.com", "dob":datetime(1996,5,5,5,15,30) },
        {"first_name": "shiva", "last_name":"kumar", "salary":12345678, "email":"shiva@gmail.com", "dob":datetime(1996,5,5,5,15,30)}
         ]
    return render(request,"polls/render.html", context={"data" : my_data, "users": my_users})


class HomePageView(TemplateView):
    template_name = "polls/render.html"

    def get_context_data(self,**kwargs):
        my_data={
            "list":["Python", "Django", "selinium"],
            "python":["2.7","3.8","3.10"],
            "django":["2.3.1", "4.1.2"],
            "user" :{
                "first_name": "praveen",
                "last_name":"Kumar",
                "email":"praveen@gmail.com"
            }
        }
        my_users=[
            {"first_name": "pradeep", "last_name":"kumar", "salary":12345678, "email":"pradeep@gmail.com", "dob":datetime(1994,4,23,5,30,30) },
            {"first_name": "praveen", "last_name":"kumar", "salary":12345678, "email":"praveen@gmail.com", "dob":datetime(1996,5,5,5,15,30) },
            {"first_name": "shiva", "last_name":"kumar", "salary":12345678, "email":"shiva@gmail.com", "dob":datetime(1996,5,5,5,15,30)}
        ]
        context={"data" : my_data, "users": my_users}
        return context
#Without django forms.
def from_user(request):
    if request.method == "POST":
        """
        <input name="name" palceholder="Enter your Fullname"><br>
        <input name="email" placeholder="Enter your Emial"><br>
        <input name="phone" placeholder="Entermyour PhoneNumber"><br>
        
        view:
        request.POST
        ipdb> request.method
        'POST'
        ipdb> request.POST
        <QueryDict: {
        """
        return HttpResponse(f'{request.POST["name"]} - {request.POST["phone"]} - {request.POST["email"]}')
    else:
        return render(request, "polls/fun-wodf-form.html", {})

#with django forms.
from.forms import UserForm
def from_user_django_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponse(f'{form.data["name"]} - {form.data["phone"]} - {form.data["email"]}')
    else:
        form = UserForm()
    return render(request, "polls/fun-wdf-form.html", {"form": form})

#Django forms with class based views
