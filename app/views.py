from django.shortcuts import render, redirect
from .forms import StudentForm
# Create your views here.


def home(request):
    #submitted = False
    submitted = request.GET.get('submitted', False)
    template_name = "app/home.html"
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            print("===== FORM SUBMITTED =====")
            print("Name:", student.name)
            print("Email:", student.email)
            print("Message:", student.message)
            print("==========================")
            submitted = True
            return redirect('/?submitted=True')

    else:
        form = StudentForm()

    return render(request, template_name, {
        "form": form,
        "submitted": submitted
    })

#docker restart django_app

#docker logs -f django_app
