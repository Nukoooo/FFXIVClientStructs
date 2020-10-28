# current exe version: 2020.10.21.0001.0000

def NameAddr(ea, name):
    idc.MakeName(ea, name)

print "Importing IDA data ..."

# functions
NameAddr(0x140058EF0, "FFXIVString_ctor")
NameAddr(0x140059B80, "FFXIVString_SetString")
NameAddr(0x14005FD30, "MemoryManager_Alloc")
NameAddr(0x140064790, "IsMacClient")
NameAddr(0x14008E2B0, "Client::System::Framework_ctor")
NameAddr(0x14008E6B0, "Client::System::Framework_Setup")
NameAddr(0x140090B50, "Client::System::Framework_Tick")
NameAddr(0x140091710, "Client::System::Framework_GetUIModule")
NameAddr(0x1400925B0, "Client::System::Framework::Task_RunTask_Begin")
NameAddr(0x1400926D0, "Client::System::Framework::Task_RunTask_Draw2DBegin")
NameAddr(0x140092AE0, "Client::System::Framework::Task_RunTask_UpdateGraphicsScene")
NameAddr(0x140092B90, "Client::System::Framework::Task_RunTask_UpdateBonePhysics")
NameAddr(0x140092C10, "Client::System::Framework::Task_RunTask_ResourceManager")
NameAddr(0x140092C20, "Client::System::Framework::Task_RunTask_UpdateGame")
NameAddr(0x1400936C0, "Client::System::Framework::TaskManager_ctor")
NameAddr(0x140093EE0, "Client::System::Framework::Task_TaskRunner") # task starter which runs the task's function pointer
NameAddr(0x1400AA590, "Client::UI::RaptureAtkUnitManager_ctor")
NameAddr(0x1400AFDE0, "Client::UI::RaptureAtkModule_ctor")
NameAddr(0x1400D2610, "Client::UI::RaptureAtkModule_UpdateTask1")
NameAddr(0x140155950, "Component::GUI::AtkUnitBase_GetPosition")
NameAddr(0x140155970, "Component::GUI::AtkUnitBase_GetX")
NameAddr(0x140155980, "Component::GUI::AtkUnitBase_GetY")
NameAddr(0x1401565A0, "Component::GUI::AtkUnitBase_SetX")
NameAddr(0x1401565C0, "Component::GUI::AtkUnitBase_SetY")
NameAddr(0x140164DA0, "Client::System::Crypt::SimpleString_Encrypt")
NameAddr(0x140164E00, "Client::System::Crypt::SimpleString_Decrypt")
NameAddr(0x14016DEF0, "Client::System::Framework::TaskManager_SetTask")
NameAddr(0x14017CA80, "Client::Graphics::Environment::EnvManager_ctor")
NameAddr(0x1401919A0, "j_SleepEx")
NameAddr(0x14019CB40, "Client::System::Resource::Handle::ResourceHandle_DecRef")
NameAddr(0x14019CB70, "Client::System::Resource::Handle::ResourceHandle_IncRef")
NameAddr(0x14019EA30, "Client::System::Resource::Handle::ResourceHandle_GetData")
NameAddr(0x1401ACF20, "ResourceManager_GetResourceAsync") # no vtbl on this class wouldnt be surprised if it was Client::System::Resource::ResourceManager or something though
NameAddr(0x1401AD140, "ResourceManager_GetResourceSync")
NameAddr(0x1401B5500, "Client::System::Resource::Handle::ModelResourceHandle_GetMaterialFileNameBySlot")
NameAddr(0x1401CE970, "Client::Graphics::Primitive::Manager_ctor")
NameAddr(0x1401D3850, "Client::Graphics::AllocatorManager_ctor")
NameAddr(0x1401EA6E0, "Client::UI::Agent::AgentInterface_ctor")
NameAddr(0x1401EA7E0, "Client::UI::AgentInterface_IsAgentActive")
NameAddr(0x1401F2990, "Client::UI::Agent::AgentModule_ctor")
NameAddr(0x14020CD10, "Client::UI::Agent::AgentLobby_ctor")
NameAddr(0x1402F9ED0, "Client::Graphics::Kernel::Device_ctor")
NameAddr(0x140318C20, "Client::Graphics::Render::GraphicsConfig_ctor")
NameAddr(0x140322600, "Client::Graphics::Render::AmbientLight_ctor")
NameAddr(0x140324570, "Client::Graphics::Render::Model_ctor")
NameAddr(0x1403246C0, "Client::Graphics::Render::Model_SetupFromModelResourceHandle")
NameAddr(0x14035C620, "Client::Graphics::Render::RenderManager_ctor")
NameAddr(0x14035D800, "Client::Graphics::Render::RenderManager_CreateModel")
NameAddr(0x14035EAE0, "Client::Graphics::Render::ShadowManager_ctor")
NameAddr(0x140363110, "Client::Graphics::Render::LightingManager::LightingRenderer_ctor")
NameAddr(0x14036D9C0, "Client::Graphics::Render::LightingManager_ctor")
NameAddr(0x14036E1A0, "Client::Graphics::Render::RenderTargetManager_ctor")
NameAddr(0x14038EF50, "Client::Graphics::PostEffect::PostEffectManager_ctor")
NameAddr(0x140424850, "Client::Graphics::Scene::DrawObject_ctor")
NameAddr(0x140424E00, "Client::Graphics::Scene::World_ctor")
NameAddr(0x1404250C0, "Client::Graphics::Scene::Camera_ctor")
NameAddr(0x140426B90, "Client::Graphics::Scene::CameraManager_ctor")
NameAddr(0x14042A2C0, "Client::Graphics::Scene::CharacterUtility_ctor")
NameAddr(0x14042A4D0, "Client::Graphics::Scene::CharacterUtility_CreateDXRenderObjects")
NameAddr(0x14042A920, "Client::Graphics::Scene::CharacterUtility_LoadDataFiles")
NameAddr(0x14042E6A0, "Client::Graphics::Scene::CharacterUtility_GetSlotEqpFlags")
NameAddr(0x140431740, "Client::Graphics::Scene::CharacterBase_ctor")
NameAddr(0x140443770, "Client::Graphics::Scene::CharacterBase_CreateSlotStorage")
NameAddr(0x140435530, "Client::Graphics::Scene::CharacterBase_CreateBonePhysicsModule")
NameAddr(0x140436FA0, "Client::Graphics::Scene::CharacterBase_LoadAnimation")
NameAddr(0x140437970, "Client::Graphics::Scene::CharacterBase_LoadMDLForSlot")
NameAddr(0x140437A60, "Client::Graphics::Scene::CharacterBase_LoadIMCForSlot")
NameAddr(0x140437C30, "Client::Graphics::Scene::CharacterBase_LoadAllMTRLsFromMDLInSlot")
NameAddr(0x140437DD0, "Client::Graphics::Scene::CharacterBase_LoadAllDecalTexFromMDLInSlot")
NameAddr(0x140437F40, "Client::Graphics::Scene::CharacterBase_LoadPHYBForSlot")
NameAddr(0x1404386F0, "Client::Graphics::Scene::CharacterBase_CopyIMCForSlot")
NameAddr(0x140438A60, "Client::Graphics::Scene::CharacterBase_CreateStagingArea")
NameAddr(0x140438B80, "Client::Graphics::Scene::CharacterBase_PopulateMaterialsFromStaging")
NameAddr(0x140438CD0, "Client::Graphics::Scene::CharacterBase_LoadMDLSubFilesIntoStaging")
NameAddr(0x140438EE0, "Client::Graphics::Scene::CharacterBase_LoadMDLSubFilesForSlot")
NameAddr(0x1404391B0, "Client::Graphics::Scene::CharacterBase_UpdateMaterials")
NameAddr(0x140439990, "PrepareColorSet")
NameAddr(0x140439C60, "ReadStainingTemplate")
NameAddr(0x14043B260, "Client::Graphics::Scene::CharacterBase_CreateRenderModelForMDL")
NameAddr(0x14043C960, "Client::Graphics::Scene::Human_ctor")
NameAddr(0x14043CBA0, "Client::Graphics::Scene::Human_SetupFromCharacterData")
NameAddr(0x14043CEB0, "Client::Graphics::Scene::Human_CleanupRender")
NameAddr(0x14043D630, "Client::Graphics::Scene::Human_UpdateRender")
NameAddr(0x14043DD30, "Client::Graphics::Scene::Human_FlagSlotForUpdate")
NameAddr(0x14043DDB0, "Client::Graphics::Scene::Human_GetDataForSlot")
NameAddr(0x14043E4B0, "Client::Graphics::Scene::Human_ResolveMDLPath")
NameAddr(0x14043F270, "Client::Graphics::Scene::Human_ResolveMTRLPath")
NameAddr(0x14043FC60, "Client::Graphics::Scene::Human_GetDyeForSlot")
NameAddr(0x140456D20, "Client::Graphics::Scene::ResidentResourceManager_ctor")
NameAddr(0x140456D50, "Client::Graphics::Scene::ResidentResourceManager_nullsub_1")
NameAddr(0x140456D80, "Client::Graphics::Scene::ResidentResourceManager_LoadDataFiles")
NameAddr(0x1404588D0, "Client::Graphics::Scene::CharacterBase_dtor")
NameAddr(0x1404596B0, "Client::Graphics::Scene::Human_dtor")
NameAddr(0x14048BD60, "Client::Game::Control::TargetSystem_ctor")
NameAddr(0x1404B4C30, "Component::GUI::AtkStage_ctor")
NameAddr(0x1404C47E0, "Component::GUI::AtkResNode_ctor")
NameAddr(0x1404C55C0, "Component::GUI::AtkResNode_SetPositionAndFlagForUpdate")
NameAddr(0x1404C5610, "Component::GUI::AtkResNode_SetPosition")
NameAddr(0x1404C6810, "Component::GUI::AtkResNode_Init")
NameAddr(0x1404C7E00, "Component::GUI::AtkTextNode_SetForegroundColour")
NameAddr(0x1404CD980, "Component::GUI::AtkResNode_SetupFromULDFileBuffer")
NameAddr(0x1404CE7F0, "CreateAtkNode")
NameAddr(0x1404CFC00, "CreateAtkComponent")
NameAddr(0x1404D0F20, "Component::GUI::AtkResNode_SetSize")
NameAddr(0x1404D2830, "Component::GUI::AtkUnitBase_ctor")
NameAddr(0x1404D2F80, "Component::GUI::AtkUnitBase_SetPosition")
NameAddr(0x1404D3100, "Component::GUI::AtkUnitBase_SetAlpha")
NameAddr(0x1404D33E0, "GetScaleListEntryFromScale")
NameAddr(0x1404D3500, "Component::GUI::AtkUnitBase_SetScale")
NameAddr(0x1404D3870, "Component::GUI::AtkUnitBase_CalculateBounds")
NameAddr(0x1404D5FC0, "Component::GUI::AtkStage_GetSingleton1")
NameAddr(0x1404D5FD0, "Component::GUI::AtkStage_GetSingleton2")
NameAddr(0x1404DD560, "Component::GUI::AtkUnitManager_ctor")
NameAddr(0x1404DF070, "Client::UI::RaptureAtkUnitManager_GetAddonByName")
NameAddr(0x1404E1840, "Client::UI::RaptureAtkUnitManager_SetUnitScale")
NameAddr(0x1404E1B00, "GetScaleForListOption")
NameAddr(0x1404EA760, "Component::GUI::AtkComponentBase_ctor")
NameAddr(0x1404EAA10, "Component::GUI::AtkComponentBase_GetOwnerNodePosition")
NameAddr(0x1404EB590, "Component::GUI::AtkComponentButton_SetEnabledState")
NameAddr(0x1404EBE90, "Component::GUI::AtkComponentButton_ctor")
NameAddr(0x1404EE3D0, "Component::GUI::AtkComponentIcon_ctor")
NameAddr(0x1404EEF10, "Component::GUI::AtkComponentListItemRenderer_ctor")
NameAddr(0x1404FA160, "Component::GUI::AtkComponentList_ctor")
NameAddr(0x1404FEAF0, "Component::GUI::AtkComponentTreeList_ctor")
NameAddr(0x140503760, "Component::GUI::AtkModule_ctor")
NameAddr(0x140507710, "Component::GUI::AtkComponentCheckBox_ctor")
NameAddr(0x140508630, "Component::GUI::AtkComponentGaugeBar_ctor")
NameAddr(0x14050A760, "Component::GUI::AtkComponentSlider_ctor")
NameAddr(0x14050BB70, "Component::GUI::AtkComponentInputBase_ctor")
NameAddr(0x14050D330, "Component::GUI::AtkComponentTextInput_ctor")
NameAddr(0x140511A40, "Component::GUI::AtkComponentNumericInput_ctor")
NameAddr(0x1405156E0, "Component::GUI::AtkComponentDropDownList_ctor")
NameAddr(0x140516BD0, "Component::GUI::AtkComponentRadioButton_ctor")
NameAddr(0x1405174A0, "Component::GUI::AtkComponentTab_ctor")
NameAddr(0x140517A80, "Component::GUI::AtkComponentGuildLeveCard_ctor")
NameAddr(0x140517E10, "Component::GUI::AtkComponentTextNineGrid_ctor")
NameAddr(0x14051D210, "Component::GUI::AtkComponentMap_ctor")
NameAddr(0x14051FC40, "Component::GUI::AtkComponentPreview_ctor")
NameAddr(0x140520CA0, "Component::GUI::AtkComponentScrollBar_ctor")
NameAddr(0x1405226B0, "Component::GUI::AtkComponentIconText_ctor")
NameAddr(0x140523930, "Component::GUI::AtkComponentDragDrop_ctor")
NameAddr(0x140525590, "Component::GUI::AtkComponentMultipurpose_ctor")
NameAddr(0x140525EC0, "Component::GUI::AtkComponentWindow_ctor")
NameAddr(0x14052B2D0, "Component::GUI::AtkComponentJournalCanvas_ctor")
NameAddr(0x14052EF50, "Component::GUI::AtkComponentUnknownButton_ctor")
NameAddr(0x1405378E0, "Component::GUI::AtkCollisionNode_ctor")
NameAddr(0x140537940, "Component::GUI::AtkComponentNode_ctor")
NameAddr(0x1405379A0, "Component::GUI::AtkCounterNode_ctor")
NameAddr(0x140537A20, "Component::GUI::AtkImageNode_ctor")
NameAddr(0x140537A80, "Component::GUI::AtkNineGridNode_ctor")
NameAddr(0x140537BD0, "Component::GUI::AtkTextNode_ctor")
NameAddr(0x1405389B0, "Component::GUI::AtkComponentNode_Destroy")
NameAddr(0x140538F00, "Component::GUI::AtkCollisionNode_Destroy")
NameAddr(0x140539C10, "Component::GUI::AtkCounterNode_Destroy")
NameAddr(0x14053A380, "Component::GUI::AtkImageNode_Destroy")
NameAddr(0x14053A510, "Component::GUI::AtkNineGridNode_Destroy")
NameAddr(0x14053A5D0, "Component::GUI::AtkResNode_Destroy")
NameAddr(0x14053A7D0, "Component::GUI::AtkTextNode_Destroy")
NameAddr(0x1405B0DE0, "Client::UI::UI3DModule_ctor")
NameAddr(0x1405B9E30, "Client::UI::UIModule_ctor")
NameAddr(0x1405F02C0, "Client::UI::Misc::ConfigModule_ctor")
NameAddr(0x140615610, "Client::UI::Misc::RaptureHotbarModule_ctor")
NameAddr(0x14061E3D0, "Client::UI::Misc::PronounModule_ctor")
NameAddr(0x140654770, "Client::UI::Misc::RaptureMacroModule_vfunc4")
NameAddr(0x1406551E0, "Client::UI::Misc::RaptureMacroModule_ReadFile")
NameAddr(0x1406555C0, "Client::UI::Misc::RaptureMacroModule_WriteFile")
NameAddr(0x1406BA700, "Client::Game::Object::GameObject_Initialize")
NameAddr(0x1406BA960, "Client::Game::Object::GameObject_ctor")
NameAddr(0x1406C2230, "Client::Game::Character::Character_EnableDraw")
NameAddr(0x1406C2A40, "Client::Game::Character::Character_DisableDraw")
NameAddr(0x1406C4220, "Client::Game::Character::Character_GetObjectKind")
NameAddr(0x1406CCF40, "Client::Game::Character::Character_dtor")
NameAddr(0x1406CD5D0, "Client::Game::Character::Character_SetDrawObject")
NameAddr(0x1406DCDE0, "Client::Graphics::Scene::CharacterBase_Create")
NameAddr(0x1406E5330, "Client::Game::Character::Character_ctor")
NameAddr(0x1406E5410, "Client::Game::Character::Companion_ctor")
NameAddr(0x140703FD0, "Client::UI::Shell::RaptureShellModule_ctor")
NameAddr(0x1407082C0, "Client::UI::Shell::RaptureShellModule_SetChatChannel")
NameAddr(0x140736560, "CreateBattleCharaStore")
NameAddr(0x140736B30, "BattleCharaStore_LookupBattleCharaByObjectID")
NameAddr(0x140737070, "Client::Game::Character::BattleChara_ctor")
NameAddr(0x140737150, "Client::Game::Character::BattleChara_dtor")
NameAddr(0x140817F70, "Client::UI::Agent::AgentHUD_ctor")
NameAddr(0x140877150, "Client::UI::Agent::AgentMap_ctor")
NameAddr(0x1408792C0, "Client::UI::AgentMap::MapMarkerStructSearchName_Evaluate")
NameAddr(0x1408B80B0, "Client::UI::Agent::AgentHUDLayout_ctor")
NameAddr(0x1408B81B0, "Client::UI::Agent::AgentHUDLayout_Show")
NameAddr(0x1408B8220, "Client::UI::Agent::AgentHUDLayout_Hide")
NameAddr(0x1408B8D80, "CreateSelectYesno")
NameAddr(0x140A6BA20, "EventFramework_GetSingleton")
NameAddr(0x140A74040, "EventFramework_ProcessDirectorUpdate")
NameAddr(0x1410BBA70, "Client::Game::Camera_ctor")
NameAddr(0x140CA8440, "Client::UI::AddonHudSelectYesno_ctor")
NameAddr(0x140E885B0, "Client::UI::AddonAreaMap_ctor")
NameAddr(0x140E9FE20, "Client::UI::AddonNamePlate_ctor")
NameAddr(0x140EA1E60, "Client::UI::AddonNamePlate_UpdateNameplates")
NameAddr(0x140FDD850, "Client::UI::AddonHudLayoutWindow_ctor")
NameAddr(0x140FDEAE0, "Client::UI::AddonHudLayoutScreen_ctor")
NameAddr(0x140FE33E0, "Client::UI::AddonHudLayoutScreen_HandleEvent")
NameAddr(0x140FE59E0, "Client::UI::AddonHudLayoutScreen_SetAddonScale")
NameAddr(0x14107AFE0, "Client::Game::Character::Companion_EnableDraw")
NameAddr(0x14129D680, "crc")
NameAddr(0x141317414, "FreeMemory")

# globals
NameAddr(0x14163DB20, "g_HUDScaleTable")
NameAddr(0x141CBEDA0, "g_ActionManager")
NameAddr(0x141CE7D90, "g_Framework")
NameAddr(0x141CE7F60, "g_KernelDevice")
NameAddr(0x141CE9128, "g_GraphicsConfig")
NameAddr(0x141CE9138, "g_Framework_2") # these both point to framework
NameAddr(0x141CE9178, "g_AllocatorManager")
NameAddr(0x141CE9180, "g_PrimitiveManager")
NameAddr(0x141CE9188, "g_RenderManager")
NameAddr(0x141CE9190, "g_ShadowManager")
NameAddr(0x141CE9198, "g_LightingManager")
NameAddr(0x141CE91A0, "g_RenderTargetManager")
NameAddr(0x141CE91A8, "g_StreamingManager")
NameAddr(0x141CE91B0, "g_PostEffectManager")
NameAddr(0x141CE91B8, "g_EnvManager")
NameAddr(0x141CE91C0, "g_World")
NameAddr(0x141CE91C8, "g_CameraManager")
NameAddr(0x141CE91D0, "g_CharacterUtility")
NameAddr(0x141CE91D8 "g_ResidentResourceManager")
NameAddr(0x141CEB748, "g_CullingManager")
NameAddr(0x141CEB768, "g_TaskManager")
NameAddr(0x141CF09F0, "g_ResourceManager")
NameAddr(0x141D02A20, "g_OcclusionCullingManager")
NameAddr(0x141D0AC20, "g_CameraHolder")
NameAddr(0x141D0AD70, "g_TargetSystem")
NameAddr(0x141D0F200, "g_AtkStage")
NameAddr(0x141D32870, "g_BattleCharaStore") # this is a struct/object containing a list of all battlecharas (0x100) and the memory ptrs below
NameAddr(0x141D32B90, "g_BattleCharaMemory")
NameAddr(0x141D32B98, "g_CompanionMemory")
NameAddr(0x141D32BC0, "g_ActorList")
NameAddr(0x141D33900, "g_ActorListEnd")
NameAddr(0x141D57D50, "g_EventFramework")

# vtbl
NameAddr(0x1415F43D0, "vtbl_Client::System::Framework")	
NameAddr(0x1415FDFB0, "vtbl_Component::GUI::AtkUnitList")	
NameAddr(0x1415FDFB8, "vtbl_Component::GUI::AtkUnitManager")	
NameAddr(0x1415FE110, "vtbl_Client::UI::RaptureAtkUnitManager")	
NameAddr(0x1415FE368, "vtbl_Client::UI::RaptureAtkModule")	
NameAddr(0x141619778, "vtbl_Client::UI::Agent::AgentInterface")	
NameAddr(0x141619BA0, "vtbl_Client::UI::Agent::AgentModule")	
NameAddr(0x141639290, "vtbl_Client::Graphics::Scene::Object")	
NameAddr(0x1416392C0, "vtbl_Client::Graphics::Scene::DrawObject")	
NameAddr(0x141639748, "vtbl_Client::Graphics::Scene::CharacterBase")	
NameAddr(0x141639A58, "vtbl_Client::Graphics::Scene::Human")	
NameAddr(0x14163DB80, "vtbl_Component::GUI::AtkArrayData")	
NameAddr(0x14163DB90, "vtbl_Component::GUI::NumberArrayData")	
NameAddr(0x14163DBA0, "vtbl_Component::GUI::StringArrayData")	
NameAddr(0x14163DBB0, "vtbl_Component::GUI::ExtendArrayData")	
NameAddr(0x14163DE28, "vtbl_Component::GUI::AtkStage")	
NameAddr(0x14163E6D0, "vtbl_Component::GUI::AtkResNode")	
NameAddr(0x14163E6E8, "vtbl_Component::GUI::AtkImageNode")	
NameAddr(0x14163E700, "vtbl_Component::GUI::AtkTextNode")	
NameAddr(0x14163E718, "vtbl_Component::GUI::AtkNineGridNode")	
NameAddr(0x14163E730, "vtbl_Component::GUI::AtkCounterNode")	
NameAddr(0x14163E748, "vtbl_Component::GUI::AtkCollisionNode")	
NameAddr(0x14163E760, "vtbl_Component::GUI::AtkComponentNode")	
NameAddr(0x14163E778, "vtbl_Component::GUI::AtkUnitBase")	
NameAddr(0x14163EA00, "vtbl_Component::GUI::AtkComponentBase")	
NameAddr(0x14163EAA0, "vtbl_Component::GUI::AtkComponentButton")	
NameAddr(0x14163EB68, "vtbl_Component::GUI::AtkComponentIcon")	
NameAddr(0x14163EC88, "vtbl_Component::GUI::AtkComponentListItemRenderer")	
NameAddr(0x14163EDF8, "vtbl_Component::GUI::AtkComponentList")	
NameAddr(0x14163EF60, "vtbl_Component::GUI::AtkComponentTreeList")	
NameAddr(0x14163F0C8, "vtbl_Component::GUI::AtkModule")	
NameAddr(0x14163F370, "vtbl_Component::GUI::AtkComponentCheckBox")	
NameAddr(0x14163F440, "vtbl_Component::GUI::AtkComponentGaugeBar")	
NameAddr(0x14163F4E0, "vtbl_Component::GUI::AtkComponentSlider")	
NameAddr(0x14163F580, "vtbl_Component::GUI::AtkComponentInputBase")	
NameAddr(0x14163F620, "vtbl_Component::GUI::AtkComponentTextInput")	
NameAddr(0x14163F720, "vtbl_Component::GUI::AtkComponentNumericInput")	
NameAddr(0x14163F7E8, "vtbl_Component::GUI::AtkComponentDropDownList")	
NameAddr(0x14163F888, "vtbl_Component::GUI::AtkComponentRadioButton")	
NameAddr(0x14163F998, "vtbl_Component::GUI::AtkComponentTab")	
NameAddr(0x14163FAA8, "vtbl_Component::GUI::AtkComponentGuildLeveCard")	
NameAddr(0x14163FB48, "vtbl_Component::GUI::AtkComponentTextNineGrid")	
NameAddr(0x14163FCA0, "vtbl_Component::GUI::AtkComponentMap")	
NameAddr(0x14163FD40, "vtbl_Component::GUI::AtkComponentPreview")	
NameAddr(0x14163FDE0, "vtbl_Component::GUI::AtkComponentScrollBar")	
NameAddr(0x14163FE80, "vtbl_Component::GUI::AtkComponentIconText")	
NameAddr(0x14163FF20, "vtbl_Component::GUI::AtkComponentDragDrop")	
NameAddr(0x141640040, "vtbl_Component::GUI::AtkComponentMultipurpose")	
NameAddr(0x1416401B0, "vtbl_Component::GUI::AtkComponentWindow")	
NameAddr(0x141640280, "vtbl_Component::GUI::AtkComponentJournalCanvas")	
NameAddr(0x141640320, "vtbl_Component::GUI::AtkComponentUnknownButton")	
NameAddr(0x14164D2B8, "vtbl_Client::UI::UI3DModule::ObjectInfo")	
NameAddr(0x14164D2E8, "vtbl_Client::UI::UI3DModule::MemberInfo")	
NameAddr(0x14164D348, "vtbl_Client::UI::UI3DModule")	
NameAddr(0x14164D360, "vtbl_Client::UI::UIModule")	
NameAddr(0x1416543E0, "vtbl_Client::Game::Object::GameObject")	
NameAddr(0x141654F88, "vtbl_Client::Game::Character::Character")	
NameAddr(0x141655270, "vtbl_Client::Game::Character::Companion")	
NameAddr(0x141665FF8, "vtbl_Client::Game::Character::BattleChara")	
NameAddr(0x1416685D0, "vtbl_Client::Game::ActionManager")	
NameAddr(0x14166B110, "vtbl_Client::UI::Agent::AgentMap::MapMarkerStructSearchName")	
NameAddr(0x14166B120, "vtbl_Client::UI::Agent::AgentMap")	
NameAddr(0x14166BD20, "vtbl_Client::UI::Agent::AgentHudLayout")	
NameAddr(0x141762280, "vtbl_Client::UI::Atk2DAreaMap")	
NameAddr(0x141774E28, "vtbl_Client::UI::AddonAreaMap")	
NameAddr(0x141776C78, "vtbl_Client::UI::AddonNamePlate")	
NameAddr(0x1417A67F0, "vtbl_Client::UI::AddonHudLayoutWindow")	
NameAddr(0x1417A6A08, "vtbl_Client::UI::AddonHudLayoutScreen")