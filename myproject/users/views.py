# from rest_framework import generics, permissions
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

# from .models import Developer, YourAPI
# from .serializers import DeveloperSerializer, YourAPISerializer

# class DeveloperRegisterView(generics.CreateAPIView):
#     queryset = Developer.objects.all()
#     serializer_class = DeveloperSerializer

# class YourAPIListView(generics.ListAPIView):
#     queryset = YourAPI.objects.all()
#     serializer_class = YourAPISerializer
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]


from django.shortcuts import render
from django.conf import settings

import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')



def my_view(request):
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
