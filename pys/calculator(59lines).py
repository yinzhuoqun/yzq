import wx

class CalculatorFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1, '计算器', size=(500,600))
        self.SetMaxSize((500,600))
        self.SetMinSize((500,600))
        self.panel = wx.Panel(self,-1)
        self.init_monitor()
        self.init_buttons()
        
    def gen_callback(self,char):
        def callback(event,text=char):
            if text in '()1234567890+-*/.':
                self.monitor_ctrl.WriteText(text)
            elif text =='DEL':
                value = self.monitor_ctrl.GetValue()
                self.monitor_ctrl.SetValue(value[:-1])
            elif text =='C':
                self.monitor_ctrl.SetValue('0')
            elif text =='=':
                value = self.monitor_ctrl.GetValue()
                try:
                    v = eval(value)
                    self.monitor_ctrl.SetValue(value+'\n='+str(v))
                except:
                    self.monitor_ctrl.SetValue(value+'\nError!')
        return callback

    def init_monitor(self):
        self.monitor_ctrl = wx.TextCtrl(self.panel,style=wx.TE_MULTILINE,size=(500,100))
        self.monitor_ctrl.SetEditable(False)
        self.monitor_ctrl.SetCanFocus(False)
        self.monitor_box = wx.BoxSizer(wx.VERTICAL)
        self.monitor_box.Add(self.monitor_ctrl,proportion=1,flag = wx.EXPAND | wx.LEFT|wx.RIGHT)

    def init_buttons(self):
        self.buttons=[]
        for c in list('()')+['DEL']+list('C123*456/789-.0+='):
            button = wx.Button(self.panel, -1, c, size=(125,80),name=c)
            button.Bind(wx.EVT_BUTTON, self.gen_callback(c))
            self.buttons.append(button)
        button_box = wx.BoxSizer(orient = wx.VERTICAL)
        button_box.Add(self.monitor_box,proportion=0,flag = wx.EXPAND | wx.LEFT|wx.RIGHT)
        buttons = None
        for i in range(len(self.buttons)):
            if i % 4==0:
                if buttons:button_box.Add(buttons,proportion=1,flag = wx.EXPAND | wx.ALL)
                buttons = wx.BoxSizer(orient = wx.HORIZONTAL)
            button = self.buttons[i]
            buttons.Add(button,proportion=0,flag = wx.EXPAND )
        button_box.Add(buttons,proportion=1,flag = wx.EXPAND | wx.ALL)
        self.panel.SetSizer(button_box)


app = wx.App()
frame = CalculatorFrame()
frame.Show()
app.MainLoop()