## User data
Database attached contains information.

Passwords:

admin Moscow10

ivan 10

ksu 10

nata Moscow10



## Emails
For testing purposes I used 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Messages are printed to console.

For gettnig email messages:

1. Change in settings.py:
  * EMAIL_BACKEND - just comment out
  * EMAIL_HOST 
  * EMAIL_PORT 
  * EMAIL_HOST_USER 
  * EMAIL_HOST_PASSWORD 
  * SITE_URL 
2. Change emai(s) of user(s) to yours
