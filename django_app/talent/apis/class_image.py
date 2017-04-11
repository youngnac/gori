from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from member.models import Tutor
from talent.models import Talent, ClassImage
from talent.serializers import ClassImageWrapperSerializers, ClassImageSerializer
from utils import tutor_verify

__all__ = (
    'ClassImageListCreateView',
    'ClassImageRetrieveView',
)


class ClassImageListCreateView(generics.ListCreateAPIView):
    queryset = ClassImage.objects.all()
    serializer_class = ClassImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        talent = Talent.objects.get(pk=request.data['talent_pk'])
        if tutor_verify(request, talent):
            ClassImage.objects.create(
                talent=talent,
                image=request.FILES['image'],
            )

            ret_message = '[{talent}]에 [{image}]가 추가되었습니다.'.format(
                talent=talent.title,
                image=request.FILES['image'],
            )
            ret = {
                'detail': ret_message,
            }
            return Response(ret, status=status.HTTP_201_CREATED)

        ret = {
            'detail': '권한이 없습니다.',
        }
        return Response(ret, status=status.HTTP_401_UNAUTHORIZED)


class ClassImageRetrieveView(generics.RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = ClassImageWrapperSerializers