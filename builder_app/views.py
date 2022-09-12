from rest_framework import generics, permissions

from .serializers import TableSerializer
from .models import TableInfo


class TablesInfoView(generics.ListCreateAPIView):
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TableInfo.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
