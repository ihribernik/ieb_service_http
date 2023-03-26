from market.views import ProductViewSet

product_list = ProductViewSet.as_view({
    'get': 'list'
})

product_detail = ProductViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root)
]
