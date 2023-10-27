from django.shortcuts import render
from . models import send_data,dynamic_data


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def landing(request):
    data = dynamic_data.objects.all()
    return render(request, 'index.html', {'data': data})



def send_landing(request):
    if request.method == 'POST':
        FullName = request.POST.get('FullName')
        Email = request.POST.get('Email')
        PhoneNumber = request.POST.get('PhoneNumber')
        Name = request.POST.get('Name')
        print('================================================================>>',
            FullName,
            Email,
            PhoneNumber,
            Name,
        )
        if FullName is not None and Email is not None and PhoneNumber is not None and Name is not None:
            send_data(FullName=FullName, Email=Email, PhoneNumber=PhoneNumber, Name=Name).save()
        return JsonResponse({"message": "Data received and processed successfully"}, status=200)
    else:
        return JsonResponse({"error": "Invalid data received"}, status=400)



def admin_admin(request):
    return render(request, "admin.html", {'admin': send_data.objects.all(), 'count': send_data.objects.count()})
