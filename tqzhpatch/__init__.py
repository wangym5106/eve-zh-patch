import logmodule

import zhpatchsvc

if boot.region != 'optic':
    zhpatchsvc.start_service()
