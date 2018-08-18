import ctypes
import VDMError
import DatabaseManagerIF
import DSEManagerIF

class App:
    
    DataBaseManager = None
    
    def InitializeModule():
        
        print("Initializing modules (VDM) ...")
        result1 = VDMError.NotAny
        result1_p = ctypes.pointer(ctypes.c_int(VDMError.NotAny))
        App.DatabaseManager = DatabaseManagerIF.CreateDatabaseManager("voc5", ref result1)
        if(App.DatabaseManager == None or result1 != VDMError.None):
            raise Exception("App.ModuleResult.Fail")

        print("Initializing modules (DSE) ...")

if __name__ == '__main__':
    DatabaseManagerIF.path = input(DatabaseManagerIF.path)
    DatabaseManagerIF.load_vdm_path()
