echo "Pip Güncelleniyor"
pip install --upgrade pip

echo "requirements kuruluyor..."
pip install -r requirements.txt

echo "Statik dosyalar toplanıyor..."
py manage.py collectstatic 

echo "Tamamlandı"