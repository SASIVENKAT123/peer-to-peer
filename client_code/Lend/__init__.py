from ._anvil_designer import LendTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lend(LendTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("signup")

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("login")



