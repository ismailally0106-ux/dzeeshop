from django.shortcuts import render
from .models import Category, Product, Order

def dashboard(request):
    context = {
        'total_revenue': 892400,
        'revenue_trend': '+12.5%',
        'new_orders': 156,
        'orders_trend': '+8.2%',
        'total_products': 342,
        'products_trend': '+6 new this week',
        'total_customers': 2841,
        'customers_trend': '+18.3%',
        'this_month_revenue': '₦2.4M',
        'total_orders_count': 1247,
        'recent_orders': [
            {'product': 'Wireless Headphones', 'icon': 'fa-headphones', 'qty': 2, 'amount': '₦45,000', 'status': 'Delivered'},
            {'product': 'iPhone 15 Pro Max', 'icon': 'fa-mobile-alt', 'qty': 1, 'amount': '₦1,450,000', 'status': 'Shipped'},
            {'product': 'MacBook Air M3', 'icon': 'fa-laptop', 'qty': 1, 'amount': '₦2,200,000', 'status': 'Pending'},
            {'product': 'Samsung Galaxy Tab S9', 'icon': 'fa-tablet-alt', 'qty': 3, 'amount': '₦780,000', 'status': 'Cancelled'},
            {'product': 'Apple Watch Series 9', 'icon': 'fa-clock', 'qty': 2, 'amount': '₦620,000', 'status': 'Delivered'},
        ],
        'categories': [
            {'name': 'Smartphones', 'icon': 'fa-mobile-alt', 'color': '#ff6a00', 'count': 86},
            {'name': 'Laptops & PCs', 'icon': 'fa-laptop', 'color': '#007bff', 'count': 54},
            {'name': 'Audio & Headphones', 'icon': 'fa-headphones', 'color': '#28a745', 'count': 42},
            {'name': 'Tablets & iPads', 'icon': 'fa-tablet-alt', 'color': '#6f42c1', 'count': 28},
            {'name': 'Wearables', 'icon': 'fa-clock', 'color': '#dc3545', 'count': 35},
            {'name': 'TVs & Home Theater', 'icon': 'fa-tv', 'color': '#17a2b8', 'count': 22},
            {'name': 'Gaming', 'icon': 'fa-gamepad', 'color': '#e83e8c', 'count': 30},
            {'name': 'Accessories', 'icon': 'fa-plug', 'color': '#fd7e14', 'count': 45},
        ],
        'timeline': [
            {'year': 2019, 'desc': 'Double Zee founded as a small electronics stall in Kano market.'},
            {'year': 2021, 'desc': 'Expanded to online store — first 100 orders fulfilled.'},
            {'year': 2023, 'desc': 'Opened second showroom in Abuja. Team grew to 15 staff.'},
            {'year': 2025, 'desc': '1,000+ products listed. 2,800+ customers served nationwide.'},
        ],
        'owner_name': 'Ismail',
        'shop_name': 'Double Zee Electronics Shop',
    }
    return render(request, 'dashboard/index.html', context)
