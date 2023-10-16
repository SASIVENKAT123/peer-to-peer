from ._anvil_designer import FeedbackTemplate
from anvil import *

class Feedback(FeedbackTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("Feedback Submitted")
    


