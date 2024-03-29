from django.shortcuts import render, redirect
from distributor.models.DistributorModel import Distributor

def distributor_list_create(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        if fullname and email: 
            Distributor.objects.create(fullname=fullname, email=email)

    distributors = Distributor.objects.all()

    return render(request, 'distributor_create.html', {'distributors': distributors})

