import asyncio


from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm



@login_required
def my_secure_view(request):
    html = "<html><body><h1>Hey, it's David</h1><p>Wait for 10 seconds...</p></body></html>"
    return HttpResponse(html)



# @require_http_methods(["GET", "POST"])
# def create_student(request):
    
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new student record to the database
#             return redirect(
#                 reverse("success")
#             )  # Redirect to the success page using URL name
#     else:
#         form = StudentForm()

#     return render(request, "create_student.html", {"form": form})


# def success(request):
#     return render(request, "success.html")


def Home(request):
    return HttpResponse('Hi This is Home Page')
   

async def my_async_view(request):

    await asyncio.sleep(10)
    return JsonResponse({"message": "Hello, async world!"})


def custom_404_view(request, exception):
    return HttpResponseNotFound("<h1>This Page not found</h1>")


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to a home page or another page after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

   