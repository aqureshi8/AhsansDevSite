# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    tech_used = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    picture_path = models.CharField(max_length=200)
    git_url = models.CharField(max_length=300)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    picture_path = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.occupation.name + ", " + self.title


class Accomplishment(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.position.occupation.name + ", " + self.position.title + " - " + self.name


class CoverLetterParagraph(models.Model):

    BASE = "Base"
    PROJECT = "Project"
    OCCUPATION = "Occupation"
    COURSE = "Course"

    TYPE_CHOICES = (
        (BASE, "Base"),
        (PROJECT, "Project"),
        (OCCUPATION, "Occupation"),
        (COURSE, "Course"),
    )

    HEADER = "Header"
    INTRODUCTION = "Introduction"
    FIRST_PARAGRAPH = "Paragraph 1"
    SECOND_PARAGRAPH = "Paragraph 2"
    THIRD_PARAGRAPH = "Paragraph 3"
    CONCLUSION = "Conclusion"
    FOOTER = "Footer"

    POSITION_CHOICES = (
        (HEADER, "Header"),
        (INTRODUCTION, "Introduction"),
        (FIRST_PARAGRAPH, "Paragraph 1"),
        (SECOND_PARAGRAPH, "Paragraph 2"),
        (THIRD_PARAGRAPH, "Paragraph 3"),
        (CONCLUSION, "Conclusion"),
        (FOOTER, "Footer"),
    )

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    paragraph_position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    paragraph = models.TextField(max_length=950)

    def __str__(self):
        return self.name + " " + self.type


class Media(models.Model):
    RESUME = "resume"
    IMAGE = "image"
    OTHER = "other"

    MEDIA_CHOICES = (
        (RESUME, "Resume"),
        (IMAGE, "Image"),
        (OTHER, "Other"),
    )

    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100, choices=MEDIA_CHOICES)
    file = models.FileField()
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_name + " (" + self.file_type + ")"
