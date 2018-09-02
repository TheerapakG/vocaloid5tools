import ctypes
import csharptypes

import VDMError
import DatabaseManagerIF
import DSEManagerIF
import DSE_License
import LicenseResult
import WVSMModuleIF

path = "vocaloid editor path: "

def load_path():
    DatabaseManagerIF.path = path
    DatabaseManagerIF.load_vdm_path()
    DSEManagerIF.path = path
    DSEManagerIF.load_dse_path()
    DSE_License.load_dse_dll(DSEManagerIF.dse)
    WVSMModuleIF.path = path
    WVSMModuleIF.load_vsm_path()

class App:
    
    DatabaseManager = None
    DSEManager = None
    SequenceManager = None
    
    def InitializeModule():

        print("NOT Checking for software update ...")
        
        print("Initializing modules (VDM) ...")
        result1 = VDMError.VDMError.NotAny
        result1_p = ctypes.pointer(ctypes.c_int(VDMError.VDMError.NotAny))
        App.DatabaseManager = DatabaseManagerIF.DatabaseManagerIF.CreateDatabaseManager("voc5", result1_p)
        if(App.DatabaseManager == None or result1 != VDMError.VDMError.NotAny):
            if (result1 == VDMError.VDMError.VoiceBankNotFound):
                print("GeneralError: Resources.VerifyLicense_NoVoice")
            else:
                print("GeneralError: Resources.MsgBox_DatabaseManagerInitialization_Error")
            raise Exception("App.ModuleResult.Fail")

        print("Initializing modules (DSE) ...")
        App.DSEManager = DSEManagerIF.DSEManagerIF.CreateManager(App.DatabaseManager)
        if (App.DSEManager == None):
            print("GeneralError: Resources.MsgBox_DSEManagerInitialization_Error")
            raise Exception("App.ModuleResult.Fail")
        licenseResult = LicenseResult.LicenseResult.Undefined
        flag2 = False
        licenseList = list()
        for _license in App.DSEManager.GetLicenses():
            if(_license.CompType == DSE_License.License.Type.Application):
                if(_license.CompID == "BWMZBX5ALBWWZWEB"):
                    licenseResult = _license.Result
                    continue
                continue
            elif(_license.CompType == DSE_License.License.Type.Voice):
                flag2 = True
                if(_license.Result == LicenseResult.LicenseResult.ValidExpiryKey):
                    continue
                elif(_license.Result == LicenseResult.LicenseResult.NoError):
                    continue
                else:
                    if(5 <= _license.CompVersion.Major):
                        licenseList.append(_license)
                        continue
                    continue
            else:
                continue
        if(licenseResult == LicenseResult.LicenseResult.Trial):
            print("VOCALOID5 Editor not authorized. Please enter a valid VOCALOID5 serial number into the VOCALOID Authorizer.")
            print("there's suppose to be a yes/no dialog box here to launch authorizer")
            raise Exception("App.ModuleResult.AuthorizationFail")
        if(licenseResult == LicenseResult.LicenseResult.ValidExpiryKey or licenseResult == LicenseResult.LicenseResult.NoError):
            if(not flag2):
                print("Resources.VerifyLicense_NoVoice")
                raise Exception("App.ModuleResult.AuthorizationFail")
            if (0 < len(licenseList)):
                _str = "Resources.VerifyLicense_VoiceNotAuthorized" + "\n\n"
                for index in range(0, len(licenseList)):
                    if(5 <= index):
                        _str = _str + "  (remaining {0} voices)".format(len(licenseList) - index) + "\n"
                        break
                    _str = _str + "- " + licenseList[index].CompName + "\n"
                message = _str + "\n" + "Please enter the applicable serial number for this voice into the VOCALOID Authorizer"
                print(message)
                print("there's suppose to be a yes/no dialog box here to launch authorizer")
                raise Exception("App.ModuleResult.AuthorizationFail")
            
            print("Initializing modules (VSM) ...")
            App.SequenceManager = WVSMModuleIF.WVSMModuleIF.CreateManager("voc5")
            if(App.SequenceManager == None):
                raise Exception("Resources.MsgBox_VSMInitialization_Error")
            App.SequenceManager.SetDatabaseManager(App.DatabaseManager)
            App.SequenceManager.SetDSEManager(App.DSEManager)

if __name__ == '__main__':
    path = input(path)
    load_path()
    App.InitializeModule()
