from django.urls import path
from . import views

urlpatterns = [
    path('Invoice_Company', views.Invoice_Company, name='Invoice_Company'),
    path('Invoice_keywords', views.Invoice_keywords, name='Invoice_keywords'),
    path('Invoice_full_text', views.Invoice_full_text, name='Invoice_full_text'),
    path('Invoice_uploaded_by', views.Invoice_uploaded_by, name='Invoice_uploaded_by'),
    path('Email_From', views.Email_From, name='Email_From'),
    path('Email_To', views.Email_To, name='Email_To'),
    path('Email_keywords', views.Email_keywords, name='Email_keywords'),
    path('Email_Body', views.Email_Body, name='Email_Body'),
    path('Email_Subject', views.Email_Subject, name='Email_Subject'),
    path('Email_Attachments', views.Email_Attachments, name='Email_Attachments'),
    path('Email_uploaded_by', views.Email_uploaded_by, name='Email_uploaded_by'),
    path('Others_keywords', views.Others_keywords, name='Others_keywords'),
    path('Others_full_text', views.Others_full_text, name='Others_full_text'),
    path('Others_uploaded_by', views.Others_uploaded_by, name='Others_uploaded_by'),
    path('All_file_name', views.All_file_name, name="All_file_name"),
    path('All_full_text', views.All_full_text, name="All_full_text"),
    path('All_keywords', views.All_keywords, name="All_keywords"),
    path('All_uploaded_by', views.All_uploaded_by, name="All_uploaded_by"),
    path('search', views.search, name= 'search'),
]