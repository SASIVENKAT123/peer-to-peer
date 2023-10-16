from ._anvil_designer import Form1Template

from anvil import *



class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)



    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("login")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Borrow")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Lend")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("FAQ")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Feedback")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Chat")

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("signup")







