def Add():
  TestedApps.Orders.Run()
  for i in range(10):
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    Aliases.Orders.OrderForm.Group.Customer.Click()
    Aliases.Orders.OrderForm.Group.Customer.set_Text("customer")
    Aliases.Orders.OrderForm.Group.Street.Click()
    Aliases.Orders.OrderForm.Group.Street.SetText("street")
    Aliases.Orders.OrderForm.Group.State.Click()
    Aliases.Orders.OrderForm.Group.state.SetText("ap")
    Aliases.Orders.OrderForm.Group.city1.Click()
    Aliases.Orders.OrderForm.Group.city1.SetText("hyd")
    Aliases.Orders.OrderForm.Group.Zip.Click()
    Aliases.Orders.OrderForm.Group.Zip.SetText("776556")
    Aliases.Orders.OrderForm.Group.CardNo.Click()
    Aliases.Orders.OrderForm.Group.CardNo.SetText("7657765")
    Aliases.Orders.OrderForm.ButtonOK.Click()
def edit():
  for i in range(10):
          if(i%2==0):
            Aliases.Orders.MainForm.Ordersview.Clickitem(i)
            Aliases.Orders.MainForm.MainMenu.Click("Orders|edit order...")
            Aliases.Orders.OrderForm.Group.Customer.Click()
            Aliases.Orders.OrderForm.Group.Customer.set_Text("sonia")
            Aliases.Orders.OrderForm.ButtonOK.Click()
           
def Delete():
  for i in range(5):
            if(i%2==1):
             Aliases.Orders.MainForm.Ordersview.Clickitem(i)
             Aliases.Orders.MainForm.MainMenu.Click("Orders|Delete order")
             Aliases.Orders.dlgConfirmation.btnYes.ClickButton()
  Aliases.Orders.MainForm.Close()
  Aliases.Orders.dlgConfirmation.btnNo.Click()