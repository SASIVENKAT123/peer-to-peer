from ._anvil_designer import Form8Template
from anvil import *

class Form8(Form8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
