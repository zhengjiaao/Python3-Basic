# views.py

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

class MyAPIView(APIView):
    @api_view(['GET'])
    # @extend_schema(  # todo 无效
    #     tags=['Module 1'],
    #     summary='my_api_view1',
    #     description='This is the API description',
    #     responses={200: 'Success response'},
    # )
    def my_api_view1(request):
        """swagger3视图集中的注释"""
        # Your code here
        return Response("Success")

    @api_view(['GET'])
    @extend_schema(  # todo 无效
        description='This is another API description',
        tags=['Module 2'],
        responses={200: 'Success response'},
    )
    def my_api_view2(request):
        # Your code here
        return Response('Success')
