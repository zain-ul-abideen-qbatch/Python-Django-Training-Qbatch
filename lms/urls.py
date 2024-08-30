from django.contrib import admin
from django.urls import include, path



from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets
from students.models import DummyTable

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DummyTable
        fields = '__all__'

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = DummyTable.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employee', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



urlpatterns = [
    path("admin/", admin.site.urls), path("", include("students.urls")),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]