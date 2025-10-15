from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.authtoken.models import Token
from.models import User
from.serializers import UserRegistrationSerailizer , UserLoginSerailizer

@api_view(['Post'])
@permission_classes([AllowAny])
def login_user(request):
    if request.method == 'post'
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            token,created = token.objects.get_or_create(user=user)
            return Response({
                'message':'Login seccessful',
                'user':{
                    'id':user.id,
                    'username':user.username,
                    'email':user.email
                    },
                    'token':token.key
           },status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
