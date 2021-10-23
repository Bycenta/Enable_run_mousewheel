0.1 Search : 

	def GetState(self):
		return self.state


0.1.1 Add Below : 

	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			if self.GetState() == "STATUS":
				self.SetState("SKILL")
			elif self.GetState() == "SKILL":
				self.SetState("EMOTICON")
			elif self.GetState() == "EMOTICON":
				self.SetState("QUEST")
		else:
			if self.GetState() == "SKILL":
				self.SetState("STATUS")
			elif self.GetState() == "EMOTICON":
				self.SetState("SKILL")
			elif self.GetState() == "QUEST":
				self.SetState("EMOTICON")



Thx for this forum80
