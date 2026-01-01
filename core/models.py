from django.db import models


# ---------------------------
# CONSTANTS / CHOICES
# ---------------------------

MOBILE_NUMBER_CODE = (
    ('+977', '+977'),  # Nepal
    ('+91', '+91'),
    ('+92', '+92'),
)

FOOD_ITEM_CATEGORY = (
    ('veg', 'Veg'),
    ('non_veg', 'Non Veg'),
    ('drinks', 'Drinks'),
    ('snacks', 'Snacks'),
    ('desserts', 'Desserts'),
    ('beverage', 'Beverage'),
)



ORDER_STATUS = (
    ('pending', 'Pending'),
    ('preparing', 'Preparing'),
    ('served', 'Served'),
    ('paid', 'Paid'),
)


# ---------------------------
# BASE MODEL
# ---------------------------

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ---------------------------
# CUSTOMER (OPTIONAL)
# ---------------------------

class Customer(TimeStampModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_code = models.CharField(
        max_length=5, choices=MOBILE_NUMBER_CODE, default='+977'
    )
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ---------------------------
# TABLE MODEL
# ---------------------------

class Table(TimeStampModel):
    table_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"Table {self.table_number}"


# ---------------------------
# MENU / FOOD ITEM
# ---------------------------

class MenuItem(TimeStampModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=FOOD_ITEM_CATEGORY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_items/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# ---------------------------
# ORDER
# ---------------------------

class Order(TimeStampModel):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default='pending'
    )

    def __str__(self):
        return f"Order #{self.id}"


# ---------------------------
# ORDER ITEM (ORDER ↔ MENU)
# ---------------------------

class OrderItem(TimeStampModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items'
    )
    item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"


# ---------------------------
# PAYMENT
# ---------------------------

class Payment(TimeStampModel):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    payment_method = models.CharField(
        max_length=20,
        choices=(('cash', 'Cash'), ('qr', 'QR'), ('card', 'Card')),
        default='cash'
    )
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"


# ---------------------------
# FEEDBACK
# ---------------------------

class Feedback(TimeStampModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Feedback for Order #{self.order.id}"
