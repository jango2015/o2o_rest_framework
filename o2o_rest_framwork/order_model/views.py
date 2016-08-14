from datetime import datetime

from rest_framework.generics import CreateAPIView,GenericAPIView,RetrieveAPIView,UpdateAPIView



from .models import Application
from .serializers import ApplicationCreateSerializer,ApplicationDetailSerializer
from o2o_rest_framwork.department_model.models import RecruitmentInformation


class CreateApplicationAPIView(CreateAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer


    def perform_create(self, serializer):

        post = RecruitmentInformation.objects.get(id=int(self.kwargs['id']))

        serializer.save(date=datetime.today().date(),applier=self.request.user,recruitment=post)


class ApplicationDetailAPIView(RetrieveAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicationDetailSerializer
