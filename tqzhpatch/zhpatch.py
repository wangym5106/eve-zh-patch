import localization
import localization.const


def unlock_zh():

    localization.__GetLocalization().languagesDefined.add('zh')

    def _ReadLocalizationMainPickle_decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if 'zh' not in ret:
                ret.append('zh')
            return ret
        return wrapper

    localization.__GetLocalization()._ReadLocalizationMainPickle = _ReadLocalizationMainPickle_decorator(localization.__GetLocalization()._ReadLocalizationMainPickle)

    
def set_primary_language():
    
    def _GetPrimaryLanguage_zh(self=None):
        return localization.const.LOCALE_SHORT_CHINESE

    localization.__GetLocalization()._GetPrimaryLanguage = _GetPrimaryLanguage_zh
    localization.__GetLocalization()._primaryLanguageID = localization.const.LOCALE_SHORT_CHINESE


def apply_localization():
    prefs.SetValue('localizationImportantNames',1)
    prefs.SetValue('languageTooltip', True)
    prefs.SetValue('localizationHighlightImportant', True)
    localization.LoadLanguageData()
    localization.ClearImportantNameSetting()
    sm.ChainEvent('ProcessUIRefresh')
    sm.ScatterEvent('OnUIRefresh')


