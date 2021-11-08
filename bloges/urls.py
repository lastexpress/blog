from django.urls import path
from . import views

app_name = 'bloges'


urlpatterns = [
    path('', views.IndexView, name="index"),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
    # path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    # path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('<slug:category_slug>', views.IndexView, name='cat_img_by_category'),
    # path('<int:id>/', views.cat_img_detail, name='cat_img_detail'),
    # path('blog/bloges/', views.BlogView.as_view(), name='blogeses'),
    # path('blog/singleblog/', views.BlogSingleView.as_view(), name='singleblog'),
]