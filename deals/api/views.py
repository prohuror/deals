import csv
import io

from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import FileUploadSerializer
from ..tasks import import_deals


class DealUploader(generics.CreateAPIView):
    """Веб-приложение для загрузки и приведению к словарю csv-файла"""
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        dict_reader = csv.DictReader(io_string)
        deals = list(dict_reader)
        import_deals.delay(deals)
        return Response({'result': True, 'message': 'Загрузка началась'}, status=status.HTTP_204_NO_CONTENT)
