import sys
import os
sys.path.insert(0,os.path.join(os.path.dirname(__file__)))
from algebra742live import create_app 
application = create_app()

