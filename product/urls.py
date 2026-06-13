from django.urls import path
from .import views

app_name = 'product'
urlpatterns = [
    # |============================================================================|
                                    # urlAPI
    path('detail/<int:pk>', views.ProductApiDeView.as_view()),
    path('all/', views.AllProductViewSet.as_view({'get': 'list'})),
    path('color/', views.ColorViewSet.as_view({'get': 'list'})),
    path('size/', views.SizeViewSet.as_view({'get': 'list'})),

    # |=============================================================================|

    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
]