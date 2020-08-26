export ENV='production'

echo '########################'
echo 'install host machine requirements.'
echo '########################'
sudo apt-get -y install pipenv
sudo apt-get -y install nginx

echo '########################'
echo 'prepare source code'
echo '########################'
sudo git pull origin

echo '########################'
echo 'install dependencies from Pipfile'
echo '########################'

pipenv install

echo '########################'
echo 'collect static'
echo '########################'
pipenv run python manage.py collectstatic --noinput



echo '########################'
echo 'migrate database'
echo '########################'
pipenv run python manage.py migrate


echo '########################'
echo 'gunicorn service setting & nginx setting'
echo '########################'
sudo cp ./gunicorn.service /etc/systemd/system/gunicorn.service
sudo cp ./nginx.conf /etc/nginx/sites-enabled/nginx.conf

echo '########################'
echo 'start server'
echo '########################'
sudo systemctl daemon-reload
sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl status nginx
sudo systemctl status gunicorn



