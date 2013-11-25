from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from .views import redirect_to_name

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'www_personalgenomes_org.views.home', name='home'),
    # url(r'^www_personalgenomes_org/', include('www_personalgenomes_org.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='www_personalgenomes_org/index.html')),

    # About pages

    url(r'^mission/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/mission.html'),
        name='mission'),
    url(r'^mission.html/?$', redirect_to_name, {'url_name': 'mission'}),
    url(r'^about.html/?$', redirect_to_name, {'url_name': 'mission'}),

    url(r'^people/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/people.html'),
        name='people'),
    url(r'^people.html/?$', redirect_to_name, {'url_name': 'people'}),

    url(r'^press/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/press.html'),
        name='press'),
    url(r'^news.html/?$', redirect_to_name, {'url_name': 'press'}),

    url(r'^publications/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/publications.html'),
        name='publications'),
    url(r'^research.html/?$', redirect_to_name, {'url_name': 'publications'}),

    # Participate pages

    url(r'^pgp/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp.html'),
        name='pgp'),
    url(r'^project.html/?$', redirect_to_name, {'url_name': 'pgp'}),

    url(r'^why-participate/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/why-participate.html'),
        name='why-participate'),
    url(r'^whyparticipate.html/?$', redirect_to_name, {'url_name': 'why-participate'}),

    url(r'^non-anonymous/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/non-anonymous.html'),
        name='non-anonymous'),

    url(r'^risks-benefits/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/risks-benefits.html'),
        name='risks-benefits'),
    url(r'^considerations.html/?$', redirect_to_name, {'url_name': 'risks-benefits'}),

    url(r'^pgp-sign-up/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/pgp-sign-up.html'),
        name='pgp-sign-up'),
    url(r'^signup.html/?$', redirect_to_name, {'url_name':'pgp-sign-up'}),
    url(r'^eligibility.html/?$', redirect_to_name, {'url_name':'pgp-sign-up'}),

    # Research pages

    url(r'^get-data/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/get-data.html'),
        name='get-data'),

    url(r'^sharing/?',
        TemplateView.as_view(template_name='www_personalgenomes_org/sharing.html'),
        name='sharing'),
    url(r'^sharing.html/?$', redirect_to_name, {'url_name':'sharing'}),

    # Global network pages

    url(r'^network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/network.html'),
        name='network'),
    url(r'^international.html/?$', redirect_to_name, {'url_name':'network'}),

    url(r'^join-network/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/join-network.html'),
        name='join-network'),

    url(r'^harvard',
        include('harvard.urls', namespace="harvard")),
    url(r'^canada',
        include('canada.urls', namespace="canada")),

    # Support page

    url(r'^donate/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/donate.html'),
        name='donate'),
    url(r'donate.html/?$', redirect_to_name, {'url_name':'donate'}),
    url(r'donate/?$', redirect_to_name, {'url_name':'donate'}),
    url(r'donate/index.html/?$', redirect_to_name, {'url_name':'donate'}),
    url(r'donate/other.html/?$', redirect_to_name, {'url_name':'donate'}),
    url(r'donate/matching.html/?$', redirect_to_name, {'url_name':'donate'}),

    # Footer pages

    url(r'^contact-us/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/contact-us.html'),
        name='contact-us'),
    url(r'contact.html', redirect_to_name, {'url_name':'contact-us'}),
    url(r'^tos/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/tos.html'),
        name='tos'),
    url(r'tos.html', redirect_to_name, {'url_name':'tos'}),
    url(r'^website-privacy-policy/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/website-privacy-policy.html'),
        name='website-privacy-policy'),
    url(r'privacypolicy.html/?$', redirect_to_name, {'url_name':'website-privacy-policy'}),

    # Unlinked by existing pages
    url(r'getlabs2014/?$',
        TemplateView.as_view(template_name='www_personalgenomes_org/getlabs2014.html'),
        name='getlabs2014'),

    # Additional redirects

    url(r'^consent/?$', redirect_to_name, {'url_name':'harvard:documents'}),
    url(r'^consent/index.html/?$', redirect_to_name, {'url_name':'harvard:documents'}),
    url(r'^medicalcenters.html/?$', redirect_to_name, {'url_name':'harvard:collection-centers'}),
    url(r'consent/PGP_Consent_Approved_02212013.pdf',
        RedirectView.as_view(url='/static/docs/harvard/PGP_Consent_Approved_02212013.pdf')),
    url(r'exam/v20120430-study-guide.pdf',
        RedirectView.as_view(url='/static/docs/harvard/v20120430-study-guide.pdf')),

)
