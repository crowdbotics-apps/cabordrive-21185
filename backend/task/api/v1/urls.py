from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskViewSet, MessageViewSet, TaskTransactionViewSet, RatingViewSet

router = DefaultRouter()
router.register("tasktransaction", TaskTransactionViewSet)
router.register("rating", RatingViewSet)
router.register("message", MessageViewSet)
router.register("task", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
