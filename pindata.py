import os
from peewee import *
from termcolor import colored

# path to you database, default is current folder
DB_PATH = 'pindata.db'

db = SqliteDatabase( DB_PATH )

class BaseModel( Model ):
  """Base model class for this application that all model will extend from"""
  class Meta:
    database = db

class Pin( BaseModel ):
  """Pin model"""
  number      = IntegerField()
  about       = CharField()
  assigned    = BooleanField()
  description = CharField( null=True )

  def reset( self ):
    self.assigned = False;
    description = None;
    self.save()

  @staticmethod
  def populate():
    Pin.create( number=1,   assigned=False,  about='+3.3v' )
    Pin.create( number=2,   assigned=False,  about='+5v' )
    Pin.create( number=3,   assigned=False,  about='GPIO 0' )
    Pin.create( number=4,   assigned=False,  about='+5v' )
    Pin.create( number=5,   assigned=False,  about='GPIO 1' )
    Pin.create( number=6,   assigned=False,  about='GND' )
    Pin.create( number=7,   assigned=False,  about='GPIO 4 1-wire' )
    Pin.create( number=8,   assigned=False,  about='GPIO 14 UART0_TXD' )
    Pin.create( number=9,   assigned=False,  about='GND' )
    Pin.create( number=10,  assigned=False,  about='GPIO 15 UART0_RXD' )
    Pin.create( number=11,  assigned=False,  about='GPIO 17' )
    Pin.create( number=12,  assigned=False,  about='GPIO 18 PCM_CLK' )
    Pin.create( number=13,  assigned=False,  about='GPIO 21' )
    Pin.create( number=14,  assigned=False,  about='GND' )
    Pin.create( number=15,  assigned=False,  about='GPIO 22' )
    Pin.create( number=16,  assigned=False,  about='GPIO 23' )
    Pin.create( number=17,  assigned=False,  about='GPIO +3.3v' )
    Pin.create( number=18,  assigned=False,  about='GPIO 24' )
    Pin.create( number=19,  assigned=False,  about='GPIO 10 SPI0_MOSI' )
    Pin.create( number=20,  assigned=False,  about='GND' )
    Pin.create( number=21,  assigned=False,  about='GPIO 9 SPI0_MISO' )
    Pin.create( number=22,  assigned=False,  about='GPIO 25' )
    Pin.create( number=23,  assigned=False,  about='GPIO 11 SPI0SCLK' )
    Pin.create( number=24,  assigned=False,  about='GPIO 8 SPI_CE0_N' )
    Pin.create( number=25,  assigned=False,  about='GND' )
    Pin.create( number=26,  assigned=False,  about='GPIO 7 SPI0_CE1_N' )

# connect to our database
db.connect()

# create the tables and populate with defalut data
if not Pin.table_exists():
  Pin.create_table()
  Pin.populate()

while True:
  os.system( 'clear' )
  pins = Pin.select()

  # header
  print( colored( '%-5s %-25s %-10s %-30s' % ( 'Pin', 'About', 'Assigned?', 'Description' ), attrs=['bold'] ) )
  print '-----------------------------------------------------------'
  
  for pin in pins:
    assigned = 'Y' if pin.assigned else 'N'
    description = '' if pin.description is None else pin.description
    text = '%-5s %-25s %-10s %-30s' % ( pin.number, pin.about, assigned, description )
    if pin.assigned:
      text = colored( text, 'red' )    
    
    print( text )

  number_of_used_pins = pins.where( Pin.assigned == True ).count()
  print 'Pin(s) currently in use: %d' % number_of_used_pins

  pin_number = int( raw_input( 'Modify Pin: ') )
  selected_pin = Pin.get( Pin.number == pin_number )

  command = raw_input( '>>  ' )
  if command == 'update':
    selected_pin.description = raw_input( 'Description: ')
    selected_pin.assigned = True
    selected_pin.save()

  if command == 'reset':
    selected_pin.reset();

  if command == 'exit':
    break;















