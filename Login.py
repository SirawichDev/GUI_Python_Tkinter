from appJar import gui

app = gui()

def exit_button(button):
    if button == "Cancel":
        app.stop()
    elif button == "Check":
        Checker()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("Username",usr,"Password:",pwd,"Secret_keys",Checker())


def Checker():
    sec_keys = app.getEntry("v1")
    if sec_keys == '1559':
        app.setEntryValid("v1")
        return sec_keys




app.addLabel("title","Admin Login")
app.setLabelBg("title","yellow")
app.addLabelEntry("Username")
app.addValidationEntry("v1")
app.setEntryDefault("v1","Secret Keys")
app.setEntryDefault("Username","Email")
app.addLabelSecretEntry("Password")
app.addButtons(["Submit","Check","Cancel"],exit_button)


app.go()
