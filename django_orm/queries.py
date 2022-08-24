# Get all users who were created within the last month and sorted by their emails from Z to A order
# from app.models import Customer
# Customer.objects.all()
# import datetime
# Customer.objects.filter(created_at__range=('2022-06-12 11:53:59.598972+00:00', '2022-07-12 11:53:59.598972+00:00')).order_by('email')
#
# Get top 10 biggest orders within the system
# top_total_price = (Order.objects.order_by('-total_price').values_list('total_price', flat=True).distinct())
# top_records = (Order.objects.order_by('-total_price').filter(total_price__in=top_total_price[:10]))
# print(top_records)
#
# Get a total sum of last month's orders
# from django.db.models import Count, Sum
# metrics = {'sales_sum': Sum('total_price'),}
# queryset = Order.objects.values('created_at__month').annotate(**metrics).order_by('created_at__month')
# print(queryset)
#
# Select specific user with all his orders together ordered by order date descending
# Order.objects.filter(customer_id='5').order_by('created_at')