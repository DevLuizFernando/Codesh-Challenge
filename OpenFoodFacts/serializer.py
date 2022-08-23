from rest_framework import serializers
from OpenFoodFacts.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
    def validate_name(self, product_name):
        if not product_name.isalpha():
            raise serializers.ValidationError({'product_name':"Não inclua números neste campo"})
        return product_name