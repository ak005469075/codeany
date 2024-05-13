from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from time import sleep

app = Application(backend="uia").connect(title_re="Inbox*")
dlg = app.top_window()
current_count = 0
remove = 2
while True:
        try:
                unread = dlg.InboxListBox
                items = unread.item_count()
                if items==1:
                        sleep(20)
                        continue
                if items != current_count:
                        for i in range(1,items-current_count-(remove-1)):
                                if "Yesterday" in unread.texts()[i][0]:
                                        remove = 3
                                        continue
                                unread[i].select()
                                message = dlg.child_window(auto_id="RootFocusControl", control_type="Document").Hyperlink.invoke()
                                sleep(45)
                                dlg.type_keys("{ENTER}")
                                unread[i].select()
                        current_count = items - remove
                sleep(20)
        except:
                pass
