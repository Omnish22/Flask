from models.alert import Alert

alerts = Alert.getAll()
for alert in alerts:
    alert.loadItemPrice()
    alert.notifyIfPriceReached()
    
if not alerts:
    print("no alerts")