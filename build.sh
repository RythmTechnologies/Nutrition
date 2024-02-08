echo "Pip Güncelleniyor..."
pip install --upgrade pip

echo "Requirements kuruluyor..."
pip install -r requirements.txt

echo "Statik dosyalar toplanıyor..."
python manage.py collectstatic --noinput

echo "Tamamlandı"