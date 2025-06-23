from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def get_page(request):
    dishes = Dishes.objects.all()
    paginator = Paginator(dishes,5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context={
        'page_obj':page_obj
    }
    return render(request,'table.html',context)

