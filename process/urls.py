from rest_framework.routers import DefaultRouter
from process.views import *

router = DefaultRouter()
router.register('data', DataViewSet)
router.register('station', StationViewSet)

urlpatterns = router.urls
