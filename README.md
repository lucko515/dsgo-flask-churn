# DSGo - Churn prediction Flask app

This is the main repository for Flask Churn prediction application implemented for workshop "Building data products".

## Installation

### Installation all dependencies with `pip`

```bash
pip install -r requirements.txt
```

### Deploy Flask Server steps

1. Install apache
`sudo apt-get install apache2`

2. Install Wsgi 
- Python 2
`sudo apt-get install libapache2-mod-wsgi`
- Python 3
`sudo apt-get install libapache2-mod-wsgi-py3`

3. Activate Wsgi
`sudo a2enmod wsgi`



4. Go to site directory of Apacghe 2

`cd /var/www/`

5. Clone this repo

`git clone https://github.com/lucko515/dsgo-flask-churn`

6. Rename the folder to ChurnApp

`mv dsgo-flask-churn ChurnApp`

7. Update/Upgrade packages
`sudo apt-get update`
`sudo apt-get upgrade`

8. Install pip
- Python 2
`apt-get install python-pip`
- Python 3
`apt-get install python3-pip`

9. Install depen for this project 
NOTE: __change dir to ChurnApp before executing this command__

`pip install -r requirements.txt`


10. Create ChurnApp apache site config
`nano /etc/apache2/sites-available/ChurnApp.conf`

11. Copy this to the file:
```
<VirtualHost *:80>
                ServerName your_IP_address
                ServerAdmin test_email@email.com
                WSGIScriptAlias / /var/www/ChurnApp/churnapp.wsgi
                <Directory /var/www/ChurnApp/ChurnApp/>
                        Order allow,deny
                        Allow from all
                </Directory>
                Alias /static /var/www/ChurnApp/ChurnApp/static
                <Directory /var/www/ChurnApp/ChurnApp/static/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

12. Activate the ChurnApp
`sudo a2ensite ChurnApp`

13. Restart apache2 
`service apache2 reload`
`service apache2 restart`

## Contact

Add me on [LinkedIn](https://www.linkedin.com/in/luka-anicin/).



