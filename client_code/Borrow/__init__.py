from ._anvil_designer import BorrowTemplate
from anvil import *

class Borrow(BorrowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("login")

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("signup")



