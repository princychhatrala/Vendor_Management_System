from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render
from rest_framework.mixins import *
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg
from rest_framework import generics, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'vendor_code'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'vendor_code'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'on_time_delivery_rate': serializer.data['on_time_delivery_rate'],
                         'quality_rating_avg': serializer.data['quality_rating_avg'],
                         'average_response_time': serializer.data['average_response_time'],
                         'fulfillment_rate': serializer.data['fulfillment_rate']})


class AcknowledgementPurchaseOrderView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer=serializer)
            instance.acknowledgement_date = timezone.now()
            instance.save()

            # Recalculate average_response_time for the vendor associated with the purchase order
            vendor = instance.vendor
            response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgement_date__isnull=False).values_list('acknowledgement_date', 'issue_date')
            average_response_time = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_times) / len(response_times) if response_times else 0
            vendor.average_response_time = average_response_time
            vendor.save()

            return Response({'acknowledgement_date': instance.acknowledgement_date}, status=status.HTTP_200_OK)
        else:
            raise ValidationError(serializer.errors)
