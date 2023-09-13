from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict

from .models import Item
import json
# Create your views here.

# print('I am here')

@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            desc = data.get('desc')
            price = data.get('price')

            if not name or not desc or price is None:
                return JsonResponse({'Message': 'Name, Desc and Price is required fields'},status=400)

            item = Item(name=name,desc=desc,price=price)
            item.save()
            return JsonResponse({"Message":"Item created successfully!"},status=200)
        except Exception as e:
            return JsonResponse({'Message':f'An error occured: {str(e)}'},status=500)

def read_items(request):
    try:
        # print("This is all items function")
        items = Item.objects.all()
        item_list = [{'id':item.id,'name':item.name, 'description':item.desc,'price':item.price} for item in items]
        return JsonResponse({'items':item_list},status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error':'No items found. '},status=404)
    except Exception as e:
        return JsonResponse({'error':f'An error occured: {str(e)}'},status=500)

def retreive_item(request,item_id):
    try:
        item = Item.objects.get(pk=item_id)
        res =  model_to_dict(item)
        return JsonResponse({'item':res})
    except ObjectDoesNotExist:
        return JsonResponse({'Error':'Item not found'},status=404)
    except Exception as e:
        return JsonResponse({'Error':f'An error occured: {str(e)}'},status=500)

@csrf_exempt
def update_item(request,item_id):
    try:
        item = Item.objects.get(pk=item_id)

        if request.method == 'PUT':
            data = json.loads(request.body)

            item.name = data['name']
            item.desc = data['desc']
            item.price = data['price']

            item.save()
            return JsonResponse({'message':'Item Updated Successfully!'})
    except ObjectDoesNotExist:
        return JsonResponse({'message':'Item not found'},status=404)
    except json.JSONDecodeError:
        return JsonResponse({'message':'Invalid JSON data in request body. '},status=400)
    except KeyError as e:
        return JsonResponse({'message':f'Missing or iinvalid field in JSON data: {str(e)}'},status=400)
    except Exception as e:
        return JsonResponse({'message':f'An error occured: {str(e)}'},status=500)



@csrf_exempt
def delete_item(request,item_id):
        try:
            item = Item.objects.get(pk=item_id)

            if request.method == 'DELETE':
                item.delete()
                return JsonResponse({'message':'Item deleted successfully!'})
            else:
                return JsonResponse({'message':'Invalid HTTP method, Use DELETE to delete an item'},status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message':'Item not found'},status=404)
        except Exception as e:
            return JsonResponse({'message':f'An error occured: {str(e)}'},status=500)