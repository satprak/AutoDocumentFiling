from django.shortcuts import render
from pymongo import MongoClient
import datetime
from django.http import JsonResponse
from django.core import serializers
from .models import Product
import json

#___________autocomplete fxn for providing list of suggestion words___________________________
def autocomplete(t1,doc_type,field):
    if t1:
        t1 = t1[::-1]
        text = ""
        for i in t1:
            if i=='+' or i=='-' or i=='|':
                break
            else:
                text = i+text
        t2=[]
        client =  MongoClient('mongodb://localhost:27017/')
        text= text.lower()
        length=len(text)
        if not length:
            return JsonResponse([], safe=False)
        list1 = list(client.adf_main.adf_list.find({'doc_type':doc_type}))
        list2= list1[0][field]
        list3=[]
        count =0
        for x in list2:
            if len(x['word'])>=length:
                if x['word'][:length]==text:
                    list3.append(x['word'])
                    count+=1
                    if count ==10:
                        break
        return list3

#____fxns for autocomplete for different different fields in front end________________________
def Invoice_Company(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Invoice','Company'),safe=False)
def Invoice_keywords(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Invoice','keywords'), safe=False)
def Invoice_full_text(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Invoice','full_text'), safe=False)
def Email_From(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Email','From'), safe=False)
def Email_To(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Email','To'), safe=False)
def Email_keywords(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Email','keywords'), safe=False)
def Email_Body(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Email','Body'), safe=False)
def Email_Subject(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Email','Subject'), safe=False)
def Email_Attachments(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Email','Attachments'), safe=False)
def Others_keywords(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Others','keywords'), safe=False)
def Others_full_text(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'Others','full_text'), safe=False)
def All_file_name(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'All','file_name'), safe=False)
def All_full_text(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'All','full_text'), safe=False)
def All_keywords(request):
    if 'term' in request.GET:
        return JsonResponse(autocomplete(request.GET['term'],'All','keywords'), safe=False)

#_____fxn for searching text having + - | ________________________________________
def text_search(key_string,search_in,dic,s):
    temp = '*'
    current = ""
    and_list=[]
    not_list=[]
    or_list=[]
    for i in key_string:
        if(i=='+' or i=='-' or i=='|'):
            if(temp=='+'):
                and_list.append(current)
            elif(temp=='-'):
                not_list.append(current)
            elif(temp=='|'):
                or_list.append(current)

            temp = i
            current= ""

        else:
            current+=i
    if(temp=='+'):
        and_list.append(current)
    elif(temp=='-'):
        not_list.append(current)
    elif(temp=='|'):
        or_list.append(current)
    
    list1=[]#******list for and(+)***********
    dic1=dic
    if len(and_list):
        for word in and_list:
            s=s+word+" "
            list1.append({search_in: { '$regex': word, '$options': 'i' } })
        dic1 = {'$and':[dic,{ '$and': list1}]}

    list2=[]#******list for not(-)***********
    dic2=dic
    if len(not_list):
        for word in not_list:
            list2.append({search_in: { '$regex': word, '$options': 'i' } })
        dic2 = {'$and':[dic,{'$nor': list2}]}

    list3=[]#******list for or(|)***********
    dic3=dic
    if len(or_list):
        for word in or_list:
            s=s+word+" "
            list3.append({search_in: { '$regex': word, '$options': 'i' } })
        dic3 = {'$and':[dic,{'$or': list3}]}
    
    return [dic1,dic2,dic3,s]

def search(request):
    if request.method == 'POST':
        client =  MongoClient('mongodb://localhost:27017/')
        if request.POST["doc_type"] == 'Others':
            is_header = request.POST.get('header',False)
            is_para = request.POST.get('Paragraph',False)
            Header_Para = request.POST["Header_Para"]
            keyword = request.POST["keyword"]
            client = MongoClient('mongodb://localhost:27017/')
            docs=[]
            dic={}
            dic['doc_type'] = 'Others'
            
            s = ""
            # ********************header selected************
            if is_header:
                temp = text_search(Header_Para,'headers',dic,s)
                temp_main_dic1 = temp[0:-1]
                s=temp[-1]
                temp = text_search(keyword,'keywords',dic,s)
                temp_main_dic2 = temp[0:-1]
                s=temp[-1]
                temp_main_dic = temp_main_dic1 + temp_main_dic2
                doc1= client.adf_main.adf_frontend.find({'$and':temp_main_dic} )
                docs.append(list(doc1))
# ********************paragraph selected************
            if is_para:
                temp = text_search(Header_Para,'paragraphs',dic,s)
                temp_main_dic1 = temp[0:-1]
                s=temp[-1]
                temp = text_search(keyword,'keywords',dic,s)
                temp_main_dic2 = temp[0:-1]
                s=temp[-1]
                temp_main_dic = temp_main_dic1 + temp_main_dic2
                doc1= client.adf_main.adf_frontend.find({'$and':temp_main_dic} )
                docs.append(list(doc1))
            
            if len(docs)==2:#____if both header and para are selected____________
                new_list=docs[0]
                for x in docs[1]:
                    flag=1
                    for y in docs[0]:
                        if x['file_name']==y['file_name'] and x['page_number']==y['page_number']:
                            flag=0
                            break
                    if flag:
                        new_list.append(x)
                docs.clear()
                docs=new_list
            
            if len(docs)==0:#____if neither header nor para are selected____________
                temp = text_search(keyword,'keywords',dic,s)
                temp_main_dic = temp[0:-1]
                s=temp[-1]
                doc1 = client.adf_main.adf_frontend.find({'$and':temp_main_dic})
                docs=doc1
            docs1={}
            docs1['main'] = docs
            docs1["to_search"]=s
            return render(request, 'search/others.html', {'docs':docs1})

        elif request.POST["doc_type"] == 'Email':
            df = client.adf_main.adf_frontend
            docs=[]
            s=""
            in_start_date = request.POST["Start_Date"]
            in_end_date = request.POST["End_Date"]
            #print(in_date,type(in_date))
            if(in_start_date):
                in_start_date = datetime.datetime.strptime(in_start_date, '%Y-%m-%d')
            else:
                in_start_date = datetime.datetime(1500, 5, 17)
            #print(in_date,type(in_date))
            if(in_end_date):
                in_end_date = datetime.datetime.strptime(in_end_date, '%Y-%m-%d')
            else:
                in_end_date = datetime.datetime.now()
            
            main_dic=[]
            #  ******* -------  To: -----*******
            to_string = request.POST["To"]   # psenwar@gmail.com+satyamprakashiitk2022@gmail.com
            dic={}
            dic['doc_type'] = 'Email'
            temp_main_dic = text_search(to_string,'To',dic,s)
            s=temp_main_dic[-1]
            for i in temp_main_dic[0:-1]:
                main_dic.append(i)          


            dic_date = {'$and':[{'date':{'$gt':in_start_date}},{'date':{'$lt':in_end_date}}]}
            main_dic.append(dic_date)

#  ******* -------  FROM: -----*******
            from_string = request.POST["From"]   # psenwar@gmail.com+satyamprakashiitk2022@gmail.com
            if len(from_string):
                dic={}
                dic['doc_type'] = 'Email'
                temp_main_dic = text_search(to_string,'From',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i) 
          # ***** -----  BODY search ----- *******
            body_string = request.POST["Body"]   # psenwar@gmail.com+satyamprakashiitk2022@gmail.com
            if len(body_string):
                dic={}
                dic['doc_type'] = 'Email'
                temp_main_dic = text_search(body_string,'Body',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i) 

            #****** ---- Subject ----*****
            sub_string = request.POST["Subject"]   # psenwar@gmail.com+satyamprakashiitk2022@gmail.com
            if len(sub_string):
                dic={}
                dic['doc_type'] = 'Email'
                temp_main_dic = text_search(sub_string,'Subject',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i) 

            #****** ---- Keyword ----*****
            key_string = request.POST["keyword"]   # psenwar@gmail.com+satyamprakashiitk2022@gmail.com
            if len(key_string):
                dic={}
                dic['doc_type'] = 'Email'
                temp_main_dic = text_search(key_string,'keywords',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i) 
            #****** ---- Attachments ----*****
            Attachments_string = request.POST["Attachments"]   # psenwar@gmail.com+satyamprakashiitk2022@gmail.com
            if len(Attachments_string):
                dic={}
                dic['doc_type'] = 'Email'
                temp_main_dic = text_search(Attachments_string,'Attachments',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i) 
            # ******** - mongoDB queries ****** ---- 
            
            doc1= df.find({'$and':main_dic} )
            docs={}
            docs['main'] = doc1
            docs["to_search"] = s
            #print("docs", docs)
            
            #docs = db.find({'doc_type':'Email'})   
            return render(request , 'search/email_search.html', {'docs':docs})

        elif request.POST["doc_type"] == 'Invoice':
            df = client.adf_main.adf_frontend
            docs=[]
            s=""
            in_start_date = request.POST['date1']
            in_end_date = request.POST['date2']
            if(in_start_date):
                in_start_date = datetime.datetime.strptime(in_start_date, '%Y-%m-%d')
            else:
                in_start_date = datetime.datetime(1500, 5, 17)
            #print(in_date,type(in_date))
            if(in_end_date):
                in_end_date = datetime.datetime.strptime(in_end_date, '%Y-%m-%d')
            else:
                in_end_date = datetime.datetime.now()
            dic={}
            dic['doc_type'] = 'Invoice'
            main_dic = []
            #_________________company___________________________
            company = request.POST['com']
            temp_main_dic = text_search(company,'issuer',dic,s)
            s=temp_main_dic[-1]
            for i in temp_main_dic[0:-1]:
                main_dic.append(i) 
            #____________________date_________________________________________
            dic_date = {'$and':[{'date':{'$gt':in_start_date}},{'date':{'$lt':in_end_date}}]}
            main_dic.append(dic_date)
            #_________________amount________________________________
            st_amount = request.POST['st_amount']
            end_amount = request.POST['end_amount']
            if(st_amount):
                st_amount=int(st_amount)
                dic_amt = {'$and':[{'amount':{'$gt':st_amount}}]}
            else:
                dic_amt = {'$and':[{'amount':{'$gt':0}}]}
            main_dic.append(dic_amt)
            if(end_amount):
                end_amount=int(end_amount)
                dic_amt = {'$and':[{'amount':{'$lt':end_amount}}]}
            else:
                dic_amt = {'$and':[{'amount':{'$lt':9999999999}}]}
            main_dic.append(dic_amt)

            #_______________keyword__________________________________
            key_string = request.POST['keyword']
            if len(key_string):
                temp_main_dic = text_search(key_string,'keywords',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i)
            #_______________full text__________________________________
            full = request.POST['full']
            if len(full):
                temp_main_dic = text_search(full,'content_text',dic,s)
                s=temp_main_dic[-1]
                for i in temp_main_dic[0:-1]:
                    main_dic.append(i) 
        #__________mongo query ____________________
            doc1 = df.find({'$and':main_dic})
            docs={}
            docs["main"] = doc1
            docs["to_search"] = s
            return render(request, 'search/invoice_search.html', {'docs': docs})
        
        elif request.POST["doc_type"] == 'All':
            df = client.adf_main.adf_frontend
            dic={}
            s = ""
            dic = { "doc_type": { "$in": ["Email","Others","Invoice"] } }
            main_dic=[]
            #____keyword________________
            to_string = request.POST["keyword"]   
            temp_main_dic = text_search(to_string,'keywords',dic,s)
            s=temp_main_dic[-1]
            for i in temp_main_dic[0:-1]:
                main_dic.append(i)  
            #____full text________________
            to_string = request.POST["content_text"]   
            temp_main_dic = text_search(to_string,'content_text',dic,s)
            s=temp_main_dic[-1]
            for i in temp_main_dic[0:-1]:
                main_dic.append(i)  
            #---** ---- searching in file_name ---**  
            to_string = request.POST["file_name"]   
            temp_main_dic = text_search(to_string,'file_name',dic,s)
            s=temp_main_dic[-1]
            for i in temp_main_dic[0:-1]:
                main_dic.append(i) 
            doc1= df.find({'$and':main_dic} )
            docs={}
            docs["main"] = doc1
            docs["to_search"] = s
            return render(request , 'search/all.html', {'docs':docs})
            

    else:
        dic={}
        try:
            dic['type']=request.GET['type']
            
        except:
            pass
        # print(dic)
        return render(request, 'search/search.html',dic)