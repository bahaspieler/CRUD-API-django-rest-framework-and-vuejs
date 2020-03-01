from .models import product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.views import APIView
import json
import re

p_gte= re.compile(r'g', re.I)
p_lte= re.compile(r'l', re.I)

# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


catagory=['null']
info_site =[]
info_search =[]

def info_caching(lis, apnd):
    if not lis[0] in [j for i in apnd for j in i]:
        apnd.append(lis)
        # print('appended')
    else:
        try:

            x = [apnd.index(i) for i in apnd if lis[0] in i]
            del apnd[x[0]]
            apnd.append(lis)

            # print(x)
        except:
            print('doesnt exist')

def info_position(lis,id):
    for sub_list in lis:
        if id in sub_list:
            return lis.index(sub_list)


class GetFieldList(APIView):
    def post(self,request):
        data = json.loads(request.body)
        print(data)
        user_name= data['first_name']
        user_id = data['from_user']

        filter = data['text'].split()
        if filter[0] == 'Product' or filter[0] == 'Price':
            site_info=[data['from_user'],data['text']]
            info_caching(site_info, info_site)

        else:
            search_info= [data['from_user'],data['text']]
            info_caching(search_info,info_search)

        print('info site: ',info_site)
        print('info search: ',info_search)

        info_site_position = info_position(info_site,user_id)
        info_search_position = info_position(info_search, user_id)

        print('info_site_position: ', info_site_position)
        print('info_search_position: ',info_search_position)

        try:
            filter2= info_search[info_search_position][1].split()
        except:
            print("Search hasn't inserted")
        # print(filter)
        try:

            if filter[0] == 'Product' or filter[0] == 'Price':
                catagory[0] = filter[0]

                text ='insert'
                return Response({"text": text, "code": 200})

            if info_site[info_site_position][1] == 'Product':
                text1 = product.objects.all().filter(name__icontains=info_search[info_search_position][1])
                text = list(text1.values('name','price'))


            elif info_site[info_site_position][1] == 'Price' and p_gte.findall(filter2[0]) !=[]:
                text1 = product.objects.all().filter(price__gte=int(filter2[1]))
                product(text1)
                text = list(text1.values('name','price'))

            elif info_site[info_site_position][1] == 'Price' and p_lte.findall(filter2[0]) !=[]:
                text1 = product.objects.all().filter(price__lte=filter2[1])
                text = list(text1.values('name','price'))



            else:
                text = "Please enter the correct value"

            return Response({"text":text,"code":200})

        except:
            return Response({"code":401})