If you have these codes do not add!!!!!!!!!!!!!



0.1 Search : 

[...]
	def __init__(self, eventMinimize, eventClose):
		ui.ScriptWindow.__init__(self)
		self.targetName = ""
		self.eventMinimize = eventMinimize
		self.eventClose = eventClose
		self.eventAcceptTarget = None


0.1.1 Add Below : 

[...]
		if app.ENABLE_RUN_MOUSE_WHEEL:
			self.onRunMouseWheelEvent = None



0.2 Search : 


if "__main__" == __name__:


0.2.1

[...]

	if app.ENABLE_RUN_MOUSE_WHEEL:
		def OnRunMouseWheel(self, nLen):
			if nLen > 0:
				self.scrollBar.OnUp()
			else:
				self.scrollBar.OnDown()

		def SetOnRunMouseWheelEvent(self, event):
			self.onRunMouseWheelEvent = __mem_func__(event)

[...]





