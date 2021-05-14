web: gunicorn shorturls.wsgi --log-file -
worker: python main/management/commands/bot.py $PORT
