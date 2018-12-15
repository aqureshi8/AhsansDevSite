# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.utils.timezone import now
from django.core.mail import send_mail

from django.views.static import serve

import forms
from models import Occupation, Project, CoverLetterParagraph, Media


class ChallengeView(TemplateView):
    template_name = 'mainSite/challenge.html'


class AboutMeView(TemplateView):
    template_name = 'mainSite/aboutMe.html'

    def get_context_data(self, **kwargs):
        """Sets page context"""
        context = super(AboutMeView, self).get_context_data()
        context['pageName'] = 'About Me'
        return context


class ContactMeView(FormView):
    template_name = 'mainSite/contact.html'
    form_class = forms.ContactForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'pageName': 'Contact Me'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['name'] + ' - ' + form.cleaned_data['email'] + ' - The Resume',
                      form.cleaned_data['message'],
                      'noreply@thisisahsan.com',
                      ['ahsan.qureshi8@gmail.com'])
            return render(request, 'mainSite/thankYou.html', {'pageName': 'Contact Me',
                                                              'name': form.cleaned_data['name'],
                                                              'email': form.cleaned_data['email'],
                                                              'message': form.cleaned_data['message'],
                                                              })
        return render(request, self.template_name, {'form': form, 'pageName': 'Contact Me'})

    def get_context_data(self, **kwargs):
        """Sets page context"""
        context = super(ContactMeView, self).get_context_data()
        context['pageName'] = 'Contact Me'
        return context


class CoverLetterView(FormView):
    template_name = 'mainSite/createCoverLetter.html'
    form_class = forms.CoverLetterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'pageName': 'Cover Letter'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            header = CoverLetterParagraph.objects.filter(paragraph_position='Header')[0]
            introduction = CoverLetterParagraph.objects.filter(paragraph_position='Introduction')[0]
            paragraph1 = CoverLetterParagraph.objects.filter(name=form.cleaned_data['paragraph1'])[0]
            paragraph2 = CoverLetterParagraph.objects.filter(name=form.cleaned_data['paragraph2'])[0]
            paragraph3 = CoverLetterParagraph.objects.filter(name=form.cleaned_data['paragraph3'])[0]
            conclusion = CoverLetterParagraph.objects.filter(paragraph_position='Conclusion')[0]
            footer = CoverLetterParagraph.objects.filter(paragraph_position='Footer')[0]

            header.paragraph = header.paragraph.replace('[TODAY]', now().strftime('%B %d, %Y'))
            print header.paragraph.replace('[TODAY]', now().strftime('%B %d, %Y'))
            header.paragraph = header.paragraph.replace('[COMPANY_NAME]', form.cleaned_data['company_name'])
            header.paragraph = header.paragraph.replace('[COMPANY_STREET]', form.cleaned_data['company_address_street'])
            header.paragraph = header.paragraph.replace('[COMPANY_CITY]', form.cleaned_data['company_address_city'])
            header.paragraph = header.paragraph.replace('[COMPANY_STATE]', form.cleaned_data['company_address_state'])
            header.paragraph = header.paragraph.replace('[COMPANY_ZIP]', form.cleaned_data['company_address_zip'])
            introduction.paragraph = introduction.paragraph.replace('[COMPANY_NAME]', form.cleaned_data['company_name'])
            introduction.paragraph = introduction.paragraph.replace('[JOB_TITLE]', form.cleaned_data['job_title'])
            conclusion.paragraph = conclusion.paragraph.replace('[JOB_TITLE]', form.cleaned_data['job_title'])
            return render(request, 'mainSite/coverLetter.html', {'header': header,
                                                                 'introduction': introduction,
                                                                 'paragraph1': paragraph1,
                                                                 'paragraph2': paragraph2,
                                                                 'paragraph3': paragraph3,
                                                                 'conclusion': conclusion,
                                                                 'footer': footer,
                                                                 'pageName': 'Cover Letter'})
        return render(request, self.template_name, {'form': form, 'pageName': 'Cover Letter'})


class EducationView(ListView):
    model = Occupation
    template_name = 'mainSite/education.html'
    context_object_name = 'educationList'

    def get_context_data(self, **kwargs):
        """Sets page context"""
        context = super(EducationView, self).get_context_data()
        context['pageName'] = 'Education'
        return context

    def get_queryset(self):
        """Returns all occupations with type 'Education'"""
        return Occupation.objects.filter(type='Education')


class EmploymentView(ListView):
    model = Occupation
    template_name = 'mainSite/employment.html'
    context_object_name = 'employmentList'

    def get_context_data(self, **kwargs):
        """Sets page context"""
        context = super(EmploymentView, self).get_context_data()
        context['pageName'] = 'Employment'
        return context

    def get_queryset(self):
        """Returns all occupations with type 'Employment"""
        return Occupation.objects.filter(type="Employment")


class IndexView(TemplateView):
    template_name = 'mainSite/index.html'


class ProjectsView(ListView):
    model = Project
    template_name = 'mainSite/projects.html'
    context_object_name = 'projectList'

    def get_context_data(self, **kwargs):
        """Sets page context"""
        context = super(ProjectsView, self).get_context_data()
        context['pageName'] = 'Projects'
        return context

    def get_queryset(self):
        """Returns all Projects"""
        return Project.objects.all()


class ResumeView(TemplateView):
    template_name = 'mainSite/resume.html'

    def get_context_data(self, **kwargs):
        """Sets page context"""
        context = super(ResumeView, self).get_context_data()
        context['pageName'] = 'Resume'

        latest_resume = Media.objects.order_by('-upload_date')[0]
        url_file_name = latest_resume.file.url.split('/')[-1]
        context['latest_resume'] = '/static/' + url_file_name
        return context


class SocialMediaView(TemplateView):
    template_name = 'mainSite/socialMedia.html'

