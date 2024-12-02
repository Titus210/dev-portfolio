from django.urls import path
from core.views.contact_views import get_all_contacts, submit_contact_message
from core.views.frontend_views import home, about, projects, contact, blog
from core.views.project_views import project_list, project_detail
from core.views.blog_views import blog_list, blog_detail
from core.views.skill_views import skill_list
# from core.views import populate_dummy_data
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),

    # requests URLS
    path('projects/', project_list, name='project_list'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('skills/', skill_list, name='skill_list'),
    path('submit-message/', submit_contact_message, name='submit_contact_message'),
    path('contacts/', get_all_contacts, name='get_all_contacts')
    # path('populate/', populate_dummy_data, name='populate_dummy_data'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # project serves media files during development