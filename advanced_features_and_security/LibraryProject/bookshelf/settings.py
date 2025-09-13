INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # main app containing CustomUser and Book model
]

# Use custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'


# ===========================
# Security Settings
# ===========================

# Prevent cross-site scripting (XSS)
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking by disallowing iframes
X_FRAME_OPTIONS = "DENY"

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Force cookies to be sent only over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
