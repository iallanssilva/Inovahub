Inovahub
Landing Page

1. Lembrar de incluir o arquivo .env, seguindo o exemplo e alterando as permissões para não deixar o novo arquivo exposto e vazar informações sensíveis. 

SECRET_KEY=
DEBUG=
ALLOWED_HOST=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

2. Para HTTPS lembrar de retirar os comentários nas seguintes linhas settings.py:

MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
    ...

 HTTPS Settings
 SESSION_COOKIE_SECURE = True
 CSRF_COOKIE_SECURE = True
 SECURE_SSL_REDIRECT = True

 HSTS Settings
 SECURE_HSTS_SECONDS = 31536000  # 1 year
 SECURE_HSTS_PRELOAD = True
 SECURE_HSTS_INCLUDE_SUBDOMAINS = True

3. Lembre-se de servir os arquivos de mídia diretamente no seu servidor. 
