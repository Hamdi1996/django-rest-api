from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete )',
            'Is Similar to tradtiondal Djngo View',
            'Gives you the most',
            'IS',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

