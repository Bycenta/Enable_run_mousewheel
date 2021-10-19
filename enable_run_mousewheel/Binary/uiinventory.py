0.1 Search : 

...
	def Hide(self):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			self.OnCloseQuestionDialog()
			return
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()
 
		if self.wndBelt:
			self.isOpenedBeltWindowWhenClosingInventory = self.wndBelt.IsOpeningInventory()		# 인벤토리 창이 닫힐 때 벨트 인벤토리도 열려 있었는가?
			print "Is Opening Belt Inven?? ", self.isOpenedBeltWindowWhenClosingInventory
			self.wndBelt.Close()

		if self.wndMenu:
			self.wndMenu.Close()
			
		if self.dlgPickMoney:
			self.dlgPickMoney.Close()
		
		if self.dlgPickItem:
			self.dlgPickItem.Close()
		wndMgr.Hide(self.hWnd)


0.1.1 Add Below : 

	def OnRunMouseWheel(self, a):
		if a > 0:
			index = self.inventoryPageIndex-1
			if index < 0:
				self.inventoryPageIndex = 3
				index = 3
			else:
				self.inventoryPageIndex = index
		else:
			index = 1 + self.inventoryPageIndex
			if index > 3:
				self.inventoryPageIndex = 0
				index = 0
			else:
				self.inventoryPageIndex = index

		for i in xrange(4):
			self.inventoryTab[i].SetUp()

		self.inventoryTab[index].Down()

		self.RefreshBagSlotWindow()