import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('DJANGO_KEY')

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',                 # MUST be first
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]



EXTRA_APPS = [
    'core',
    'manager',
]


INSTALLED_APPS += EXTRA_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    # ====================
    # SITE BRANDING & THEME
    # ====================
    "site_title": "Mitho Chiya Dashboard",
    "site_header": "Mitho Chiya Admin",
    "site_brand": "Mitho Chiya ☕",
    "site_logo": "chiya/img/logo.png",
    "site_logo_classes": "img-circle shadow-sm",
    "site_icon": "chiya/img/favicon.ico",
    "login_logo": "chiya/img/logo-login.png",
    "login_logo_dark": "chiya/img/logo-dark.png",
    
    # Welcome message
    "welcome_sign": "Welcome to Mitho Chiya Management Portal",
    "copyright": "© 2024 Mitho Chiya Pvt. Ltd. All Rights Reserved",
    
    # ====================
    # THEME & COLOR SCHEME
    # ====================
    "theme": "lux",  # Options: flatly, darkly, lux, simplex, sandstone, materia
    "dark_mode_theme": "darkly",  # Dark mode theme
    
    # Color customization
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    
    # ====================
    # LAYOUT & NAVIGATION
    # ====================
    # Sidebar settings
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    
    # Order in sidebar
    "order_with_respect_to": [
        "auth",
        "auth.user",
        "auth.group",
        "chiya",
        "chiya.product",
        "chiya.order",
        "chiya.customer",
        "chiya.category",
        "chiya.review",
    ],
    
    # ====================
    # TOP MENU
    # ====================
    "topmenu_links": [
        # Dashboard
        {
            "name": "Dashboard",
            "url": "admin:index",
            "icon": "fas fa-tachometer-alt",
            "permissions": ["auth.view_user"]
        },
        
        # Quick Actions
        {
            "name": "Quick Orders",
            "url": "admin:chiya_order_add",
            "icon": "fas fa-bolt",
            "permissions": ["chiya.add_order"]
        },
        
        # External links
        {
            "name": "Live Store",
            "url": "https://mithochiya.com",
            "new_window": True,
            "icon": "fas fa-store"
        },
        {
            "name": "Analytics",
            "url": "https://analytics.mithochiya.com",
            "new_window": True,
            "icon": "fas fa-chart-line"
        },
        
        # Model dropdowns
        {"model": "auth.user"},
        {"app": "chiya"},
        
        # Support
        {
            "name": "Support",
            "url": "https://support.mithochiya.com",
            "new_window": True,
            "icon": "fas fa-headset"
        },
    ],
    
    # ====================
    # USER MENU
    # ====================
    "usermenu_links": [
        {
            "name": "Profile",
            "url": "admin:auth_user_change",
            "icon": "fas fa-user-edit",
            "permissions": ["auth.change_user"]
        },
        {
            "name": "Settings",
            "url": "admin:auth_user_changelist",
            "icon": "fas fa-cogs"
        },
        {
            "name": "Support",
            "url": "https://support.mithochiya.com",
            "new_window": True,
            "icon": "fas fa-question-circle"
        },
        {
            "name": "Documentation",
            "url": "/admin/docs/",
            "icon": "fas fa-book"
        },
        {"model": "auth.user"},
    ],
    
    # ====================
    # SIDEBAR CUSTOMIZATION
    # ====================
    "custom_links": {
        "chiya": [
            {
                "name": "Sales Dashboard",
                "url": "/admin/sales-dashboard/",
                "icon": "fas fa-chart-pie",
                "permissions": ["chiya.view_order"],
                "badge": {
                    "text": "Live",
                    "color": "success"
                }
            },
            {
                "name": "Customer Messages",
                "url": "admin:chiya_message_changelist",
                "icon": "fas fa-comments",
                "permissions": ["chiya.view_message"],
                "badge": {
                    "text": "New",
                    "color": "danger"
                }
            },
            {
                "name": "Inventory Report",
                "url": "/admin/inventory-report/",
                "icon": "fas fa-clipboard-list",
                "permissions": ["chiya.view_product"]
            },
            {
                "name": "Quick Add Product",
                "url": "admin:chiya_product_add",
                "icon": "fas fa-plus-circle",
                "permissions": ["chiya.add_product"]
            }
        ],
        "auth": [
            {
                "name": "User Activity",
                "url": "/admin/user-activity/",
                "icon": "fas fa-user-clock",
                "permissions": ["auth.view_user"]
            }
        ]
    },
    
    # ====================
    # ICONS
    # ====================
    "icons": {
        # Auth app
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-circle",
        "auth.group": "fas fa-users",
        
        # Chiya app
        "chiya": "fas fa-mug-hot",
        "chiya.product": "fas fa-coffee",
        "chiya.order": "fas fa-shopping-bag",
        "chiya.customer": "fas fa-user-tie",
        "chiya.category": "fas fa-tags",
        "chiya.review": "fas fa-star",
        "chiya.message": "fas fa-envelope",
        "chiya.payment": "fas fa-credit-card",
        "chiya.shipping": "fas fa-truck",
        
        # Common
        "sites": "fas fa-globe",
    },
    
    "default_icon_parents": "fas fa-chevron-right",
    "default_icon_children": "fas fa-circle-notch",
    
    # ====================
    # SEARCH & FILTERS
    # ====================
    "search_model": [
        "auth.User",
        "auth.Group",
        "chiya.Product",
        "chiya.Order",
        "chiya.Customer",
        "chiya.Category",
    ],
    
    "show_search_bar": True,
    "search_input_placeholder": "Search...",
    
    # ====================
    # UI COMPONENTS
    # ====================
    # Modal windows
    "related_modal_active": True,
    "modal_close_button": True,
    
    # Forms
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
        "chiya.product": "horizontal_tabs",
        "chiya.order": "collapsible",
    },
    
    # ====================
    # CUSTOMIZATION OPTIONS
    # ====================
    # Show UI builder for admin users
    "show_ui_builder": True,
    
    # Language
    "language_chooser": True,
    
    # ====================
    # CUSTOM CSS & JS
    # ====================
    "custom_css": "css/admin_custom.css",
    "custom_js": "js/admin_custom.js",
    
    # Use CDN for fonts
    "use_google_fonts_cdn": True,
    
    # ====================
    # PERFORMANCE & BEHAVIOR
    # ====================
    # Actions
    "actions_sticky_top": True,
    "actions_per_page": 25,
    
    # List view
    "list_per_page": 50,
    "list_max_show_all": 200,
    
    # Date formatting
    "date_format": "Y-m-d",
    "time_format": "H:i",
    "datetime_format": "Y-m-d H:i",
    
    # ====================
    # NOTIFICATIONS
    # ====================
    "show_notifications": True,
    
    # ====================
    # FOOTER
    # ====================
    "footer_text": "Mitho Chiya - Brewing Happiness Since 2024",
    
    # ====================
    # SECURITY & PERMISSIONS
    # ====================
    "user_avatar": "chiya/img/default-avatar.png",
    
    # ====================
    # MISC
    # ====================
    # Collapse sidebar groups
    "collapse_navigation": False,
    
    # Recent actions
    "show_recent_actions": True,
    "recent_actions_limit": 10,
}

# Jazzmin UI Tweaks for enhanced appearance
JAZZMIN_UI_TWEAKS = {
    # Theme variations
    "theme": "lux",
    "dark_mode_theme": "darkly",
    
    # Navbar variations
    "navbar": "navbar-dark navbar-primary",
    "navbar_fixed": True,
    "footer_fixed": False,
    "sidebar_fixed": True,
    
    # Layout variations
    "layout": "sidebar-mini",
    
    # Brand styling
    "brand_colour": "navbar-primary",
    
    # Button variations
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    
    # Sidebar variations
    "accent": "accent-primary",
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_child_indent": True,
    "sidebar_nav_flat_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_compact_style": False,
    
    # Background variations
    "body_small_text": False,
    "brand_small_text": False,
    "navbar_small_text": False,
    "footer_small_text": False,
    "sidebar_small_text": False,
    
    # Color schemes
    "navbar_style": "navbar-dark",
    "sidebar_style": "sidebar-dark-primary",
    
    # Card variations
    "card": "card-outline",
    "card_header": True,
    "card_background": False,
    
    # Progress bars
    "progress_small_height": False,
    
    # Breadcrumbs
    "breadcrumbs": True,
    "breadcrumbs_separator": "/",
    
    # Misc
    "no_navbar_border": False,
    "no_border": False,
}

# Additional admin site customization
ADMIN_SITE_HEADER = "Mitho Chiya Administration"
ADMIN_SITE_TITLE = "Mitho Chiya Admin Portal"
ADMIN_INDEX_TITLE = "Dashboard Overview"