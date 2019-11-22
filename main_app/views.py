from django.shortcuts import render, HttpResponse
from .rockauto import rockauto
from .rockauto import ebay

def result(request):
    return HttpResponse('<h1> Result view is Working </h1>')

def index(request):
    context = {}
    return render(request, 'index.html', context)

def register(request):
    year_query = request.GET.get('optone','')
    make_query = request.GET.get('opttwo','')
    model_query = request.GET.get('optthree','')
    engine_size_query = request.GET.get('optfour','')
    user_part_input_query = request.GET.get('user_part_input','')
    rockauto_query = make_query + ' ' + year_query + ' ' + model_query + ' ' + engine_size_query + ' ' + user_part_input_query
    rockauto_function_returns = rockauto(rockauto_query)
    ebay_function_returns = ebay(rockauto_query, user_part_input_query)
    ebay_cheapest_item_price = ebay_function_returns[0]
    curr_url = ebay_function_returns[1]
    google_corrected_query2 = ebay_function_returns[2]
    ebay_cheapest_item_photo_link = ebay_function_returns[3]
    ebay_cheapest_item_absolute_link = ebay_function_returns[4]
    rockauto_lowest_price = rockauto_function_returns[0]
    rockauto_curr_url =  rockauto_function_returns[1]
    google_corrected_query = rockauto_function_returns[2]
    rockauto_cheapest_item_iamge_link = rockauto_function_returns[3]
    context = {'year_query':year_query,
                'make_query':make_query,
                'model_query':model_query,
               'engine_size_query':engine_size_query,
               'user_part_input_query':user_part_input_query,
               'rockauto_lowest_price':rockauto_lowest_price,
               'rockauto_curr_url':rockauto_curr_url,
               'google_corrected_query':google_corrected_query,
               'rockauto_cheapest_item_image_link': rockauto_cheapest_item_iamge_link,
               'ebay_cheapest_item_price': ebay_cheapest_item_price,
                'curr_url' : curr_url,
                'google_corrected_query2' : google_corrected_query2,
               'ebay_cheapest_item_photo_link' : ebay_cheapest_item_photo_link,
               'ebay_cheapest_item_absolute_link' : ebay_cheapest_item_absolute_link,

               }

    return render(request, 'result.html', context)

