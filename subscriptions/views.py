from django.shortcuts import render, redirect  # Ensure this import is present
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Subscription
import json

def home(request):
    return render(request, 'home.html')  # Adjust the path as necessary

def customer_list(request):
    # Get all customers from the database
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

@csrf_exempt  
def create_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')

        customer = Customer(name=name, email=email)
        customer.save()

        return JsonResponse({'message': 'Customer created successfully', 'customer_id': customer.id})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def create_subscription(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract the required fields from the request data
            plan = data.get('plan')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            customer_id = data.get('customer_id')

            # Ensure customer exists
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                return JsonResponse({'error': 'Customer not found'}, status=404)

            # Create the subscription
            subscription = Subscription(
                customer=customer,
                plan=plan,
                start_date=start_date,
                end_date=end_date,
                active=True  # default active to True
            )
            subscription.save()

            return JsonResponse({'message': 'Subscription created successfully', 'subscription_id': subscription.id})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def subscription_list(request):
    # Get all subscriptions from the database
    subscriptions = Subscription.objects.all()
    return render(request, 'subscription_list.html', {'subscriptions': subscriptions})
