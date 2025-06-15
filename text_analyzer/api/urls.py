from django.urls import path
from .views import (
    status_view, version_view, metrics_view,
    RegisterView, LoginView, LogoutView,
    ChangePasswordView, DeleteUserView, DocumentDetailView,
    DocumentStatisticsView, DocumentDeleteView, DocumentListCreateView, CollectionListView, CollectionDetailView, CollectionStatisticsView,
    CollectionAddDocumentView, CollectionRemoveDocumentView, CollectionCreateView, DocumentHuffmanView
)

urlpatterns = [
    path("status", status_view),
    path("version", version_view),
    path("metrics", metrics_view),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('users/<uuid:user_id>/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('users/<uuid:user_id>/delete/', DeleteUserView.as_view(), name='delete-user'),
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<uuid:document_id>/', DocumentDetailView.as_view(), name='document-detail'),
    path('documents/<uuid:document_id>/statistics/', DocumentStatisticsView.as_view(), name='document-statistics'),
    path('documents/<uuid:document_id>/delete/', DocumentDeleteView.as_view(), name='document-delete'),
    path('collections/', CollectionListView.as_view(), name='collection-list'),
    path('collections/<uuid:collection_id>/', CollectionDetailView.as_view(), name='collection-detail'),
    path('collections/<uuid:collection_id>/statistics/', CollectionStatisticsView.as_view(),
         name='collection-statistics'),
    path('collection/<uuid:collection_id>/<uuid:document_id>/', CollectionAddDocumentView.as_view(),
         name='collection-add'),
    path('collection/<uuid:collection_id>/<uuid:document_id>/delete/', CollectionRemoveDocumentView.as_view(),
         name='collection-remove'),
    path('collections/create/', CollectionCreateView.as_view(), name='collection-create'),
    path('documents/<uuid:document_id>/huffman/', DocumentHuffmanView.as_view(), name='document-huffman'),
]
