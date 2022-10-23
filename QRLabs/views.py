from copy import error
import email
from email import message
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
                    "pdf":request.POST['pdf'],
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

            
            r = requests.post(url=API_ENDPOINT, data=data)
            tex = r.json()['content']
            uid=str(uuid.uuid4())[:5]
            
            # qr = Qrcodes.objects.create(**request.POST.dict(), **extra)
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
            return JsonResponse({
                'success': 'Successfully created a Qrcode.',
            })
        return JsonResponse({
        'failed': 'failed to create a Qrcode.',
    }, status=404)


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
    obj = Qrcodes.objects.get(pk=objId)
    obj.isDynamic=False
    obj.save()
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
    return render(request,'editcontent.html',{'objId':objId})


@csrf_exempt
def editcontentsave(request,objId):
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
                    "pdf":request.POST['pdf'],
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
                obj.pdf=request.POST['pdf']


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
    if request.user.is_authenticated:
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
                    "pdf":request.POST['pdf'],
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

            
            r = requests.post(url=API_ENDPOINT, data=data)
            tex = r.json()['content']
            print(tex)
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
                    "pdf":request.POST['pdf'],
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
                obj.pdf=request.POST['pdf']


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