from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import login_view
from apps.dashboard.views import dashboard_view
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('apps.accounts.urls')),
]

urlpatterns += i18n_patterns(
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('transactions/', include('apps.transactions.urls')),
    path('wallets/', include('apps.wallets.urls')),
    path('categories/', include('apps.categories.urls')),
)
