# core/views.py
from django.shortcuts import render

def home(request):
    # Step 1: build a Python list of “service” objects (as simple dicts)
    services = [
        {
            # You can either use an external URL or reference {% static %} in the template.
            # Here we’re using full URLs for simplicity:
            "image_url": "https://ooni.com/cdn/shop/articles/20220211142347-margherita-9920_ba86be55-674e-4f35-8094-2067ab41a671.jpg",
            "name": "Classic Margherita Pizza",
            "description": "A timeless favorite with fresh mozzarella, basil leaves, and our signature tomato sauce.",
            "price": "$12.99"
        },
        {
            "image_url": "https://www.kitchensanctuary.com/wp-content/uploads/2021/05/Double-Cheeseburger-square-FS-42.jpg",
            "name": "Double Beef Burger",
            "description": "Two layers of 100% Angus beef, cheddar cheese, lettuce, tomato, and our secret sauce.",
            "price": "$10.49"
        },
        {
            "image_url": "https://thedefineddish.com/wp-content/uploads/2023/05/1L8A3824.jpg",
            "name": "Creamy Alfredo Pasta",
            "description": "Fettuccine tossed in a rich garlic‐parmesan cream sauce, topped with parsley.",
            "price": "$11.25"
        },
    ]

    # Step 2: pass that list into the template context
    return render(request, 'core/home.html', {
        'services': services
    })
    
def menu(request):
    services = [
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Spicy Pepperoni Pizza",
            "description": "Loaded with spicy pepperoni, mozzarella, and a zesty tomato sauce.",
            "price": "$13.99"
        },
        {
            "image_url": "https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg",
            "name": "Grilled Chicken Sandwich",
            "description": "Juicy grilled chicken breast, lettuce, tomato, and mayo on a toasted bun.",
            "price": "$9.99"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Veggie Delight Pizza",
            "description": "A medley of bell peppers, onions, olives, and mushrooms on a crispy crust.",
            "price": "$12.49"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "BBQ Chicken Pizza",
            "description": "Tangy BBQ sauce, grilled chicken, red onions, and cilantro.",
            "price": "$14.25"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Classic Caesar Salad",
            "description": "Crisp romaine, parmesan, croutons, and creamy Caesar dressing.",
            "price": "$7.50"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Garlic Breadsticks",
            "description": "Freshly baked breadsticks brushed with garlic butter and herbs.",
            "price": "$4.99"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Buffalo Wings",
            "description": "Spicy buffalo wings served with ranch or blue cheese dip.",
            "price": "$8.99"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Mushroom Risotto",
            "description": "Creamy risotto with sautéed mushrooms and parmesan cheese.",
            "price": "$11.75"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Tiramisu",
            "description": "Classic Italian dessert with espresso-soaked ladyfingers and mascarpone cream.",
            "price": "$6.50"
        },
        {
            "image_url": "https://images.pexels.com/photos/461382/pexels-photo-461382.jpeg",
            "name": "Lemonade",
            "description": "Freshly squeezed lemonade served over ice.",
            "price": "$2.99"
        },
    ]
    return render(request, 'core/menu.html', {
        'services': services
    })   
     
def reservation(request):
    return render(request, 'core/reservation.html')

def tracking(request):
    # Hard-coded order data
    order = {
        "id": "123456",
        "restaurant_name": "Khana Khazana",
        "eta": "30 minutes",
        "delivery_address": "123 Main Street, Karachi",
        "contact_number": "+92 300 1234567",
        "status": "Out for Delivery",  # <-- current status
    }

    # Define the full sequence of statuses (in the exact order you want them displayed)
    STATUS_SEQUENCE = [
        "Order Placed",
        "Preparing",
        "Out for Delivery",
        "Delivered",
    ]

    # Determine which steps should be marked as completed
    try:
        current_index = STATUS_SEQUENCE.index(order["status"])
    except ValueError:
        current_index = 0

    steps = []
    for idx, label in enumerate(STATUS_SEQUENCE):
        steps.append({
            "label": label,
            "completed": (idx <= current_index)
        })

    context = {
        "order": order,
        "steps": steps,
    }
    return render(request, "core/tracking.html", context)

def contact(request):
    return render(request, 'core/contact.html')
