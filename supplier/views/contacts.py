from rest_framework.viewsets import ModelViewSet

from supplier.models import Contacts
from supplier.permissions import IsActivePermission
from supplier.serializers.contacts_serializers import ContactsSerializer


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (IsActivePermission,)
