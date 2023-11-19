# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)]
# From type library '{42B8BE9B-D0CD-49BE-9B52-6C8C8482BC86}'
# On Tue Sep 19 20:11:06 2023
'Nikon LV Series Microscope Control 1.0 Type Library'
makepy_version = '0.5.01'
python_version = 0x3090cf0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{42B8BE9B-D0CD-49BE-9B52-6C8C8482BC86}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	AccessoryDICPrism             =9          # from enum EnumAccessory
	AccessoryDICPrismShift        =10         # from enum EnumAccessory
	AccessoryDiaLamp              =4          # from enum EnumAccessory
	AccessoryDiaLampVoltage       =5          # from enum EnumAccessory
	AccessoryEpiApertureStop      =7          # from enum EnumAccessory
	AccessoryEpiLamp              =2          # from enum EnumAccessory
	AccessoryEpiLampVoltage       =3          # from enum EnumAccessory
	AccessoryEpiShutter           =12         # from enum EnumAccessory
	AccessoryFilterBlockCassette  =6          # from enum EnumAccessory
	AccessoryNDFilter             =11         # from enum EnumAccessory
	AccessoryNosepiece            =1          # from enum EnumAccessory
	AccessoryZDrive               =8          # from enum EnumAccessory
	AfRun                         =2          # from enum EnumAf
	AfUnknown                     =-1         # from enum EnumAf
	AfWait                        =1          # from enum EnumAf
	AfBF                          =1          # from enum EnumAfObservationMode
	AfDF                          =2          # from enum EnumAfObservationMode
	AfOPT1                        =3          # from enum EnumAfObservationMode
	AfOPT2                        =4          # from enum EnumAfObservationMode
	AfObservationModeUnknown      =-1         # from enum EnumAfObservationMode
	AfRecipe01                    =0          # from enum EnumAfRecipeMode
	AfRecipe02                    =1          # from enum EnumAfRecipeMode
	AfRecipe03                    =2          # from enum EnumAfRecipeMode
	AfRecipe04                    =3          # from enum EnumAfRecipeMode
	AfRecipe05                    =4          # from enum EnumAfRecipeMode
	AfRecipe06                    =5          # from enum EnumAfRecipeMode
	AfRecipe07                    =6          # from enum EnumAfRecipeMode
	AfRecipe08                    =7          # from enum EnumAfRecipeMode
	AfRecipe09                    =8          # from enum EnumAfRecipeMode
	AfRecipe10                    =9          # from enum EnumAfRecipeMode
	AfRecipeUnknown               =-1         # from enum EnumAfRecipeMode
	AfSearchMode1                 =1          # from enum EnumAfSearch
	AfSearchMode2                 =2          # from enum EnumAfSearch
	AfSearchUnknown               =-1         # from enum EnumAfSearch
	AfStatusJustFocus             =1          # from enum EnumAfStatus
	AfStatusOutOfRange            =9          # from enum EnumAfStatus
	AfStatusOverFocus             =3          # from enum EnumAfStatus
	AfStatusUnderFocus            =2          # from enum EnumAfStatus
	AfStatusUnknown               =-1         # from enum EnumAfStatus
	AperturePresetsUnknown        =-1         # from enum EnumAperturePresets
	KeepingRadius                 =0          # from enum EnumAperturePresets
	StoredRadius                  =1          # from enum EnumAperturePresets
	ThreeQuartersOfIris           =2          # from enum EnumAperturePresets
	AF_Controller                 =3          # from enum EnumController
	ControllerUnknown             =-1         # from enum EnumController
	E_Controller                  =2          # from enum EnumController
	LV100NDA_Controller           =4          # from enum EnumController
	LV150NA_Controller            =5          # from enum EnumController
	LVINAD_Controller             =7          # from enum EnumController
	LVNCNTN_Controller            =6          # from enum EnumController
	LV_Controller                 =1          # from enum EnumController
	DICPositionA                  =1          # from enum EnumDICPosition
	DICPositionB                  =2          # from enum EnumDICPosition
	DICPositionUnknown            =-1         # from enum EnumDICPosition
	DiaEnable                     =2          # from enum EnumEpiDiaLampMode
	EpiDiaDisable                 =0          # from enum EnumEpiDiaLampMode
	EpiDiaEnable                  =3          # from enum EnumEpiDiaLampMode
	EpiDiaLampModeUnknown         =-1         # from enum EnumEpiDiaLampMode
	EpiEnable                     =1          # from enum EnumEpiDiaLampMode
	FiberTypeExfo                 =3          # from enum EnumFiberType
	FiberTypeNikon                =4          # from enum EnumFiberType
	FiberTypeUnknown              =0          # from enum EnumFiberType
	BarrierFilter                 =2          # from enum EnumFilterType
	DichroicMirror                =3          # from enum EnumFilterType
	ExcitationFilter              =1          # from enum EnumFilterType
	FilterBlock                   =4          # from enum EnumFilterType
	FilterNotMounted              =0          # from enum EnumFilterType
	FilterUnknown                 =-1         # from enum EnumFilterType
	IlluminantPresetsEpiMemDiaMem =0          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiMemDiaNone=2          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiMemDiaOff =1          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiNoneDiaMem=6          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiNoneDiaNone=8          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiNoneDiaOff=7          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiOffDiaMem =3          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiOffDiaNone=5          # from enum EnumIlluminantPresets
	IlluminantPresetsEpiOffDiaOff =4          # from enum EnumIlluminantPresets
	IlluminantPresetsUnknown      =-1         # from enum EnumIlluminantPresets
	InterlockDisabled             =0          # from enum EnumInterlockMode
	InterlockEnabled              =1          # from enum EnumInterlockMode
	InterlockUnknown              =-1         # from enum EnumInterlockMode
	LampPresetsEpiNoneDiaNone     =3          # from enum EnumLampPresets
	LampPresetsEpiNoneDiaOff      =4          # from enum EnumLampPresets
	LampPresetsEpiNoneDiaOn       =5          # from enum EnumLampPresets
	LampPresetsEpiOffDiaNone      =6          # from enum EnumLampPresets
	LampPresetsEpiOffDiaOff       =7          # from enum EnumLampPresets
	LampPresetsEpiOffDiaOn        =8          # from enum EnumLampPresets
	LampPresetsEpiOnDiaNone       =0          # from enum EnumLampPresets
	LampPresetsEpiOnDiaOff        =1          # from enum EnumLampPresets
	LampPresetsEpiOnDiaOn         =2          # from enum EnumLampPresets
	LampPresetsUnknown            =-1         # from enum EnumLampPresets
	LampTypeInternal              =1          # from enum EnumLampType
	LampTypeInternalLED           =7          # from enum EnumLampType
	LampTypeLED                   =5          # from enum EnumLampType
	LampTypeOutside               =2          # from enum EnumLampType
	LampTypeOutsideLED            =8          # from enum EnumLampType
	LampTypeUnknown               =0          # from enum EnumLampType
	LimitationError               =3          # from enum EnumLimitation
	LimitationLower               =1          # from enum EnumLimitation
	LimitationNone                =0          # from enum EnumLimitation
	LimitationUnknown             =-1         # from enum EnumLimitation
	LimitationUpper               =2          # from enum EnumLimitation
	NosepieceControlNone          =1          # from enum EnumNosepieceControl
	NosepieceControlUnknown       =-1         # from enum EnumNosepieceControl
	Skip                          =3          # from enum EnumNosepieceControl
	ZLimit                        =2          # from enum EnumNosepieceControl
	ZLimitAndSkip                 =4          # from enum EnumNosepieceControl
	BrightField                   =1          # from enum EnumObservationMode
	DIC                           =3          # from enum EnumObservationMode
	DarkField                     =2          # from enum EnumObservationMode
	Fluorescence1                 =4          # from enum EnumObservationMode
	Fluorescence2                 =5          # from enum EnumObservationMode
	ObservationMode1              =7          # from enum EnumObservationMode
	ObservationMode2              =8          # from enum EnumObservationMode
	ObservationMode3              =9          # from enum EnumObservationMode
	ObservationMode4              =10         # from enum EnumObservationMode
	ObservationMode5              =11         # from enum EnumObservationMode
	ObservationMode6              =12         # from enum EnumObservationMode
	ObservationModeAll            =15         # from enum EnumObservationMode
	ObservationModeNone           =0          # from enum EnumObservationMode
	ObservationModeUnknown        =-1         # from enum EnumObservationMode
	BrightFieldEpi                =2          # from enum EnumOptionalObservationMode
	BrightFieldEpiDia             =1          # from enum EnumOptionalObservationMode
	DICEpi                        =6          # from enum EnumOptionalObservationMode
	DICEpiDia                     =5          # from enum EnumOptionalObservationMode
	DarkFieldEpi                  =4          # from enum EnumOptionalObservationMode
	DarkFieldEpiDia               =3          # from enum EnumOptionalObservationMode
	Fluorescence1Epi              =8          # from enum EnumOptionalObservationMode
	Fluorescence1EpiDia           =7          # from enum EnumOptionalObservationMode
	Fluorescence2Epi              =10         # from enum EnumOptionalObservationMode
	Fluorescence2EpiDia           =9          # from enum EnumOptionalObservationMode
	OptionalObservationDia        =11         # from enum EnumOptionalObservationMode
	OptionalObservationModeNone   =0          # from enum EnumOptionalObservationMode
	OptionalObservationModeUnknown=-1         # from enum EnumOptionalObservationMode
	AfSearchModeUnknown           =-1         # from enum EnumSearchMode
	AfSearchModeUp                =1          # from enum EnumSearchMode
	AfSearchModeUpDown            =2          # from enum EnumSearchMode
	AfSearchModeWait              =0          # from enum EnumSearchMode
	Speed0                        =0          # from enum EnumSpeed
	Speed1                        =1          # from enum EnumSpeed
	Speed2                        =2          # from enum EnumSpeed
	Speed3                        =3          # from enum EnumSpeed
	Speed4                        =4          # from enum EnumSpeed
	Speed5                        =5          # from enum EnumSpeed
	Speed6                        =6          # from enum EnumSpeed
	Speed7                        =7          # from enum EnumSpeed
	SpeedUnknown                  =-1         # from enum EnumSpeed
	StatusFalse                   =0          # from enum EnumStatus
	StatusTrue                    =1          # from enum EnumStatus
	StatusUnknown                 =-1         # from enum EnumStatus
	Tolerance1                    =0          # from enum EnumTolerance
	Tolerance10                   =9          # from enum EnumTolerance
	Tolerance2                    =1          # from enum EnumTolerance
	Tolerance3                    =2          # from enum EnumTolerance
	Tolerance4                    =3          # from enum EnumTolerance
	Tolerance5                    =4          # from enum EnumTolerance
	Tolerance6                    =5          # from enum EnumTolerance
	Tolerance7                    =6          # from enum EnumTolerance
	Tolerance8                    =7          # from enum EnumTolerance
	Tolerance9                    =8          # from enum EnumTolerance
	ToleranceUnknown              =-1         # from enum EnumTolerance
	Transmission0                 =0          # from enum EnumTransmission
	Transmission1                 =3          # from enum EnumTransmission
	Transmission2                 =6          # from enum EnumTransmission
	Transmission3                 =12         # from enum EnumTransmission
	Transmission4                 =25         # from enum EnumTransmission
	Transmission5                 =50         # from enum EnumTransmission
	Transmission6                 =100        # from enum EnumTransmission
	TransmissionUnknown           =-1         # from enum EnumTransmission
	ZDriveTypeIMA_FMA             =1          # from enum EnumZDriveType
	ZDriveTypeModuleAF            =2          # from enum EnumZDriveType
	ZDriveTypeUnknown             =0          # from enum EnumZDriveType
	NIKONLV_DATABASE_ERROR_BASE   =-536214252 # from enum Enum_NikonLvError
	NIKONLV_DEVICE_ERROR_BASE     =-536214352 # from enum Enum_NikonLvError
	NIKONLV_ERROR_BADCODE         =-536214247 # from enum Enum_NikonLvError
	NIKONLV_ERROR_BADPOSITION     =-536214248 # from enum Enum_NikonLvError
	NIKONLV_ERROR_BADRESPONSE     =-536214347 # from enum Enum_NikonLvError
	NIKONLV_ERROR_BUSY            =-536214349 # from enum Enum_NikonLvError
	NIKONLV_ERROR_CONSTANT        =-536214249 # from enum Enum_NikonLvError
	NIKONLV_ERROR_CREATE_FILE     =-536214051 # from enum Enum_NikonLvError
	NIKONLV_ERROR_DATABASEFULL    =-536214250 # from enum Enum_NikonLvError
	NIKONLV_ERROR_DEVICE          =-536214346 # from enum Enum_NikonLvError
	NIKONLV_ERROR_DIRECTSHOW      =-536214152 # from enum Enum_NikonLvError
	NIKONLV_ERROR_DRIVER          =-536214351 # from enum Enum_NikonLvError
	NIKONLV_ERROR_GET_IMAGE       =-536214149 # from enum Enum_NikonLvError
	NIKONLV_ERROR_GET_IMAGESIZE   =-536214150 # from enum Enum_NikonLvError
	NIKONLV_ERROR_GRAPH_RUNNING   =-536214148 # from enum Enum_NikonLvError
	NIKONLV_ERROR_INVALIDARG      =-536214341 # from enum Enum_NikonLvError
	NIKONLV_ERROR_INVALIDCMD      =-536214342 # from enum Enum_NikonLvError
	NIKONLV_ERROR_INVALID_FORMAT  =-536214151 # from enum Enum_NikonLvError
	NIKONLV_ERROR_INVALID_HANDLE  =-536214052 # from enum Enum_NikonLvError
	NIKONLV_ERROR_NOACCESSORY     =-536214340 # from enum Enum_NikonLvError
	NIKONLV_ERROR_NODEVICE        =-536214343 # from enum Enum_NikonLvError
	NIKONLV_ERROR_NODEVICES       =-536214336 # from enum Enum_NikonLvError
	NIKONLV_ERROR_NOTCONNECTED    =-536214344 # from enum Enum_NikonLvError
	NIKONLV_ERROR_NOTCUSTOM       =-536214251 # from enum Enum_NikonLvError
	NIKONLV_ERROR_NOTMOUNTED      =-536214246 # from enum Enum_NikonLvError
	NIKONLV_ERROR_OVERFLOW        =-536214348 # from enum Enum_NikonLvError
	NIKONLV_ERROR_PORTTIMEOUT     =-536214345 # from enum Enum_NikonLvError
	NIKONLV_ERROR_SENDOVERFLOW    =-536214339 # from enum Enum_NikonLvError
	NIKONLV_ERROR_TRANSFER        =-536214350 # from enum Enum_NikonLvError
	NIKONLV_ERROR_TRANSMITFAIL    =-536214337 # from enum Enum_NikonLvError
	NIKONLV_ERROR_UNSAFE          =-536214338 # from enum Enum_NikonLvError

from win32com.client import DispatchBaseClass
class IDICPrism(DispatchBaseClass):
	'IDICPrism Interface'
	CLSID = IID('{40FCAC43-8012-4FDF-9083-D29B4372FC80}')
	coclass_clsid = IID('{43DC7FFC-1699-4C9A-99C7-4CFC8892044B}')

	def AdjustDicCalibration(self):
		'Adjusts the calibration value.'
		return self._oleobj_.InvokeTypes(226, LCID, 1, (24, 0), (),)

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def GoOutOfPosition(self):
		'Control to DIC escape position.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def InitializeDicCalibration(self):
		'Initialize the calibration value.'
		return self._oleobj_.InvokeTypes(227, LCID, 1, (24, 0), (),)

	def ReadDicCalibration(self):
		'Gets the calibration value.'
		return self._oleobj_.InvokeTypes(225, LCID, 1, (3, 0), (),)

	def SetDicCalibration(self, lValue=defaultNamedNotOptArg):
		'Sets the calibration value.'
		return self._oleobj_.InvokeTypes(228, LCID, 1, (24, 0), ((3, 1),),lValue
			)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"DICPosition": (220, 2, (12, 0), (), "DICPosition", None),
		"IsCalibration": (458, 2, (12, 0), (), "IsCalibration", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsOutOfPosition": (222, 2, (12, 0), (), "IsOutOfPosition", None),
		"Limitation": (208, 2, (12, 0), (), "Limitation", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"PhaseDifference": (448, 2, (12, 0), (), "PhaseDifference", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		"_DICPosition": (221, 2, (3, 0), (), "_DICPosition", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsCalibration": (459, 2, (3, 0), (), "_IsCalibration", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsOutOfPosition": (223, 2, (3, 0), (), "_IsOutOfPosition", None),
		"_Limitation": (209, 2, (3, 0), (), "_Limitation", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_PhaseDifference": (449, 2, (5, 0), (), "_PhaseDifference", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"DICPosition": ((220, LCID, 4, 0),()),
		"PhaseDifference": ((448, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_DICPosition": ((221, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsCalibration": ((459, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsOutOfPosition": ((223, LCID, 4, 0),()),
		"_Limitation": ((209, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_PhaseDifference": ((449, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDatabase(DispatchBaseClass):
	'IDatabase Interface'
	CLSID = IID('{C64C5896-AF8D-4520-B67F-E2C284A17015}')
	coclass_clsid = IID('{52BCED18-FB30-4D67-BC91-38456E6CAA91}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		# Method 'BarrierFilters' returns object of type 'IDbBarrierFilters'
		"BarrierFilters": (35, 2, (9, 0), (), "BarrierFilters", '{7FC48C7D-6C9F-4EE4-8EA5-F6A5C695410E}'),
		# Method 'DichroicMirrors' returns object of type 'IDbDichroicMirrors'
		"DichroicMirrors": (36, 2, (9, 0), (), "DichroicMirrors", '{17E1D932-1A32-4716-91C6-A4F4195AD69D}'),
		# Method 'ExcitationFilters' returns object of type 'IDbExcitationFilters'
		"ExcitationFilters": (34, 2, (9, 0), (), "ExcitationFilters", '{5224855F-17CF-4B8B-8D4A-096DEF8A1028}'),
		# Method 'FilterBlocks' returns object of type 'IDbFilterBlocks'
		"FilterBlocks": (37, 2, (9, 0), (), "FilterBlocks", '{74AE41DD-4F6A-40B2-AC6E-30361A6CA3F5}'),
		# Method 'ObjectiveDics' returns object of type 'IDbObjectiveDics'
		"ObjectiveDics": (52, 2, (9, 0), (), "ObjectiveDics", '{E063359B-97AD-472A-A089-4F32DABB9F29}'),
		# Method 'ObjectiveModels' returns object of type 'IDbObjectiveModels'
		"ObjectiveModels": (50, 2, (9, 0), (), "ObjectiveModels", '{7F23BB36-32A4-45C0-9E6E-C344DFC1B002}'),
		# Method 'ObjectiveTypes' returns object of type 'IDbObjectiveTypes'
		"ObjectiveTypes": (51, 2, (9, 0), (), "ObjectiveTypes", '{375F6905-A9EB-445B-B5C0-DF78C0A4F8C4}'),
		# Method 'Objectives' returns object of type 'IDbObjectives'
		"Objectives": (32, 2, (9, 0), (), "Objectives", '{2204072B-6007-4D6B-AB10-30B8EB6CD97E}'),
		"PresetBarrierFilters": (45, 2, (3, 0), (), "PresetBarrierFilters", None),
		"PresetDichroicMirrors": (46, 2, (3, 0), (), "PresetDichroicMirrors", None),
		"PresetExcitationFilters": (44, 2, (3, 0), (), "PresetExcitationFilters", None),
		"PresetFilterBlocks": (47, 2, (3, 0), (), "PresetFilterBlocks", None),
		"PresetObjectiveModels": (48, 2, (3, 0), (), "PresetObjectiveModels", None),
		"PresetObjectiveTypes": (49, 2, (3, 0), (), "PresetObjectiveTypes", None),
		"PresetObjectives": (42, 2, (3, 0), (), "PresetObjectives", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbBarrierFilter(DispatchBaseClass):
	'IDbBarrierFilter Interface'
	CLSID = IID('{1B069B84-282E-42EF-A0AA-0338C9C7B654}')
	coclass_clsid = IID('{A7D2C363-A7A8-440D-BD9E-BC399DE12B9E}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (0, 2, (3, 0), (), "Code", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (14, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Data": ((12, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"Position": ((14, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbBarrierFilters(DispatchBaseClass):
	'IDbBarrierFilters Interface'
	CLSID = IID('{7FC48C7D-6C9F-4EE4-8EA5-F6A5C695410E}')
	coclass_clsid = IID('{688E3601-6AAD-4551-BC82-C411201C26F1}')

	def Add(self, pNewData=defaultNamedNotOptArg):
		'Adds a barrier filter to the list of barrier filters.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((36, 1),),pNewData
			)

	# Result is of type IDbBarrierFilter
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified barrier filter in the barrier filter list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1B069B84-282E-42EF-A0AA-0338C9C7B654}')
		return ret

	def Remove(self, lIndex=defaultNamedNotOptArg):
		'Removes a barrier filter from the list of barrier filters.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),lIndex
			)

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified barrier filter in the barrier filter list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1B069B84-282E-42EF-A0AA-0338C9C7B654}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbDichroicMirror(DispatchBaseClass):
	'IDbDichroicMirror Interface'
	CLSID = IID('{E6FCB965-784B-4F18-9296-91AE9849D93C}')
	coclass_clsid = IID('{D87CB878-07B8-4790-AF9A-411D4A090022}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (0, 2, (3, 0), (), "Code", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (14, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Data": ((12, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"Position": ((14, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbDichroicMirrors(DispatchBaseClass):
	'IDbDichroicMirrors Interface'
	CLSID = IID('{17E1D932-1A32-4716-91C6-A4F4195AD69D}')
	coclass_clsid = IID('{90DF6DA2-E579-4F57-B6D4-8FCC9F89B0FA}')

	def Add(self, pNewData=defaultNamedNotOptArg):
		'Adds a dichroic mirror to the list of dichroic mirrors.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((36, 1),),pNewData
			)

	# Result is of type IDbDichroicMirror
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified dichroic mirror in the dichroic mirror list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E6FCB965-784B-4F18-9296-91AE9849D93C}')
		return ret

	def Remove(self, lIndex=defaultNamedNotOptArg):
		'Removes a dichroic mirror from the list of dichroic mirrors.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),lIndex
			)

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified dichroic mirror in the dichroic mirror list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E6FCB965-784B-4F18-9296-91AE9849D93C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbExcitationFilter(DispatchBaseClass):
	'IDbExcitationFilter Interface'
	CLSID = IID('{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}')
	coclass_clsid = IID('{A1F02B27-F0BC-498A-8D3D-9E49C1A8A616}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (0, 2, (3, 0), (), "Code", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (14, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Data": ((12, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"Position": ((14, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbExcitationFilters(DispatchBaseClass):
	'IDbExcitationFilters Interface'
	CLSID = IID('{5224855F-17CF-4B8B-8D4A-096DEF8A1028}')
	coclass_clsid = IID('{5C9124B1-A227-4D41-9CC3-E799DD70C5F0}')

	def Add(self, pNewData=defaultNamedNotOptArg):
		'Adds a excitation filter to the list of excitation filters.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((36, 1),),pNewData
			)

	# Result is of type IDbExcitationFilter
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified excitation filter in the excitation filter list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}')
		return ret

	def Remove(self, lIndex=defaultNamedNotOptArg):
		'Removes a excitation filter from the list of excitation filters.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),lIndex
			)

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified excitation filter in the excitation filter list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbFilterBlock(DispatchBaseClass):
	'IDbFilterBlock Interface'
	CLSID = IID('{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}')
	coclass_clsid = IID('{22713002-A419-4E9E-B637-31B498728121}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"BarrierFilterCode": (37, 2, (3, 0), (), "BarrierFilterCode", None),
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (0, 2, (3, 0), (), "Code", None),
		"Composition": (31, 2, (36, 0), (), "Composition", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"DichroicMirrorCode": (36, 2, (3, 0), (), "DichroicMirrorCode", None),
		"ExcitationFilterCode": (35, 2, (3, 0), (), "ExcitationFilterCode", None),
		"FilterBlockData": (30, 2, (36, 0), (), "FilterBlockData", None),
		"FilterType": (32, 2, (3, 0), (), "FilterType", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (14, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"BarrierFilterCode": ((37, LCID, 4, 0),()),
		"Composition": ((31, LCID, 4, 0),()),
		"Data": ((12, LCID, 4, 0),()),
		"DichroicMirrorCode": ((36, LCID, 4, 0),()),
		"ExcitationFilterCode": ((35, LCID, 4, 0),()),
		"FilterBlockData": ((30, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"Position": ((14, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbFilterBlocks(DispatchBaseClass):
	'IDbFilterBlocks Interface'
	CLSID = IID('{74AE41DD-4F6A-40B2-AC6E-30361A6CA3F5}')
	coclass_clsid = IID('{DCD1A352-9EDD-4C04-97CC-735CA7604926}')

	def Add(self, pNewData=defaultNamedNotOptArg):
		'Adds a filter block to the list of filter blocks.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((36, 1),),pNewData
			)

	# Result is of type IDbFilterBlock
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified filter block in the filter block list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}')
		return ret

	def Remove(self, lIndex=defaultNamedNotOptArg):
		'Removes a filter block from the list of filter blocks.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),lIndex
			)

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified filter block in the filter block list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbObjective(DispatchBaseClass):
	'IDbObjective Interface'
	CLSID = IID('{29C5F645-840A-487F-AB19-E306973D4DD9}')
	coclass_clsid = IID('{A4D9888B-C013-4A67-ABF6-151B232C1CA9}')

	def SetObjectiveData(self, lObjectiveModel=defaultNamedNotOptArg, lObjectiveType=defaultNamedNotOptArg, dMagnification=defaultNamedNotOptArg, dWorkingDistance=defaultNamedNotOptArg
			, dNumericalAperture=defaultNamedNotOptArg, lCondenserType=defaultNamedNotOptArg, lDICPrismPosition=defaultNamedNotOptArg):
		'Sets the properties of this objective.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1), (5, 1), (5, 1), (3, 1), (3, 1)),lObjectiveModel
			, lObjectiveType, dMagnification, dWorkingDistance, dNumericalAperture, lCondenserType
			, lDICPrismPosition)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (0, 2, (3, 0), (), "Code", None),
		"CondenserType": (41, 2, (3, 0), (), "CondenserType", None),
		"DICPrismPosition": (42, 2, (3, 0), (), "DICPrismPosition", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Description": (31, 2, (8, 0), (), "Description", None),
		"Magnification": (34, 2, (5, 0), (), "Magnification", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"NumericalAperture": (35, 2, (5, 0), (), "NumericalAperture", None),
		"ObjectiveData": (37, 2, (36, 0), (), "ObjectiveData", None),
		"ObjectiveModel": (39, 2, (3, 0), (), "ObjectiveModel", None),
		"ObjectiveType": (38, 2, (3, 0), (), "ObjectiveType", None),
		"Position": (14, 2, (3, 0), (), "Position", None),
		"WorkingDistance": (36, 2, (5, 0), (), "WorkingDistance", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Data": ((12, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"ObjectiveData": ((37, LCID, 4, 0),()),
		"Position": ((14, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbObjectiveDic(DispatchBaseClass):
	'IDbObjectiveDic Interface'
	CLSID = IID('{2077315B-1C2B-422E-8355-376F7DB532BF}')
	coclass_clsid = IID('{E5FDFD81-FA9A-4667-AD94-E1505D1F32B7}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"Name": (53, 2, (8, 0), (), "Name", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbObjectiveDics(DispatchBaseClass):
	'IDbObjectiveDics Interface'
	CLSID = IID('{E063359B-97AD-472A-A089-4F32DABB9F29}')
	coclass_clsid = IID('{4300DCFA-BBE3-4DAD-87DE-3FB0FC4592B1}')

	# Result is of type IDbObjectiveDic
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified objective model in the objective model list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2077315B-1C2B-422E-8355-376F7DB532BF}')
		return ret

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified objective model in the objective model list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2077315B-1C2B-422E-8355-376F7DB532BF}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbObjectiveModel(DispatchBaseClass):
	'IDbObjectiveModel Interface'
	CLSID = IID('{4667A60B-E710-4E47-A139-6686B8D194A6}')
	coclass_clsid = IID('{8DE4446A-39A9-4B89-9F3B-B285B24483FC}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"Name": (53, 2, (8, 0), (), "Name", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbObjectiveModels(DispatchBaseClass):
	'IDbObjectiveModels Interface'
	CLSID = IID('{7F23BB36-32A4-45C0-9E6E-C344DFC1B002}')
	coclass_clsid = IID('{B911DB65-903F-4F19-9A14-046F63ACD0CD}')

	# Result is of type IDbObjectiveModel
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified objective model in the objective model list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4667A60B-E710-4E47-A139-6686B8D194A6}')
		return ret

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified objective model in the objective model list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4667A60B-E710-4E47-A139-6686B8D194A6}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbObjectiveType(DispatchBaseClass):
	'IDbObjectiveType Interface'
	CLSID = IID('{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}')
	coclass_clsid = IID('{0309400B-38C2-403C-BE7F-27B3CEE68551}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"Name": (53, 2, (8, 0), (), "Name", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDbObjectiveTypes(DispatchBaseClass):
	'IDbObjectiveTypes Interface'
	CLSID = IID('{375F6905-A9EB-445B-B5C0-DF78C0A4F8C4}')
	coclass_clsid = IID('{E081B9B1-422A-4741-A30B-35F966968518}')

	# Result is of type IDbObjectiveType
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified objective type in the objective type list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}')
		return ret

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified objective type in the objective type list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDbObjectives(DispatchBaseClass):
	'IDbObjectives Interface'
	CLSID = IID('{2204072B-6007-4D6B-AB10-30B8EB6CD97E}')
	coclass_clsid = IID('{A2FB0ED5-93D0-460D-8195-A07CADC1C75F}')

	def Add(self, pNewData=defaultNamedNotOptArg):
		'Adds an objective to the list of objectives.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (3, 0), ((36, 1),),pNewData
			)

	# Result is of type IDbObjective
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified objective in the objective list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{29C5F645-840A-487F-AB19-E306973D4DD9}')
		return ret

	def Remove(self, lIndex=defaultNamedNotOptArg):
		'Removes an objective from the list of objectives.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),lIndex
			)

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified objective in the objective list.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{29C5F645-840A-487F-AB19-E306973D4DD9}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDevice(DispatchBaseClass):
	'Communications and port settings for Nikon Instruments.'
	CLSID = IID('{F1283CC9-B953-4A63-A677-769CC13EA403}')
	coclass_clsid = None

	def Connect(self):
		'Connects to a device.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def Disconnect(self):
		'Disconnects from a device.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def GetLongData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'Sends a command to get 32-bit integer data from a device.'
		return self._ApplyTypes_(22, 1, (24, 0), ((8, 1), (8, 1), (16387, 3)), 'GetLongData', None,LockCookie
			, strCommand, pVal)

	def GetStatusData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'Sends a command to get a device property as StatusUnknown, StatusTrue or StatusFalse.'
		return self._ApplyTypes_(21, 1, (24, 0), ((8, 1), (8, 1), (16387, 3)), 'GetStatusData', None,LockCookie
			, strCommand, pVal)

	def GetStringData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'Sends a command to get 32-bit character data from a device.'
		return self._ApplyTypes_(20, 1, (24, 0), ((8, 1), (8, 1), (16392, 3)), 'GetStringData', None,LockCookie
			, strCommand, pVal)

	def SendLongData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, lArgument=defaultNamedNotOptArg):
		'Sends a command to set a device property to a 32-bit integer.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),LockCookie
			, strCommand, lArgument)

	def SendStatusData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, statusArgument=defaultNamedNotOptArg):
		'Sends a command to set a device property to StatusTrue or StatusFalse.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),LockCookie
			, strCommand, statusArgument)

	def SendStringData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, strArgument=defaultNamedNotOptArg):
		'Sends a command to set a string property using a 32-bit character pointer property.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1)),LockCookie
			, strCommand, strArgument)

	_prop_map_get_ = {
		"Address": (1, 2, (8, 0), (), "Address", None),
		"Connected": (12, 2, (3, 0), (), "Connected", None),
		"LastResponse": (15, 2, (8, 0), (), "LastResponse", None),
	}
	_prop_map_put_ = {
		"Connected": ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDeviceClient(DispatchBaseClass):
	'Guarantees per-object access to an IDevice.'
	CLSID = IID('{1B52A395-B324-4054-B143-2F20C52EA5C4}')
	coclass_clsid = None

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDiaLamp(DispatchBaseClass):
	'IDiaLamp Interface'
	CLSID = IID('{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}')
	coclass_clsid = IID('{4D8E961D-5593-4C7D-BB72-ABF66FADE539}')

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def Off(self):
		'Turns the lamp off.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def On(self):
		'Turns the lamp on.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def SetVoltageForCamera(self):
		'Selects the appropriate lamp voltage for digital imaging.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsOn": (202, 2, (12, 0), (), "IsOn", None),
		"LampType": (232, 2, (12, 0), (), "LampType", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		"Voltage": (220, 2, (12, 0), (), "Voltage", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsOn": (203, 2, (3, 0), (), "_IsOn", None),
		"_LampType": (233, 2, (3, 0), (), "_LampType", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
		"_Voltage": (221, 2, (5, 0), (), "_Voltage", None),
	}
	_prop_map_put_ = {
		"IsOn": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"Voltage": ((220, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsOn": ((203, LCID, 4, 0),()),
		"_LampType": ((233, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
		"_Voltage": ((221, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IEpiApertureStop(DispatchBaseClass):
	'IEpiApertureStop Interface'
	CLSID = IID('{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}')
	coclass_clsid = IID('{3AE83DE1-2AF8-4215-BE75-71FD9D324E9B}')

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def SetApertureDefaults(self):
		'Sets the default aperture values.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"ApertureStop": (220, 2, (12, 0), (), "ApertureStop", None),
		"CompensationRatio": (222, 2, (12, 0), (), "CompensationRatio", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		"_ApertureStop": (221, 2, (5, 0), (), "_ApertureStop", None),
		"_CompensationRatio": (223, 2, (5, 0), (), "_CompensationRatio", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"ApertureStop": ((220, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_ApertureStop": ((221, LCID, 4, 0),()),
		"_CompensationRatio": ((223, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IEpiLamp(DispatchBaseClass):
	'IEpiLamp Interface'
	CLSID = IID('{05952D05-F83A-49CB-8BB8-DE0E625284BD}')
	coclass_clsid = IID('{F5481148-DE7C-4DBA-A432-C761C6339B00}')

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def Off(self):
		'Turns the lamp off.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def On(self):
		'Turns the lamp on.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def SetVoltageForCamera(self):
		'Selects the appropriate lamp voltage for digital imaging.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsOn": (202, 2, (12, 0), (), "IsOn", None),
		"LampType": (232, 2, (12, 0), (), "LampType", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		"Voltage": (220, 2, (12, 0), (), "Voltage", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsOn": (203, 2, (3, 0), (), "_IsOn", None),
		"_LampType": (233, 2, (3, 0), (), "_LampType", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
		"_Voltage": (221, 2, (5, 0), (), "_Voltage", None),
	}
	_prop_map_put_ = {
		"IsOn": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"Voltage": ((220, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsOn": ((203, LCID, 4, 0),()),
		"_LampType": ((233, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
		"_Voltage": ((221, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IEpiShutter(DispatchBaseClass):
	'IEpiShutter Interface'
	CLSID = IID('{0C3DB625-1025-4E8B-B563-8D085C27C704}')
	coclass_clsid = IID('{58343FAD-ACC0-449D-B82E-2E0875F46591}')

	def Close(self):
		'Close the shutter for episcopic illumination.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def Open(self):
		'Open the shutter for episcopic illumination.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def OpenWithTimer(self, lTimer=defaultNamedNotOptArg):
		'Open shutter with timer.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((3, 1),),lTimer
			)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"FiberType": (232, 2, (12, 0), (), "FiberType", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsOpened": (202, 2, (12, 0), (), "IsOpened", None),
		"IsShutterOpen": (32, 2, (3, 0), (), "IsShutterOpen", None),
		"IsSupportedOpenWithTimer": (31, 2, (3, 0), (), "IsSupportedOpenWithTimer", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_FiberType": (233, 2, (3, 0), (), "_FiberType", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsOpened": (203, 2, (3, 0), (), "_IsOpened", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"IsOpened": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_FiberType": ((233, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsOpened": ((203, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFilterBlock(DispatchBaseClass):
	'IFilterBlock Interface'
	CLSID = IID('{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}')
	coclass_clsid = IID('{6892031F-DC07-4667-A4DA-C30D6D54F5FA}')

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"BarrierFilterCode": (37, 2, (3, 0), (), "BarrierFilterCode", None),
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (14, 2, (3, 0), (), "Code", None),
		"Composition": (31, 2, (36, 0), (), "Composition", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"DichroicMirrorCode": (36, 2, (3, 0), (), "DichroicMirrorCode", None),
		"ExcitationFilterCode": (35, 2, (3, 0), (), "ExcitationFilterCode", None),
		"FilterBlockData": (30, 2, (36, 0), (), "FilterBlockData", None),
		"FilterType": (34, 2, (3, 0), (), "FilterType", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (0, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"BarrierFilterCode": ((37, LCID, 4, 0),()),
		"Code": ((14, LCID, 4, 0),()),
		"Composition": ((31, LCID, 4, 0),()),
		"DichroicMirrorCode": ((36, LCID, 4, 0),()),
		"ExcitationFilterCode": ((35, LCID, 4, 0),()),
		"FilterBlockData": ((30, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Position'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Position", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFilterBlockCassette(DispatchBaseClass):
	'IFilterBlockCassette Interface'
	CLSID = IID('{D2695568-651D-4AA8-9D88-B74FC2E878B5}')
	coclass_clsid = IID('{6BAB6C19-4BB2-4063-82B5-F44C958EC878}')

	def DisableInterlock(self):
		'Disables the use of interlock presets for the nosepiece.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def EnableInterlock(self):
		'Enables the use of interlock presets for the nosepiece.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), (),)

	def Forward(self):
		'Rotates the cassette clockwise.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def Reverse(self):
		'Rotates the cassette counter-clockwise.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		# Method 'FilterBlocks' returns object of type 'IFilterBlocks'
		"FilterBlocks": (30, 2, (9, 0), (), "FilterBlocks", '{BBF77FB4-8F04-425E-87AD-985B4B9481DF}'),
		"IsInterlockEnabled": (222, 2, (12, 0), (), "IsInterlockEnabled", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Position": (202, 2, (12, 0), (), "Position", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsInterlockEnabled": (223, 2, (3, 0), (), "_IsInterlockEnabled", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_Position": (203, 2, (3, 0), (), "_Position", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"IsInterlockEnabled": ((222, LCID, 4, 0),()),
		"Position": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsInterlockEnabled": ((223, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_Position": ((203, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFilterBlocks(DispatchBaseClass):
	'IFilterBlocks Interface'
	CLSID = IID('{BBF77FB4-8F04-425E-87AD-985B4B9481DF}')
	coclass_clsid = IID('{DEE8D261-66BA-4A91-B19F-F07E21A53E51}')

	# Result is of type IFilterBlock
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified filter block in the barrier wheel.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}')
		return ret

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified filter block in the barrier wheel.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INDFilter(DispatchBaseClass):
	'INDFilter Interface'
	CLSID = IID('{42DCE3AB-488B-490A-83C2-00153CD925B2}')
	coclass_clsid = IID('{0359B876-5B67-4974-AB2A-E8720139E42D}')

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"FiberType": (232, 2, (12, 0), (), "FiberType", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Position": (222, 2, (12, 0), (), "Position", None),
		"Transmission": (220, 2, (12, 0), (), "Transmission", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_FiberType": (233, 2, (3, 0), (), "_FiberType", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_Position": (223, 2, (3, 0), (), "_Position", None),
		"_Transmission": (221, 2, (5, 0), (), "_Transmission", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"Position": ((222, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_FiberType": ((233, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_Position": ((223, LCID, 4, 0),()),
		"_Transmission": ((221, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class INikonLv(DispatchBaseClass):
	'INikonLv Interface'
	CLSID = IID('{C6AA054A-D7F4-46FA-A419-657D4BD4C2FF}')
	coclass_clsid = IID('{FF503DBE-D320-4074-9816-F97F9F1C6215}')

	def ClearPassword(self):
		'Clear a password for the microscope.'
		return self._oleobj_.InvokeTypes(69, LCID, 1, (24, 0), (),)

	def ClearSystemName(self):
		'Clear a user-defined name for the microscope.'
		return self._oleobj_.InvokeTypes(68, LCID, 1, (24, 0), (),)

	def DisableBuzzer(self):
		'Disables the buzzer for the specified controller.'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), (),)

	def DisableSwitch(self):
		'Disables the specified switch of a switch bank.'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (24, 0), (),)

	def EnableBuzzer(self):
		'Enables the buzzer for the specified controller.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), (),)

	def EnableSwitch(self):
		'Enables the specified switch of a switch bank.'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), (),)

	def GetData(self, strCommand=defaultNamedNotOptArg):
		'Sends a command to get 32-bit character data from a device.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(63, LCID, 1, (8, 0), ((8, 1),),strCommand
			)

	def GetData2(self, strCommand=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'Sends a command to get 32-bit character data from a device.'
		return self._ApplyTypes_(70, 1, (24, 0), ((8, 1), (16392, 2)), 'GetData2', None,strCommand
			, pVal)

	def IsBuzzerEnabled(self):
		'Determines if the buzzer is enabled for the specified controller.'
		return self._oleobj_.InvokeTypes(56, LCID, 1, (3, 0), (),)

	def IsSwitchEnabled(self):
		'Determines if the specified switch of a switch bank is on.'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (3, 0), (),)

	def ReadChecksum(self):
		'Reads the check sum of the specified controller.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(65, LCID, 1, (8, 0), (),)

	def ReadProgramName(self):
		'Reads the program name of the specified controller.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(66, LCID, 1, (8, 0), (),)

	def ReadVersion(self):
		'Reads the firmware version of the specified controller.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(52, LCID, 1, (8, 0), (),)

	def SendData(self, strCommand=defaultNamedNotOptArg):
		'Sends a command to the device to set a string property (32-bit character pointer).'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), ((8, 1),),strCommand
			)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		# Method 'DICPrism' returns object of type 'IDICPrism'
		"DICPrism": (36, 2, (9, 0), (), "DICPrism", '{40FCAC43-8012-4FDF-9083-D29B4372FC80}'),
		# Method 'Database' returns object of type 'IDatabase'
		"Database": (30, 2, (9, 0), (), "Database", '{C64C5896-AF8D-4520-B67F-E2C284A17015}'),
		# Method 'Device' returns object of type 'INikonLvDevice'
		"Device": (22, 2, (9, 0), (), "Device", '{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}'),
		# Method 'Devices' returns object of type 'INikonLvDevices'
		"Devices": (25, 2, (9, 0), (), "Devices", '{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}'),
		# Method 'DiaLamp' returns object of type 'IDiaLamp'
		"DiaLamp": (41, 2, (9, 0), (), "DiaLamp", '{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}'),
		# Method 'EpiApertureStop' returns object of type 'IEpiApertureStop'
		"EpiApertureStop": (46, 2, (9, 0), (), "EpiApertureStop", '{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}'),
		# Method 'EpiLamp' returns object of type 'IEpiLamp'
		"EpiLamp": (42, 2, (9, 0), (), "EpiLamp", '{05952D05-F83A-49CB-8BB8-DE0E625284BD}'),
		# Method 'EpiShutter' returns object of type 'IEpiShutter'
		"EpiShutter": (43, 2, (9, 0), (), "EpiShutter", '{0C3DB625-1025-4E8B-B563-8D085C27C704}'),
		# Method 'FilterBlockCassette' returns object of type 'IFilterBlockCassette'
		"FilterBlockCassette": (33, 2, (9, 0), (), "FilterBlockCassette", '{D2695568-651D-4AA8-9D88-B74FC2E878B5}'),
		"IsLocked": (64, 2, (3, 0), (), "IsLocked", None),
		# Method 'NDFilter' returns object of type 'INDFilter'
		"NDFilter": (44, 2, (9, 0), (), "NDFilter", '{42DCE3AB-488B-490A-83C2-00153CD925B2}'),
		# Method 'Nosepiece' returns object of type 'INosepiece'
		"Nosepiece": (71, 2, (9, 0), (), "Nosepiece", '{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}'),
		# Method 'Nosepiece1' returns object of type 'INosepiece1'
		"Nosepiece1": (31, 2, (9, 0), (), "Nosepiece1", '{AACCE357-70D3-4A64-B693-61ADE12FAF55}'),
		"Password": (67, 2, (8, 0), (), "Password", None),
		# Method 'Presets' returns object of type 'IPresets'
		"Presets": (72, 2, (9, 0), (), "Presets", '{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}'),
		# Method 'Presets1' returns object of type 'IPresets1'
		"Presets1": (61, 2, (9, 0), (), "Presets1", '{E30E636B-DA15-4CFA-8B91-61877484F743}'),
		"SystemName": (53, 2, (8, 0), (), "SystemName", None),
		"VersionOfSDK": (73, 2, (8, 0), (), "VersionOfSDK", None),
		# Method 'ZDrive' returns object of type 'IZDrive'
		"ZDrive": (34, 2, (9, 0), (), "ZDrive", '{962D3580-F901-4AC4-9CF3-49A1CE779E45}'),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"DICPrism": ((36, LCID, 4, 0),()),
		"Database": ((30, LCID, 4, 0),()),
		"Device": ((22, LCID, 4, 0),()),
		"DiaLamp": ((41, LCID, 4, 0),()),
		"EpiApertureStop": ((46, LCID, 4, 0),()),
		"EpiLamp": ((42, LCID, 4, 0),()),
		"EpiShutter": ((43, LCID, 4, 0),()),
		"FilterBlockCassette": ((33, LCID, 4, 0),()),
		"NDFilter": ((44, LCID, 4, 0),()),
		"Nosepiece": ((71, LCID, 4, 0),()),
		"Nosepiece1": ((31, LCID, 4, 0),()),
		"Password": ((67, LCID, 4, 0),()),
		"Presets": ((72, LCID, 4, 0),()),
		"Presets1": ((61, LCID, 4, 0),()),
		"SystemName": ((53, LCID, 4, 0),()),
		"ZDrive": ((34, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class INikonLv1(DispatchBaseClass):
	'INikonLv1 Interface'
	CLSID = IID('{712EC5D6-4EFA-4D5E-B5B3-01D8D2437DF7}')
	coclass_clsid = None

	def ClearPassword(self):
		'Clear a password for the microscope.'
		return self._oleobj_.InvokeTypes(69, LCID, 1, (24, 0), (),)

	def ClearSystemName(self):
		'Clear a user-defined name for the microscope.'
		return self._oleobj_.InvokeTypes(68, LCID, 1, (24, 0), (),)

	def DisableBuzzer(self):
		'Disables the buzzer for the specified controller.'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), (),)

	def DisableSwitch(self):
		'Disables the specified switch of a switch bank.'
		return self._oleobj_.InvokeTypes(55, LCID, 1, (24, 0), (),)

	def EnableBuzzer(self):
		'Enables the buzzer for the specified controller.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), (),)

	def EnableSwitch(self):
		'Enables the specified switch of a switch bank.'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), (),)

	def GetData(self, strCommand=defaultNamedNotOptArg):
		'Sends a command to get 32-bit character data from a device.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(63, LCID, 1, (8, 0), ((8, 1),),strCommand
			)

	def GetData2(self, strCommand=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'Sends a command to get 32-bit character data from a device.'
		return self._ApplyTypes_(70, 1, (24, 0), ((8, 1), (16392, 2)), 'GetData2', None,strCommand
			, pVal)

	def IsBuzzerEnabled(self):
		'Determines if the buzzer is enabled for the specified controller.'
		return self._oleobj_.InvokeTypes(56, LCID, 1, (3, 0), (),)

	def IsSwitchEnabled(self):
		'Determines if the specified switch of a switch bank is on.'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (3, 0), (),)

	def ReadChecksum(self):
		'Reads the check sum of the specified controller.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(65, LCID, 1, (8, 0), (),)

	def ReadProgramName(self):
		'Reads the program name of the specified controller.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(66, LCID, 1, (8, 0), (),)

	def ReadVersion(self):
		'Reads the firmware version of the specified controller.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(52, LCID, 1, (8, 0), (),)

	def SendData(self, strCommand=defaultNamedNotOptArg):
		'Sends a command to the device to set a string property (32-bit character pointer).'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), ((8, 1),),strCommand
			)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		# Method 'DICPrism' returns object of type 'IDICPrism'
		"DICPrism": (36, 2, (9, 0), (), "DICPrism", '{40FCAC43-8012-4FDF-9083-D29B4372FC80}'),
		# Method 'Database' returns object of type 'IDatabase'
		"Database": (30, 2, (9, 0), (), "Database", '{C64C5896-AF8D-4520-B67F-E2C284A17015}'),
		# Method 'Device' returns object of type 'INikonLvDevice'
		"Device": (22, 2, (9, 0), (), "Device", '{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}'),
		# Method 'Devices' returns object of type 'INikonLvDevices'
		"Devices": (25, 2, (9, 0), (), "Devices", '{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}'),
		# Method 'DiaLamp' returns object of type 'IDiaLamp'
		"DiaLamp": (41, 2, (9, 0), (), "DiaLamp", '{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}'),
		# Method 'EpiApertureStop' returns object of type 'IEpiApertureStop'
		"EpiApertureStop": (46, 2, (9, 0), (), "EpiApertureStop", '{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}'),
		# Method 'EpiLamp' returns object of type 'IEpiLamp'
		"EpiLamp": (42, 2, (9, 0), (), "EpiLamp", '{05952D05-F83A-49CB-8BB8-DE0E625284BD}'),
		# Method 'EpiShutter' returns object of type 'IEpiShutter'
		"EpiShutter": (43, 2, (9, 0), (), "EpiShutter", '{0C3DB625-1025-4E8B-B563-8D085C27C704}'),
		# Method 'FilterBlockCassette' returns object of type 'IFilterBlockCassette'
		"FilterBlockCassette": (33, 2, (9, 0), (), "FilterBlockCassette", '{D2695568-651D-4AA8-9D88-B74FC2E878B5}'),
		"IsLocked": (64, 2, (3, 0), (), "IsLocked", None),
		# Method 'NDFilter' returns object of type 'INDFilter'
		"NDFilter": (44, 2, (9, 0), (), "NDFilter", '{42DCE3AB-488B-490A-83C2-00153CD925B2}'),
		# Method 'Nosepiece1' returns object of type 'INosepiece1'
		"Nosepiece1": (31, 2, (9, 0), (), "Nosepiece1", '{AACCE357-70D3-4A64-B693-61ADE12FAF55}'),
		"Password": (67, 2, (8, 0), (), "Password", None),
		# Method 'Presets1' returns object of type 'IPresets1'
		"Presets1": (61, 2, (9, 0), (), "Presets1", '{E30E636B-DA15-4CFA-8B91-61877484F743}'),
		"SystemName": (53, 2, (8, 0), (), "SystemName", None),
		# Method 'ZDrive' returns object of type 'IZDrive'
		"ZDrive": (34, 2, (9, 0), (), "ZDrive", '{962D3580-F901-4AC4-9CF3-49A1CE779E45}'),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"DICPrism": ((36, LCID, 4, 0),()),
		"Database": ((30, LCID, 4, 0),()),
		"Device": ((22, LCID, 4, 0),()),
		"DiaLamp": ((41, LCID, 4, 0),()),
		"EpiApertureStop": ((46, LCID, 4, 0),()),
		"EpiLamp": ((42, LCID, 4, 0),()),
		"EpiShutter": ((43, LCID, 4, 0),()),
		"FilterBlockCassette": ((33, LCID, 4, 0),()),
		"NDFilter": ((44, LCID, 4, 0),()),
		"Nosepiece1": ((31, LCID, 4, 0),()),
		"Password": ((67, LCID, 4, 0),()),
		"Presets1": ((61, LCID, 4, 0),()),
		"SystemName": ((53, LCID, 4, 0),()),
		"ZDrive": ((34, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class INikonLvDevice(DispatchBaseClass):
	'INikonLvDevice Interface'
	CLSID = IID('{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}')
	coclass_clsid = IID('{4193F944-5653-4A37-BB45-23C53BF3D8D2}')

	def Connect(self):
		'Connects to a device.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def Disconnect(self):
		'Disconnects from a device.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def GetLongData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'Sends a command to get 32-bit integer data from a device.'
		return self._ApplyTypes_(22, 1, (24, 0), ((8, 1), (8, 1), (16387, 3)), 'GetLongData', None,LockCookie
			, strCommand, pVal)

	def GetStatusData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'Sends a command to get a device property as StatusUnknown, StatusTrue or StatusFalse.'
		return self._ApplyTypes_(21, 1, (24, 0), ((8, 1), (8, 1), (16387, 3)), 'GetStatusData', None,LockCookie
			, strCommand, pVal)

	def GetStringData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'Sends a command to get 32-bit character data from a device.'
		return self._ApplyTypes_(20, 1, (24, 0), ((8, 1), (8, 1), (16392, 3)), 'GetStringData', None,LockCookie
			, strCommand, pVal)

	def SendLongData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, lArgument=defaultNamedNotOptArg):
		'Sends a command to set a device property to a 32-bit integer.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),LockCookie
			, strCommand, lArgument)

	def SendStatusData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, statusArgument=defaultNamedNotOptArg):
		'Sends a command to set a device property to StatusTrue or StatusFalse.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),LockCookie
			, strCommand, statusArgument)

	def SendStringData(self, LockCookie=defaultNamedNotOptArg, strCommand=defaultNamedNotOptArg, strArgument=defaultNamedNotOptArg):
		'Sends a command to set a string property using a 32-bit character pointer property.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1)),LockCookie
			, strCommand, strArgument)

	def WaitForDevice(self, lMaxTimeouts=defaultNamedNotOptArg):
		'Waits until all commands have completed.'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (3, 0), ((3, 1),),lMaxTimeouts
			)

	def _CalcNaCrossMag(self, nNosepiece=defaultNamedNotOptArg):
		'Hidden method to Calc Na * Mag'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (5, 0), ((3, 1),),nNosepiece
			)

	def _ReadStatusValue(self, offset=defaultNamedNotOptArg):
		'Hidden method to read Status from Device Data'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (3, 0), ((3, 1),),offset
			)

	def _ResetWait(self):
		'Hidden method to reset the wait counter used by WaitForDevice.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Address": (1, 2, (8, 0), (), "Address", None),
		"Connected": (12, 2, (3, 0), (), "Connected", None),
		"DeviceIndex": (43, 2, (3, 0), (), "DeviceIndex", None),
		"Index": (44, 2, (3, 0), (), "Index", None),
		"IsAvailable": (37, 2, (3, 0), (), "IsAvailable", None),
		"IsSimulation": (38, 2, (3, 0), (), "IsSimulation", None),
		"LastResponse": (15, 2, (8, 0), (), "LastResponse", None),
		"LvDeviceType": (84, 2, (12, 0), (), "LvDeviceType", None),
		"Overlapped": (34, 2, (3, 0), (), "Overlapped", None),
		"_LvDeviceType": (85, 2, (3, 0), (), "_LvDeviceType", None),
	}
	_prop_map_put_ = {
		"Connected": ((12, LCID, 4, 0),()),
		"Overlapped": ((34, LCID, 4, 0),()),
		"_LvDeviceType": ((85, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class INikonLvDevices(DispatchBaseClass):
	'INikonLvDevices Interface'
	CLSID = IID('{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}')
	coclass_clsid = IID('{04CC91ED-5553-46C5-89C3-FCDFCAD3CED3}')

	# Result is of type INikonLvDevice
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Index=defaultNamedNotOptArg):
		'The specified device in the list of available Nikon Lv devices.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}')
		return ret

	def Refresh(self):
		'Hidden method to update the device list.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'The specified device in the list of available Nikon Lv devices.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INosepiece(DispatchBaseClass):
	'INosepiece Interface'
	CLSID = IID('{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}')
	coclass_clsid = IID('{DB3D3ADF-C358-4A0C-9CDD-5E947310C788}')

	def DisableInterlock(self):
		'Disables the use of interlock presets for the nosepiece.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def EnableInterlock(self):
		'Enables the use of interlock presets for the nosepiece.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), (),)

	def Forward(self):
		'Rotates the cassette clockwise.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def LimitedReverse(self):
		'Rotates the cassette counter-clockwise.'
		return self._oleobj_.InvokeTypes(224, LCID, 1, (24, 0), (),)

	def Reverse(self):
		'Rotates the cassette counter-clockwise.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsInterlockEnabled": (222, 2, (12, 0), (), "IsInterlockEnabled", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsNosepieceControlError": (33, 2, (3, 0), (), "IsNosepieceControlError", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"NosepieceControl": (220, 2, (12, 0), (), "NosepieceControl", None),
		# Method 'Objectives' returns object of type 'IObjectives'
		"Objectives": (30, 2, (9, 0), (), "Objectives", '{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}'),
		"Position": (202, 2, (12, 0), (), "Position", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsInterlockEnabled": (223, 2, (3, 0), (), "_IsInterlockEnabled", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_NosepieceControl": (221, 2, (3, 0), (), "_NosepieceControl", None),
		"_Position": (203, 2, (3, 0), (), "_Position", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"IsInterlockEnabled": ((222, LCID, 4, 0),()),
		"NosepieceControl": ((220, LCID, 4, 0),()),
		"Position": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsInterlockEnabled": ((223, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_NosepieceControl": ((221, LCID, 4, 0),()),
		"_Position": ((203, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class INosepiece1(DispatchBaseClass):
	'INosepiece1 Interface'
	CLSID = IID('{AACCE357-70D3-4A64-B693-61ADE12FAF55}')
	coclass_clsid = None

	def DisableInterlock(self):
		'Disables the use of interlock presets for the nosepiece.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def EnableInterlock(self):
		'Enables the use of interlock presets for the nosepiece.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), (),)

	def Forward(self):
		'Rotates the cassette clockwise.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def Reverse(self):
		'Rotates the cassette counter-clockwise.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsInterlockEnabled": (222, 2, (12, 0), (), "IsInterlockEnabled", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsNosepieceControlError": (33, 2, (3, 0), (), "IsNosepieceControlError", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"NosepieceControl": (220, 2, (12, 0), (), "NosepieceControl", None),
		# Method 'Objectives' returns object of type 'IObjectives'
		"Objectives": (30, 2, (9, 0), (), "Objectives", '{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}'),
		"Position": (202, 2, (12, 0), (), "Position", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsInterlockEnabled": (223, 2, (3, 0), (), "_IsInterlockEnabled", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_NosepieceControl": (221, 2, (3, 0), (), "_NosepieceControl", None),
		"_Position": (203, 2, (3, 0), (), "_Position", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"IsInterlockEnabled": ((222, LCID, 4, 0),()),
		"NosepieceControl": ((220, LCID, 4, 0),()),
		"Position": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsInterlockEnabled": ((223, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_NosepieceControl": ((221, LCID, 4, 0),()),
		"_Position": ((203, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IObjective(DispatchBaseClass):
	'IObjective Interface'
	CLSID = IID('{5AB19F95-28DE-425F-835B-46F3DB18E34C}')
	coclass_clsid = IID('{89608928-C071-429E-9238-18D7218912F0}')

	def SetObjectiveData(self, lObjectiveModel=defaultNamedNotOptArg, lObjectiveType=defaultNamedNotOptArg, dMagnification=defaultNamedNotOptArg, dWorkingDistance=defaultNamedNotOptArg
			, dNumericalAperture=defaultNamedNotOptArg, lCondenserType=defaultNamedNotOptArg, lDICPrismPosition=defaultNamedNotOptArg):
		'Sets the properties of this objective.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1), (5, 1), (5, 1), (3, 1), (3, 1)),lObjectiveModel
			, lObjectiveType, dMagnification, dWorkingDistance, dNumericalAperture, lCondenserType
			, lDICPrismPosition)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (14, 2, (3, 0), (), "Code", None),
		"CondenserType": (41, 2, (3, 0), (), "CondenserType", None),
		"DICPrismPosition": (42, 2, (3, 0), (), "DICPrismPosition", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Description": (31, 2, (8, 0), (), "Description", None),
		"Magnification": (34, 2, (5, 0), (), "Magnification", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"NumericalAperture": (35, 2, (5, 0), (), "NumericalAperture", None),
		"ObjectiveData": (37, 2, (36, 0), (), "ObjectiveData", None),
		"ObjectiveModel": (39, 2, (3, 0), (), "ObjectiveModel", None),
		"ObjectiveType": (38, 2, (3, 0), (), "ObjectiveType", None),
		"Position": (0, 2, (3, 0), (), "Position", None),
		"WorkingDistance": (36, 2, (5, 0), (), "WorkingDistance", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Code": ((14, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"ObjectiveData": ((37, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Position'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Position", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IObjectives(DispatchBaseClass):
	'IObjectives Interface'
	CLSID = IID('{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}')
	coclass_clsid = IID('{C394D185-D859-42BE-95D9-42FE36DB051D}')

	# Result is of type IObjective
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, lIndex=defaultNamedNotOptArg):
		'The specified objective in the barrier wheel.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5AB19F95-28DE-425F-835B-46F3DB18E34C}')
		return ret

	_prop_map_get_ = {
		"Count": (31, 2, (3, 0), (), "Count", None),
		# Method '_NewEnum' returns object of type 'IEnumVARIANT'
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, lIndex=defaultNamedNotOptArg):
		'The specified objective in the barrier wheel.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5AB19F95-28DE-425F-835B-46F3DB18E34C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(31, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPort(DispatchBaseClass):
	'Port settings for Nikon Instruments.'
	CLSID = IID('{514DCB75-DF97-4DFA-8407-CE33D6D558F4}')
	coclass_clsid = None

	def Connect(self):
		'Connects to a device.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def Disconnect(self):
		'Disconnects from a device.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Address": (1, 2, (8, 0), (), "Address", None),
		"Connected": (12, 2, (3, 0), (), "Connected", None),
		"LastResponse": (15, 2, (8, 0), (), "LastResponse", None),
	}
	_prop_map_put_ = {
		"Connected": ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPositionAccessory(DispatchBaseClass):
	'IPositionAccessory Interface'
	CLSID = IID('{44CB7864-5C26-4F35-8CF8-BBA8CC885A14}')
	coclass_clsid = None

	def MoveAbsolute(self, Pos=defaultNamedNotOptArg):
		'Moves the stage to a specified z-axis position.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 1),),Pos
			)

	def MoveRelative(self, Pos=defaultNamedNotOptArg):
		'Moves the stage to a specified z-axis position.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((3, 1),),Pos
			)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"Limitation": (208, 2, (12, 0), (), "Limitation", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Position": (202, 2, (12, 0), (), "Position", None),
		"Speed": (204, 2, (12, 0), (), "Speed", None),
		"Tolerance": (206, 2, (12, 0), (), "Tolerance", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_Limitation": (209, 2, (3, 0), (), "_Limitation", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_Position": (203, 2, (5, 0), (), "_Position", None),
		"_Speed": (205, 2, (3, 0), (), "_Speed", None),
		"_Tolerance": (207, 2, (3, 0), (), "_Tolerance", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"Speed": ((204, LCID, 4, 0),()),
		"Tolerance": ((206, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_Limitation": ((209, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_Position": ((203, LCID, 4, 0),()),
		"_Speed": ((205, LCID, 4, 0),()),
		"_Tolerance": ((207, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPresets(DispatchBaseClass):
	'IPresets Interface'
	CLSID = IID('{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}')
	coclass_clsid = IID('{792D4C23-39C9-46C9-A664-D9D5A552EA9D}')

	def AdjustMemorizedPresets(self, Accessory=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def AdjustMemorizedPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def AdjustUserPresets(self, Accessory=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def AdjustUserPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def ApplyPresets(self, ObservationMode=defaultNamedNotOptArg):
		'Moves microscope accessories to preset positions by setting the observation mode.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((3, 1),),ObservationMode
			)

	def GetLastValue(self, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, pdEPI=pythoncom.Missing, pdDIA=pythoncom.Missing
			, pdEpiApertureStop=pythoncom.Missing):
		'Gets the last value of preset.'
		return self._ApplyTypes_(427, 1, (24, 0), ((3, 1), (3, 1), (16389, 2), (16389, 2), (16389, 2)), 'GetLastValue', None,ObservationMode
			, ObjectivePosition, pdEPI, pdDIA, pdEpiApertureStop)

	def InitializeMemorizedPresets(self, Accessory=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def InitializeMemorizedPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def InitializeUserPresets(self, Accessory=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def InitializeUserPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def IsDefault(self, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the type of preset is default.'
		return self._oleobj_.InvokeTypes(425, LCID, 1, (3, 0), ((3, 1), (3, 1)),ObservationMode
			, ObjectivePosition)

	def ReadDefaultPresets(self, Accessory=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the default value for the specified accessory given an observation mode and an objective position.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (5, 0), ((3, 1), (3, 1)),Accessory
			, ObjectivePosition)

	def ReadInterlockMode(self, Accessory=defaultNamedNotOptArg):
		'Reads the interlock mode.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (3, 0), ((3, 1),),Accessory
			)

	def ReadLampPresets(self, ObservationMode=defaultNamedNotOptArg, pLampPreset=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(39, 1, (24, 0), ((3, 1), (16387, 2)), 'ReadLampPresets', None,ObservationMode
			, pLampPreset)

	def ReadMemorizedPresets(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the memorized value for the specified accessory given an observation mode and an objective position.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (5, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def ReadPresetModes(self, ObservationMode=defaultNamedNotOptArg, pOptionalObservationMode=pythoncom.Missing, pInterlock=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(35, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2)), 'ReadPresetModes', None,ObservationMode
			, pOptionalObservationMode, pInterlock)

	def ReadPresetModesEx(self, ObservationMode=defaultNamedNotOptArg, pOptionalObservationMode=pythoncom.Missing, pInterlock=pythoncom.Missing, pObjectivePosition=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(209, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2)), 'ReadPresetModesEx', None,ObservationMode
			, pOptionalObservationMode, pInterlock, pObjectivePosition)

	def ReadPresets(self, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, pIlluminantPresets=pythoncom.Missing, pAperturePresets=pythoncom.Missing
			, pFilterPosition=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(429, 1, (24, 0), ((3, 1), (3, 1), (16387, 2), (16387, 2), (16387, 2)), 'ReadPresets', None,ObservationMode
			, ObjectivePosition, pIlluminantPresets, pAperturePresets, pFilterPosition)

	def ReadUserPresets(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the memorized value for the specified accessory given an observation mode and an objective position.'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (5, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def SetInterlockMode(self, Accessory=defaultNamedNotOptArg, lMode=defaultNamedNotOptArg):
		'Sets the interlock mode.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), ((3, 1), (3, 1)),Accessory
			, lMode)

	def SetLampPresets(self, ObservationMode=defaultNamedNotOptArg, LampPreset=defaultNamedNotOptArg):
		'Sets the type of preset that will be used for each accessory when a custom observation mode is selected.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((3, 1), (3, 1)),ObservationMode
			, LampPreset)

	def SetLastValue(self, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, dEPI=defaultNamedNotOptArg, dDIA=defaultNamedNotOptArg
			, dEpiApertureStop=defaultNamedNotOptArg):
		'Sets the last value of preset.'
		return self._oleobj_.InvokeTypes(426, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1), (5, 1), (5, 1)),ObservationMode
			, ObjectivePosition, dEPI, dDIA, dEpiApertureStop)

	def SetMemorizedPresets(self, Accessory=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((3, 1), (5, 1)),Accessory
			, dValue)

	def SetMemorizedPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1)),Accessory
			, ObservationMode, ObjectivePosition, dValue)

	def SetPresetModes(self, ObservationMode=defaultNamedNotOptArg, OptionalObservationMode=defaultNamedNotOptArg, Interlock=defaultNamedNotOptArg):
		'Sets the type of preset that will be used for each accessory when a custom observation mode is selected.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),ObservationMode
			, OptionalObservationMode, Interlock)

	def SetPresetModesEx(self, ObservationMode=defaultNamedNotOptArg, OptionalObservationMode=defaultNamedNotOptArg, Interlock=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Sets the type of preset that will be used for each accessory when a custom observation mode is selected.'
		return self._oleobj_.InvokeTypes(208, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),ObservationMode
			, OptionalObservationMode, Interlock, ObjectivePosition)

	def SetPresets(self, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, IlluminantPresets=defaultNamedNotOptArg, AperturePresets=defaultNamedNotOptArg
			, FilterPosition=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(428, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),ObservationMode
			, ObjectivePosition, IlluminantPresets, AperturePresets, FilterPosition)

	def SetPresetsToDefault(self, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Sets the type of preset to default.'
		return self._oleobj_.InvokeTypes(424, LCID, 1, (24, 0), ((3, 1), (3, 1)),ObservationMode
			, ObjectivePosition)

	def SetUserPresets(self, Accessory=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (24, 0), ((3, 1), (5, 1)),Accessory
			, dValue)

	def SetUserPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1)),Accessory
			, ObservationMode, ObjectivePosition, dValue)

	def UpdateObservationInfo(self):
		'Sets the interlock mode.'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"AfObservationMode": (420, 2, (12, 0), (), "AfObservationMode", None),
		"AfRecipeMode": (422, 2, (12, 0), (), "AfRecipeMode", None),
		"EpiDiaLampMode": (204, 2, (12, 0), (), "EpiDiaLampMode", None),
		"InitialMode": (206, 2, (12, 0), (), "InitialMode", None),
		"ObservationMode": (202, 2, (12, 0), (), "ObservationMode", None),
		"_AfObservationMode": (421, 2, (3, 0), (), "_AfObservationMode", None),
		"_AfRecipeMode": (423, 2, (3, 0), (), "_AfRecipeMode", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_EpiDiaLampMode": (205, 2, (3, 0), (), "_EpiDiaLampMode", None),
		"_InitialMode": (207, 2, (3, 0), (), "_InitialMode", None),
		"_ObservationMode": (203, 2, (3, 0), (), "_ObservationMode", None),
	}
	_prop_map_put_ = {
		"AfObservationMode": ((420, LCID, 4, 0),()),
		"AfRecipeMode": ((422, LCID, 4, 0),()),
		"EpiDiaLampMode": ((204, LCID, 4, 0),()),
		"InitialMode": ((206, LCID, 4, 0),()),
		"ObservationMode": ((202, LCID, 4, 0),()),
		"_AfObservationMode": ((421, LCID, 4, 0),()),
		"_AfRecipeMode": ((423, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_EpiDiaLampMode": ((205, LCID, 4, 0),()),
		"_InitialMode": ((207, LCID, 4, 0),()),
		"_ObservationMode": ((203, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPresets1(DispatchBaseClass):
	'IPresets1 Interface'
	CLSID = IID('{E30E636B-DA15-4CFA-8B91-61877484F743}')
	coclass_clsid = None

	def AdjustMemorizedPresets(self, Accessory=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def AdjustMemorizedPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def AdjustUserPresets(self, Accessory=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def AdjustUserPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Adjusts the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def ApplyPresets(self, ObservationMode=defaultNamedNotOptArg):
		'Moves microscope accessories to preset positions by setting the observation mode.'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((3, 1),),ObservationMode
			)

	def InitializeMemorizedPresets(self, Accessory=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def InitializeMemorizedPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def InitializeUserPresets(self, Accessory=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (24, 0), ((3, 1),),Accessory
			)

	def InitializeUserPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Initialize the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def ReadDefaultPresets(self, Accessory=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the default value for the specified accessory given an observation mode and an objective position.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (5, 0), ((3, 1), (3, 1)),Accessory
			, ObjectivePosition)

	def ReadInterlockMode(self, Accessory=defaultNamedNotOptArg):
		'Reads the interlock mode.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (3, 0), ((3, 1),),Accessory
			)

	def ReadLampPresets(self, ObservationMode=defaultNamedNotOptArg, pLampPreset=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(39, 1, (24, 0), ((3, 1), (16387, 2)), 'ReadLampPresets', None,ObservationMode
			, pLampPreset)

	def ReadMemorizedPresets(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the memorized value for the specified accessory given an observation mode and an objective position.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (5, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def ReadPresetModes(self, ObservationMode=defaultNamedNotOptArg, pOptionalObservationMode=pythoncom.Missing, pInterlock=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(35, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2)), 'ReadPresetModes', None,ObservationMode
			, pOptionalObservationMode, pInterlock)

	def ReadPresetModesEx(self, ObservationMode=defaultNamedNotOptArg, pOptionalObservationMode=pythoncom.Missing, pInterlock=pythoncom.Missing, pObjectivePosition=pythoncom.Missing):
		'Reads the type of preset that is used for each accessory for the specified observation mode.'
		return self._ApplyTypes_(209, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2)), 'ReadPresetModesEx', None,ObservationMode
			, pOptionalObservationMode, pInterlock, pObjectivePosition)

	def ReadUserPresets(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Gets the memorized value for the specified accessory given an observation mode and an objective position.'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (5, 0), ((3, 1), (3, 1), (3, 1)),Accessory
			, ObservationMode, ObjectivePosition)

	def SetInterlockMode(self, Accessory=defaultNamedNotOptArg, lMode=defaultNamedNotOptArg):
		'Sets the interlock mode.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), ((3, 1), (3, 1)),Accessory
			, lMode)

	def SetLampPresets(self, ObservationMode=defaultNamedNotOptArg, LampPreset=defaultNamedNotOptArg):
		'Sets the type of preset that will be used for each accessory when a custom observation mode is selected.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((3, 1), (3, 1)),ObservationMode
			, LampPreset)

	def SetMemorizedPresets(self, Accessory=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((3, 1), (5, 1)),Accessory
			, dValue)

	def SetMemorizedPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1)),Accessory
			, ObservationMode, ObjectivePosition, dValue)

	def SetPresetModes(self, ObservationMode=defaultNamedNotOptArg, OptionalObservationMode=defaultNamedNotOptArg, Interlock=defaultNamedNotOptArg):
		'Sets the type of preset that will be used for each accessory when a custom observation mode is selected.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),ObservationMode
			, OptionalObservationMode, Interlock)

	def SetPresetModesEx(self, ObservationMode=defaultNamedNotOptArg, OptionalObservationMode=defaultNamedNotOptArg, Interlock=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg):
		'Sets the type of preset that will be used for each accessory when a custom observation mode is selected.'
		return self._oleobj_.InvokeTypes(208, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),ObservationMode
			, OptionalObservationMode, Interlock, ObjectivePosition)

	def SetUserPresets(self, Accessory=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (24, 0), ((3, 1), (5, 1)),Accessory
			, dValue)

	def SetUserPresetsEx(self, Accessory=defaultNamedNotOptArg, ObservationMode=defaultNamedNotOptArg, ObjectivePosition=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg):
		'Sets the presets for the current observation mode based on the current optics.'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1)),Accessory
			, ObservationMode, ObjectivePosition, dValue)

	def UpdateObservationInfo(self):
		'Sets the interlock mode.'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"AfObservationMode": (420, 2, (12, 0), (), "AfObservationMode", None),
		"AfRecipeMode": (422, 2, (12, 0), (), "AfRecipeMode", None),
		"EpiDiaLampMode": (204, 2, (12, 0), (), "EpiDiaLampMode", None),
		"InitialMode": (206, 2, (12, 0), (), "InitialMode", None),
		"ObservationMode": (202, 2, (12, 0), (), "ObservationMode", None),
		"_AfObservationMode": (421, 2, (3, 0), (), "_AfObservationMode", None),
		"_AfRecipeMode": (423, 2, (3, 0), (), "_AfRecipeMode", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_EpiDiaLampMode": (205, 2, (3, 0), (), "_EpiDiaLampMode", None),
		"_InitialMode": (207, 2, (3, 0), (), "_InitialMode", None),
		"_ObservationMode": (203, 2, (3, 0), (), "_ObservationMode", None),
	}
	_prop_map_put_ = {
		"AfObservationMode": ((420, LCID, 4, 0),()),
		"AfRecipeMode": ((422, LCID, 4, 0),()),
		"EpiDiaLampMode": ((204, LCID, 4, 0),()),
		"InitialMode": ((206, LCID, 4, 0),()),
		"ObservationMode": ((202, LCID, 4, 0),()),
		"_AfObservationMode": ((421, LCID, 4, 0),()),
		"_AfRecipeMode": ((423, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_EpiDiaLampMode": ((205, LCID, 4, 0),()),
		"_InitialMode": ((207, LCID, 4, 0),()),
		"_ObservationMode": ((203, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IScopeAccessory(DispatchBaseClass):
	'IScopeAccessory Interface'
	CLSID = IID('{E81BC383-036A-457F-AAF1-DA6836A688BB}')
	coclass_clsid = None

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IShutterAccessory(DispatchBaseClass):
	'IShutterAccessory Interface'
	CLSID = IID('{854DA829-1CE9-44D0-8EC6-831CD1F4D13D}')
	coclass_clsid = None

	def Close(self):
		'Close the shutter for episcopic illumination.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def Open(self):
		'Open the shutter for episcopic illumination.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsOpened": (202, 2, (12, 0), (), "IsOpened", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsOpened": (203, 2, (3, 0), (), "_IsOpened", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"IsOpened": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsOpened": ((203, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITurretAccessory(DispatchBaseClass):
	'ITurretAccessory Interface'
	CLSID = IID('{11096D75-7F3D-47DA-AB61-CE84840E6D0C}')
	coclass_clsid = None

	def Forward(self):
		'Rotates the cassette clockwise.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def Reverse(self):
		'Rotates the cassette counter-clockwise.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Position": (202, 2, (12, 0), (), "Position", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_Position": (203, 2, (3, 0), (), "_Position", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"Position": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_Position": ((203, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVolumeAccessory(DispatchBaseClass):
	'IVolumeAccessory Interface'
	CLSID = IID('{1465605C-A9EC-414A-8205-F98C782243DE}')
	coclass_clsid = None

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVolumeAccessory2(DispatchBaseClass):
	'IVolumeAccessory Interface'
	CLSID = IID('{C159095B-7FDE-496B-B47F-9749DA5F4ECB}')
	coclass_clsid = None

	def Decrease(self):
		'Decreases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def Increase(self):
		'Increases the lamp voltage by one step.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def Off(self):
		'Turns the lamp off.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def On(self):
		'Turns the lamp on.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsOn": (202, 2, (12, 0), (), "IsOn", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsOn": (203, 2, (3, 0), (), "_IsOn", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
	}
	_prop_map_put_ = {
		"IsOn": ((202, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsOn": ((203, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IZDrive(DispatchBaseClass):
	'IZDrive Interface'
	CLSID = IID('{962D3580-F901-4AC4-9CF3-49A1CE779E45}')
	coclass_clsid = IID('{F79F5221-2326-4AE4-812A-83B7CE69CDB3}')

	def AbortZ(self):
		'Stop if Z-Drive moving.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def CurrentToSoftwareLowerLimit(self):
		'Set current position to software lower limit.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), (),)

	def CurrentToSoftwareUpperLimit(self):
		'Set current position to software upper limit.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), (),)

	def InitSoftwareLowerLimit(self):
		'Initialize software lower limit.'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), (),)

	def InitSoftwareUpperLimit(self):
		'Initialize software upper limit.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), (),)

	def MoveAbsolute(self, Pos=defaultNamedNotOptArg):
		'Moves the stage to a specified z-axis position.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 1),),Pos
			)

	def MoveRelative(self, Pos=defaultNamedNotOptArg):
		'Moves the stage to a specified z-axis position.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((3, 1),),Pos
			)

	def Refocus(self):
		'Refocuses after replacing a slide.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), (),)

	def SearchAF(self, lValue=defaultNamedNotOptArg):
		'Start AF search.'
		return self._oleobj_.InvokeTypes(235, LCID, 1, (24, 0), ((3, 1),),lValue
			)

	def StopAF(self):
		'Stop AF search.'
		return self._oleobj_.InvokeTypes(236, LCID, 1, (24, 0), (),)

	def ZEscape(self):
		'Repositions the stage to allow a slide to be replaced.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), (),)

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"AF": (468, 2, (12, 0), (), "AF", None),
		"AfOffset": (474, 2, (12, 0), (), "AfOffset", None),
		"AfOffsetMode": (478, 2, (12, 0), (), "AfOffsetMode", None),
		"AfSearchMode": (480, 2, (12, 0), (), "AfSearchMode", None),
		"AfStatus": (466, 2, (12, 0), (), "AfStatus", None),
		"IsAfSearch": (476, 2, (12, 0), (), "IsAfSearch", None),
		"IsMounted": (200, 2, (12, 0), (), "IsMounted", None),
		"IsSupportedAF": (45, 2, (3, 0), (), "IsSupportedAF", None),
		"IsZEscape": (230, 2, (12, 0), (), "IsZEscape", None),
		"Limitation": (208, 2, (12, 0), (), "Limitation", None),
		"LowerLimit": (194, 2, (12, 0), (), "LowerLimit", None),
		"Name": (11, 2, (8, 0), (), "Name", None),
		"Position": (202, 2, (12, 0), (), "Position", None),
		"SoftwareLowerLimit": (226, 2, (12, 0), (), "SoftwareLowerLimit", None),
		"SoftwareUpperLimit": (228, 2, (12, 0), (), "SoftwareUpperLimit", None),
		"Speed": (204, 2, (12, 0), (), "Speed", None),
		"Tolerance": (206, 2, (12, 0), (), "Tolerance", None),
		"Type": (10, 2, (3, 0), (), "Type", None),
		"Unit": (12, 2, (8, 0), (), "Unit", None),
		"UpperLimit": (196, 2, (12, 0), (), "UpperLimit", None),
		"Value": (192, 2, (12, 0), (), "Value", None),
		"ValuePerUnit": (198, 2, (12, 0), (), "ValuePerUnit", None),
		"ZDriveType": (232, 2, (12, 0), (), "ZDriveType", None),
		"_AF": (469, 2, (3, 0), (), "_AF", None),
		"_AfOffset": (475, 2, (3, 0), (), "_AfOffset", None),
		"_AfOffsetMode": (479, 2, (3, 0), (), "_AfOffsetMode", None),
		"_AfSearchMode": (481, 2, (3, 0), (), "_AfSearchMode", None),
		"_AfStatus": (467, 2, (3, 0), (), "_AfStatus", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
		"_IsAfSearch": (477, 2, (3, 0), (), "_IsAfSearch", None),
		"_IsMounted": (201, 2, (3, 0), (), "_IsMounted", None),
		"_IsZEscape": (231, 2, (3, 0), (), "_IsZEscape", None),
		"_Limitation": (209, 2, (3, 0), (), "_Limitation", None),
		"_LowerLimit": (195, 2, (3, 0), (), "_LowerLimit", None),
		"_Position": (203, 2, (5, 0), (), "_Position", None),
		"_SoftwareLowerLimit": (227, 2, (3, 0), (), "_SoftwareLowerLimit", None),
		"_SoftwareUpperLimit": (229, 2, (3, 0), (), "_SoftwareUpperLimit", None),
		"_Speed": (205, 2, (3, 0), (), "_Speed", None),
		"_Tolerance": (207, 2, (3, 0), (), "_Tolerance", None),
		"_UpperLimit": (197, 2, (3, 0), (), "_UpperLimit", None),
		"_Value": (193, 2, (3, 0), (), "_Value", None),
		"_ValuePerUnit": (199, 2, (3, 0), (), "_ValuePerUnit", None),
		"_ZDriveType": (233, 2, (3, 0), (), "_ZDriveType", None),
	}
	_prop_map_put_ = {
		"AF": ((468, LCID, 4, 0),()),
		"AfOffset": ((474, LCID, 4, 0),()),
		"AfOffsetMode": ((478, LCID, 4, 0),()),
		"AfStatus": ((466, LCID, 4, 0),()),
		"IsZEscape": ((230, LCID, 4, 0),()),
		"SoftwareLowerLimit": ((226, LCID, 4, 0),()),
		"SoftwareUpperLimit": ((228, LCID, 4, 0),()),
		"Speed": ((204, LCID, 4, 0),()),
		"Tolerance": ((206, LCID, 4, 0),()),
		"Value": ((192, LCID, 4, 0),()),
		"_AF": ((469, LCID, 4, 0),()),
		"_AfOffset": ((475, LCID, 4, 0),()),
		"_AfOffsetMode": ((479, LCID, 4, 0),()),
		"_AfSearchMode": ((481, LCID, 4, 0),()),
		"_AfStatus": ((467, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
		"_IsAfSearch": ((477, LCID, 4, 0),()),
		"_IsMounted": ((201, LCID, 4, 0),()),
		"_IsZEscape": ((231, LCID, 4, 0),()),
		"_Limitation": ((209, LCID, 4, 0),()),
		"_LowerLimit": ((195, LCID, 4, 0),()),
		"_Position": ((203, LCID, 4, 0),()),
		"_SoftwareLowerLimit": ((227, LCID, 4, 0),()),
		"_SoftwareUpperLimit": ((229, LCID, 4, 0),()),
		"_Speed": ((205, LCID, 4, 0),()),
		"_Tolerance": ((207, LCID, 4, 0),()),
		"_UpperLimit": ((197, LCID, 4, 0),()),
		"_Value": ((193, LCID, 4, 0),()),
		"_ValuePerUnit": ((199, LCID, 4, 0),()),
		"_ZDriveType": ((233, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(192, 2, (12, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IDbElement(DispatchBaseClass):
	'Hidden IDbElement Interface'
	CLSID = IID('{7A43F152-ECFA-4552-8F9F-743739747E2E}')
	coclass_clsid = None

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (0, 2, (3, 0), (), "Code", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (14, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Data": ((12, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"Position": ((14, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IDeviceEvents:
	'Hidden interface to send status events to listening clients.'
	CLSID = CLSID_Sink = IID('{4C158046-E52B-4799-9E5C-4E67D7C26A97}')
	coclass_clsid = IID('{4193F944-5653-4A37-BB45-23C53BF3D8D2}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStatusChanged",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
#		'The device controller has provided a status update.'


class _IDeviceLink(DispatchBaseClass):
	'A hidden interface to cache per-object data for use with IDevice.'
	CLSID = IID('{763DE5EF-0773-4CD9-9C55-4DE5C1A25279}')
	coclass_clsid = None

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IDevicesEvents:
	'Hidden interface to send events when the list of devices changes.'
	CLSID = CLSID_Sink = IID('{93064318-E550-4A42-B875-DCF54B283A8A}')
	coclass_clsid = IID('{04CC91ED-5553-46C5-89C3-FCDFCAD3CED3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStatusChanged",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnStatusChanged(self, DeviceIndex=defaultNamedNotOptArg, strStatus=defaultNamedNotOptArg):
#		'The device manager has provided a status update.'


class _IElement(DispatchBaseClass):
	'Hidden IElement Interface'
	CLSID = IID('{CB55C547-DE84-477E-B325-B01B9D925FE5}')
	coclass_clsid = None

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Code": (14, 2, (3, 0), (), "Code", None),
		"Data": (12, 2, (36, 0), (), "Data", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		"Position": (0, 2, (3, 0), (), "Position", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Code": ((14, LCID, 4, 0),()),
		"Name": ((15, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Position'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Position", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IElementBase(DispatchBaseClass):
	'Hidden IElementBase Interface'
	CLSID = IID('{31A2EE70-74AC-453D-B4CB-59420D05F4B6}')
	coclass_clsid = None

	def _OnStatusChanged(self, strStatus=defaultNamedNotOptArg):
		'Hidden method to respond to status events.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),strStatus
			)

	_prop_map_get_ = {
		"CanModify": (13, 2, (3, 0), (), "CanModify", None),
		"Name": (15, 2, (8, 0), (), "Name", None),
		# Method '_Device' returns object of type 'IDevice'
		"_Device": (4, 2, (9, 0), (), "_Device", '{F1283CC9-B953-4A63-A677-769CC13EA403}'),
	}
	_prop_map_put_ = {
		"Name": ((15, LCID, 4, 0),()),
		"_Device": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Nikon.LvMic.DicPrism.1'
class DICPrism(CoClassBaseClass): # A CoClass
	# DICPrism Class
	CLSID = IID('{43DC7FFC-1699-4C9A-99C7-4CFC8892044B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDICPrism,
	]
	default_interface = IDICPrism

# This CoClass is known by the name 'Nikon.LvMic.Database.1'
class Database(CoClassBaseClass): # A CoClass
	# Database Class
	CLSID = IID('{52BCED18-FB30-4D67-BC91-38456E6CAA91}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDatabase,
	]
	default_interface = IDatabase

# This CoClass is known by the name 'Nikon.LvMic.DbBarrierFilter.1'
class DbBarrierFilter(CoClassBaseClass): # A CoClass
	# DbBarrierFilter Class
	CLSID = IID('{A7D2C363-A7A8-440D-BD9E-BC399DE12B9E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbBarrierFilter,
	]
	default_interface = IDbBarrierFilter

# This CoClass is known by the name 'Nikon.LvMic.DbBarrierFilters.1'
class DbBarrierFilters(CoClassBaseClass): # A CoClass
	# DbBarrierFilters Class
	CLSID = IID('{688E3601-6AAD-4551-BC82-C411201C26F1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbBarrierFilters,
	]
	default_interface = IDbBarrierFilters

# This CoClass is known by the name 'Nikon.LvMic.DbDichroicMirror.1'
class DbDichroicMirror(CoClassBaseClass): # A CoClass
	# DbDichroicMirror Class
	CLSID = IID('{D87CB878-07B8-4790-AF9A-411D4A090022}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbDichroicMirror,
	]
	default_interface = IDbDichroicMirror

# This CoClass is known by the name 'Nikon.LvMic.DbDichroicMirrors.1'
class DbDichroicMirrors(CoClassBaseClass): # A CoClass
	# DbDichroicMirrors Class
	CLSID = IID('{90DF6DA2-E579-4F57-B6D4-8FCC9F89B0FA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbDichroicMirrors,
	]
	default_interface = IDbDichroicMirrors

# This CoClass is known by the name 'Nikon.LvMic.DbExcitationFilter.1'
class DbExcitationFilter(CoClassBaseClass): # A CoClass
	# DbExcitationFilter Class
	CLSID = IID('{A1F02B27-F0BC-498A-8D3D-9E49C1A8A616}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbExcitationFilter,
	]
	default_interface = IDbExcitationFilter

# This CoClass is known by the name 'Nikon.LvMic.DbExcitationFilters.1'
class DbExcitationFilters(CoClassBaseClass): # A CoClass
	# DbExcitationFilters Class
	CLSID = IID('{5C9124B1-A227-4D41-9CC3-E799DD70C5F0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbExcitationFilters,
	]
	default_interface = IDbExcitationFilters

# This CoClass is known by the name 'Nikon.LvMic.DbFilterBlock.1'
class DbFilterBlock(CoClassBaseClass): # A CoClass
	# DbFilterBlock Class
	CLSID = IID('{22713002-A419-4E9E-B637-31B498728121}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbFilterBlock,
	]
	default_interface = IDbFilterBlock

# This CoClass is known by the name 'Nikon.LvMic.DbFilterBlocks.1'
class DbFilterBlocks(CoClassBaseClass): # A CoClass
	# DbFilterBlocks Class
	CLSID = IID('{DCD1A352-9EDD-4C04-97CC-735CA7604926}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbFilterBlocks,
	]
	default_interface = IDbFilterBlocks

# This CoClass is known by the name 'Nikon.LvMic.DbObjective.1'
class DbObjective(CoClassBaseClass): # A CoClass
	# DbObjective Class
	CLSID = IID('{A4D9888B-C013-4A67-ABF6-151B232C1CA9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjective,
	]
	default_interface = IDbObjective

# This CoClass is known by the name 'LvMic.DbObjectiveDic.1'
class DbObjectiveDic(CoClassBaseClass): # A CoClass
	# DbObjectiveDic Class
	CLSID = IID('{E5FDFD81-FA9A-4667-AD94-E1505D1F32B7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectiveDic,
	]
	default_interface = IDbObjectiveDic

# This CoClass is known by the name 'LvMic.DbObjectiveDics.1'
class DbObjectiveDics(CoClassBaseClass): # A CoClass
	# DbObjectiveDics Class
	CLSID = IID('{4300DCFA-BBE3-4DAD-87DE-3FB0FC4592B1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectiveDics,
	]
	default_interface = IDbObjectiveDics

# This CoClass is known by the name 'LvMic.DbObjectiveModel.1'
class DbObjectiveModel(CoClassBaseClass): # A CoClass
	# DbObjectiveModel Class
	CLSID = IID('{8DE4446A-39A9-4B89-9F3B-B285B24483FC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectiveModel,
	]
	default_interface = IDbObjectiveModel

# This CoClass is known by the name 'LvMic.DbObjectiveModels.1'
class DbObjectiveModels(CoClassBaseClass): # A CoClass
	# DbObjectiveModels Class
	CLSID = IID('{B911DB65-903F-4F19-9A14-046F63ACD0CD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectiveModels,
	]
	default_interface = IDbObjectiveModels

# This CoClass is known by the name 'LvMic.DbObjectiveType.1'
class DbObjectiveType(CoClassBaseClass): # A CoClass
	# DbObjectiveType Class
	CLSID = IID('{0309400B-38C2-403C-BE7F-27B3CEE68551}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectiveType,
	]
	default_interface = IDbObjectiveType

# This CoClass is known by the name 'LvMic.DbObjectiveTypes.1'
class DbObjectiveTypes(CoClassBaseClass): # A CoClass
	# DbObjectiveTypes Class
	CLSID = IID('{E081B9B1-422A-4741-A30B-35F966968518}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectiveTypes,
	]
	default_interface = IDbObjectiveTypes

# This CoClass is known by the name 'Nikon.LvMic.DbObjectives.1'
class DbObjectives(CoClassBaseClass): # A CoClass
	# DbObjectives Class
	CLSID = IID('{A2FB0ED5-93D0-460D-8195-A07CADC1C75F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDbObjectives,
	]
	default_interface = IDbObjectives

# This CoClass is known by the name 'Nikon.LvMic.DiaLamp.1'
class DiaLamp(CoClassBaseClass): # A CoClass
	# DiaLamp Class
	CLSID = IID('{4D8E961D-5593-4C7D-BB72-ABF66FADE539}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDiaLamp,
	]
	default_interface = IDiaLamp

# This CoClass is known by the name 'Nikon.LvMic.EpiApertureStop.1'
class EpiApertureStop(CoClassBaseClass): # A CoClass
	# EpiApertureStop Class
	CLSID = IID('{3AE83DE1-2AF8-4215-BE75-71FD9D324E9B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IEpiApertureStop,
	]
	default_interface = IEpiApertureStop

# This CoClass is known by the name 'Nikon.LvMic.EpiLamp.1'
class EpiLamp(CoClassBaseClass): # A CoClass
	# EpiLamp Class
	CLSID = IID('{F5481148-DE7C-4DBA-A432-C761C6339B00}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IEpiLamp,
	]
	default_interface = IEpiLamp

# This CoClass is known by the name 'Nikon.LvMic.EpiShutter.1'
class EpiShutter(CoClassBaseClass): # A CoClass
	# EpiShutter Class
	CLSID = IID('{58343FAD-ACC0-449D-B82E-2E0875F46591}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IEpiShutter,
	]
	default_interface = IEpiShutter

# This CoClass is known by the name 'Nikon.LvMic.FilterBlock.1'
class FilterBlock(CoClassBaseClass): # A CoClass
	# FilterBlock Class
	CLSID = IID('{6892031F-DC07-4667-A4DA-C30D6D54F5FA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFilterBlock,
	]
	default_interface = IFilterBlock

# This CoClass is known by the name 'Nikon.LvMic.FilterBlockCassette.1'
class FilterBlockCassette(CoClassBaseClass): # A CoClass
	# FilterBlockCassette Class
	CLSID = IID('{6BAB6C19-4BB2-4063-82B5-F44C958EC878}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFilterBlockCassette,
	]
	default_interface = IFilterBlockCassette

# This CoClass is known by the name 'Nikon.LvMic.FilterBlocks.1'
class FilterBlocks(CoClassBaseClass): # A CoClass
	# FilterBlocks Class
	CLSID = IID('{DEE8D261-66BA-4A91-B19F-F07E21A53E51}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFilterBlocks,
	]
	default_interface = IFilterBlocks

# This CoClass is known by the name 'Nikon.LvMic.NDFilter.1'
class NDFilter(CoClassBaseClass): # A CoClass
	# NDFilter Class
	CLSID = IID('{0359B876-5B67-4974-AB2A-E8720139E42D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INDFilter,
	]
	default_interface = INDFilter

# This CoClass is known by the name 'Nikon.LvMic.NikonLv.1'
class NikonLv(CoClassBaseClass): # A CoClass
	# NikonLv Class
	CLSID = IID('{FF503DBE-D320-4074-9816-F97F9F1C6215}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INikonLv,
	]
	default_interface = INikonLv

# This CoClass is known by the name 'Nikon.LvMic.NikonLvDevice.1'
class NikonLvDevice(CoClassBaseClass): # A CoClass
	# Communications and port settings for Nikon Lv Microscopes.
	CLSID = IID('{4193F944-5653-4A37-BB45-23C53BF3D8D2}')
	coclass_sources = [
		_IDeviceEvents,
	]
	default_source = _IDeviceEvents
	coclass_interfaces = [
		INikonLvDevice,
	]
	default_interface = INikonLvDevice

# This CoClass is known by the name 'Nikon.LvMic.NikonLvDevices.1'
class NikonLvDevices(CoClassBaseClass): # A CoClass
	# Nikon Lv Device Manager Class
	CLSID = IID('{04CC91ED-5553-46C5-89C3-FCDFCAD3CED3}')
	coclass_sources = [
		_IDevicesEvents,
	]
	default_source = _IDevicesEvents
	coclass_interfaces = [
		INikonLvDevices,
	]
	default_interface = INikonLvDevices

# This CoClass is known by the name 'Nikon.LvMic.Nosepiece.1'
class Nosepiece(CoClassBaseClass): # A CoClass
	# Nosepiece Class
	CLSID = IID('{DB3D3ADF-C358-4A0C-9CDD-5E947310C788}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INosepiece,
	]
	default_interface = INosepiece

# This CoClass is known by the name 'Nikon.LvMic.Objective.1'
class Objective(CoClassBaseClass): # A CoClass
	# Objective Class
	CLSID = IID('{89608928-C071-429E-9238-18D7218912F0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IObjective,
	]
	default_interface = IObjective

# This CoClass is known by the name 'Nikon.LvMic.Objectives.1'
class Objectives(CoClassBaseClass): # A CoClass
	# Objectives Class
	CLSID = IID('{C394D185-D859-42BE-95D9-42FE36DB051D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IObjectives,
	]
	default_interface = IObjectives

# This CoClass is known by the name 'Nikon.LvMic.Presets.1'
class Presets(CoClassBaseClass): # A CoClass
	# Presets Class
	CLSID = IID('{792D4C23-39C9-46C9-A664-D9D5A552EA9D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPresets,
	]
	default_interface = IPresets

# This CoClass is known by the name 'Nikon.LvMic.ZDrive.1'
class ZDrive(CoClassBaseClass): # A CoClass
	# ZDrive Class
	CLSID = IID('{F79F5221-2326-4AE4-812A-83B7CE69CDB3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IZDrive,
	]
	default_interface = IZDrive

IDICPrism_vtables_dispatch_ = 1
IDICPrism_vtables_ = [
	(( 'GoOutOfPosition' , ), 31, (31, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Limitation' , 'pVal' , ), 208, (208, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( '_Limitation' , 'pVal' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 1024 , )),
	(( '_Limitation' , 'pVal' , ), 209, (209, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 1024 , )),
	(( 'DICPosition' , 'pVal' , ), 220, (220, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DICPosition' , 'pVal' , ), 220, (220, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( '_DICPosition' , 'pVal' , ), 221, (221, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 1024 , )),
	(( '_DICPosition' , 'pVal' , ), 221, (221, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 1024 , )),
	(( 'IsOutOfPosition' , 'pVal' , ), 222, (222, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( '_IsOutOfPosition' , 'pVal' , ), 223, (223, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
	(( '_IsOutOfPosition' , 'pVal' , ), 223, (223, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 1024 , )),
	(( 'PhaseDifference' , 'pVal' , ), 448, (448, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'PhaseDifference' , 'pVal' , ), 448, (448, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( '_PhaseDifference' , 'pVal' , ), 449, (449, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 1024 , )),
	(( '_PhaseDifference' , 'pVal' , ), 449, (449, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 1024 , )),
	(( 'ReadDicCalibration' , 'pValue' , ), 225, (225, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'AdjustDicCalibration' , ), 226, (226, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'InitializeDicCalibration' , ), 227, (227, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'SetDicCalibration' , 'lValue' , ), 228, (228, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'IsCalibration' , 'pVal' , ), 458, (458, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( '_IsCalibration' , 'pVal' , ), 459, (459, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 1024 , )),
	(( '_IsCalibration' , 'pVal' , ), 459, (459, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 1024 , )),
]

IDatabase_vtables_dispatch_ = 1
IDatabase_vtables_ = [
	(( 'Objectives' , 'ppVal' , ), 32, (32, (), [ (16393, 10, None, "IID('{2204072B-6007-4D6B-AB10-30B8EB6CD97E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ExcitationFilters' , 'ppVal' , ), 34, (34, (), [ (16393, 10, None, "IID('{5224855F-17CF-4B8B-8D4A-096DEF8A1028}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'BarrierFilters' , 'ppVal' , ), 35, (35, (), [ (16393, 10, None, "IID('{7FC48C7D-6C9F-4EE4-8EA5-F6A5C695410E}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DichroicMirrors' , 'ppVal' , ), 36, (36, (), [ (16393, 10, None, "IID('{17E1D932-1A32-4716-91C6-A4F4195AD69D}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FilterBlocks' , 'ppVal' , ), 37, (37, (), [ (16393, 10, None, "IID('{74AE41DD-4F6A-40B2-AC6E-30361A6CA3F5}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PresetObjectives' , 'pObjectives' , ), 42, (42, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PresetExcitationFilters' , 'pExcitationFilters' , ), 44, (44, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PresetBarrierFilters' , 'pBarrierFilters' , ), 45, (45, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PresetDichroicMirrors' , 'pDichroicMirrors' , ), 46, (46, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PresetFilterBlocks' , 'pFilterBlocks' , ), 47, (47, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PresetObjectiveModels' , 'pObjectiveModels' , ), 48, (48, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PresetObjectiveTypes' , 'pObjectiveTypes' , ), 49, (49, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveModels' , 'ppVal' , ), 50, (50, (), [ (16393, 10, None, "IID('{7F23BB36-32A4-45C0-9E6E-C344DFC1B002}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveTypes' , 'ppVal' , ), 51, (51, (), [ (16393, 10, None, "IID('{375F6905-A9EB-445B-B5C0-DF78C0A4F8C4}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveDics' , 'ppVal' , ), 52, (52, (), [ (16393, 10, None, "IID('{E063359B-97AD-472A-A089-4F32DABB9F29}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IDbBarrierFilter_vtables_dispatch_ = 1
IDbBarrierFilter_vtables_ = [
]

IDbBarrierFilters_vtables_dispatch_ = 1
IDbBarrierFilters_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{1B069B84-282E-42EF-A0AA-0338C9C7B654}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pNewData' , 'pIndex' , ), 32, (32, (), [ (36, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'lIndex' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDbDichroicMirror_vtables_dispatch_ = 1
IDbDichroicMirror_vtables_ = [
]

IDbDichroicMirrors_vtables_dispatch_ = 1
IDbDichroicMirrors_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E6FCB965-784B-4F18-9296-91AE9849D93C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pNewData' , 'pIndex' , ), 32, (32, (), [ (36, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'lIndex' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDbExcitationFilter_vtables_dispatch_ = 1
IDbExcitationFilter_vtables_ = [
]

IDbExcitationFilters_vtables_dispatch_ = 1
IDbExcitationFilters_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pNewData' , 'pIndex' , ), 32, (32, (), [ (36, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'lIndex' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDbFilterBlock_vtables_dispatch_ = 1
IDbFilterBlock_vtables_ = [
	(( 'FilterBlockData' , 'pVal' , ), 30, (30, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FilterBlockData' , 'pVal' , ), 30, (30, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Composition' , 'pVal' , ), 31, (31, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Composition' , 'pVal' , ), 31, (31, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'FilterType' , 'pVal' , ), 32, (32, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ExcitationFilterCode' , 'pVal' , ), 35, (35, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ExcitationFilterCode' , 'pVal' , ), 35, (35, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DichroicMirrorCode' , 'pVal' , ), 36, (36, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DichroicMirrorCode' , 'pVal' , ), 36, (36, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BarrierFilterCode' , 'pVal' , ), 37, (37, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BarrierFilterCode' , 'pVal' , ), 37, (37, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IDbFilterBlocks_vtables_dispatch_ = 1
IDbFilterBlocks_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pNewData' , 'pIndex' , ), 32, (32, (), [ (36, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'lIndex' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDbObjective_vtables_dispatch_ = 1
IDbObjective_vtables_ = [
	(( 'Description' , 'pVal' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Magnification' , 'pVal' , ), 34, (34, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NumericalAperture' , 'pVal' , ), 35, (35, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'WorkingDistance' , 'pVal' , ), 36, (36, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveData' , 'pVal' , ), 37, (37, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveData' , 'pVal' , ), 37, (37, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveType' , 'pVal' , ), 38, (38, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveModel' , 'pVal' , ), 39, (39, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectiveData' , 'lObjectiveModel' , 'lObjectiveType' , 'dMagnification' , 'dWorkingDistance' , 
			 'dNumericalAperture' , 'lCondenserType' , 'lDICPrismPosition' , ), 40, (40, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CondenserType' , 'pVal' , ), 41, (41, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DICPrismPosition' , 'pVal' , ), 42, (42, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IDbObjectiveDic_vtables_dispatch_ = 1
IDbObjectiveDic_vtables_ = [
	(( 'Name' , 'pVal' , ), 53, (53, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDbObjectiveDics_vtables_dispatch_ = 1
IDbObjectiveDics_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{2077315B-1C2B-422E-8355-376F7DB532BF}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDbObjectiveModel_vtables_dispatch_ = 1
IDbObjectiveModel_vtables_ = [
	(( 'Name' , 'pVal' , ), 53, (53, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDbObjectiveModels_vtables_dispatch_ = 1
IDbObjectiveModels_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4667A60B-E710-4E47-A139-6686B8D194A6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDbObjectiveType_vtables_dispatch_ = 1
IDbObjectiveType_vtables_ = [
	(( 'Name' , 'pVal' , ), 53, (53, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDbObjectiveTypes_vtables_dispatch_ = 1
IDbObjectiveTypes_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDbObjectives_vtables_dispatch_ = 1
IDbObjectives_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{29C5F645-840A-487F-AB19-E306973D4DD9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pNewData' , 'pIndex' , ), 32, (32, (), [ (36, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'lIndex' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDevice_vtables_dispatch_ = 1
IDevice_vtables_ = [
	(( 'GetStringData' , 'LockCookie' , 'strCommand' , 'pVal' , ), 20, (20, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16392, 3, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetStatusData' , 'LockCookie' , 'strCommand' , 'pVal' , ), 21, (21, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 3, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetLongData' , 'LockCookie' , 'strCommand' , 'pVal' , ), 22, (22, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 3, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SendStringData' , 'LockCookie' , 'strCommand' , 'strArgument' , ), 23, (23, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SendStatusData' , 'LockCookie' , 'strCommand' , 'statusArgument' , ), 24, (24, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SendLongData' , 'LockCookie' , 'strCommand' , 'lArgument' , ), 25, (25, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IDeviceClient_vtables_dispatch_ = 1
IDeviceClient_vtables_ = [
]

IDiaLamp_vtables_dispatch_ = 1
IDiaLamp_vtables_ = [
	(( 'SetVoltageForCamera' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Voltage' , 'pVal' , ), 220, (220, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Voltage' , 'pVal' , ), 220, (220, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( '_Voltage' , 'pVal' , ), 221, (221, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
	(( '_Voltage' , 'pVal' , ), 221, (221, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 1024 , )),
	(( 'LampType' , 'pVal' , ), 232, (232, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( '_LampType' , 'pVal' , ), 233, (233, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 1024 , )),
	(( '_LampType' , 'pVal' , ), 233, (233, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 1024 , )),
]

IEpiApertureStop_vtables_dispatch_ = 1
IEpiApertureStop_vtables_ = [
	(( 'SetApertureDefaults' , ), 30, (30, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ApertureStop' , 'pVal' , ), 220, (220, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ApertureStop' , 'pVal' , ), 220, (220, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( '_ApertureStop' , 'pVal' , ), 221, (221, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 1024 , )),
	(( '_ApertureStop' , 'pVal' , ), 221, (221, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 1024 , )),
	(( 'CompensationRatio' , 'pVal' , ), 222, (222, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( '_CompensationRatio' , 'pVal' , ), 223, (223, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 1024 , )),
	(( '_CompensationRatio' , 'pVal' , ), 223, (223, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 1024 , )),
]

IEpiLamp_vtables_dispatch_ = 1
IEpiLamp_vtables_ = [
	(( 'SetVoltageForCamera' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Voltage' , 'pVal' , ), 220, (220, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Voltage' , 'pVal' , ), 220, (220, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( '_Voltage' , 'pVal' , ), 221, (221, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
	(( '_Voltage' , 'pVal' , ), 221, (221, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 1024 , )),
	(( 'LampType' , 'pVal' , ), 232, (232, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( '_LampType' , 'pVal' , ), 233, (233, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 1024 , )),
	(( '_LampType' , 'pVal' , ), 233, (233, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 1024 , )),
]

IEpiShutter_vtables_dispatch_ = 1
IEpiShutter_vtables_ = [
	(( 'OpenWithTimer' , 'lTimer' , ), 30, (30, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IsSupportedOpenWithTimer' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'IsShutterOpen' , 'pVal' , ), 32, (32, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FiberType' , 'pVal' , ), 232, (232, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( '_FiberType' , 'pVal' , ), 233, (233, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 1024 , )),
	(( '_FiberType' , 'pVal' , ), 233, (233, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
]

IFilterBlock_vtables_dispatch_ = 1
IFilterBlock_vtables_ = [
	(( 'FilterBlockData' , 'pVal' , ), 30, (30, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FilterBlockData' , 'pVal' , ), 30, (30, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Composition' , 'pVal' , ), 31, (31, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Composition' , 'pVal' , ), 31, (31, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FilterType' , 'pVal' , ), 34, (34, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ExcitationFilterCode' , 'pVal' , ), 35, (35, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ExcitationFilterCode' , 'pVal' , ), 35, (35, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DichroicMirrorCode' , 'pVal' , ), 36, (36, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DichroicMirrorCode' , 'pVal' , ), 36, (36, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BarrierFilterCode' , 'pVal' , ), 37, (37, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BarrierFilterCode' , 'pVal' , ), 37, (37, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IFilterBlockCassette_vtables_dispatch_ = 1
IFilterBlockCassette_vtables_ = [
	(( 'FilterBlocks' , 'ppVal' , ), 30, (30, (), [ (16393, 10, None, "IID('{BBF77FB4-8F04-425E-87AD-985B4B9481DF}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'EnableInterlock' , ), 31, (31, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'DisableInterlock' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'IsInterlockEnabled' , 'pVal' , ), 222, (222, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'IsInterlockEnabled' , 'pVal' , ), 222, (222, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( '_IsInterlockEnabled' , 'pVal' , ), 223, (223, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
	(( '_IsInterlockEnabled' , 'pVal' , ), 223, (223, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 1024 , )),
]

IFilterBlocks_vtables_dispatch_ = 1
IFilterBlocks_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

INDFilter_vtables_dispatch_ = 1
INDFilter_vtables_ = [
	(( 'Transmission' , 'pVal' , ), 220, (220, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( '_Transmission' , 'pVal' , ), 221, (221, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 1024 , )),
	(( '_Transmission' , 'pVal' , ), 221, (221, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 1024 , )),
	(( 'Position' , 'pVal' , ), 222, (222, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 222, (222, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( '_Position' , 'pVal' , ), 223, (223, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 1024 , )),
	(( '_Position' , 'pVal' , ), 223, (223, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 1024 , )),
	(( 'FiberType' , 'pVal' , ), 232, (232, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( '_FiberType' , 'pVal' , ), 233, (233, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 1024 , )),
	(( '_FiberType' , 'pVal' , ), 233, (233, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
]

INikonLv_vtables_dispatch_ = 1
INikonLv_vtables_ = [
	(( 'Nosepiece' , 'ppVal' , ), 71, (71, (), [ (16393, 10, None, "IID('{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Nosepiece' , 'ppVal' , ), 71, (71, (), [ (9, 1, None, "IID('{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}')") , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Presets' , 'ppVal' , ), 72, (72, (), [ (16393, 10, None, "IID('{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Presets' , 'ppVal' , ), 72, (72, (), [ (9, 1, None, "IID('{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}')") , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'VersionOfSDK' , 'pVal' , ), 73, (73, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
]

INikonLv1_vtables_dispatch_ = 1
INikonLv1_vtables_ = [
	(( 'Device' , 'ppVal' , ), 22, (22, (), [ (16393, 10, None, "IID('{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Device' , 'ppVal' , ), 22, (22, (), [ (9, 1, None, "IID('{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Devices' , 'ppVal' , ), 25, (25, (), [ (16393, 10, None, "IID('{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Database' , 'ppVal' , ), 30, (30, (), [ (16393, 10, None, "IID('{C64C5896-AF8D-4520-B67F-E2C284A17015}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Database' , 'ppVal' , ), 30, (30, (), [ (9, 1, None, "IID('{C64C5896-AF8D-4520-B67F-E2C284A17015}')") , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Nosepiece1' , 'ppVal' , ), 31, (31, (), [ (16393, 10, None, "IID('{AACCE357-70D3-4A64-B693-61ADE12FAF55}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Nosepiece1' , 'ppVal' , ), 31, (31, (), [ (9, 1, None, "IID('{AACCE357-70D3-4A64-B693-61ADE12FAF55}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FilterBlockCassette' , 'ppVal' , ), 33, (33, (), [ (16393, 10, None, "IID('{D2695568-651D-4AA8-9D88-B74FC2E878B5}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FilterBlockCassette' , 'ppVal' , ), 33, (33, (), [ (9, 1, None, "IID('{D2695568-651D-4AA8-9D88-B74FC2E878B5}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ZDrive' , 'ppVal' , ), 34, (34, (), [ (16393, 10, None, "IID('{962D3580-F901-4AC4-9CF3-49A1CE779E45}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ZDrive' , 'ppVal' , ), 34, (34, (), [ (9, 1, None, "IID('{962D3580-F901-4AC4-9CF3-49A1CE779E45}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DICPrism' , 'ppVal' , ), 36, (36, (), [ (16393, 10, None, "IID('{40FCAC43-8012-4FDF-9083-D29B4372FC80}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'DICPrism' , 'ppVal' , ), 36, (36, (), [ (9, 1, None, "IID('{40FCAC43-8012-4FDF-9083-D29B4372FC80}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DiaLamp' , 'ppVal' , ), 41, (41, (), [ (16393, 10, None, "IID('{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DiaLamp' , 'ppVal' , ), 41, (41, (), [ (9, 1, None, "IID('{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'EpiLamp' , 'ppVal' , ), 42, (42, (), [ (16393, 10, None, "IID('{05952D05-F83A-49CB-8BB8-DE0E625284BD}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'EpiLamp' , 'ppVal' , ), 42, (42, (), [ (9, 1, None, "IID('{05952D05-F83A-49CB-8BB8-DE0E625284BD}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'EpiShutter' , 'ppVal' , ), 43, (43, (), [ (16393, 10, None, "IID('{0C3DB625-1025-4E8B-B563-8D085C27C704}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'EpiShutter' , 'ppVal' , ), 43, (43, (), [ (9, 1, None, "IID('{0C3DB625-1025-4E8B-B563-8D085C27C704}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NDFilter' , 'ppVal' , ), 44, (44, (), [ (16393, 10, None, "IID('{42DCE3AB-488B-490A-83C2-00153CD925B2}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'NDFilter' , 'ppVal' , ), 44, (44, (), [ (9, 1, None, "IID('{42DCE3AB-488B-490A-83C2-00153CD925B2}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'EpiApertureStop' , 'ppVal' , ), 46, (46, (), [ (16393, 10, None, "IID('{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'EpiApertureStop' , 'ppVal' , ), 46, (46, (), [ (9, 1, None, "IID('{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'EnableBuzzer' , ), 50, (50, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DisableBuzzer' , ), 51, (51, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ReadVersion' , 'pVal' , ), 52, (52, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SystemName' , 'pVal' , ), 53, (53, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SystemName' , 'pVal' , ), 53, (53, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'EnableSwitch' , ), 54, (54, (), [ ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'DisableSwitch' , ), 55, (55, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'IsBuzzerEnabled' , 'pStatus' , ), 56, (56, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'IsSwitchEnabled' , 'pStatus' , ), 57, (57, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Presets1' , 'ppVal' , ), 61, (61, (), [ (16393, 10, None, "IID('{E30E636B-DA15-4CFA-8B91-61877484F743}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Presets1' , 'ppVal' , ), 61, (61, (), [ (9, 1, None, "IID('{E30E636B-DA15-4CFA-8B91-61877484F743}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SendData' , 'strCommand' , ), 62, (62, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GetData' , 'strCommand' , 'pVal' , ), 63, (63, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'IsLocked' , 'pVal' , ), 64, (64, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ReadChecksum' , 'pVal' , ), 65, (65, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ReadProgramName' , 'pVal' , ), 66, (66, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 67, (67, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 67, (67, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ClearSystemName' , ), 68, (68, (), [ ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ClearPassword' , ), 69, (69, (), [ ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'GetData2' , 'strCommand' , 'pVal' , ), 70, (70, (), [ (8, 1, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
]

INikonLvDevice_vtables_dispatch_ = 1
INikonLvDevice_vtables_ = [
	(( 'Overlapped' , 'pVal' , ), 34, (34, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Overlapped' , 'pVal' , ), 34, (34, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'WaitForDevice' , 'lMaxTimeouts' , 'pVal' , ), 35, (35, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( '_ResetWait' , ), 36, (36, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'IsAvailable' , 'pVal' , ), 37, (37, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'IsSimulation' , 'pVal' , ), 38, (38, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( '_ReadStatusValue' , 'offset' , 'pVal' , ), 39, (39, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( '_CalcNaCrossMag' , 'nNosepiece' , 'pVal' , ), 40, (40, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LvDeviceType' , 'pVal' , ), 84, (84, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( '_LvDeviceType' , 'pVal' , ), 85, (85, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 1024 , )),
	(( '_LvDeviceType' , 'pVal' , ), 85, (85, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 1024 , )),
	(( 'DeviceIndex' , 'pVal' , ), 43, (43, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Index' , 'pVal' , ), 44, (44, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

INikonLvDevices_vtables_dispatch_ = 1
INikonLvDevices_vtables_ = [
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'pVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'pVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

INosepiece_vtables_dispatch_ = 1
INosepiece_vtables_ = [
	(( 'LimitedReverse' , ), 224, (224, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

INosepiece1_vtables_dispatch_ = 1
INosepiece1_vtables_ = [
	(( 'Objectives' , 'ppVal' , ), 30, (30, (), [ (16393, 10, None, "IID('{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'EnableInterlock' , ), 31, (31, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'DisableInterlock' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'IsNosepieceControlError' , 'pVal' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'NosepieceControl' , 'pVal' , ), 220, (220, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'NosepieceControl' , 'pVal' , ), 220, (220, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( '_NosepieceControl' , 'pVal' , ), 221, (221, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 1024 , )),
	(( '_NosepieceControl' , 'pVal' , ), 221, (221, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 1024 , )),
	(( 'IsInterlockEnabled' , 'pVal' , ), 222, (222, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'IsInterlockEnabled' , 'pVal' , ), 222, (222, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( '_IsInterlockEnabled' , 'pVal' , ), 223, (223, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 1024 , )),
	(( '_IsInterlockEnabled' , 'pVal' , ), 223, (223, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 1024 , )),
]

IObjective_vtables_dispatch_ = 1
IObjective_vtables_ = [
	(( 'Description' , 'pVal' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Magnification' , 'pVal' , ), 34, (34, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NumericalAperture' , 'pVal' , ), 35, (35, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'WorkingDistance' , 'pVal' , ), 36, (36, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveData' , 'pVal' , ), 37, (37, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveData' , 'pVal' , ), 37, (37, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveType' , 'pVal' , ), 38, (38, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveModel' , 'pVal' , ), 39, (39, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectiveData' , 'lObjectiveModel' , 'lObjectiveType' , 'dMagnification' , 'dWorkingDistance' , 
			 'dNumericalAperture' , 'lCondenserType' , 'lDICPrismPosition' , ), 40, (40, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CondenserType' , 'pVal' , ), 41, (41, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DICPrismPosition' , 'pVal' , ), 42, (42, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IObjectives_vtables_dispatch_ = 1
IObjectives_vtables_ = [
	(( 'Item' , 'lIndex' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{5AB19F95-28DE-425F-835B-46F3DB18E34C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPort_vtables_dispatch_ = 1
IPort_vtables_ = [
	(( 'Address' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Disconnect' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Connected' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Connected' , 'pVal' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LastResponse' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IPositionAccessory_vtables_dispatch_ = 1
IPositionAccessory_vtables_ = [
	(( 'MoveAbsolute' , 'Pos' , ), 20, (20, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MoveRelative' , 'Pos' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 202, (202, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( '_Position' , 'pVal' , ), 203, (203, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 1024 , )),
	(( '_Position' , 'pVal' , ), 203, (203, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 1024 , )),
	(( 'Speed' , 'pVal' , ), 204, (204, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'pVal' , ), 204, (204, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( '_Speed' , 'pVal' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 1024 , )),
	(( '_Speed' , 'pVal' , ), 205, (205, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 1024 , )),
	(( 'Tolerance' , 'pVal' , ), 206, (206, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Tolerance' , 'pVal' , ), 206, (206, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( '_Tolerance' , 'pVal' , ), 207, (207, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
	(( '_Tolerance' , 'pVal' , ), 207, (207, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 1024 , )),
	(( 'Limitation' , 'pVal' , ), 208, (208, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( '_Limitation' , 'pVal' , ), 209, (209, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 1024 , )),
	(( '_Limitation' , 'pVal' , ), 209, (209, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 1024 , )),
]

IPresets_vtables_dispatch_ = 1
IPresets_vtables_ = [
	(( 'SetPresetsToDefault' , 'ObservationMode' , 'ObjectivePosition' , ), 424, (424, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'IsDefault' , 'ObservationMode' , 'ObjectivePosition' , 'pbIsDefault' , ), 425, (425, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'SetLastValue' , 'ObservationMode' , 'ObjectivePosition' , 'dEPI' , 'dDIA' , 
			 'dEpiApertureStop' , ), 426, (426, (), [ (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , 
			 (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'GetLastValue' , 'ObservationMode' , 'ObjectivePosition' , 'pdEPI' , 'pdDIA' , 
			 'pdEpiApertureStop' , ), 427, (427, (), [ (3, 1, None, None) , (3, 1, None, None) , (16389, 2, None, None) , 
			 (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'SetPresets' , 'ObservationMode' , 'ObjectivePosition' , 'IlluminantPresets' , 'AperturePresets' , 
			 'FilterPosition' , ), 428, (428, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'ReadPresets' , 'ObservationMode' , 'ObjectivePosition' , 'pIlluminantPresets' , 'pAperturePresets' , 
			 'pFilterPosition' , ), 429, (429, (), [ (3, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , 
			 (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
]

IPresets1_vtables_dispatch_ = 1
IPresets1_vtables_ = [
	(( 'ApplyPresets' , 'ObservationMode' , ), 30, (30, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ReadMemorizedPresets' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , 'pCalculatedValue' , 
			 ), 31, (31, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AdjustMemorizedPresets' , 'Accessory' , ), 32, (32, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'InitializeMemorizedPresets' , 'Accessory' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SetMemorizedPresets' , 'Accessory' , 'dValue' , ), 34, (34, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ReadPresetModes' , 'ObservationMode' , 'pOptionalObservationMode' , 'pInterlock' , ), 35, (35, (), [ 
			 (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SetPresetModes' , 'ObservationMode' , 'OptionalObservationMode' , 'Interlock' , ), 36, (36, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ReadInterlockMode' , 'Accessory' , 'pValue' , ), 37, (37, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SetInterlockMode' , 'Accessory' , 'lMode' , ), 38, (38, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ReadLampPresets' , 'ObservationMode' , 'pLampPreset' , ), 39, (39, (), [ (3, 1, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SetLampPresets' , 'ObservationMode' , 'LampPreset' , ), 40, (40, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ReadDefaultPresets' , 'Accessory' , 'ObjectivePosition' , 'pValue' , ), 41, (41, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AdjustMemorizedPresetsEx' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , ), 42, (42, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'InitializeMemorizedPresetsEx' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , ), 43, (43, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetMemorizedPresetsEx' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , 'dValue' , 
			 ), 44, (44, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ReadUserPresets' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , 'pCalculatedValue' , 
			 ), 45, (45, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AdjustUserPresets' , 'Accessory' , ), 46, (46, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'InitializeUserPresets' , 'Accessory' , ), 47, (47, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SetUserPresets' , 'Accessory' , 'dValue' , ), 48, (48, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AdjustUserPresetsEx' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , ), 49, (49, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'InitializeUserPresetsEx' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , ), 50, (50, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SetUserPresetsEx' , 'Accessory' , 'ObservationMode' , 'ObjectivePosition' , 'dValue' , 
			 ), 51, (51, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UpdateObservationInfo' , ), 52, (52, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ObservationMode' , 'pVal' , ), 202, (202, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ObservationMode' , 'pVal' , ), 202, (202, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( '_ObservationMode' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 1024 , )),
	(( '_ObservationMode' , 'pVal' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 1024 , )),
	(( 'EpiDiaLampMode' , 'pVal' , ), 204, (204, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'EpiDiaLampMode' , 'pVal' , ), 204, (204, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( '_EpiDiaLampMode' , 'pVal' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 1024 , )),
	(( '_EpiDiaLampMode' , 'pVal' , ), 205, (205, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 1024 , )),
	(( 'InitialMode' , 'pVal' , ), 206, (206, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'InitialMode' , 'pVal' , ), 206, (206, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( '_InitialMode' , 'pVal' , ), 207, (207, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 1024 , )),
	(( '_InitialMode' , 'pVal' , ), 207, (207, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 1024 , )),
	(( 'SetPresetModesEx' , 'ObservationMode' , 'OptionalObservationMode' , 'Interlock' , 'ObjectivePosition' , 
			 ), 208, (208, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ReadPresetModesEx' , 'ObservationMode' , 'pOptionalObservationMode' , 'pInterlock' , 'pObjectivePosition' , 
			 ), 209, (209, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'AfObservationMode' , 'pVal' , ), 420, (420, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'AfObservationMode' , 'pVal' , ), 420, (420, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( '_AfObservationMode' , 'pVal' , ), 421, (421, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 1024 , )),
	(( '_AfObservationMode' , 'pVal' , ), 421, (421, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 1024 , )),
	(( 'AfRecipeMode' , 'pVal' , ), 422, (422, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'AfRecipeMode' , 'pVal' , ), 422, (422, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( '_AfRecipeMode' , 'pVal' , ), 423, (423, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 1024 , )),
	(( '_AfRecipeMode' , 'pVal' , ), 423, (423, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 1024 , )),
]

IScopeAccessory_vtables_dispatch_ = 1
IScopeAccessory_vtables_ = [
	(( 'Type' , 'pVal' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 11, (11, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'pVal' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 192, (192, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 192, (192, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( '_Value' , 'pVal' , ), 193, (193, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 1024 , )),
	(( '_Value' , 'pVal' , ), 193, (193, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 1024 , )),
	(( 'LowerLimit' , 'pVal' , ), 194, (194, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( '_LowerLimit' , 'pVal' , ), 195, (195, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 1024 , )),
	(( '_LowerLimit' , 'pVal' , ), 195, (195, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 1024 , )),
	(( 'UpperLimit' , 'pVal' , ), 196, (196, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( '_UpperLimit' , 'pVal' , ), 197, (197, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 1024 , )),
	(( '_UpperLimit' , 'pVal' , ), 197, (197, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 1024 , )),
	(( 'ValuePerUnit' , 'pVal' , ), 198, (198, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( '_ValuePerUnit' , 'pVal' , ), 199, (199, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 1024 , )),
	(( '_ValuePerUnit' , 'pVal' , ), 199, (199, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 1024 , )),
	(( 'IsMounted' , 'pVal' , ), 200, (200, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( '_IsMounted' , 'pVal' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 1024 , )),
	(( '_IsMounted' , 'pVal' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 1024 , )),
]

IShutterAccessory_vtables_dispatch_ = 1
IShutterAccessory_vtables_ = [
	(( 'Open' , ), 20, (20, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'IsOpened' , 'pVal' , ), 202, (202, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IsOpened' , 'pVal' , ), 202, (202, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( '_IsOpened' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 1024 , )),
	(( '_IsOpened' , 'pVal' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 1024 , )),
]

ITurretAccessory_vtables_dispatch_ = 1
ITurretAccessory_vtables_ = [
	(( 'Forward' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Reverse' , ), 23, (23, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 202, (202, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 202, (202, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( '_Position' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 1024 , )),
	(( '_Position' , 'pVal' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 1024 , )),
]

IVolumeAccessory_vtables_dispatch_ = 1
IVolumeAccessory_vtables_ = [
	(( 'Increase' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Decrease' , ), 23, (23, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IVolumeAccessory2_vtables_dispatch_ = 1
IVolumeAccessory2_vtables_ = [
	(( 'On' , ), 20, (20, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Off' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsOn' , 'pVal' , ), 202, (202, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IsOn' , 'pVal' , ), 202, (202, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( '_IsOn' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 1024 , )),
	(( '_IsOn' , 'pVal' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 1024 , )),
]

IZDrive_vtables_dispatch_ = 1
IZDrive_vtables_ = [
	(( 'AbortZ' , ), 38, (38, (), [ ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'InitSoftwareLowerLimit' , ), 39, (39, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'CurrentToSoftwareLowerLimit' , ), 40, (40, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'InitSoftwareUpperLimit' , ), 41, (41, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'CurrentToSoftwareUpperLimit' , ), 42, (42, (), [ ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Refocus' , ), 43, (43, (), [ ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ZEscape' , ), 44, (44, (), [ ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'IsSupportedAF' , 'pVal' , ), 45, (45, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'SoftwareLowerLimit' , 'pVal' , ), 226, (226, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SoftwareLowerLimit' , 'pVal' , ), 226, (226, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( '_SoftwareLowerLimit' , 'pVal' , ), 227, (227, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 1024 , )),
	(( '_SoftwareLowerLimit' , 'pVal' , ), 227, (227, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 1024 , )),
	(( 'SoftwareUpperLimit' , 'pVal' , ), 228, (228, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'SoftwareUpperLimit' , 'pVal' , ), 228, (228, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( '_SoftwareUpperLimit' , 'pVal' , ), 229, (229, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 1024 , )),
	(( '_SoftwareUpperLimit' , 'pVal' , ), 229, (229, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 1024 , )),
	(( 'IsZEscape' , 'pVal' , ), 230, (230, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'IsZEscape' , 'pVal' , ), 230, (230, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( '_IsZEscape' , 'pVal' , ), 231, (231, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 1024 , )),
	(( '_IsZEscape' , 'pVal' , ), 231, (231, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 1024 , )),
	(( 'ZDriveType' , 'pVal' , ), 232, (232, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( '_ZDriveType' , 'pVal' , ), 233, (233, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 1024 , )),
	(( '_ZDriveType' , 'pVal' , ), 233, (233, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 1024 , )),
	(( 'AfStatus' , 'pVal' , ), 466, (466, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'AfStatus' , 'pVal' , ), 466, (466, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( '_AfStatus' , 'pVal' , ), 467, (467, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 1024 , )),
	(( '_AfStatus' , 'pVal' , ), 467, (467, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 1024 , )),
	(( 'AF' , 'pVal' , ), 468, (468, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'AF' , 'pVal' , ), 468, (468, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( '_AF' , 'pVal' , ), 469, (469, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 1024 , )),
	(( '_AF' , 'pVal' , ), 469, (469, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 1024 , )),
	(( 'SearchAF' , 'lValue' , ), 235, (235, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'StopAF' , ), 236, (236, (), [ ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'AfOffset' , 'pVal' , ), 474, (474, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'AfOffset' , 'pVal' , ), 474, (474, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( '_AfOffset' , 'pVal' , ), 475, (475, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 1024 , )),
	(( '_AfOffset' , 'pVal' , ), 475, (475, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 648 , (3, 0, None, None) , 1024 , )),
	(( 'IsAfSearch' , 'pVal' , ), 476, (476, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( '_IsAfSearch' , 'pVal' , ), 477, (477, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 1024 , )),
	(( '_IsAfSearch' , 'pVal' , ), 477, (477, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 1024 , )),
	(( 'AfOffsetMode' , 'pVal' , ), 478, (478, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'AfOffsetMode' , 'pVal' , ), 478, (478, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( '_AfOffsetMode' , 'pVal' , ), 479, (479, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 1024 , )),
	(( '_AfOffsetMode' , 'pVal' , ), 479, (479, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 1024 , )),
	(( 'AfSearchMode' , 'pVal' , ), 480, (480, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( '_AfSearchMode' , 'pVal' , ), 481, (481, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 1024 , )),
	(( '_AfSearchMode' , 'pVal' , ), 481, (481, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 728 , (3, 0, None, None) , 1024 , )),
]

_IDbElement_vtables_dispatch_ = 1
_IDbElement_vtables_ = [
	(( 'Code' , 'pVal' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Data' , 'pVal' , ), 12, (12, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Data' , 'pVal' , ), 12, (12, (), [ (36, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

_IDeviceLink_vtables_dispatch_ = 1
_IDeviceLink_vtables_ = [
	(( '_OnStatusChanged' , 'strStatus' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_Device' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{F1283CC9-B953-4A63-A677-769CC13EA403}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_Device' , 'pVal' , ), 4, (4, (), [ (9, 1, None, "IID('{F1283CC9-B953-4A63-A677-769CC13EA403}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

_IElement_vtables_dispatch_ = 1
_IElement_vtables_ = [
	(( 'Position' , 'pVal' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Data' , 'pVal' , ), 12, (12, (), [ (36, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Code' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Code' , 'pVal' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

_IElementBase_vtables_dispatch_ = 1
_IElementBase_vtables_ = [
	(( 'CanModify' , 'pVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
	'ElementData': '{9595F283-BF84-4E1A-8357-BE0EE3D1844C}',
	'ObjectiveData': '{C111C5E4-A822-4E1D-B530-F67132324232}',
	'FilterBlockData': '{BF4DF32B-45B6-46FB-AD15-68DC782485F5}',
	'CompositionData': '{16CA4F5F-C075-4D16-A605-9CC91C13D279}',
}

CLSIDToClassMap = {
	'{4C158046-E52B-4799-9E5C-4E67D7C26A97}' : _IDeviceEvents,
	'{93064318-E550-4A42-B875-DCF54B283A8A}' : _IDevicesEvents,
	'{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}' : INikonLvDevice,
	'{4193F944-5653-4A37-BB45-23C53BF3D8D2}' : NikonLvDevice,
	'{F1283CC9-B953-4A63-A677-769CC13EA403}' : IDevice,
	'{514DCB75-DF97-4DFA-8407-CE33D6D558F4}' : IPort,
	'{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}' : INikonLvDevices,
	'{04CC91ED-5553-46C5-89C3-FCDFCAD3CED3}' : NikonLvDevices,
	'{40FCAC43-8012-4FDF-9083-D29B4372FC80}' : IDICPrism,
	'{43DC7FFC-1699-4C9A-99C7-4CFC8892044B}' : DICPrism,
	'{1465605C-A9EC-414A-8205-F98C782243DE}' : IVolumeAccessory,
	'{E81BC383-036A-457F-AAF1-DA6836A688BB}' : IScopeAccessory,
	'{763DE5EF-0773-4CD9-9C55-4DE5C1A25279}' : _IDeviceLink,
	'{962D3580-F901-4AC4-9CF3-49A1CE779E45}' : IZDrive,
	'{F79F5221-2326-4AE4-812A-83B7CE69CDB3}' : ZDrive,
	'{44CB7864-5C26-4F35-8CF8-BBA8CC885A14}' : IPositionAccessory,
	'{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}' : IDiaLamp,
	'{4D8E961D-5593-4C7D-BB72-ABF66FADE539}' : DiaLamp,
	'{C159095B-7FDE-496B-B47F-9749DA5F4ECB}' : IVolumeAccessory2,
	'{05952D05-F83A-49CB-8BB8-DE0E625284BD}' : IEpiLamp,
	'{F5481148-DE7C-4DBA-A432-C761C6339B00}' : EpiLamp,
	'{42DCE3AB-488B-490A-83C2-00153CD925B2}' : INDFilter,
	'{0359B876-5B67-4974-AB2A-E8720139E42D}' : NDFilter,
	'{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}' : INosepiece,
	'{DB3D3ADF-C358-4A0C-9CDD-5E947310C788}' : Nosepiece,
	'{AACCE357-70D3-4A64-B693-61ADE12FAF55}' : INosepiece1,
	'{11096D75-7F3D-47DA-AB61-CE84840E6D0C}' : ITurretAccessory,
	'{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}' : IObjectives,
	'{5AB19F95-28DE-425F-835B-46F3DB18E34C}' : IObjective,
	'{CB55C547-DE84-477E-B325-B01B9D925FE5}' : _IElement,
	'{31A2EE70-74AC-453D-B4CB-59420D05F4B6}' : _IElementBase,
	'{89608928-C071-429E-9238-18D7218912F0}' : Objective,
	'{C394D185-D859-42BE-95D9-42FE36DB051D}' : Objectives,
	'{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}' : IFilterBlock,
	'{6892031F-DC07-4667-A4DA-C30D6D54F5FA}' : FilterBlock,
	'{BBF77FB4-8F04-425E-87AD-985B4B9481DF}' : IFilterBlocks,
	'{DEE8D261-66BA-4A91-B19F-F07E21A53E51}' : FilterBlocks,
	'{D2695568-651D-4AA8-9D88-B74FC2E878B5}' : IFilterBlockCassette,
	'{6BAB6C19-4BB2-4063-82B5-F44C958EC878}' : FilterBlockCassette,
	'{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}' : IEpiApertureStop,
	'{3AE83DE1-2AF8-4215-BE75-71FD9D324E9B}' : EpiApertureStop,
	'{0C3DB625-1025-4E8B-B563-8D085C27C704}' : IEpiShutter,
	'{58343FAD-ACC0-449D-B82E-2E0875F46591}' : EpiShutter,
	'{854DA829-1CE9-44D0-8EC6-831CD1F4D13D}' : IShutterAccessory,
	'{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}' : IPresets,
	'{792D4C23-39C9-46C9-A664-D9D5A552EA9D}' : Presets,
	'{E30E636B-DA15-4CFA-8B91-61877484F743}' : IPresets1,
	'{29C5F645-840A-487F-AB19-E306973D4DD9}' : IDbObjective,
	'{A4D9888B-C013-4A67-ABF6-151B232C1CA9}' : DbObjective,
	'{7A43F152-ECFA-4552-8F9F-743739747E2E}' : _IDbElement,
	'{2204072B-6007-4D6B-AB10-30B8EB6CD97E}' : IDbObjectives,
	'{A2FB0ED5-93D0-460D-8195-A07CADC1C75F}' : DbObjectives,
	'{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}' : IDbFilterBlock,
	'{22713002-A419-4E9E-B637-31B498728121}' : DbFilterBlock,
	'{74AE41DD-4F6A-40B2-AC6E-30361A6CA3F5}' : IDbFilterBlocks,
	'{DCD1A352-9EDD-4C04-97CC-735CA7604926}' : DbFilterBlocks,
	'{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}' : IDbExcitationFilter,
	'{A1F02B27-F0BC-498A-8D3D-9E49C1A8A616}' : DbExcitationFilter,
	'{5224855F-17CF-4B8B-8D4A-096DEF8A1028}' : IDbExcitationFilters,
	'{5C9124B1-A227-4D41-9CC3-E799DD70C5F0}' : DbExcitationFilters,
	'{1B069B84-282E-42EF-A0AA-0338C9C7B654}' : IDbBarrierFilter,
	'{A7D2C363-A7A8-440D-BD9E-BC399DE12B9E}' : DbBarrierFilter,
	'{7FC48C7D-6C9F-4EE4-8EA5-F6A5C695410E}' : IDbBarrierFilters,
	'{688E3601-6AAD-4551-BC82-C411201C26F1}' : DbBarrierFilters,
	'{E6FCB965-784B-4F18-9296-91AE9849D93C}' : IDbDichroicMirror,
	'{D87CB878-07B8-4790-AF9A-411D4A090022}' : DbDichroicMirror,
	'{17E1D932-1A32-4716-91C6-A4F4195AD69D}' : IDbDichroicMirrors,
	'{90DF6DA2-E579-4F57-B6D4-8FCC9F89B0FA}' : DbDichroicMirrors,
	'{C64C5896-AF8D-4520-B67F-E2C284A17015}' : IDatabase,
	'{52BCED18-FB30-4D67-BC91-38456E6CAA91}' : Database,
	'{7F23BB36-32A4-45C0-9E6E-C344DFC1B002}' : IDbObjectiveModels,
	'{4667A60B-E710-4E47-A139-6686B8D194A6}' : IDbObjectiveModel,
	'{375F6905-A9EB-445B-B5C0-DF78C0A4F8C4}' : IDbObjectiveTypes,
	'{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}' : IDbObjectiveType,
	'{E063359B-97AD-472A-A089-4F32DABB9F29}' : IDbObjectiveDics,
	'{2077315B-1C2B-422E-8355-376F7DB532BF}' : IDbObjectiveDic,
	'{C6AA054A-D7F4-46FA-A419-657D4BD4C2FF}' : INikonLv,
	'{FF503DBE-D320-4074-9816-F97F9F1C6215}' : NikonLv,
	'{712EC5D6-4EFA-4D5E-B5B3-01D8D2437DF7}' : INikonLv1,
	'{1B52A395-B324-4054-B143-2F20C52EA5C4}' : IDeviceClient,
	'{8DE4446A-39A9-4B89-9F3B-B285B24483FC}' : DbObjectiveModel,
	'{B911DB65-903F-4F19-9A14-046F63ACD0CD}' : DbObjectiveModels,
	'{0309400B-38C2-403C-BE7F-27B3CEE68551}' : DbObjectiveType,
	'{E081B9B1-422A-4741-A30B-35F966968518}' : DbObjectiveTypes,
	'{E5FDFD81-FA9A-4667-AD94-E1505D1F32B7}' : DbObjectiveDic,
	'{4300DCFA-BBE3-4DAD-87DE-3FB0FC4592B1}' : DbObjectiveDics,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}' : 'INikonLvDevice',
	'{F1283CC9-B953-4A63-A677-769CC13EA403}' : 'IDevice',
	'{514DCB75-DF97-4DFA-8407-CE33D6D558F4}' : 'IPort',
	'{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}' : 'INikonLvDevices',
	'{40FCAC43-8012-4FDF-9083-D29B4372FC80}' : 'IDICPrism',
	'{1465605C-A9EC-414A-8205-F98C782243DE}' : 'IVolumeAccessory',
	'{E81BC383-036A-457F-AAF1-DA6836A688BB}' : 'IScopeAccessory',
	'{763DE5EF-0773-4CD9-9C55-4DE5C1A25279}' : '_IDeviceLink',
	'{962D3580-F901-4AC4-9CF3-49A1CE779E45}' : 'IZDrive',
	'{44CB7864-5C26-4F35-8CF8-BBA8CC885A14}' : 'IPositionAccessory',
	'{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}' : 'IDiaLamp',
	'{C159095B-7FDE-496B-B47F-9749DA5F4ECB}' : 'IVolumeAccessory2',
	'{05952D05-F83A-49CB-8BB8-DE0E625284BD}' : 'IEpiLamp',
	'{42DCE3AB-488B-490A-83C2-00153CD925B2}' : 'INDFilter',
	'{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}' : 'INosepiece',
	'{AACCE357-70D3-4A64-B693-61ADE12FAF55}' : 'INosepiece1',
	'{11096D75-7F3D-47DA-AB61-CE84840E6D0C}' : 'ITurretAccessory',
	'{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}' : 'IObjectives',
	'{5AB19F95-28DE-425F-835B-46F3DB18E34C}' : 'IObjective',
	'{CB55C547-DE84-477E-B325-B01B9D925FE5}' : '_IElement',
	'{31A2EE70-74AC-453D-B4CB-59420D05F4B6}' : '_IElementBase',
	'{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}' : 'IFilterBlock',
	'{BBF77FB4-8F04-425E-87AD-985B4B9481DF}' : 'IFilterBlocks',
	'{D2695568-651D-4AA8-9D88-B74FC2E878B5}' : 'IFilterBlockCassette',
	'{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}' : 'IEpiApertureStop',
	'{0C3DB625-1025-4E8B-B563-8D085C27C704}' : 'IEpiShutter',
	'{854DA829-1CE9-44D0-8EC6-831CD1F4D13D}' : 'IShutterAccessory',
	'{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}' : 'IPresets',
	'{E30E636B-DA15-4CFA-8B91-61877484F743}' : 'IPresets1',
	'{29C5F645-840A-487F-AB19-E306973D4DD9}' : 'IDbObjective',
	'{7A43F152-ECFA-4552-8F9F-743739747E2E}' : '_IDbElement',
	'{2204072B-6007-4D6B-AB10-30B8EB6CD97E}' : 'IDbObjectives',
	'{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}' : 'IDbFilterBlock',
	'{74AE41DD-4F6A-40B2-AC6E-30361A6CA3F5}' : 'IDbFilterBlocks',
	'{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}' : 'IDbExcitationFilter',
	'{5224855F-17CF-4B8B-8D4A-096DEF8A1028}' : 'IDbExcitationFilters',
	'{1B069B84-282E-42EF-A0AA-0338C9C7B654}' : 'IDbBarrierFilter',
	'{7FC48C7D-6C9F-4EE4-8EA5-F6A5C695410E}' : 'IDbBarrierFilters',
	'{E6FCB965-784B-4F18-9296-91AE9849D93C}' : 'IDbDichroicMirror',
	'{17E1D932-1A32-4716-91C6-A4F4195AD69D}' : 'IDbDichroicMirrors',
	'{C64C5896-AF8D-4520-B67F-E2C284A17015}' : 'IDatabase',
	'{7F23BB36-32A4-45C0-9E6E-C344DFC1B002}' : 'IDbObjectiveModels',
	'{4667A60B-E710-4E47-A139-6686B8D194A6}' : 'IDbObjectiveModel',
	'{375F6905-A9EB-445B-B5C0-DF78C0A4F8C4}' : 'IDbObjectiveTypes',
	'{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}' : 'IDbObjectiveType',
	'{E063359B-97AD-472A-A089-4F32DABB9F29}' : 'IDbObjectiveDics',
	'{2077315B-1C2B-422E-8355-376F7DB532BF}' : 'IDbObjectiveDic',
	'{C6AA054A-D7F4-46FA-A419-657D4BD4C2FF}' : 'INikonLv',
	'{712EC5D6-4EFA-4D5E-B5B3-01D8D2437DF7}' : 'INikonLv1',
	'{1B52A395-B324-4054-B143-2F20C52EA5C4}' : 'IDeviceClient',
}


NamesToIIDMap = {
	'_IDeviceEvents' : '{4C158046-E52B-4799-9E5C-4E67D7C26A97}',
	'_IDevicesEvents' : '{93064318-E550-4A42-B875-DCF54B283A8A}',
	'INikonLvDevice' : '{E80F3D06-DD0A-4474-8DF2-CA79E2ACC7ED}',
	'IDevice' : '{F1283CC9-B953-4A63-A677-769CC13EA403}',
	'IPort' : '{514DCB75-DF97-4DFA-8407-CE33D6D558F4}',
	'INikonLvDevices' : '{3D33843A-7BFE-4F92-BD68-5DCB9DC2D754}',
	'IDICPrism' : '{40FCAC43-8012-4FDF-9083-D29B4372FC80}',
	'IVolumeAccessory' : '{1465605C-A9EC-414A-8205-F98C782243DE}',
	'IScopeAccessory' : '{E81BC383-036A-457F-AAF1-DA6836A688BB}',
	'_IDeviceLink' : '{763DE5EF-0773-4CD9-9C55-4DE5C1A25279}',
	'IZDrive' : '{962D3580-F901-4AC4-9CF3-49A1CE779E45}',
	'IPositionAccessory' : '{44CB7864-5C26-4F35-8CF8-BBA8CC885A14}',
	'IDiaLamp' : '{482F57C3-6D2F-43F2-BAB9-3B4AA2FF4ED6}',
	'IVolumeAccessory2' : '{C159095B-7FDE-496B-B47F-9749DA5F4ECB}',
	'IEpiLamp' : '{05952D05-F83A-49CB-8BB8-DE0E625284BD}',
	'INDFilter' : '{42DCE3AB-488B-490A-83C2-00153CD925B2}',
	'INosepiece' : '{69E3858F-4AFE-4D7A-8C41-6C7F752F9C3A}',
	'INosepiece1' : '{AACCE357-70D3-4A64-B693-61ADE12FAF55}',
	'ITurretAccessory' : '{11096D75-7F3D-47DA-AB61-CE84840E6D0C}',
	'IObjectives' : '{21CBB8EE-2998-4E75-BE4E-B3D13969A9A8}',
	'IObjective' : '{5AB19F95-28DE-425F-835B-46F3DB18E34C}',
	'_IElement' : '{CB55C547-DE84-477E-B325-B01B9D925FE5}',
	'_IElementBase' : '{31A2EE70-74AC-453D-B4CB-59420D05F4B6}',
	'IFilterBlock' : '{64BF7A79-8CF0-44E8-89A9-D0F8A3799FBA}',
	'IFilterBlocks' : '{BBF77FB4-8F04-425E-87AD-985B4B9481DF}',
	'IFilterBlockCassette' : '{D2695568-651D-4AA8-9D88-B74FC2E878B5}',
	'IEpiApertureStop' : '{A5E747EF-C28B-4A9E-B3E9-BAC50A39227E}',
	'IEpiShutter' : '{0C3DB625-1025-4E8B-B563-8D085C27C704}',
	'IShutterAccessory' : '{854DA829-1CE9-44D0-8EC6-831CD1F4D13D}',
	'IPresets' : '{6769FF13-B85B-4BF1-B340-894DF0AF6D1C}',
	'IPresets1' : '{E30E636B-DA15-4CFA-8B91-61877484F743}',
	'IDbObjective' : '{29C5F645-840A-487F-AB19-E306973D4DD9}',
	'_IDbElement' : '{7A43F152-ECFA-4552-8F9F-743739747E2E}',
	'IDbObjectives' : '{2204072B-6007-4D6B-AB10-30B8EB6CD97E}',
	'IDbFilterBlock' : '{029CD889-4F5D-4B7C-A12C-3C5463AC3DC1}',
	'IDbFilterBlocks' : '{74AE41DD-4F6A-40B2-AC6E-30361A6CA3F5}',
	'IDbExcitationFilter' : '{1F84AA44-74C7-4C77-A98D-AAE194BFC2FE}',
	'IDbExcitationFilters' : '{5224855F-17CF-4B8B-8D4A-096DEF8A1028}',
	'IDbBarrierFilter' : '{1B069B84-282E-42EF-A0AA-0338C9C7B654}',
	'IDbBarrierFilters' : '{7FC48C7D-6C9F-4EE4-8EA5-F6A5C695410E}',
	'IDbDichroicMirror' : '{E6FCB965-784B-4F18-9296-91AE9849D93C}',
	'IDbDichroicMirrors' : '{17E1D932-1A32-4716-91C6-A4F4195AD69D}',
	'IDatabase' : '{C64C5896-AF8D-4520-B67F-E2C284A17015}',
	'IDbObjectiveModels' : '{7F23BB36-32A4-45C0-9E6E-C344DFC1B002}',
	'IDbObjectiveModel' : '{4667A60B-E710-4E47-A139-6686B8D194A6}',
	'IDbObjectiveTypes' : '{375F6905-A9EB-445B-B5C0-DF78C0A4F8C4}',
	'IDbObjectiveType' : '{B5AB7334-ABBC-4094-BD44-C29F7D3631D5}',
	'IDbObjectiveDics' : '{E063359B-97AD-472A-A089-4F32DABB9F29}',
	'IDbObjectiveDic' : '{2077315B-1C2B-422E-8355-376F7DB532BF}',
	'INikonLv' : '{C6AA054A-D7F4-46FA-A419-657D4BD4C2FF}',
	'INikonLv1' : '{712EC5D6-4EFA-4D5E-B5B3-01D8D2437DF7}',
	'IDeviceClient' : '{1B52A395-B324-4054-B143-2F20C52EA5C4}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

