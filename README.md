# Hadhramout's Comp Sci Faculty Website
> Work in progress, stay tuned for now






## Deployment (Apache)
### HTTP.CONF
```md
LoadFile "C:/Users/asus/AppData/Local/Programs/Python/Python39/python39.dll"
LoadModule wsgi_module "c:/users/asus/coding/projects/hu-compfa/env/lib/site-packages/mod_wsgi/server/mod_wsgi.cp39-win_amd64.pyd"
WSGIPythonHome "c:/users/asus/coding/projects/hu-compfa/env"
```
### HTTP-VHOSTS.CONF
```md
# virtual SupervisionTool
<VirtualHost *:80>
    ServerName localhost 

    ServerAlias localhost

    WSGIScriptAlias /  "path\to\wsgi_windows.py" application-group=%{GLOBAL}

    ErrorLog "logs/website_for_collage.error.log"
    CustomLog "logs/website_for_collage.access.log" combined
    
    <Directory "path\to\college">
        <Files wsgi_windows.py>
            Require all granted
        </Files>
    </Directory>

    Alias /static "path/to/static"
    <Directory "C:/Users/asus/Coding/Projects/hu-compfa/website/static">
        Require all granted
    </Directory>

    Alias /media "path/to/media"
    <Directory "C:/Users/asus/Coding/Projects/hu-compfa/media">
        Require all granted
    </Directory>
</VirtualHost>
# end virtual SupervisionTool```

## Developed By
Mohammed Al Attas [(@dev_muh)](https://twitter.com/dev_muh)
## Maintained By
Abdullah Binsaad [(iiAbady)](https://github.com/iiAbady)