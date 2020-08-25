# install host machine requirements.
sudo apt-get -y install pipenv
sudo apt-get -y install nginx
pip install gunicorn

# prepare source code
sudo git pull origin

# get into python virtual environment
pipenv shell

# install dependencies from Pipfile
pipenv install
# collect static
python manage.py collectstatic
# gunicorn setting & nginx setting
sudo cp ./gunicorn.service /etc/systemd/system/gunicorn.service
sudo cp ./nginx.conf /etc/nginx/sites-enabled/nginx.conf



