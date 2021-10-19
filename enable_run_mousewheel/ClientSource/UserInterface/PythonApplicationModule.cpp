0.1 Search : 

#ifdef ENABLE_ENERGY_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_ENERGY_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_ENERGY_SYSTEM",	0);
#endif


0.1.1 Add ABOVE : 

#ifdef ENABLE_RUN_MOUSE_WHEEL
	PyModule_AddIntConstant(poModule, "ENABLE_RUN_MOUSE_WHEEL", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_RUN_MOUSE_WHEEL", 0);
#endif















