import sqlite3
import os
db = sqlite3.connect ('pindata.db')
curs = db.cursor()
x = curs.execute
def createtable():
    curs.execute ('CREATE TABLE pindata (id INTEGER PRIMARY KEY, pin INT, assign TEXT, intended TEXT)')

def generatepins():
    x ('DELETE FROM pindata')
    x ('INSERT INTO pindata (pin) VALUES ("1")')
    x ('INSERT INTO pindata (pin) VALUES ("2")')
    x ('INSERT INTO pindata (pin) VALUES ("3")')
    x ('INSERT INTO pindata (pin) VALUES ("4")')
    x ('INSERT INTO pindata (pin) VALUES ("5")')
    x ('INSERT INTO pindata (pin) VALUES ("6")')
    x ('INSERT INTO pindata (pin) VALUES ("7")')
    x ('INSERT INTO pindata (pin) VALUES ("8")')
    x ('INSERT INTO pindata (pin) VALUES ("9")')
    x ('INSERT INTO pindata (pin) VALUES ("10")')
    x ('INSERT INTO pindata (pin) VALUES ("11")')
    x ('INSERT INTO pindata (pin) VALUES ("12")')
    x ('INSERT INTO pindata (pin) VALUES ("13")')
    x ('INSERT INTO pindata (pin) VALUES ("14")')
    x ('INSERT INTO pindata (pin) VALUES ("15")')
    x ('INSERT INTO pindata (pin) VALUES ("16")')
    x ('INSERT INTO pindata (pin) VALUES ("17")')
    x ('INSERT INTO pindata (pin) VALUES ("18")')
    x ('INSERT INTO pindata (pin) VALUES ("19")')
    x ('INSERT INTO pindata (pin) VALUES ("20")')
    x ('INSERT INTO pindata (pin) VALUES ("21")')
    x ('INSERT INTO pindata (pin) VALUES ("22")')
    x ('INSERT INTO pindata (pin) VALUES ("23")')
    x ('INSERT INTO pindata (pin) VALUES ("24")')
    x ('INSERT INTO pindata (pin) VALUES ("25")')
    x ('INSERT INTO pindata (pin) VALUES ("26")')
    x ('UPDATE pindata SET intended="+3.3v" WHERE pin="1"')
    x ('UPDATE pindata SET intended="+5v" WHERE pin="2"')
    x ('UPDATE pindata SET intended="GPIO 0" WHERE pin="3"')
    x ('UPDATE pindata SET intended="+5V" WHERE pin="4"')
    x ('UPDATE pindata SET intended="GPIO 1" WHERE pin="5"')
    x ('UPDATE pindata SET intended="GND" WHERE pin="6"')
    x ('UPDATE pindata SET intended="GPIO 4 1-wire" WHERE pin="7"')
    x ('UPDATE pindata SET intended="GPIO 14 UART0_TXD" WHERE pin="8"')
    x ('UPDATE pindata SET intended="GND" WHERE pin="9"')
    x ('UPDATE pindata SET intended="GPIO 15 UART0_RXD" WHERE pin="10"')
    x ('UPDATE pindata SET intended="GPIO 17" WHERE pin="11"')
    x ('UPDATE pindata SET intended="GPIO 18 PCM_CLK" WHERE pin="12"')
    x ('UPDATE pindata SET intended="GPIO 21" WHERE pin="13"')
    x ('UPDATE pindata SET intended="GND" WHERE pin="14"')
    x ('UPDATE pindata SET intended="GPIO 22" WHERE pin="15"')
    x ('UPDATE pindata SET intended="GPIO 23" WHERE pin="16"')
    x ('UPDATE pindata SET intended="GPIO +3.3v" WHERE pin="17"')
    x ('UPDATE pindata SET intended="GPIO 24" WHERE pin="18"')
    x ('UPDATE pindata SET intended="GPIO 10 SPI0_MOSI" WHERE pin="19"')
    x ('UPDATE pindata SET intended="GND" WHERE pin="20"')
    x ('UPDATE pindata SET intended="GPIO 9 SPI0_MISO" WHERE pin="21"')
    x ('UPDATE pindata SET intended="GPIO 25" WHERE pin="22"')
    x ('UPDATE pindata SET intended="GPIO 11 SPI0SCLK" WHERE pin="23"')
    x ('UPDATE pindata SET intended="GPIO 8 SPI_CE0_N" WHERE pin="24"')
    x ('UPDATE pindata SET intended="GND" WHERE pin="25"')
    x ('UPDATE pindata SET intended="GPIO 7 SPI0_CE1_N" WHERE pin="26"')
    db.commit()

try:
    createtable()
except:
    print ("Already Created")

check = 'SELECT COUNT(id) FROM pindata'
query = x (check)
result = query.fetchone()
check = result[0]
if check < 1:
    generatepins()




true = 1
while true:
    os.system("clear")
    x ('select * from pindata')
    result = curs.fetchall()
    print '%-5s %-30s %-20s' % ("Pin","Description","Default")
    print '-----------------------------------------------------------'
    for i in result:
        print '%-5s %-30s %-20s %1s' % (i[1],i[2],i[3],i[1])
    print ("")
    result = x ('SELECT COUNT(assign) FROM pindata')
    result = curs.fetchone()
    print result[0], ("Pin(s) currently in use")
    print ("")
    print ("type in (exit) to quit.")
    selectpin = raw_input("Modify Pin:")
    if selectpin == ("exit"):
        exit()
    print ("(update) or (delete)")
    do = raw_input("Do:")
    if do == ("update"):
        pindetail = raw_input("Description:")
        result = x ('UPDATE pindata SET assign=? WHERE pin=?', [pindetail, selectpin])
        db.commit()

    if do == ("delete"):
        result = x ('UPDATE pindata SET assign=NULL WHERE pin=?', [selectpin])
        db.commit()

    if do == ("exit"):
        exit()















