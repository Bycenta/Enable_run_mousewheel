0.1 Search : 

void CPythonApplication::OnMouseWheel(int nLen)
{
.....
}

0.1.1 Replace with : 

#ifdef ENABLE_RUN_MOUSE_WHEEL
void CPythonApplication::OnMouseWheel(int nLen)
{
	if (!(UI::CWindowManager::Instance().RunMouseWheelEvent(nLen)))
	{
		CCameraManager& rkCmrMgr = CCameraManager::Instance();
		CCamera* pkCmrCur = rkCmrMgr.GetCurrentCamera();
		if (pkCmrCur)
			pkCmrCur->Wheel(nLen);
	}
}
#else
void CPythonApplication::OnMouseWheel(int nLen)
{
	CCameraManager& rkCmrMgr=CCameraManager::Instance();
	CCamera* pkCmrCur=rkCmrMgr.GetCurrentCamera();
	if (pkCmrCur)
		pkCmrCur->Wheel(nLen);
}
#endif










