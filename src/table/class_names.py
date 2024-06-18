
class ClassNames:
    CAccount = "CAccount"
    CAccounts = "CAccounts"
    CResourceLink = "CResourceLink"
    CCChampionDef = "CCChampionDef"
    CChar = "CChar"
    CCharBase = "CCharBase"
    CCharNPC = "CCharNPC"
    CCharPlayer = "CCharPlayer"
    CClient = "CClient"
    CDialogDef = "CDialogDef"
    CDialogResponseArgs = "CDialogResponseArgs"
    CEntity = "CEntity"
    CSFileObj = "CSFileObj"
    CSFileObjContainer = "CSFileObjContainer"
    CScriptObj = "CScriptObj"
    CScriptTriggerArgs = "CScriptTriggerArgs"
    CScript = "CScript"
    CResourceRefArray = "CResourceRefArray"
    CRegionWorld = "CRegionWorld"
    CRegion = "CRegion"
    CWorld = "CWorld"
    CWorldCache = "CWorldCache"
    CWorldComm = "CWorldComm"
    CWorldGameTime = "CWorldGameTime"
    CWorldMap = "CWorldMap"
    CWorldTicker = "CWorldTicker"
    CWorldTickingList = "CWorldTickingList"
    CWorldThread = "CWorldThread"
    CWebPageDef = "CWebPageDef"
    CServerDef = "CServerDef"
    CServer = "CServer"
    CSector = "CSector"
    CSectorBase = "CSectorBase"
    CSectorList = "CSectorList"
    CRegionResourceDef = "CRegionResourceDef"
    CRandGroupDef = "CRandGroupDef"
    CSpellDef = "CSpellDef"
    CSkillClassDef = "CSkillClassDef"
    CItemTypeDef = "CItemTypeDef"
    CServerConfig = "CServerConfig"
    CObjBase = "CObjBase"
    CContainer = "CContainer"
    CItemContainer = "CItemContainer"
    CGMPage = "CGMPage"
    CItemBase = "CItemBase"
    CItem = "CItem"
    CItemCommCrystal = "CItemCommCrystal"
    CItemCorpse = "CItemCorpse"
    CItemMulti = "CItemMulti"
    CItemMultiCustom = "CItemMultiCustom"
    CItemMap = "CItemMap"
    CItemMessage = "CItemMessage"
    CItemVendable = "CItemVendable"
    CItemShip = "CItemShip"
    CCSpawn = "CCSpawn"
    CItemStone = "CItemStone"
    CDataBase = "CDataBase"
    CItemBaseMulti = "CItemBaseMulti"
    CPathFinder = "CPathFinder"
    CPartyDef = "CPartyDef"
    CSObjCont = "CSObjCont"
    CSObjList = "CSObjList"
    CSQLite = "CSQLite"
    CStoneMember = "CStoneMember"
    CTimedObject = "CTimedObject"
    CVarDefCont = "CVarDefCont"
    CVarDefContNum = "CVarDefContNum"
    CVarDefContStr = "CVarDefContStr"
    CVarDefMap = "CVarDefMap"
    CNetworkInput = "CNetworkInput"
    CNetworkOutput = "CNetworkOutput"
    CNetworkThread = "CNetworkThread"
    CNetworkManager = "CNetworkManager"
    
    # Conditionally defined class
    try:
        from win32 import CNTWindow
        CNTWindow = "CNTWindow"
    except ImportError:
        CNTWindow = None
