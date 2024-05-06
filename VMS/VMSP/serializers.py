from rest_framework import serializers
from .models import Vendor, PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def validate(self, data):
        if data.get('delivery_date') and data.get('order_date') and data['delivery_date'] <= data['order_date']:
            raise serializers.ValidationError({'delivery_date': "Delivery date must be after order date."})
        return data
