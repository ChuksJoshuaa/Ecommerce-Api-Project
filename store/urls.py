from django.urls import path
#from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

# we used the basename to generate the name of views whether list view or detail view when queryset is not available or commented out

router = routers.DefaultRouter()
router.register('products', views.ProductViewset, basename='products')
router.register('collections', views.CollectionViewset)
router.register('cart', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')


products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
# the child prefixes of product comprises of reviews
products_router.register('reviews', views.ReviewViewset,
                         basename='product-review')


carts_router = routers.NestedDefaultRouter(
    router, 'cart', lookup='cart')
carts_router.register('items', views.CartItemViewSet,
                      basename='cart-items')

urlpatterns = router.urls + products_router.urls + carts_router.urls
