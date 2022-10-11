from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import ChickenItems,Category,OrderModel

class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/index.html')
class About(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/about.html')

class Order(View):
    def get(self,request,*args,**kwargs):
        appetizers = ChickenItems.objects.filter(category__name__contains = "appetizers")
        desserts = ChickenItems.objects.filter(category__name__contains = "Dessert")
        drink = ChickenItems.objects.filter(category__name__contains = "drink")
        entres = ChickenItems.objects.filter(category__name__contains = "Entre")


        context ={
            'appetizers' :appetizers,
            'desserts' : desserts,
            'drink' : drink,
            'entres' : entres
        }

        return render (request,'customer/order.html',context)
    def post(self,request,*args,**kwargs):
        order_items = {
           'items' : []
        }
        items = request.POST.getlist('items[]')

        for item in items:
            chicken_item = ChickenItems.objects.get(pk__contains = int(item))
            item_data = {
                'id' : chicken_item.pk,
                'name' : chicken_item.name,
                'price' : chicken_item.price
            }
            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price +=item['price']
            item_ids.append(item['id']) 

        order=OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items':order_items['items'],
            'price':price
        }   

        return render(request,'customer/order_confirmation.html',context)     
            


