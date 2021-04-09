from django.db import models

# Create your models here.
from django_client_framework.models import Serializable, AccessControlled
from django_client_framework.serializers import ModelSerializer
from django.db.models import CharField, ForeignKey, CASCADE
from django_client_framework.api import register_api_model
from django_client_framework.permissions import default_groups, set_perms_shortcut

@register_api_model
class Group(Serializable, AccessControlled):
    id_number = CharField(max_length=16)

    @classmethod
    def serializer_class(cls):
        return GroupSerializer

    class PermissionManager(AccessControlled.PermissionManager):
        def add_perms(self, brand):
            set_perms_shortcut(default_groups.anyone, brand, "r")


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        exclude = []

@register_api_model
class Person(Serializable, AccessControlled):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    group = ForeignKey("Group", related_name="belong_group", on_delete=CASCADE, null=True)

    @classmethod
    def serializer_class(cls):
        return PersonSerializer

    class PermissionManager(AccessControlled.PermissionManager):
        def add_perms(self, product):
            set_perms_shortcut(default_groups.anyone, product, "r")

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        exclude = []