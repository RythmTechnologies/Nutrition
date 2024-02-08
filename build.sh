echo "Pip Güncelleniyor..."
pip install --upgrade pip

echo "Requirements kuruluyor..."
pip install -r requirements.txt

echo "Statik dosyalar toplanıyor..."
python3.9 manage.py collectstatic

echo "Tamamlandı"