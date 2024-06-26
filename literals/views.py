
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from literals.serializers import LiteralsSerializer


class LisLiteralsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = LiteralsSerializer(context={"request": request}, data={})
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
