import svc
import service
import localization
import localization.const
import logmodule
import zhpatch

class zhPatchSvc(service.Service):
    __guid__ = 'svc.zhPatchSvc'
    __servicename__ = 'svc.zhPatchSvc'
    __notifyevents__ = ['OnSessionChanged']
    __displayname__ = 'ZH Localization Patch Service'
    
    executed = False


    def Run(self, *args):
        service.Service.Run(self, *args)

    def OnSessionChanged(self, func, *args, **kwargs):
        if not self.executed:
            zhpatch.unlock_zh()
            zhpatch.set_primary_language()
            zhpatch.apply_localization()
            self.executed = True


def start_service():
    svc.zhPatchSvc=zhPatchSvc
    sm.startInline+=('zhPatchSvc',)
    sm.StartService('zhPatchSvc')

