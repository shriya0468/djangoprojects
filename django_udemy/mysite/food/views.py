from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    item_list=item.objects.all()
    context={
    'item_list':item_list
    }
    return render(request,'index.html',context)

#class based list view
class IndexClassView(ListView):
    model=item
    template_name='index.html'
    context_object_name='item_list'

def items(request):
    return HttpResponse("It's an item view")

def detailview(request,item_id):
    itemid=item.objects.get(pk=item_id)
    context={
        'itemid':itemid
    }
    return render(request,'detail.html',context)

#class based detail view
class FoodDetail(DetailView):
    model=item
    template_name='detail.html'

def create_item(request):
    form=ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        #redirect the user to a new page(index page)
        return redirect('food:index')
    
    return render(request,'item_form.html',{'form':form})

#creating a class based view for create view
class CreateItem(CreateView):
    model=item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='item_form.html'

    def form_valid(self,form):
        form.instance.user_name=self.request.user

        return super().form_valid(form)

def update_item(request,item_id):
    items=item.objects.get(id=item_id)
    form=ItemForm(request.POST or None,instance=items)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'item_form.html',{'form':form,'items':items})

def delete_view(request,item_id):
    delete_item=item.objects.get(id=item_id)
    if request.method == 'POST':
        delete_item.delete()
        return redirect('food:index')
    return render(request,'delete.html',{'delete_item':delete_item})

