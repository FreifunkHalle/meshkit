from gluon.storage import Storage
settings = Storage()

settings.migrate = True
# use fake_migrate to repair broken tables
settings.fake_migrate = False
settings.title = 'Meshkit'
settings.subtitle = 'Freifunk Halle OpenWrt Imagebuilder'
settings.author = 'soma'
settings.author_email = 'freifunk@somakoma.de'
settings.keywords = 'Freifunk,Mesh,Wireless,Wifi,OpenWrt,Imagebuilder'
settings.description = 'This imagebuilder will build firmware images for Freifunk or similar wireless mesh networks. The firmware images are preconfigured and ready to mesh out of the box.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'c50bdbb8-ada2-4398-80da-c00f555acdde'
settings.email_server = 'mail.3dfxatwork.de'
settings.email_sender = 'meshkit@freifunk-halle.net'
settings.email_tls = True
settings.email_login = 'AUTH PLAIN bWVzaGtpdC1oYWxsZS5uZXQAbWVzaGtpdC1oYWxsZS5uZXQ7RzNta080eWlMVHdFOTZRSldF'
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []

response.title = settings.title
response.subtitle = settings.subtitle
import os
headerstream = os.popen("php /var/www/vhosts/ff-backup/htdocs/header.php").read()
footerstream = os.popen("php /var/www/vhosts/ff-backup/htdocs/footer.html").read()
