from django.urls import path
from .views import *
urlpatterns = [
    path('', problems_list_view, name='home'),
    path('detailproblem/<int:pk>', problems_detail_view, name='detailproblem'),
    path('createproblem/', problems_create_view, name='createproblem'),
    path('deleteproblem/<int:pk>', problems_delete_view, name='deleteproblem'),
    path('updateproblem/<int:pk>', problems_update_view, name='updateproblem'),
    path('allaplication', application_list_view, name='allapl'),
    path('detailapplication/<int:pk>', application_detail_view, name='detailapplication'),
    path('createapplication/<int:pk>', application_create_view, name='createapplication'),
    path('deleteapplication/<int:pk>', application_delete_view, name='deleteapplication'),
    path('updateapplication/<int:pk>', application_update_view, name='updateapplication'),
    path('allskil', skills_list_view, name='allskil'),
    path('detailskills/<int:pk>', skills_detail_view, name='detailskills'),
    path('createskills/', skills_create_view, name='createskills'),
    path('deleteskills/<int:pk>', skills_delete_view, name='deleteskills'),
    path('updateskills/<int:pk>', skills_update_view, name='updateskills'),
    path('detailcategory/<int:pk>', category_detail_view, name='detailcategory'),
    path('allcategory', category_list_view, name='allcategory'),
    path('alluser', user_list_view, name='alluser'),
    path('detailuser/<int:pk>', user_detail_view, name='detailuser'),
    path('createuser/', user_create_view, name='createuser'),
    path('deleteuser/<int:pk>', user_delete_view, name='deleteuser'),
    path('updateuser/<int:pk>', user_update_view, name='updateuser'),
]
