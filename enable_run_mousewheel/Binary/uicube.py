If you have these codes do not add!!!


0.1 Search : 

[...]
if __name__ == "__main__":
[...]

0.1.1 Add ABOVE : 

[...]
	if app.ENABLE_RUN_MOUSE_WHEEL:
		def OnRunMouseWheel(self, nLen):
			if nLen > 0:
				self.contentScrollbar.OnUp()
			else:
				self.contentScrollbar.OnDown()

		def SetOnRunMouseWheelEvent(self, event):
			self.onRunMouseWheelEvent = __mem_func__(event)

