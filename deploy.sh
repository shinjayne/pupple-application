sudo git pull origin
sudo apt-get -y install pipenv
#sudo apt-get -y install nginx
pipenv shell
pipenv install
python manage.py collectstatic
sudo cp ./gunicorn.service /etc/systemd/system/gunicorn.service
sudo cp ./nginx.conf /etc/nginx/sites-enabled/nginx.conf



