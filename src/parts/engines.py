from . import abc_parts

class BaseEngine(abc_parts.ABCPart):
    @property
    def propellant_mass(self):
        return 0.


class LR89_5(BaseEngine):
    '''
    Atlas-IE-89-5 "Buzzard" Liquid Engine

    Simple, reliable 1.25m lifter engine. Designed for use on the jettisonable
    Atlas-DBSF Booster Skirt for half staging Atlas rockets.

    Original model used on early Atlas LV3 models
    '''
    @property
    def dry_mass(self):
        return 1.75

    @property
    def thrust(self):
        return 205.

    @property
    def isp(self):
        return 256.


class LR89_7(BaseEngine):
    '''
    Atlas-IE-89-7 "Buzzard" Liquid Engine

    Simple, reliable 1.25m lifter engine. Designed for use on the jettisonable
    Atlas-DBSF Booster Skirt for half staging Atlas rockets.

    Upgraded model used on the SLV3 series and Atlas I
    '''
    @property
    def dry_mass(self):
        return 1.75

    @property
    def thrust(self):
        return 236.

    @property
    def isp(self):
        return 255.


class RS56_OBA(BaseEngine):
    '''
    Atlas-IIE-RS56-OBA "Buzzard" Liquid Engine

    Simple, reliable 1.25m lifter engine. Designed for use on the jettisonable
    Atlas-DBSF Booster Skirt for half staging Atlas rockets.

    Upgraded model used on the SLV3 series and Atlas I
    '''
    @property
    def dry_mass(self):
        return 1.75

    @property
    def thrust(self):
        return 261.

    @property
    def isp(self):
        return 263.
