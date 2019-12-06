from django.shortcuts import render, HttpResponse
from .rockauto import rockauto

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
    rockauto_function_returns = rockauto(user_part_input_query, make_query, year_query, model_query)

    context = {'year_query':year_query,
                'make_query':make_query,
                'model_query':model_query,
               'engine_size_query':engine_size_query,
               'user_part_input_query':user_part_input_query,
                'rockauto_function_returns':rockauto_function_returns
               }

    return render(request, 'result.html', context)

