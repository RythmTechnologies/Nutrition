echo "Pip Güncelleniyor..."
pip install --upgrade pip

echo "Requirements kuruluyor..."

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

echo "Tamamlandı"