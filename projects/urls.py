from rest_framework import routers
from .api import EmprendimientoViewSet,CategoriaViewSet,EmprendedorViewSet,ScoreViewSet,Video_imagenViewSet,ProductoViewSet,Reserva2ViewSet,CompraViewSet

router = routers.DefaultRouter()


router.register('api/emprendimiento', EmprendimientoViewSet, 'emprendimiento')
router.register('api/emprendedor', EmprendedorViewSet, 'emprendedor')
router.register('api/score', ScoreViewSet, 'score')
router.register('api/video_imagen', Video_imagenViewSet, 'video_imagen')
router.register('api/producto', ProductoViewSet, 'producto')
router.register('api/reserva', Reserva2ViewSet, 'reserva')
router.register('api/compra', CompraViewSet, 'compra')
router.register('api/categoria', CategoriaViewSet, 'categoria')

urlpatterns = router.urls


