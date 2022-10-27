from copy import error
import email
from email import message
import json
import base64
import uuid
from django.core.files.base import ContentFile
from turtle import title
from unicodedata import name
from xml.dom.pulldom import ErrorHandler
from xml.parsers.expat import errors
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from QRLabs.models import *
from django.http import Http404
import os
from django.http import HttpResponse
from . import settings
import requests
import pandas as pd
from svglib.svglib import svg2rlg
import uuid
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from django.http.response import HttpResponseRedirectBase

def index(request):
    qrs=Qrcodes.objects.all()
    i=[]
    for obj in qrs :
        i.append(obj)
    return render(request, 'index.html',{'scans':len(i)})


def logouts(request):
    logout(request)
    return redirect('index')

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404

def loginPage(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        return redirect('dashboard')


def logins(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid Email or Password')
    return redirect('loginPage')


def signupPage(request):
    if not request.user.is_authenticated:
        return render(request, 'signup.html')
    else:
        return redirect('dashboard')


def signup(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            user = User.objects.create_user(
                                            email=request.POST['email'],
                                            password=request.POST['password'],
                                            username=request.POST['name'],
                                            last_name=request.POST['name'],
                                            )
            if user:
                user.save()
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Email already in use')
        else:
            return redirect('dashboard')
    return redirect('signupPage')


def dashboard(request):
    if request.user.is_authenticated:
        qrs = Qrcodes.objects.filter(user_id=request.user, isDynamic=True, archived=False)
        qrcs=[]
        for obj in qrs :
            qrcs.append(obj)

        qrcs.reverse()
        folder=Folder.objects.filter(user_id=request.user)
        context={
            'qrs': qrcs,
            'folder':folder,
        }
        return render(request, 'dashboard.html',context )
    else:
        return redirect('loginPage')


def dashboardstatic(request):
    if request.user.is_authenticated:
        qrs = Qrcodes.objects.filter(user_id=request.user, isDynamic=False, archived=False)
        folder=Folder.objects.filter(user_id=request.user)
        context={
            'qrs': qrs,
            'folder':folder,
        }
        return render(request, 'dashboardStatic.html', context)
    else:
        return redirect('loginPage')


def dashboardarchived(request):
    if request.user.is_authenticated:
        qrs = Qrcodes.objects.filter(user_id=request.user, archived=True)
        folder=Folder.objects.filter(user_id=request.user)
        context={
            'qrs': qrs,
            'folder':folder,
        }
        return render(request, 'dashboardArchived.html',context)
    else:
        return redirect('loginPage')


def dashboardfolders(request):
    if request.user.is_authenticated:
        flds = Folder.objects.filter(user_id=request.user)
        return render(request, 'dashboardFolders.html', {'folder': flds})
    else:
        return redirect('loginPage')


def dashboardCreate(request):
    if request.user.is_authenticated:

        return render(request, 'dashboardCreate.html')
    else:
        return redirect('loginPage')



@csrf_exempt
def dashboardCreateSave(request):
    if request.user.is_authenticated:
        extra = {'user_id': request.user}
        # import requests
        API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"

        if request.POST.get('status'):
            extra['isDynamic'] = False
            if request.POST['type']=='link':
                data = {
                    "link_data": request.POST['link_data'],
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='text':
                data = {
                    "text_data":request.POST['text_data'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='email':
                data = {
                    "email":request.POST['email'],
                    "subject":request.POST['subject'],
                    "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='call':
                data = {
                    "country_code":request.POST['country_code'],
                    "phone_number":request.POST['phone_number'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='sms':
                data = {
                    "sms_country_code":request.POST['sms_country_code'],
                    "sms_phone_number":request.POST['sms_phone_number'],
                    "sms_message":request.POST['sms_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
            
            if request.POST['type']=='vcard':
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.vcard_fname = request.POST['vcard_fname']
                qr.vcard_lname = request.POST['vcard_lname']
                qr.vcard_phone_number = request.POST['vcard_phone_number']
                qr.vcard_email = request.POST['vcard_email']
                qr.vcard_web_url = request.POST['vcard_web_url']
                qr.vcard_mobile = request.POST['vcard_mobile']
                qr.vcard_company = request.POST['vcard_company']
                qr.vcard_job_title = request.POST['vcard_job_title']
                qr.vcard_fax = request.POST['vcard_fax']
                qr.vcard_address = request.POST['vcard_address']
                qr.vcard_city = request.POST['vcard_city']
                qr.vcard_country = request.POST['vcard_country']
                qr.vcard_post_code = request.POST['vcard_post_code']
                qr.save()
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='whatsapp':
                data = {
                    "whatsapp_country_code":request.POST['whatsapp_country_code'],
                    "whatsapp_phone_number":request.POST['whatsapp_phone_number'],
                    "whatsapp_message":request.POST['whatsapp_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='wifi':
                data = {
                    "network_name":request.POST['network_name'],
                    "network_type":request.POST['network_type'],
                    "network_password":request.POST['network_password'],
                    "wifi_hidden":request.POST['wifi_hidden'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='pdf':
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                qr.pdf = request.FILES['pdf']
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.save()
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='images':
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.save()
                images = request.FILES.getlist('images[]')
                for img in images:
                    Images.objects.create(qrcode=qr, image=img)

                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='video':
                data = {
                    "video":request.POST['video'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                    
                }

            if request.POST['type']=='pdf' or request.POST['type']=='images' or request.POST['type']=='vcard':
                r = requests.post(url=API_ENDPOINT, data=data)
                tex = r.json()['content']
                svgFile=open("mediaaa/svgs/"+str(uid)+'.svg',"w")
                svgFile.write(tex)
                svgFile.close()
                drawing = svg2rlg("mediaaa/svgs/"+str(uid)+'.svg')
                renderPDF.drawToFile(drawing, "mediaaa/pdfs/"+str(uid)+".pdf")
                renderPM.drawToFile(drawing, "mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
                renderPM.drawToFile(drawing, "static/mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
        
            else:
                r = requests.post(url=API_ENDPOINT, data=data)
                tex = r.json()['content']
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                svgFile=open("mediaaa/svgs/"+str(uid)+'.svg',"w")
                svgFile.write(tex)
                svgFile.close()
                drawing = svg2rlg("mediaaa/svgs/"+str(uid)+'.svg')
                renderPDF.drawToFile(drawing, "mediaaa/pdfs/"+str(uid)+".pdf")
                renderPM.drawToFile(drawing, "mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
                renderPM.drawToFile(drawing, "static/mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
                qr.uuid=uid
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.save()


        else:
            if request.POST['type'] != 'pdf' and request.POST['type'] != 'images':
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.save()
            
            if request.POST['type']=='link':
                data = {

                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "link_data": request.POST['link_data'],
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='text':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "text_data":request.POST['text_data'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='email':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "email":request.POST['email'],
                    # "subject":request.POST['subject'],
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='call':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "country_code":request.POST['country_code'],
                    # "phone_number":request.POST['phone_number'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='sms':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "sms_country_code":request.POST['sms_country_code'],
                    # "sms_phone_number":request.POST['sms_phone_number'],
                    # "sms_message":request.POST['sms_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }
            
            if request.POST['type']=='vcard':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": "link"
                }

            if request.POST['type']=='whatsapp':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "whatsapp_country_code":request.POST['whatsapp_country_code'],
                    # "whatsapp_phone_number":request.POST['whatsapp_phone_number'],
                    # "whatsapp_message":request.POST['whatsapp_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='wifi':
                data = {
                    # "network_name":request.POST['network_name'],
                    # "network_type":request.POST['network_type'],
                    # "network_password":request.POST['network_password'],
                    # "wifi_hidden":request.POST['wifi_hidden'],

                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='pdf':
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                qr.pdf = request.FILES['pdf']
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.save()
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='images':
                uid=str(uuid.uuid4())[:5]
                qr = Qrcodes(**request.POST.dict(), **extra)
                qr.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                qr.save()
                images = request.FILES.getlist('images[]')
                for img in images:
                    Images.objects.create(qrcode=qr, image=img)
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            if request.POST['type']=='video':
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(qr.id),
                    # "video":request.POST['video'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                    
                }

        
            r = requests.post(url=API_ENDPOINT, data=data)
            tex = r.json()['content']
            svgFile=open("mediaaa/svgs/"+str(uid)+'.svg',"w")
            svgFile.write(tex)
            svgFile.close()
            drawing = svg2rlg("mediaaa/svgs/"+str(uid)+'.svg')
            renderPDF.drawToFile(drawing, "mediaaa/pdfs/"+str(uid)+".pdf")
            renderPM.drawToFile(drawing, "mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
            renderPM.drawToFile(drawing, "static/mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
        
        
        return JsonResponse({
                'success': 'Successfully created a Qrcode.',
            })
    else:
        return redirect('loginPage')


def dashboardlock(request):
    if request.user.is_authenticated:
        qrs = Qrcodes.objects.filter(user_id=request.user)
        for qr in qrs:
            qr.status = 'false'
            qr.save()
    return redirect('dashboard')


def dashboardunlock(request):
    if request.user.is_authenticated:
        qrs = Qrcodes.objects.filter(user_id=request.user)
        for qr in qrs:
            qr.status = 'true'
            qr.save()
    return redirect('dashboard')


def dashboarddownload(request,objId):
    obj = Qrcodes.objects.get(pk=objId)
    file_path='static/mediaaa/pngs/'+str(obj.uuid)+'.png'
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type='application/Qrcodes')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    return redirect('dashboard')


def archiveObj(request,objId):
    obj = Qrcodes.objects.get(pk=objId)
    obj.archived=True
    obj.save()
    if obj.isDynamic:
        return redirect('dashboard')
    else:
        return redirect('/dashboard/statics')


def unarchiveObj(request,objId):
    obj = Qrcodes.objects.get(pk=objId)
    obj.archived=False
    obj.save()
    return redirect('/dashboard/archived')

def mkstatic(request,objId):
    API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
    obj = Qrcodes.objects.get(pk=objId)
    obj.isDynamic=False
    uid=str(uuid.uuid4())[:5]
    obj.uuid=str(uid)
    obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
    obj.save()
    if obj.type=='link':
        data = {
            "link_data": obj.link_data,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }
    
    if obj.type=='text':
        data = {
            "text_data":obj.text_data,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }

    if obj.type=='email':
        data = {
            "email":obj.email,
            "subject":obj.subject,
            "message":obj.message,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }

    if obj.type=='call':
        data = {
            "country_code":obj.country_code,
            "phone_number":obj.phone_number,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }

    if obj.type=='sms':
        data = {
            "sms_country_code":obj.sms_country_code,
            "sms_phone_number":obj.sms_phone_number,
            "sms_message":obj.sms_message,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }
            
    if obj.type=='vcard':
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/' + str(obj.id),
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": "link"
        }

    if obj.type=='whatsapp':
        data = {
            "whatsapp_country_code":obj.whatsapp_country_code,
            "whatsapp_phone_number":obj.whatsapp_phone_number,
            "whatsapp_message":obj.whatsapp_message,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }

    if obj.type=='wifi':
        data = {
            "network_name":obj.network_name,
            "network_type":obj.network_type,
            "network_password":obj.network_password,
            "wifi_hidden":obj.wifi_hidden,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": obj.type
        }

    if obj.type=='pdf':
        data = {
            "link_data": request.build_absolute_uri('/') + obj.pdf.url,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": 'link'
        }

    if obj.type=='images':
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/' + str(obj.id),
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": 'link'
        }

    if obj.type=='video':
        data = {
            "link_data": obj.video,
            "bg_color": obj.bg_color,
            "frontcolor": obj.frontcolor,
            "gradient_color": obj.gradient_color,
            "marker_out_color": obj.marker_out_color,
            "marker_in_color": obj.marker_in_color,
            "custom_logo": obj.custom_logo,
            "framecolor": obj.framecolor,
            "pattern": obj.pattern,
            "marker_out": obj.marker_out,
            "marker_in": obj.marker_in,
            "optionlogo": obj.optionlogo,
            "outer_frame": obj.outer_frame,
            "framelabel": obj.framelabel,
            "label_font": obj.label_font,
            "type": 'link'
        }

        
    r = requests.post(url=API_ENDPOINT, data=data)
    tex = r.json()['content']
    svgFile=open("mediaaa/svgs/"+str(uid)+'.svg',"w")
    svgFile.write(tex)
    svgFile.close()
    drawing = svg2rlg("mediaaa/svgs/"+str(uid)+'.svg')
    renderPDF.drawToFile(drawing, "mediaaa/pdfs/"+str(uid)+".pdf")
    renderPM.drawToFile(drawing, "mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
    renderPM.drawToFile(drawing, "static/mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
    return redirect('/dashboard/statics')

def mkdynamic(request,objId):
    obj = Qrcodes.objects.get(pk=objId)
    obj.isDynamic=True
    obj.save()
    return redirect('dashboard')

def delfolder(request,objId):
    Folder.objects.get(pk=objId).delete()
    return redirect('/dashboard/folders')

def createfolder(request):
    if request.method=='POST':
        name = request.POST['name']
        new_folder = Folder(name=name,user_id=request.user)
        new_folder.save()

        return redirect('/dashboard/folders')
    return redirect('/dashboard/folders')

def movetofolder(request,objId):
    obj = Qrcodes.objects.get(pk=objId)
    if request.method=='POST':
        folder_name=request.POST['folder_id']
    req_folder = Folder.objects.get(name=folder_name)
    obj.folder_id=req_folder
    obj.save()
    return redirect('dashboard')


def editFolder(request,objId):
    efolder = Folder.objects.get(pk=objId)
    if request.method=='POST':
        folname=request.POST['name']
        folobj=Folder.objects.get(pk=objId)
        folobj.name=folname
        folobj.save()
        return redirect('/dashboard/folders')

    return render(request,'dashboardEditFolder.html',{'efolder':efolder})

def viewfolder(request,objId):
    rfolder=Folder.objects.get(pk=objId)
    qrs=Qrcodes.objects.all()
    folder=Folder.objects.all()
    content={
        'rfolder':rfolder,
        'qrs':qrs,
        'folder':folder,
    }
    return render(request,'viewfolder.html',content)

def qrtitleset(request,objId):
    if request.method=='POST':
        rname=request.POST['qrtitlename']
        reqr = Qrcodes.objects.get(pk=objId)

        reqr.qrname=rname
        reqr.save()
        if reqr.isDynamic:
            return redirect('dashboard')
        elif reqr.archived:
            return redirect('/dashboard/archived')
        else :
            return redirect('/dashboard/statics')

def editcontent(request,objId):
    qr_data = Qrcodes.objects.get(pk=objId)
    return render(request,'editcontent.html',{'objId':objId, 'qr_data':qr_data})


@csrf_exempt
def editcontentsave(request,objId):
    obj=Qrcodes.objects.get(pk=objId)
    API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
            
    if request.POST['type']=='link':
                uid=str(uuid.uuid4())[:5]
                obj.uuid=str(uid)
                obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
                obj.link_data=request.POST['link_data']
                obj.save()
                data = {
                    "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
                    # "link_data": request.POST['link_data'],
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

    if request.POST['type']=='text':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.text_data=request.POST['text_data']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "text_data":request.POST['text_data'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }


    if request.POST['type']=='email':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.subject=request.POST['subject']
        obj.message=request.POST['message']
        obj.email=request.POST['email']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "email":request.POST['email'],
            # "subject":request.POST['subject'],
            # "message":request.POST['message'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }


    if request.POST['type']=='call':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.country_code=request.POST['country_code']
        obj.phone_number=request.POST['phone_number']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "country_code":request.POST['country_code'],
            # "phone_number":request.POST['phone_number'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }


    if request.POST['type']=='sms':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.sms_country_code=request.POST['sms_country_code']
        obj.sms_phone_number=request.POST['sms_phone_number']
        obj.sms_message=request.POST['sms_message']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "sms_country_code":request.POST['sms_country_code'],
            # "sms_phone_number":request.POST['sms_phone_number'],
            # "sms_message":request.POST['sms_message'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }



    if request.POST['type']=='vcard':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.vcard_fname=request.POST['vcard_fname']
        obj.vcard_lname=request.POST['vcard_lname']
        obj.vcard_phone_number=request.POST['vcard_phone_number']
        obj.vcard_email=request.POST['vcard_email']
        obj.vcard_web_url=request.POST['vcard_web_url']
        obj.vcard_company=request.POST['vcard_company']
        obj.vcard_job_title=request.POST['vcard_job_title']
        obj.vcard_fax=request.POST['vcard_fax']
        obj.vcard_address=request.POST['vcard_address']
        obj.vcard_city=request.POST['vcard_city']
        obj.vcard_country=request.POST['vcard_country']
        obj.vcard_post_code=request.POST['vcard_post_code']
        obj.vcard_mobile=request.POST['vcard_mobile']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }
        


    if request.POST['type']=='whatsapp':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.whatsapp_country_code=request.POST['whatsapp_country_code']
        obj.whatsapp_phone_number=request.POST['whatsapp_phone_number']
        obj.whatsapp_message=request.POST['whatsapp_message']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "whatsapp_country_code":request.POST['whatsapp_country_code'],
            # "whatsapp_phone_number":request.POST['whatsapp_phone_number'],
            # "whatsapp_message":request.POST['whatsapp_message'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }

    if request.POST['type']=='wifi':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.wifi_hidden=request.POST['wifi_hidden']
        obj.network_name=request.POST['network_name']
        obj.network_type=request.POST['network_type']
        obj.network_password=request.POST['network_password']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "network_name":request.POST['network_name'],
            # "network_type":request.POST['network_type'],
            # "network_password":request.POST['network_password'],
            # "wifi_hidden":request.POST['wifi_hidden'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }


    if request.POST['type']=='pdf':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.pdf=request.FILES['pdf']
        obj.save()
        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }


    if request.POST['type']=='images':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.save()
        Images.objects.filter(qrcode_id=obj.id).delete()
        images = request.FILES.getlist('images[]')
        for img in images:
            Images.objects.create(qrcode=obj, image=img)

        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }

    if request.POST['type']=='video':
        uid=str(uuid.uuid4())[:5]
        obj.uuid=str(uid)
        obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
        obj.video=request.POST['video']
        obj.save()

        data = {
            "link_data": request.build_absolute_uri('/') + 'qr/'+str(obj.id),
            # "video":request.POST['video'],
            "bg_color": request.POST['bg_color'],
            "frontcolor": request.POST['frontcolor'],
            "gradient_color": request.POST['gradient_color'],
            "marker_out_color": request.POST['marker_out_color'],
            "marker_in_color": request.POST['marker_in_color'],
            "custom_logo": request.POST['custom_logo'],
            "framecolor": request.POST['framecolor'],
            "pattern": request.POST['pattern'],
            "marker_out": request.POST['marker_out'],
            "marker_in": request.POST['marker_in'],
            "optionlogo": request.POST['optionlogo'],
            "outer_frame": request.POST['outer_frame'],
            "framelabel": request.POST['framelabel'],
            "label_font": request.POST['label_font'],
            "type": 'link'
        }


            
    r = requests.post(url=API_ENDPOINT, data=data)
    tex = r.json()['content']
    # uid=str(uuid.uuid4())[:5]

    svgFile=open("mediaaa/svgs/"+str(uid)+'.svg',"w")
    svgFile.write(tex)
    svgFile.close()
    drawing = svg2rlg("mediaaa/svgs/"+str(uid)+'.svg')
    renderPDF.drawToFile(drawing, "mediaaa/pdfs/"+str(uid)+".pdf")
    renderPM.drawToFile(drawing, "mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
    renderPM.drawToFile(drawing, "static/mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
    # obj.uuid=str(uid)
    # obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
    # obj.save()
    return JsonResponse({
        'success': 'Successfully created a Qrcode.',
    })
    return JsonResponse({
        'failed': 'failed to create a Qrcode.',
    }, status=404)


    
    return redirect('/dashboard')

def editshape(request,objId):
    return render( request,'editshape.html',{'objId':objId} )

@csrf_exempt
def editshapesave(request,objId):

    obj=Qrcodes.objects.get(pk=objId)
    qrtype=obj.type
    API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
    if obj.type =='link':
                data = {
                    "link_data": obj.link_data,
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if qrtype=='text':
                data = {
                    "text_data":obj.text_data,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'text',
                }

    if obj.type=='email':
                data = {
                    "email":obj.email,
                    "subject":obj.subject,
                    "message":obj.message,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='call':
                data = {
                    "country_code":obj.country_code,
                    "phone_number":obj.phone_number,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='sms':
                data = {
                    "sms_country_code":obj.sms_country_code,
                    "sms_phone_number":obj.sms_phone_number,
                    "sms_message":obj.sms_message,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }
    if obj.type=='vcard':
                data = {
                    "vcard_fname":obj.vcard_fname,
                    "vcard_lname":obj.vcard_lname,
                    "vcard_phone_number":obj.vcard_phone_number,
                    "vcard_email":obj.vcard_email,
                    "vcard_web_url":obj.vcard_web_url,
                    "vcard_mobile":obj.vcard_mobile,
                    "vcard_company":obj.vcard_company,
                    "vcard_job_title":obj.vcard_job_title,
                    "vcard_fax":obj.vcard_fax,
                    "vcard_address":obj.vcard_address,
                    "vcard_city":obj.vcard_city,
                    "vcard_country":obj.vcard_country,
                    "vcard_post_code":obj.vcard_post_code,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='whatsapp':
                data = {
                    "whatsapp_country_code":obj.whatsapp_country_code,
                    "whatsapp_phone_number":obj.whatsapp_phone_number,
                    "whatsapp_message":obj.whatsapp_message,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='wifi':
                data = {
                    "network_name":obj.network_name,
                    "network_type":obj.network_type,
                    "network_password":obj.network_password,
                    "wifi_hidden":obj.wifi_hidden,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='pdf':
                data = {
                    "pdf":obj.pdf,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='images':
                data = {
                    "images":obj.images,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='video':
                data = {
                    "video":obj.video,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'video',
                }

    r = requests.post(url=API_ENDPOINT, data=data)
    tex = r.json()['content']
    uid=str(uuid.uuid4())[:5]

    svgFile=open("mediaaa/svgs/"+str(uid)+'.svg',"w")
    svgFile.write(tex)
    svgFile.close()
    drawing = svg2rlg("mediaaa/svgs/"+str(uid)+'.svg')
    renderPDF.drawToFile(drawing, "mediaaa/pdfs/"+str(uid)+".pdf")
    renderPM.drawToFile(drawing, "mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
    renderPM.drawToFile(drawing, "static/mediaaa/pngs/"+str(uid)+".png", fmt="PNG")
    obj.uuid=str(uid)
    obj.qrCodeimage='mediaaa/pngs/'+str(uid)+'.png'
    obj.save()
    return JsonResponse({
        'success': 'Successfully created a Qrcode.',
    })
    return JsonResponse({
        'failed': 'failed to create a Qrcode.',
    }, status=404)



    return redirect('/')
@csrf_exempt
def getQrCodePreview(request):
    # if request.user.is_authenticated:
            extra = {'user_id': request.user}
            # import requests
            API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
            
            if request.POST['type']=='link':
                data = {
                    "link_data": request.POST['link_data'],
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='text':
                data = {
                    "text_data":request.POST['text_data'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='email':
                data = {
                    "email":request.POST['email'],
                    "subject":request.POST['subject'],
                    "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='call':
                data = {
                    "country_code":request.POST['country_code'],
                    "phone_number":request.POST['phone_number'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='sms':
                data = {
                    "sms_country_code":request.POST['sms_country_code'],
                    "sms_phone_number":request.POST['sms_phone_number'],
                    "sms_message":request.POST['sms_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
            if request.POST['type']=='vcard':
                data = {
                    "vcard_fname":request.POST['vcard_fname'],
                    "vcard_lname":request.POST['vcard_lname'],
                    "vcard_phone_number":request.POST['vcard_phone_number'],
                    "vcard_email":request.POST['vcard_email'],
                    "vcard_web_url":request.POST['vcard_web_url'],
                    "vcard_mobile":request.POST['vcard_mobile'],
                    "vcard_company":request.POST['vcard_company'],
                    "vcard_job_title":request.POST['vcard_job_title'],
                    "vcard_fax":request.POST['vcard_fax'],
                    "vcard_address":request.POST['vcard_address'],
                    "vcard_city":request.POST['vcard_city'],
                    "vcard_country":request.POST['vcard_country'],
                    "vcard_post_code":request.POST['vcard_post_code'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='whatsapp':
                data = {
                    "whatsapp_country_code":request.POST['whatsapp_country_code'],
                    "whatsapp_phone_number":request.POST['whatsapp_phone_number'],
                    "whatsapp_message":request.POST['whatsapp_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='wifi':
                data = {
                    "network_name":request.POST['network_name'],
                    "network_type":request.POST['network_type'],
                    "network_password":request.POST['network_password'],
                    "wifi_hidden":request.POST['wifi_hidden'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='pdf':
                data = {
                    "pdf":request.FILES['pdf'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='images':
                data = {
                    "images":request.POST['images'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }

            if request.POST['type']=='video':
                data = {
                    "link_data":request.POST['video'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'link'
                }

            
            r = requests.post(url=API_ENDPOINT, data=data)
            tex = r.json()['content']
            return HttpResponse(tex)


@csrf_exempt
def preditshapesave(request,objId):

    obj=Qrcodes.objects.get(pk=objId)
    qrtype=obj.type
    API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
    if obj.type =='link':
                data = {
                    "link_data": obj.link_data,
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if qrtype=='text':
                data = {
                    "text_data":obj.text_data,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'text',
                }

    if obj.type=='email':
                data = {
                    "email":obj.email,
                    "subject":obj.subject,
                    "message":obj.message,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='call':
                data = {
                    "country_code":obj.country_code,
                    "phone_number":obj.phone_number,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='sms':
                data = {
                    "sms_country_code":obj.sms_country_code,
                    "sms_phone_number":obj.sms_phone_number,
                    "sms_message":obj.sms_message,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }
    if obj.type=='vcard':
                data = {
                    "vcard_fname":obj.vcard_fname,
                    "vcard_lname":obj.vcard_lname,
                    "vcard_phone_number":obj.vcard_phone_number,
                    "vcard_email":obj.vcard_email,
                    "vcard_web_url":obj.vcard_web_url,
                    "vcard_mobile":obj.vcard_mobile,
                    "vcard_company":obj.vcard_company,
                    "vcard_job_title":obj.vcard_job_title,
                    "vcard_fax":obj.vcard_fax,
                    "vcard_address":obj.vcard_address,
                    "vcard_city":obj.vcard_city,
                    "vcard_country":obj.vcard_country,
                    "vcard_post_code":obj.vcard_post_code,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='whatsapp':
                data = {
                    "whatsapp_country_code":obj.whatsapp_country_code,
                    "whatsapp_phone_number":obj.whatsapp_phone_number,
                    "whatsapp_message":obj.whatsapp_message,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='wifi':
                data = {
                    "network_name":obj.network_name,
                    "network_type":obj.network_type,
                    "network_password":obj.network_password,
                    "wifi_hidden":obj.wifi_hidden,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='pdf':
                data = {
                    "pdf":obj.pdf,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='images':
                data = {
                    "images":obj.images,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": obj.type
                }

    if obj.type=='video':
                data = {
                    "video":obj.video,
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": 'video',
                }

    r = requests.post(url=API_ENDPOINT, data=data)
    tex = r.json()['content']
    return HttpResponse(tex)


@csrf_exempt
def preditcontentsave(request,objId):

    obj=Qrcodes.objects.get(pk=objId)
    API_ENDPOINT = "https://qrsample.qrlab.co/api/generate/qrcode"
            
    if request.POST['type']=='link':
                data = {
                    "link_data": request.POST['link_data'],
                    # "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.link_data=request.POST['link_data']

    if request.POST['type']=='text':
                data = {
                    "text_data":request.POST['text_data'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.text_data=request.POST['text_data']


    if request.POST['type']=='email':
                data = {
                    "email":request.POST['email'],
                    "subject":request.POST['subject'],
                    "message":request.POST['message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.subject=request.POST['subject']
                obj.message=request.POST['message']
                obj.email=request.POST['email']


    if request.POST['type']=='call':
                data = {
                    "country_code":request.POST['country_code'],
                    "phone_number":request.POST['phone_number'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.country_code=request.POST['country_code']
                obj.phone_number=request.POST['phone_number']


    if request.POST['type']=='sms':
                data = {
                    "sms_country_code":request.POST['sms_country_code'],
                    "sms_phone_number":request.POST['sms_phone_number'],
                    "sms_message":request.POST['sms_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.sms_country_code=request.POST['sms_country_code']
                obj.sms_phone_number=request.POST['sms_phone_number']
                obj.sms_message=request.POST['sms_message']



    if request.POST['type']=='vcard':
                data = {
                    "vcard_fname":request.POST['vcard_fname'],
                    "vcard_lname":request.POST['vcard_lname'],
                    "vcard_phone_number":request.POST['vcard_phone_number'],
                    "vcard_email":request.POST['vcard_email'],
                    "vcard_web_url":request.POST['vcard_web_url'],
                    "vcard_mobile":request.POST['vcard_mobile'],
                    "vcard_company":request.POST['vcard_company'],
                    "vcard_job_title":request.POST['vcard_job_title'],
                    "vcard_fax":request.POST['vcard_fax'],
                    "vcard_address":request.POST['vcard_address'],
                    "vcard_city":request.POST['vcard_city'],
                    "vcard_country":request.POST['vcard_country'],
                    "vcard_post_code":request.POST['vcard_post_code'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.vcard_fname=request.POST['vcard_fname']
                obj.vcard_lname=request.POST['vcard_lname']
                obj.vcard_phone_number=request.POST['vcard_phone_number']
                obj.vcard_email=request.POST['vcard_email']
                obj.vcard_web_url=request.POST['vcard_web_url']
                obj.vcard_company=request.POST['vcard_company']
                obj.vcard_job_title=request.POST['vcard_job_title']
                obj.vcard_fax=request.POST['vcard_fax']
                obj.vcard_address=request.POST['vcard_address']
                obj.vcard_city=request.POST['vcard_city']
                obj.vcard_country=request.POST['vcard_country']
                obj.vcard_post_code=request.POST['vcard_post_code']
                obj.vcard_mobile=request.POST['vcard_mobile']


    if request.POST['type']=='whatsapp':
                data = {
                    "whatsapp_country_code":request.POST['whatsapp_country_code'],
                    "whatsapp_phone_number":request.POST['whatsapp_phone_number'],
                    "whatsapp_message":request.POST['whatsapp_message'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.whatsapp_country_code=request.POST['whatsapp_country_code']
                obj.whatsapp_phone_number=request.POST['whatsapp_phone_number']
                obj.whatsapp_message=request.POST['whatsapp_message']


    if request.POST['type']=='wifi':
                data = {
                    "network_name":request.POST['network_name'],
                    "network_type":request.POST['network_type'],
                    "network_password":request.POST['network_password'],
                    "wifi_hidden":request.POST['wifi_hidden'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.wifi_hidden=request.POST['wifi_hidden']
                obj.network_name=request.POST['network_name']
                obj.network_type=request.POST['network_type']
                obj.network_password=request.POST['network_password']


    if request.POST['type']=='pdf':
                data = {
                    "pdf":request.FILES['pdf'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.pdf=request.FILES['pdf']


    if request.POST['type']=='images':
                data = {
                    "images":request.POST['images'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.images=request.POST['images']


    if request.POST['type']=='video':
                data = {
                    "video":request.POST['video'],
                    "bg_color": request.POST['bg_color'],
                    "frontcolor": request.POST['frontcolor'],
                    "gradient_color": request.POST['gradient_color'],
                    "marker_out_color": request.POST['marker_out_color'],
                    "marker_in_color": request.POST['marker_in_color'],
                    "custom_logo": request.POST['custom_logo'],
                    "framecolor": request.POST['framecolor'],
                    "pattern": request.POST['pattern'],
                    "marker_out": request.POST['marker_out'],
                    "marker_in": request.POST['marker_in'],
                    "optionlogo": request.POST['optionlogo'],
                    "outer_frame": request.POST['outer_frame'],
                    "framelabel": request.POST['framelabel'],
                    "label_font": request.POST['label_font'],
                    "type": request.POST['type']
                }
                obj.video=request.POST['video']


            
    r = requests.post(url=API_ENDPOINT, data=data)
    tex = r.json()['content']
    return HttpResponse(tex)

class HttpResponseRedirect(HttpResponseRedirectBase):
    status_code = 302
    allowed_schemes = ["http", "https", "tel", "mailto", "wifi", "sms", "whatsapp"]


def dynamic_qr_code(request, id):
    qr_Data = Qrcodes.objects.get(id=id)
    qr_Data.scans = qr_Data.scans + 1
    qr_Data.save()
    if qr_Data.type == 'link':
        return redirect(qr_Data.link_data)

    if qr_Data.type == 'email':
        email_url = 'mailto:' + qr_Data.email + '?subject=' + qr_Data.subject + '&body=' + qr_Data.message
        return HttpResponseRedirect(email_url)
    if qr_Data.type == 'call':
        tel_url = 'tel:' + qr_Data.country_code + qr_Data.phone_number
        return HttpResponseRedirect(tel_url)

    if qr_Data.type == 'text':
        return HttpResponse(qr_Data.text_data)
    
    if qr_Data.type == 'wifi':
        # wifi_url = 'WIFI:T:' + qr_Data.network_type + ';S:' + qr_Data.network_name + ';P:' + qr_Data.network_password + ';H:' + qr_Data.wifi_hidden + ';;'
        wifi_url = 'wifi:' + qr_Data.network_name + ':' + qr_Data.network_password + ':' + qr_Data.network_type + ':' + qr_Data.wifi_hidden
        return JsonResponse(wifi_url, safe=False)

    if qr_Data.type == 'sms':
        #sms_url for android
        sms_url_android = 'sms:' + qr_Data.sms_country_code + qr_Data.sms_phone_number + '?body=' + qr_Data.sms_message

        # sms_url for iphone
        sms_url_iphone = 'sms:' + qr_Data.sms_country_code + qr_Data.sms_phone_number + '&body=' + qr_Data.sms_message

        #identify the device and redirect to the sms_url
        #identify if the device is android or iphone
        if 'iPhone' in request.META['HTTP_USER_AGENT']:
            return HttpResponseRedirect(sms_url_iphone)
        # if 'Android' in request.META['HTTP_USER_AGENT']:
        #     return HttpResponseRedirect(sms_url_android)
        else:
            return HttpResponseRedirect(sms_url_android)

    if qr_Data.type == 'whatsapp':
        whatsapp_url = 'whatsapp://send?text=' + qr_Data.whatsapp_message + '&phone=' + qr_Data.whatsapp_country_code + qr_Data.whatsapp_phone_number
        return HttpResponseRedirect(whatsapp_url)

    if qr_Data.type == 'video':
        return HttpResponseRedirect(qr_Data.video)

    if qr_Data.type == 'pdf':
        return HttpResponseRedirect(qr_Data.pdf.url)

    if qr_Data.type == 'images':
        image_list = Images.objects.filter(qrcode_id=id)
        return render(request, 'image_list.html', {'images': image_list})

    if qr_Data.type== 'vcard':
        vcard_data = Qrcodes.objects.get(id=id)
        return render(request, 'vcard.html', {'vcard_data': vcard_data})
        
def to_internal_value(base):
    format, data = base.split(';base64,')
    file_name = str(uuid.uuid4())[:12]
    ext = format.split('/')[-1]
    complete_file_name = "%s.%s" % (
        file_name,
        ext,
    )
    data = ContentFile(base64.b64decode(data), name=complete_file_name)
    return data
    
@csrf_exempt
def social_media_create(request):
    if request.method == 'POST':
        data = request.POST.get('dp')
        if data:
            image = to_internal_value(data)
        else:
            image = None
        name = request.POST.get('name')
        title = request.POST.get('title')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        social_links = request.POST.get('socialLinks')
        social_links = json.loads(social_links)

        social_facebook_link_title = ''
        social_facebook_link = ''
        social_twitter_link_title = ''
        social_twitter_link = ''
        social_instagram_link_title = ''
        social_instagram_link   = ''
        social_linkedin_link_title  = ''
        social_linkedin_link= ''
        social_pinterest_link_title= ''
        social_pinterest_link= ''
        social_youtube_link_title= ''
        social_youtube_link= ''
        social_snapchat_link_title= ''
        social_snapchat_link= ''
        social_reddit_link_title= ''
        social_reddit_link= ''
        social_other_link_title= ''
        social_other_link= ''
        for i in social_links:
            if i['icon'] == 'facebook':
                social_facebook_link_title = i['title']
                social_facebook_link = i['link']
            if i['icon'] == 'twitter':
                social_twitter_link_title = i['title']
                social_twitter_link = i['link']
            if i['icon'] == 'instagram':
                social_instagram_link_title = i['title']
                social_instagram_link = i['link']
            if i['icon'] == 'linkedin':
                social_linkedin_link_title = i['title']
                social_linkedin_link = i['link']
            if i['icon'] == 'pinterest':
                social_pinterest_link_title = i['title']
                social_pinterest_link = i['link']
            if i['icon'] == 'youtube':
                social_youtube_link_title = i['title']
                social_youtube_link = i['link']
            if i['icon'] == 'snapchat':
                social_snapchat_link_title = i['title']
                social_snapchat_link = i['link']
            if i['icon'] == 'reddit':
                social_reddit_link_title = i['title']
                social_reddit_link = i['link']
            else:
                social_other_link_title = i['title']
                social_other_link = i['link']
            

        data={
            'full_name': name,
            'title': title,
            'email': email,
            'phone_number': phone,
            'website': website,
            'social_facebook_link_title': social_facebook_link_title,
            'social_facebook_link': social_facebook_link,
            'social_twitter_link_title': social_twitter_link_title,
            'social_twitter_link': social_twitter_link,
            'social_instagram_link_title': social_instagram_link_title,
            'social_instagram_link': social_instagram_link,
            'social_linkedin_link_title': social_linkedin_link_title,
            'social_linkedin_link': social_linkedin_link,
            'social_pinterest_link_title': social_pinterest_link_title,
            'social_pinterest_link': social_pinterest_link,
            'social_youtube_link_title': social_youtube_link_title,
            'social_youtube_link': social_youtube_link,
            'social_snapchat_link_title': social_snapchat_link_title,
            'social_snapchat_link': social_snapchat_link,
            'social_reddit_link_title': social_reddit_link_title,
            'social_reddit_link': social_reddit_link,
            'social_other_link_title': social_other_link_title,
            'social_other_link': social_other_link,
            'profile_picture': image
        }
        Qrcodes.objects.create(**data)
        #hard redirect to dashboard
        return HttpResponseRedirect('/dashboard')
    return render(request, 'create-social.html')