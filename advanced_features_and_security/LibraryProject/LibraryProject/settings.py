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


DEBUG = True   # ⚠️ For development only, set to False in production

ALLOWED_HOSTS = []  # Add your domain or server IP when deploying


# Prevent cross-site scripting (XSS)
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking by disallowing iframes
X_FRAME_OPTIONS = "DENY"

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Force cookies to be sent only over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ===========================
# HTTPS / Security Settings
# ===========================

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Instructs browsers to only use HTTPS for the next 1 year (in seconds)
SECURE_HSTS_SECONDS = 31536000  # 1 year

# Apply HSTS to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow your site to be preloaded into browser HSTS lists
SECURE_HSTS_PRELOAD = True

# Prevent cross-site scripting (XSS) by enabling the browser filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Prevent clickjacking by denying framing
X_FRAME_OPTIONS = "DENY"

# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ===========================
# Detect HTTPS behind a proxy/load balancer
# ===========================

# Tell Django to trust the X-Forwarded-Proto header from the proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




