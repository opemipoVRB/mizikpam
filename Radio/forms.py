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
$$.................. @@@  @@@  @@@   @@@@     @@@   @@@@.....................$$
$$.................. @@!  @@@  @@!   !@@      @@!   !@@......................$$
$$.................. !@!  @!@  !@!   !@!      !@!   !@!......................$$
$$.................. @!@  !@!  !!@!@!!@@!     !!@!@!!@@!.....................$$
$$.................. !@!  !!!  !!!      !!!   !!!     !!!....................$$
$$.................. :!:  !!:  !!:      :!!   !!:     :::....................$$
$$................... ::!!:!   :!:      :!:   :!:     :::....................$$
$$.................... ::::    :::      :::   :::     :::....................$$
$$...................... :      :        :      :::::::  ....................$$
$$...........................................................................$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$***************************************************************************$$
$$      forms.py  Created by  Durodola Opemipo 2018                          $$
$$    Official Email : <durodola.opemipo@venturegardengroup.com>             $$
$$            Personal Email : <opemipodurodola@gmail.com>                   $$
$$                 Telephone Number: +2348182104309                          $$
$$***************************************************************************$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                                           
"""
from django import forms
from django.contrib.auth.models import User

from Radio.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "login__input pass", 'placeholder': "Password"}))

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
            self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('photo',)
