
# UTC, UTC+2 Ajan näyttäjä rasberry pi 3b+ käyttäen lcd1602 moduulia
# Tekijä: Miko Savolainen
# Vuosi: 2022

import datetime

from rpi_lcd import LCD
lcd = LCD()

while True:

    utc_time = datetime.datetime.utcnow()
    cet_time = utc_time + datetime.timedelta(hours=2)

    lcd.text(utc_time.strftime("UTC aika: %H:%M:%S"), 1)
    lcd.text(cet_time.strftime("FIN aika: %H:%M:%S"), 2)
    

    