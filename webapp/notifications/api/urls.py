from rest_framework import routers
from django.urls import include, path

from .views import ClientViewSet, MailingViewSet, MessageViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'new-mailing', MailingViewSet)
router.register(r'new-message', MessageViewSet)
# router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
#                 basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]