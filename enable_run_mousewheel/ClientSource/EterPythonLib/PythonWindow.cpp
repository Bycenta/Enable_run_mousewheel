0.1 Search :

	BOOL CWindow::OnMouseMiddleButtonUp()
	{
		long lValue;
		if (PyCallClassMemberFunc(m_poHandler, "OnMouseMiddleButtonUp", BuildEmptyTuple(), &lValue))
		if (0 != lValue)
			return TRUE;

		return FALSE;
	}

0.1.1 Add Below :

#ifdef ENABLE_RUN_MOUSE_WHEEL
	BOOL CWindow::RunMouseWheelEvent(long nLen)
	{
		bool bValue = false;
		if (PyCallClassMemberFunc(m_poHandler, "OnRunMouseWheel", Py_BuildValue("(l)", nLen), &bValue))
			return bValue;

		return bValue;
	}
#endif

















