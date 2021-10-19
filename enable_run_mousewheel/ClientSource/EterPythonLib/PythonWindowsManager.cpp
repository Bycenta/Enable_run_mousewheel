0.1 Search :

	void CWindowManager::RunIMEUpdate()
	{
		if (m_pLockWindow)
		{
			m_pLockWindow->OnIMEUpdate();
			return;
		}

		if (!m_pActiveWindow)
			return;
		if (!m_pActiveWindow->IsRendering())
			return;

		m_pActiveWindow->OnIMEUpdate();
	}

0.1.1 Add ABOVE

#ifdef ENABLE_RUN_MOUSE_WHEEL
	bool CWindowManager::RunMouseWheelEvent(long nLen)
	{
		CWindow * pWin;
		if (pWin = GetPointWindow())
		{
			if (pWin->IsRendering() || pWin->IsShow())
			{
				if (pWin->RunMouseWheelEvent(nLen))
					return true;
				else if (pWin->GetRoot()->RunMouseWheelEvent(nLen))
					return true;
			}
		}

		return false;
	}
#endif















