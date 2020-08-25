echo '########################'
echo 'install host machine requirements.'
echo '########################'
sudo apt-get -y install pipenv
sudo apt-get -y install nginx
pip install gunicorn

echo '########################'
echo 'prepare source code'
echo '########################'
sudo git pull origin

echo '########################'
echo 'get into python virtual environment'
echo '########################'
pipenv shell

echo '########################'
echo 'install dependencies from Pipfile'
echo '########################'

pipenv install

echo '########################'
echo 'collect static'
echo '########################'
python manage.py collectstatic

echo '########################'
echo 'gunicorn setting & nginx setting'
echo '########################'
sudo cp ./gunicorn.service /etc/systemd/system/gunicorn.service
sudo cp ./nginx.conf /etc/nginx/sites-enabled/nginx.conf


