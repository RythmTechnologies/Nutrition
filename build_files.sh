echo "Pip Güncelleniyor..."
pip install --upgrade pip

echo "Requirements kuruluyor..."

pip install -r requirements.txt
python manage.py collectstatic --clear --noinput


echo "Tamamlandı"