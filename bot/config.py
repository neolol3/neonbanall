import os

class Config:
    TELEGRAM_TOKEN=os.environ['5753023029:AAEUUDBCaFlqRqzHsTckm4wuMBhbuAEL-t4']
    TELEGRAM_APP_HASH=os.environ['80c20ae3166c904aa2137523564d46df']
    TELEGRAM_APP_ID=int(os.environ['14029604'])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
