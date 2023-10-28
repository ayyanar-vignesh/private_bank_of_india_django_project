from django.db import models

# Create your models here.
class register_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    email_id=models.EmailField()
    password=models.CharField(max_length=20)
    account_number=models.CharField(max_length=100)
    my_cash=models.CharField(max_length=100)
    deposit_amount=models.CharField(max_length=100)
    withdraw_amount=models.CharField(max_length=100)
    deposit_transaction_date=models.CharField(max_length=100)
    withdraw_transaction_date=models.CharField(max_length=100)


class bank_statment_table(models.Model):
    account_holder_name=models.CharField(max_length=100)
    account_number=models.CharField(max_length=100)
    deposit_amount=models.CharField(max_length=100)
    withdraw_amount=models.CharField(max_length=100)
    balance_amount=models.CharField(max_length=100)
    transaction_date=models.CharField(max_length=100)
    








