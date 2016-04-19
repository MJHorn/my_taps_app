echo 'yes' | python manage.py flush
python manage.py stylestodb
python manage.py barstodb
python manage.py tapstodb
git add -A .
git commit -m "automated db update"
git push
