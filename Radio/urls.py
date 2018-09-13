#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$...........................................................................$$
$$..........................$$$$$$$$$$$$$....................................$$
$$.......................$$$$$$$$$$$$$$$$$$$.................................$$
$$.....................$$$$$$$$$$$$$$$$$$$$$$$...............................$$
$$....................$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$.$$...............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$...$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$.$$...$$$.............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$....................$$$$$$$$$$$$$.....$$$$$$$$$............................$$
$$......................$$$$$$$$$$$$$$$$..$$$$$$$............................$$
$$...................................$$$.....................................$$
$$.................$$................$$$$ $$$$$$$........$...................$$
$$...............$$$$$$..............$$$$$$$$$$$$$...$$$$$$..................$$
$$............$$$$..$$$$$.........................$$$$$$$$$..................$$
$$............$$$$...$$$$$$$....................$$$$$$.$$.$$.................$$
$$...............$$$$$$$$$$$$$$............$$$$$$$$..........................$$
$$.........................$$$$$$$$$...$$$$$$$...............................$$
$$..............................$$$$$$$$$$...................................$$
$$..........................$$$$$....$$$$$$$$$...............................$$
$$............$$.$$$$$$$$$$$$$............$$$$$$$$$$$$$$$$$..................$$
$$............$$.$$..$$$$.....................$$$$$$$$$$$$$$.................$$
$$..............$$$$$$............................$$.$$$$$$$.................$$
$$..................                                   ......................$$
$$.................. @@@  @@@  @@@@@@@        @@@@@@@ .......................$$
$$.................. @@@  @@@  @@@   ounts/login/@@@@     @@@   @@@@.....................$$
$$.................. @@!  @@@  @@!   ounts/login/!@@      @@!   !@@......................$$
$$.................. !@!  @!@  !@!   ounts/login/!@!      !@!   !@!......................$$
$$.................. @!@  !@!  !!@!@!ounts/login/!@@!     !!@!@!!@@!.....................$$
$$.................. !@!  !!!  !!!      !!!   !!!     !!!....................$$
$$.................. :!:  !!:  !!:      :!!   !!:     :::....................$$
$$................... ::!!:!   :!:      :!:   :!:     :::....................$$
$$.................... ::::    :::      :::   :::     :::....................$$
$$...................... :      :        :      :::::::  ....................$$
$$...........................................................................$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$***************************************************************************$$
$$      urls.py  Created by  Durodola Opemipo 2018                           $$
$$    Official Email : <durodola.opemipo@venturegardengroup.com>             $$
$$            Personal Email : <opemipodurodola@gmail.com>                   $$
$$                 Telephone Number: +2348182104309                          $$
$$***************************************************************************$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from Mizikpam import settings
from Radio import admin
from . import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('browse/<int:browse_id>/', views.browse, name='browse'),
    path('playlist/<int:playlist_id>/', views.playlist, name='playlist'),
    path('song/<int:song_id>/', views.song, name='song'),
    path('artist-profile/<int:artist_id>/', views.artist_profile, name='artist_profile'),
    path('admin-studio/', views.mizikpam_studio, name='mizikpam_studio'),
    path('most_played/', views.most_and_recently_played, name='most_and_recently_played'),
    path('update_stats/', views.update_index_page, name='update_index_page'),
    path('mood/<int:mood_id>/', views.mood, name='mood'),
    path('profile/<username>/', views.profile, name='profile'),
    # path('account/signup/', views.SignupView.as_view(), name="account_signup"),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^uploads/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
