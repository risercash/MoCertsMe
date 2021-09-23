from allauth.account.views import login, logout
from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('<int:pk>', PostDetail.as_view(), name='postdetail'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('manual/', ManualView.as_view(), name='manual'),
    path('blog/', blog, name='blog'),
    path('userbalance/', UserBalance.as_view(), name='userbalance'),
    path('errorview/', ErrorView.as_view(), name='errorview'),

    path('certificates/', SelectCertificate.as_view(), name='select_certificate'),
    path('my_certificates', MyCertificates.as_view(), name='my_certificates'),
    path('certificate/<int:number>/', CertificateDetail.as_view(), name='certificate'),
    path('accept/<int:pk>', accept, name='accept'),
    path('create_certificate/<int:nominal>/', create_certificate, name='create_certificate'),
    path('pay_certificate/<int:pk>', pay_certificate, name='pay_certificate'),
    path('cashriser/', cashriser, name='cashriser'),
    path('generate', generate, name='generate'),
    path('generate/<int:pk>', generate, name='generate'),# Эту я делал под кнопку GENERATE на странице cashriser
  
    # path('cashriser/', Cashriser.as_view(), name='cashriser'),cashriser

]
