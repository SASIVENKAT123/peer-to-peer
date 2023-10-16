from ._anvil_designer import Form9Template
from anvil import *

class Form9(Form9Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
