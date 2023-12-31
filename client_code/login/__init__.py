from ._anvil_designer import loginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class login(loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")

  def primary_color_1_click(self, **event_args):
    
    """This method is called when the button is clicked"""
    email=self.text_box_1.text
    password=self.text_box_2.text
    anvil.server.call('add_login',email,password)
    
    alert("You have logged in successfully")
def form_show(self, **event_args):
    # Scroll button1 into view
  self.primary_color_1_click().scroll_into_view()
    

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass



