from models.alert import Alert
from dotenv import load_dotenv

load_dotenv() 

alerts = Alert.getAll()
for alert in alerts:
    alert.loadItemPrice()
    print("notifying...")
    alert.notifyIfPriceReached()
    
if not alerts:
    print("no alerts")