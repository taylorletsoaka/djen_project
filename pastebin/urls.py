from django.urls import path
from .views import PasteDetail, PasteCreate, PasteDelete, PasteUpdate, PasteList


urlpatterns = [
    path('pastebin/', PasteCreate.as_view(), name='create'),
    path('pastes/', PasteList.as_view(), name='pastebin_paste_list'),
    path('paste/delete/<int:pk>', PasteDelete.as_view(), name='pastebin_paste_delete'),
    path('paste/edit/<int:pk>', PasteUpdate.as_view(), name='pastebin_paste_edit'),
    path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
]

