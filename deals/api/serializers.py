from rest_framework import serializers


class FileUploadSerializer(serializers.Serializer):
    """Serializer для формы загрузки файла csv."""
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


class DealListSerializer(serializers.Serializer):
    """Serializer для отображения списка сделок."""
    customer = serializers.CharField(max_length=100)
    item = serializers.CharField(max_length=100)
    total = serializers.IntegerField()
    quantity = serializers.IntegerField()

