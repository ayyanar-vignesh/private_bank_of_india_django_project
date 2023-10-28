from django.shortcuts import render

from . models import *

from django.contrib import messages
import random 
import datetime

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')
def login_page(request):
    return render(request,'login_page.html')
def register_page(request):
    return render(request,'register_page.html')


def register_form_submission(request):
    if request.method=='POST': 
        if register_table.objects.filter(email_id=request.POST.get('email_id')):
            print("**this email has already registered****")
            messages.error(request,'Already this email has registered!...',extra_tags='registered')
            return render(request,'register_page.html')
        else:
            account_number=random.randint(000000,999999)
            your_account_number="PBI"+"2023"+str(account_number)
            print(f"your accounbt number is:{your_account_number}")

            ex1=register_table(first_name=request.POST.get('first_name'),
                           last_name=request.POST.get('last_name'),
                           phone_number=request.POST.get('phone_number'),
                           email_id=request.POST.get('email_id'),
                           password=request.POST.get('password'),
                           account_number=your_account_number,
                           my_cash=0,
                           deposit_amount=0,
                           withdraw_amount=0,
                           )
            ex1.save()
            #mail code
            try:
                first_name=request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                email_id=request.POST.get('email_id')
                account_number=your_account_number

                subject = 'PBI Account Activated Successfully!...'
                message = f'Hi {first_name} {last_name},\nYour account number has activated successfully.\nYour account number is {account_number}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email_id, ]
                send_mail( subject, message, email_from, recipient_list )
                print("**mail sent successfully***")
            except:
                print("**mail not sent****")
            print("****data saved successfully*****")
            return render(request,'login_page.html')





def login_form_submission(request):
    if register_table.objects.filter(account_number=request.POST.get('account_number'),password=request.POST.get('password')):
        print("***login successfully****")
        logger_data=register_table.objects.get(account_number=request.POST.get('account_number'),password=request.POST.get('password'))
        #***change***
        account_number=logger_data.account_number
        view_statment=bank_statment_table.objects.filter(account_number=account_number)
        return render(request,'dashboard.html',{'logger_data':logger_data,'view_statment':view_statment})
    else:
        print("***invalid credentials***")
        messages.error(request,'Invalid credentials!...',extra_tags='failed')
        return render(request,'login_page.html')



def deposit_form_submission(request,logger_account_number):
    #****amount deposit logic*****
    full_date_time=datetime.datetime.now()
    your_cash=request.POST.get('my_cash')
    logger_data=register_table.objects.get(account_number=logger_account_number)
    my_balance=logger_data.my_cash

    my_updated_cash=int(your_cash)+int(my_balance)
    #*********************

    #*******to store bank statment table******
    account_holder_name=logger_data.first_name+" "+logger_data.last_name
    print(f"account holder name {account_holder_name}")
    account_number=logger_data.account_number
    print(f"account number {account_number}")
    deposit_amount=request.POST.get('my_cash')
    print(f"you deposit amount {deposit_amount}")
    withdraw_amount="-"
    balance_amount=my_updated_cash
    print(f"you balance is {balance_amount}")
    transaction_date=full_date_time
    print(f"transaction date {transaction_date}")

    deposit_store=bank_statment_table(account_holder_name=account_holder_name,
                                      account_number=account_number,
                                      deposit_amount=deposit_amount,
                                      withdraw_amount=withdraw_amount,
                                      balance_amount=balance_amount,
                                      transaction_date=transaction_date)
    deposit_store.save()
    print("****deposit-bank statmnet updated succesfully***")
    #************************************************
    
    ex1=register_table.objects.filter(account_number=logger_account_number).update(my_cash=my_updated_cash)
    print("**amount deposited successfully****")
    
    logger_data=register_table.objects.get(account_number=logger_account_number)
    messages.error(request,'Amount Deposited successfully!...',extra_tags='deposited')
    account_number=logger_data.account_number
    view_statment=bank_statment_table.objects.filter(account_number=account_number)
    return render(request,'dashboard.html',{'logger_data':logger_data,'view_statment':view_statment})




def withdraw_form_submission(request,logger_account_number):
    #****amount withdraw logic*****
    full_date_time=datetime.datetime.now()
    logger_data=register_table.objects.get(account_number=logger_account_number)
    my_balance=logger_data.my_cash
    withdraw_cash=request.POST.get('my_cash')
    if int(withdraw_cash)<int(my_balance):
        my_updated_cash=int(my_balance)-int(withdraw_cash)

        #*******to store bank statment table******
        account_holder_name=logger_data.first_name+" "+logger_data.last_name
        print(f"account holder name {account_holder_name}")
        account_number=logger_data.account_number
        print(f"account number {account_number}")
        deposit_amount="-"
        print(f"you deposit amount {deposit_amount}")
        withdraw_amount=withdraw_cash
        balance_amount=my_updated_cash
        print(f"you balance is {balance_amount}")
        transaction_date=full_date_time
        print(f"transaction date {transaction_date}")

        deposit_store=bank_statment_table(account_holder_name=account_holder_name,
                                      account_number=account_number,
                                      deposit_amount=deposit_amount,
                                      withdraw_amount=withdraw_amount,
                                      balance_amount=balance_amount,
                                      transaction_date=transaction_date)
        deposit_store.save()
        print("****deposit-bank statmnet updated succesfully***")
        #************************************************

        ex1=register_table.objects.filter(account_number=logger_account_number).update(my_cash=my_updated_cash)
        print("**amount deposited successfully****")
        logger_data=register_table.objects.get(account_number=logger_account_number)
        messages.error(request,'Amount withdraw successfully!...',extra_tags='deposited')
        account_number=logger_data.account_number
        view_statment=bank_statment_table.objects.filter(account_number=account_number)
        return render(request,'dashboard.html',{'logger_data':logger_data,'view_statment':view_statment})
    else:
        print("**insufficient balance**")
        logger_data=register_table.objects.get(account_number=logger_account_number)
        messages.error(request,'Insufficient balance !...',extra_tags='insuff')
        account_number=logger_data.account_number
        view_statment=bank_statment_table.objects.filter(account_number=account_number)
        return render(request,'dashboard.html',{'logger_data':logger_data,'view_statment':view_statment})
    #*************************************************
    
    
    
