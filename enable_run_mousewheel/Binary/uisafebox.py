0.1 Search : 


class MallWindow(ui.ScriptWindow):


0.1.1 Add ABOVE : 

[...]

	def OnRunMouseWheel(self, a):
		if a > 0:
			index = self.curPageIndex-1
			if index < 0:
				self.curPageIndex = 2
				index = 2
			else:
				self.curPageIndex = index
		else:
			index = 1 + self.curPageIndex
			if index > 2:
				self.curPageIndex = 0
				index = 0
			else:
				self.curPageIndex = index

		for i in xrange(3):
			self.pageButtonList[i].SetUp()

		self.pageButtonList[index].Down()

		self.RefreshSafebox()
