from django.shortcuts import render, get_object_or_404

from .models import Phones


def index(request):
    phones = Phones.objects.order_by('brand')
    context = {'phones': phones}
    return render(request, 'index.html', context)


def model_of_phone(request, phone_name):
    query = {'brand': phone_name}
    phone = get_object_or_404(Phones, **query)

    context = {
        'phone': phone,
        'types': phone.types.all(),
        'class': phone_name.lower()
    }
    return render(request, 'model_of_phone.html', context)


def image_of_phone(request, pk):
    img = Type.objects.get(id=pk)
    data = {'id': img}
    return render(request, 'image_of_phone.html', data)
