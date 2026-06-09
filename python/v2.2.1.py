from typing import Any, List, Optional, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class ChargingProfilePeriod:
    limit: float
    start_period: int

    def __init__(self, limit: float, start_period: int) -> None:
        self.limit = limit
        self.start_period = start_period

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingProfilePeriod':
        assert isinstance(obj, dict)
        limit = from_float(obj.get("limit"))
        start_period = from_int(obj.get("start_period"))
        return ChargingProfilePeriod(limit, start_period)

    def to_dict(self) -> dict:
        result: dict = {}
        result["limit"] = to_float(self.limit)
        result["start_period"] = from_int(self.start_period)
        return result


class ChargingRateUnit(Enum):
    A = "A"
    W = "W"


class ChargingProfile:
    charging_profile_period: Optional[List[ChargingProfilePeriod]]
    charging_rate_unit: ChargingRateUnit
    duration: Optional[int]
    min_charging_rate: Optional[float]
    start_date_time: Optional[str]

    def __init__(self, charging_profile_period: Optional[List[ChargingProfilePeriod]], charging_rate_unit: ChargingRateUnit, duration: Optional[int], min_charging_rate: Optional[float], start_date_time: Optional[str]) -> None:
        self.charging_profile_period = charging_profile_period
        self.charging_rate_unit = charging_rate_unit
        self.duration = duration
        self.min_charging_rate = min_charging_rate
        self.start_date_time = start_date_time

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingProfile':
        assert isinstance(obj, dict)
        charging_profile_period = from_union([from_none, lambda x: from_list(ChargingProfilePeriod.from_dict, x)], obj.get("charging_profile_period"))
        charging_rate_unit = ChargingRateUnit(obj.get("charging_rate_unit"))
        duration = from_union([from_none, from_int], obj.get("duration"))
        min_charging_rate = from_union([from_none, from_float], obj.get("min_charging_rate"))
        start_date_time = from_union([from_none, from_str], obj.get("start_date_time"))
        return ChargingProfile(charging_profile_period, charging_rate_unit, duration, min_charging_rate, start_date_time)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.charging_profile_period is not None:
            result["charging_profile_period"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ChargingProfilePeriod, x), x)], self.charging_profile_period)
        result["charging_rate_unit"] = to_enum(ChargingRateUnit, self.charging_rate_unit)
        if self.duration is not None:
            result["duration"] = from_union([from_none, from_int], self.duration)
        if self.min_charging_rate is not None:
            result["min_charging_rate"] = from_union([from_none, to_float], self.min_charging_rate)
        if self.start_date_time is not None:
            result["start_date_time"] = from_union([from_none, from_str], self.start_date_time)
        return result


class ActiveChargingProfile:
    charging_profile: ChargingProfile
    start_date_time: str

    def __init__(self, charging_profile: ChargingProfile, start_date_time: str) -> None:
        self.charging_profile = charging_profile
        self.start_date_time = start_date_time

    @staticmethod
    def from_dict(obj: Any) -> 'ActiveChargingProfile':
        assert isinstance(obj, dict)
        charging_profile = ChargingProfile.from_dict(obj.get("charging_profile"))
        start_date_time = from_str(obj.get("start_date_time"))
        return ActiveChargingProfile(charging_profile, start_date_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["charging_profile"] = to_class(ChargingProfile, self.charging_profile)
        result["start_date_time"] = from_str(self.start_date_time)
        return result


class ChargingProfileResultType(Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"


class ActiveChargingProfileResult:
    profile: Optional[ActiveChargingProfile]
    result: ChargingProfileResultType

    def __init__(self, profile: Optional[ActiveChargingProfile], result: ChargingProfileResultType) -> None:
        self.profile = profile
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'ActiveChargingProfileResult':
        assert isinstance(obj, dict)
        profile = from_union([ActiveChargingProfile.from_dict, from_none], obj.get("profile"))
        result = ChargingProfileResultType(obj.get("result"))
        return ActiveChargingProfileResult(profile, result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.profile is not None:
            result["profile"] = from_union([lambda x: to_class(ActiveChargingProfile, x), from_none], self.profile)
        result["result"] = to_enum(ChargingProfileResultType, self.result)
        return result


class AllowedType(Enum):
    ALLOWED = "ALLOWED"
    BLOCKED = "BLOCKED"
    EXPIRED = "EXPIRED"
    NOT_ALLOWED = "NOT_ALLOWED"
    NO_CREDIT = "NO_CREDIT"


class DisplayText:
    language: str
    text: str

    def __init__(self, language: str, text: str) -> None:
        self.language = language
        self.text = text

    @staticmethod
    def from_dict(obj: Any) -> 'DisplayText':
        assert isinstance(obj, dict)
        language = from_str(obj.get("language"))
        text = from_str(obj.get("text"))
        return DisplayText(language, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["language"] = from_str(self.language)
        result["text"] = from_str(self.text)
        return result


class LocationReferences:
    evse_uids: Optional[List[str]]
    location_id: str

    def __init__(self, evse_uids: Optional[List[str]], location_id: str) -> None:
        self.evse_uids = evse_uids
        self.location_id = location_id

    @staticmethod
    def from_dict(obj: Any) -> 'LocationReferences':
        assert isinstance(obj, dict)
        evse_uids = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("evse_uids"))
        location_id = from_str(obj.get("location_id"))
        return LocationReferences(evse_uids, location_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.evse_uids is not None:
            result["evse_uids"] = from_union([from_none, lambda x: from_list(from_str, x)], self.evse_uids)
        result["location_id"] = from_str(self.location_id)
        return result


class ProfileType(Enum):
    CHEAP = "CHEAP"
    FAST = "FAST"
    GREEN = "GREEN"
    REGULAR = "REGULAR"


class EnergyContract:
    contract_id: Optional[str]
    supplier_name: str

    def __init__(self, contract_id: Optional[str], supplier_name: str) -> None:
        self.contract_id = contract_id
        self.supplier_name = supplier_name

    @staticmethod
    def from_dict(obj: Any) -> 'EnergyContract':
        assert isinstance(obj, dict)
        contract_id = from_union([from_none, from_str], obj.get("contract_id"))
        supplier_name = from_str(obj.get("supplier_name"))
        return EnergyContract(contract_id, supplier_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.contract_id is not None:
            result["contract_id"] = from_union([from_none, from_str], self.contract_id)
        result["supplier_name"] = from_str(self.supplier_name)
        return result


class TokenType(Enum):
    AD_HOC_USER = "AD_HOC_USER"
    APP_USER = "APP_USER"
    OTHER = "OTHER"
    RFID = "RFID"


class WhitelistType(Enum):
    ALLOWED = "ALLOWED"
    ALLOWED_OFFLINE = "ALLOWED_OFFLINE"
    ALWAYS = "ALWAYS"
    NEVER = "NEVER"


class Token:
    contract_id: str
    country_code: str
    default_profile_type: Optional[ProfileType]
    energy_contract: Optional[EnergyContract]
    group_id: Optional[str]
    issuer: str
    language: Optional[str]
    last_updated: str
    party_id: str
    type: TokenType
    uid: str
    valid: bool
    visual_number: Optional[str]
    whitelist: WhitelistType

    def __init__(self, contract_id: str, country_code: str, default_profile_type: Optional[ProfileType], energy_contract: Optional[EnergyContract], group_id: Optional[str], issuer: str, language: Optional[str], last_updated: str, party_id: str, type: TokenType, uid: str, valid: bool, visual_number: Optional[str], whitelist: WhitelistType) -> None:
        self.contract_id = contract_id
        self.country_code = country_code
        self.default_profile_type = default_profile_type
        self.energy_contract = energy_contract
        self.group_id = group_id
        self.issuer = issuer
        self.language = language
        self.last_updated = last_updated
        self.party_id = party_id
        self.type = type
        self.uid = uid
        self.valid = valid
        self.visual_number = visual_number
        self.whitelist = whitelist

    @staticmethod
    def from_dict(obj: Any) -> 'Token':
        assert isinstance(obj, dict)
        contract_id = from_str(obj.get("contract_id"))
        country_code = from_str(obj.get("country_code"))
        default_profile_type = from_union([from_none, ProfileType], obj.get("default_profile_type"))
        energy_contract = from_union([from_none, EnergyContract.from_dict], obj.get("energy_contract"))
        group_id = from_union([from_none, from_str], obj.get("group_id"))
        issuer = from_str(obj.get("issuer"))
        language = from_union([from_none, from_str], obj.get("language"))
        last_updated = from_str(obj.get("last_updated"))
        party_id = from_str(obj.get("party_id"))
        type = TokenType(obj.get("type"))
        uid = from_str(obj.get("uid"))
        valid = from_bool(obj.get("valid"))
        visual_number = from_union([from_none, from_str], obj.get("visual_number"))
        whitelist = WhitelistType(obj.get("whitelist"))
        return Token(contract_id, country_code, default_profile_type, energy_contract, group_id, issuer, language, last_updated, party_id, type, uid, valid, visual_number, whitelist)

    def to_dict(self) -> dict:
        result: dict = {}
        result["contract_id"] = from_str(self.contract_id)
        result["country_code"] = from_str(self.country_code)
        if self.default_profile_type is not None:
            result["default_profile_type"] = from_union([from_none, lambda x: to_enum(ProfileType, x)], self.default_profile_type)
        if self.energy_contract is not None:
            result["energy_contract"] = from_union([from_none, lambda x: to_class(EnergyContract, x)], self.energy_contract)
        if self.group_id is not None:
            result["group_id"] = from_union([from_none, from_str], self.group_id)
        result["issuer"] = from_str(self.issuer)
        if self.language is not None:
            result["language"] = from_union([from_none, from_str], self.language)
        result["last_updated"] = from_str(self.last_updated)
        result["party_id"] = from_str(self.party_id)
        result["type"] = to_enum(TokenType, self.type)
        result["uid"] = from_str(self.uid)
        result["valid"] = from_bool(self.valid)
        if self.visual_number is not None:
            result["visual_number"] = from_union([from_none, from_str], self.visual_number)
        result["whitelist"] = to_enum(WhitelistType, self.whitelist)
        return result


class AuthorizationInfo:
    allowed: AllowedType
    authorization_reference: Optional[str]
    info: Optional[DisplayText]
    location: Optional[LocationReferences]
    token: Token

    def __init__(self, allowed: AllowedType, authorization_reference: Optional[str], info: Optional[DisplayText], location: Optional[LocationReferences], token: Token) -> None:
        self.allowed = allowed
        self.authorization_reference = authorization_reference
        self.info = info
        self.location = location
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorizationInfo':
        assert isinstance(obj, dict)
        allowed = AllowedType(obj.get("allowed"))
        authorization_reference = from_union([from_none, from_str], obj.get("authorization_reference"))
        info = from_union([from_none, DisplayText.from_dict], obj.get("info"))
        location = from_union([from_none, LocationReferences.from_dict], obj.get("location"))
        token = Token.from_dict(obj.get("token"))
        return AuthorizationInfo(allowed, authorization_reference, info, location, token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["allowed"] = to_enum(AllowedType, self.allowed)
        if self.authorization_reference is not None:
            result["authorization_reference"] = from_union([from_none, from_str], self.authorization_reference)
        if self.info is not None:
            result["info"] = from_union([from_none, lambda x: to_class(DisplayText, x)], self.info)
        if self.location is not None:
            result["location"] = from_union([from_none, lambda x: to_class(LocationReferences, x)], self.location)
        result["token"] = to_class(Token, self.token)
        return result


class CancelReservation:
    reservation_id: str
    response_url: str

    def __init__(self, reservation_id: str, response_url: str) -> None:
        self.reservation_id = reservation_id
        self.response_url = response_url

    @staticmethod
    def from_dict(obj: Any) -> 'CancelReservation':
        assert isinstance(obj, dict)
        reservation_id = from_str(obj.get("reservation_id"))
        response_url = from_str(obj.get("response_url"))
        return CancelReservation(reservation_id, response_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["reservation_id"] = from_str(self.reservation_id)
        result["response_url"] = from_str(self.response_url)
        return result


class AuthMethod(Enum):
    AUTH_REQUEST = "AUTH_REQUEST"
    COMMAND = "COMMAND"
    WHITELIST = "WHITELIST"


class ConnectorFormat(Enum):
    CABLE = "CABLE"
    SOCKET = "SOCKET"


class PowerType(Enum):
    AC_1__PHASE = "AC_1_PHASE"
    AC_2__PHASE = "AC_2_PHASE"
    AC_2__PHASE_SPLIT = "AC_2_PHASE_SPLIT"
    AC_3__PHASE = "AC_3_PHASE"
    DC = "DC"


class ConnectorType(Enum):
    CHADEMO = "CHADEMO"
    CHAOJI = "CHAOJI"
    DOMESTIC_A = "DOMESTIC_A"
    DOMESTIC_B = "DOMESTIC_B"
    DOMESTIC_C = "DOMESTIC_C"
    DOMESTIC_D = "DOMESTIC_D"
    DOMESTIC_E = "DOMESTIC_E"
    DOMESTIC_F = "DOMESTIC_F"
    DOMESTIC_G = "DOMESTIC_G"
    DOMESTIC_H = "DOMESTIC_H"
    DOMESTIC_I = "DOMESTIC_I"
    DOMESTIC_J = "DOMESTIC_J"
    DOMESTIC_K = "DOMESTIC_K"
    DOMESTIC_L = "DOMESTIC_L"
    DOMESTIC_M = "DOMESTIC_M"
    DOMESTIC_N = "DOMESTIC_N"
    DOMESTIC_O = "DOMESTIC_O"
    GBT_AC = "GBT_AC"
    GBT_DC = "GBT_DC"
    IEC_60309_2__SINGLE_16 = "IEC_60309_2_single_16"
    IEC_60309_2__THREE_16 = "IEC_60309_2_three_16"
    IEC_60309_2__THREE_32 = "IEC_60309_2_three_32"
    IEC_60309_2__THREE_64 = "IEC_60309_2_three_64"
    IEC_62196__T1 = "IEC_62196_T1"
    IEC_62196__T1_COMBO = "IEC_62196_T1_COMBO"
    IEC_62196__T2 = "IEC_62196_T2"
    IEC_62196__T2_COMBO = "IEC_62196_T2_COMBO"
    IEC_62196__T3_A = "IEC_62196_T3A"
    IEC_62196__T3_C = "IEC_62196_T3C"
    NEMA_10_30 = "NEMA_10_30"
    NEMA_10_50 = "NEMA_10_50"
    NEMA_14_30 = "NEMA_14_30"
    NEMA_14_50 = "NEMA_14_50"
    NEMA_5_20 = "NEMA_5_20"
    NEMA_6_30 = "NEMA_6_30"
    NEMA_6_50 = "NEMA_6_50"
    PANTOGRAPH_BOTTOM_UP = "PANTOGRAPH_BOTTOM_UP"
    PANTOGRAPH_TOP_DOWN = "PANTOGRAPH_TOP_DOWN"
    TESLA_R = "TESLA_R"
    TESLA_S = "TESLA_S"


class GeoLocation:
    latitude: str
    longitude: str

    def __init__(self, latitude: str, longitude: str) -> None:
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def from_dict(obj: Any) -> 'GeoLocation':
        assert isinstance(obj, dict)
        latitude = from_str(obj.get("latitude"))
        longitude = from_str(obj.get("longitude"))
        return GeoLocation(latitude, longitude)

    def to_dict(self) -> dict:
        result: dict = {}
        result["latitude"] = from_str(self.latitude)
        result["longitude"] = from_str(self.longitude)
        return result


class CdrLocation:
    address: str
    city: str
    connector_format: ConnectorFormat
    connector_id: str
    connector_power_type: PowerType
    connector_standard: ConnectorType
    coordinates: GeoLocation
    country: str
    evse_id: str
    evse_uid: str
    id: str
    name: Optional[str]
    postal_code: Optional[str]
    state: Optional[str]

    def __init__(self, address: str, city: str, connector_format: ConnectorFormat, connector_id: str, connector_power_type: PowerType, connector_standard: ConnectorType, coordinates: GeoLocation, country: str, evse_id: str, evse_uid: str, id: str, name: Optional[str], postal_code: Optional[str], state: Optional[str]) -> None:
        self.address = address
        self.city = city
        self.connector_format = connector_format
        self.connector_id = connector_id
        self.connector_power_type = connector_power_type
        self.connector_standard = connector_standard
        self.coordinates = coordinates
        self.country = country
        self.evse_id = evse_id
        self.evse_uid = evse_uid
        self.id = id
        self.name = name
        self.postal_code = postal_code
        self.state = state

    @staticmethod
    def from_dict(obj: Any) -> 'CdrLocation':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        city = from_str(obj.get("city"))
        connector_format = ConnectorFormat(obj.get("connector_format"))
        connector_id = from_str(obj.get("connector_id"))
        connector_power_type = PowerType(obj.get("connector_power_type"))
        connector_standard = ConnectorType(obj.get("connector_standard"))
        coordinates = GeoLocation.from_dict(obj.get("coordinates"))
        country = from_str(obj.get("country"))
        evse_id = from_str(obj.get("evse_id"))
        evse_uid = from_str(obj.get("evse_uid"))
        id = from_str(obj.get("id"))
        name = from_union([from_none, from_str], obj.get("name"))
        postal_code = from_union([from_none, from_str], obj.get("postal_code"))
        state = from_union([from_none, from_str], obj.get("state"))
        return CdrLocation(address, city, connector_format, connector_id, connector_power_type, connector_standard, coordinates, country, evse_id, evse_uid, id, name, postal_code, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["city"] = from_str(self.city)
        result["connector_format"] = to_enum(ConnectorFormat, self.connector_format)
        result["connector_id"] = from_str(self.connector_id)
        result["connector_power_type"] = to_enum(PowerType, self.connector_power_type)
        result["connector_standard"] = to_enum(ConnectorType, self.connector_standard)
        result["coordinates"] = to_class(GeoLocation, self.coordinates)
        result["country"] = from_str(self.country)
        result["evse_id"] = from_str(self.evse_id)
        result["evse_uid"] = from_str(self.evse_uid)
        result["id"] = from_str(self.id)
        if self.name is not None:
            result["name"] = from_union([from_none, from_str], self.name)
        if self.postal_code is not None:
            result["postal_code"] = from_union([from_none, from_str], self.postal_code)
        if self.state is not None:
            result["state"] = from_union([from_none, from_str], self.state)
        return result


class CdrToken:
    contract_id: str
    country_code: str
    party_id: str
    type: TokenType
    uid: str

    def __init__(self, contract_id: str, country_code: str, party_id: str, type: TokenType, uid: str) -> None:
        self.contract_id = contract_id
        self.country_code = country_code
        self.party_id = party_id
        self.type = type
        self.uid = uid

    @staticmethod
    def from_dict(obj: Any) -> 'CdrToken':
        assert isinstance(obj, dict)
        contract_id = from_str(obj.get("contract_id"))
        country_code = from_str(obj.get("country_code"))
        party_id = from_str(obj.get("party_id"))
        type = TokenType(obj.get("type"))
        uid = from_str(obj.get("uid"))
        return CdrToken(contract_id, country_code, party_id, type, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["contract_id"] = from_str(self.contract_id)
        result["country_code"] = from_str(self.country_code)
        result["party_id"] = from_str(self.party_id)
        result["type"] = to_enum(TokenType, self.type)
        result["uid"] = from_str(self.uid)
        return result


class CdrDimensionType(Enum):
    CURRENT = "CURRENT"
    ENERGY = "ENERGY"
    ENERGY_EXPORT = "ENERGY_EXPORT"
    ENERGY_IMPORT = "ENERGY_IMPORT"
    MAX_CURRENT = "MAX_CURRENT"
    MAX_POWER = "MAX_POWER"
    MIN_CURRENT = "MIN_CURRENT"
    MIN_POWER = "MIN_POWER"
    PARKING_TIME = "PARKING_TIME"
    POWER = "POWER"
    RESERVATION_TIME = "RESERVATION_TIME"
    STATE_OF_CHARGE = "STATE_OF_CHARGE"
    TIME = "TIME"


class CdrDimension:
    type: CdrDimensionType
    volume: float

    def __init__(self, type: CdrDimensionType, volume: float) -> None:
        self.type = type
        self.volume = volume

    @staticmethod
    def from_dict(obj: Any) -> 'CdrDimension':
        assert isinstance(obj, dict)
        type = CdrDimensionType(obj.get("type"))
        volume = from_float(obj.get("volume"))
        return CdrDimension(type, volume)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(CdrDimensionType, self.type)
        result["volume"] = to_float(self.volume)
        return result


class ChargingPeriod:
    dimensions: List[CdrDimension]
    start_date_time: str
    tariff_id: Optional[str]

    def __init__(self, dimensions: List[CdrDimension], start_date_time: str, tariff_id: Optional[str]) -> None:
        self.dimensions = dimensions
        self.start_date_time = start_date_time
        self.tariff_id = tariff_id

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingPeriod':
        assert isinstance(obj, dict)
        dimensions = from_list(CdrDimension.from_dict, obj.get("dimensions"))
        start_date_time = from_str(obj.get("start_date_time"))
        tariff_id = from_union([from_none, from_str], obj.get("tariff_id"))
        return ChargingPeriod(dimensions, start_date_time, tariff_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dimensions"] = from_list(lambda x: to_class(CdrDimension, x), self.dimensions)
        result["start_date_time"] = from_str(self.start_date_time)
        if self.tariff_id is not None:
            result["tariff_id"] = from_union([from_none, from_str], self.tariff_id)
        return result


class SignedValue:
    nature: str
    plain_data: str
    signed_data: str

    def __init__(self, nature: str, plain_data: str, signed_data: str) -> None:
        self.nature = nature
        self.plain_data = plain_data
        self.signed_data = signed_data

    @staticmethod
    def from_dict(obj: Any) -> 'SignedValue':
        assert isinstance(obj, dict)
        nature = from_str(obj.get("nature"))
        plain_data = from_str(obj.get("plain_data"))
        signed_data = from_str(obj.get("signed_data"))
        return SignedValue(nature, plain_data, signed_data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nature"] = from_str(self.nature)
        result["plain_data"] = from_str(self.plain_data)
        result["signed_data"] = from_str(self.signed_data)
        return result


class SignedData:
    encoding_method: str
    encoding_method_version: Optional[int]
    public_key: Optional[str]
    signed_values: List[SignedValue]
    url: Optional[str]

    def __init__(self, encoding_method: str, encoding_method_version: Optional[int], public_key: Optional[str], signed_values: List[SignedValue], url: Optional[str]) -> None:
        self.encoding_method = encoding_method
        self.encoding_method_version = encoding_method_version
        self.public_key = public_key
        self.signed_values = signed_values
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'SignedData':
        assert isinstance(obj, dict)
        encoding_method = from_str(obj.get("encoding_method"))
        encoding_method_version = from_union([from_none, from_int], obj.get("encoding_method_version"))
        public_key = from_union([from_none, from_str], obj.get("public_key"))
        signed_values = from_list(SignedValue.from_dict, obj.get("signed_values"))
        url = from_union([from_none, from_str], obj.get("url"))
        return SignedData(encoding_method, encoding_method_version, public_key, signed_values, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["encoding_method"] = from_str(self.encoding_method)
        if self.encoding_method_version is not None:
            result["encoding_method_version"] = from_union([from_none, from_int], self.encoding_method_version)
        if self.public_key is not None:
            result["public_key"] = from_union([from_none, from_str], self.public_key)
        result["signed_values"] = from_list(lambda x: to_class(SignedValue, x), self.signed_values)
        if self.url is not None:
            result["url"] = from_union([from_none, from_str], self.url)
        return result


class TariffDimensionType(Enum):
    ENERGY = "ENERGY"
    FLAT = "FLAT"
    PARKING_TIME = "PARKING_TIME"
    TIME = "TIME"


class PriceComponent:
    price: float
    step_size: int
    type: TariffDimensionType
    vat: Optional[float]

    def __init__(self, price: float, step_size: int, type: TariffDimensionType, vat: Optional[float]) -> None:
        self.price = price
        self.step_size = step_size
        self.type = type
        self.vat = vat

    @staticmethod
    def from_dict(obj: Any) -> 'PriceComponent':
        assert isinstance(obj, dict)
        price = from_float(obj.get("price"))
        step_size = from_int(obj.get("step_size"))
        type = TariffDimensionType(obj.get("type"))
        vat = from_union([from_none, from_float], obj.get("vat"))
        return PriceComponent(price, step_size, type, vat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["price"] = to_float(self.price)
        result["step_size"] = from_int(self.step_size)
        result["type"] = to_enum(TariffDimensionType, self.type)
        if self.vat is not None:
            result["vat"] = from_union([from_none, to_float], self.vat)
        return result


class DayOfWeek(Enum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class ReservationRestrictionType(Enum):
    RESERVATION = "RESERVATION"
    RESERVATION_EXPIRES = "RESERVATION_EXPIRES"


class TariffRestrictions:
    day_of_week: Optional[List[DayOfWeek]]
    end_date: Optional[str]
    end_time: Optional[str]
    max_current: Optional[float]
    max_duration: Optional[int]
    max_kwh: Optional[float]
    max_power: Optional[float]
    min_current: Optional[float]
    min_duration: Optional[int]
    min_kwh: Optional[float]
    min_power: Optional[float]
    reservation: Optional[ReservationRestrictionType]
    start_date: Optional[str]
    start_time: Optional[str]

    def __init__(self, day_of_week: Optional[List[DayOfWeek]], end_date: Optional[str], end_time: Optional[str], max_current: Optional[float], max_duration: Optional[int], max_kwh: Optional[float], max_power: Optional[float], min_current: Optional[float], min_duration: Optional[int], min_kwh: Optional[float], min_power: Optional[float], reservation: Optional[ReservationRestrictionType], start_date: Optional[str], start_time: Optional[str]) -> None:
        self.day_of_week = day_of_week
        self.end_date = end_date
        self.end_time = end_time
        self.max_current = max_current
        self.max_duration = max_duration
        self.max_kwh = max_kwh
        self.max_power = max_power
        self.min_current = min_current
        self.min_duration = min_duration
        self.min_kwh = min_kwh
        self.min_power = min_power
        self.reservation = reservation
        self.start_date = start_date
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'TariffRestrictions':
        assert isinstance(obj, dict)
        day_of_week = from_union([from_none, lambda x: from_list(DayOfWeek, x)], obj.get("day_of_week"))
        end_date = from_union([from_none, from_str], obj.get("end_date"))
        end_time = from_union([from_none, from_str], obj.get("end_time"))
        max_current = from_union([from_none, from_float], obj.get("max_current"))
        max_duration = from_union([from_none, from_int], obj.get("max_duration"))
        max_kwh = from_union([from_none, from_float], obj.get("max_kwh"))
        max_power = from_union([from_none, from_float], obj.get("max_power"))
        min_current = from_union([from_none, from_float], obj.get("min_current"))
        min_duration = from_union([from_none, from_int], obj.get("min_duration"))
        min_kwh = from_union([from_none, from_float], obj.get("min_kwh"))
        min_power = from_union([from_none, from_float], obj.get("min_power"))
        reservation = from_union([from_none, ReservationRestrictionType], obj.get("reservation"))
        start_date = from_union([from_none, from_str], obj.get("start_date"))
        start_time = from_union([from_none, from_str], obj.get("start_time"))
        return TariffRestrictions(day_of_week, end_date, end_time, max_current, max_duration, max_kwh, max_power, min_current, min_duration, min_kwh, min_power, reservation, start_date, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.day_of_week is not None:
            result["day_of_week"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(DayOfWeek, x), x)], self.day_of_week)
        if self.end_date is not None:
            result["end_date"] = from_union([from_none, from_str], self.end_date)
        if self.end_time is not None:
            result["end_time"] = from_union([from_none, from_str], self.end_time)
        if self.max_current is not None:
            result["max_current"] = from_union([from_none, to_float], self.max_current)
        if self.max_duration is not None:
            result["max_duration"] = from_union([from_none, from_int], self.max_duration)
        if self.max_kwh is not None:
            result["max_kwh"] = from_union([from_none, to_float], self.max_kwh)
        if self.max_power is not None:
            result["max_power"] = from_union([from_none, to_float], self.max_power)
        if self.min_current is not None:
            result["min_current"] = from_union([from_none, to_float], self.min_current)
        if self.min_duration is not None:
            result["min_duration"] = from_union([from_none, from_int], self.min_duration)
        if self.min_kwh is not None:
            result["min_kwh"] = from_union([from_none, to_float], self.min_kwh)
        if self.min_power is not None:
            result["min_power"] = from_union([from_none, to_float], self.min_power)
        if self.reservation is not None:
            result["reservation"] = from_union([from_none, lambda x: to_enum(ReservationRestrictionType, x)], self.reservation)
        if self.start_date is not None:
            result["start_date"] = from_union([from_none, from_str], self.start_date)
        if self.start_time is not None:
            result["start_time"] = from_union([from_none, from_str], self.start_time)
        return result


class TariffElement:
    price_components: List[PriceComponent]
    restrictions: Optional[TariffRestrictions]

    def __init__(self, price_components: List[PriceComponent], restrictions: Optional[TariffRestrictions]) -> None:
        self.price_components = price_components
        self.restrictions = restrictions

    @staticmethod
    def from_dict(obj: Any) -> 'TariffElement':
        assert isinstance(obj, dict)
        price_components = from_list(PriceComponent.from_dict, obj.get("price_components"))
        restrictions = from_union([from_none, TariffRestrictions.from_dict], obj.get("restrictions"))
        return TariffElement(price_components, restrictions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["price_components"] = from_list(lambda x: to_class(PriceComponent, x), self.price_components)
        if self.restrictions is not None:
            result["restrictions"] = from_union([from_none, lambda x: to_class(TariffRestrictions, x)], self.restrictions)
        return result


class EnergySourceCategory(Enum):
    COAL = "COAL"
    GAS = "GAS"
    GENERAL_FOSSIL = "GENERAL_FOSSIL"
    GENERAL_GREEN = "GENERAL_GREEN"
    NUCLEAR = "NUCLEAR"
    SOLAR = "SOLAR"
    WATER = "WATER"
    WIND = "WIND"


class EnergySource:
    percentage: float
    source: EnergySourceCategory

    def __init__(self, percentage: float, source: EnergySourceCategory) -> None:
        self.percentage = percentage
        self.source = source

    @staticmethod
    def from_dict(obj: Any) -> 'EnergySource':
        assert isinstance(obj, dict)
        percentage = from_float(obj.get("percentage"))
        source = EnergySourceCategory(obj.get("source"))
        return EnergySource(percentage, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["percentage"] = to_float(self.percentage)
        result["source"] = to_enum(EnergySourceCategory, self.source)
        return result


class EnvironmentalImpactCategory(Enum):
    CARBON_DIOXIDE = "CARBON_DIOXIDE"
    NUCLEAR_WASTE = "NUCLEAR_WASTE"


class EnvironmentalImpact:
    amount: float
    category: EnvironmentalImpactCategory

    def __init__(self, amount: float, category: EnvironmentalImpactCategory) -> None:
        self.amount = amount
        self.category = category

    @staticmethod
    def from_dict(obj: Any) -> 'EnvironmentalImpact':
        assert isinstance(obj, dict)
        amount = from_float(obj.get("amount"))
        category = EnvironmentalImpactCategory(obj.get("category"))
        return EnvironmentalImpact(amount, category)

    def to_dict(self) -> dict:
        result: dict = {}
        result["amount"] = to_float(self.amount)
        result["category"] = to_enum(EnvironmentalImpactCategory, self.category)
        return result


class EnergyMix:
    energy_product_name: Optional[str]
    energy_sources: Optional[List[EnergySource]]
    environ_impact: Optional[List[EnvironmentalImpact]]
    is_green_energy: bool
    supplier_name: Optional[str]

    def __init__(self, energy_product_name: Optional[str], energy_sources: Optional[List[EnergySource]], environ_impact: Optional[List[EnvironmentalImpact]], is_green_energy: bool, supplier_name: Optional[str]) -> None:
        self.energy_product_name = energy_product_name
        self.energy_sources = energy_sources
        self.environ_impact = environ_impact
        self.is_green_energy = is_green_energy
        self.supplier_name = supplier_name

    @staticmethod
    def from_dict(obj: Any) -> 'EnergyMix':
        assert isinstance(obj, dict)
        energy_product_name = from_union([from_none, from_str], obj.get("energy_product_name"))
        energy_sources = from_union([from_none, lambda x: from_list(EnergySource.from_dict, x)], obj.get("energy_sources"))
        environ_impact = from_union([from_none, lambda x: from_list(EnvironmentalImpact.from_dict, x)], obj.get("environ_impact"))
        is_green_energy = from_bool(obj.get("is_green_energy"))
        supplier_name = from_union([from_none, from_str], obj.get("supplier_name"))
        return EnergyMix(energy_product_name, energy_sources, environ_impact, is_green_energy, supplier_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.energy_product_name is not None:
            result["energy_product_name"] = from_union([from_none, from_str], self.energy_product_name)
        if self.energy_sources is not None:
            result["energy_sources"] = from_union([from_none, lambda x: from_list(lambda x: to_class(EnergySource, x), x)], self.energy_sources)
        if self.environ_impact is not None:
            result["environ_impact"] = from_union([from_none, lambda x: from_list(lambda x: to_class(EnvironmentalImpact, x), x)], self.environ_impact)
        result["is_green_energy"] = from_bool(self.is_green_energy)
        if self.supplier_name is not None:
            result["supplier_name"] = from_union([from_none, from_str], self.supplier_name)
        return result


class Price:
    excl_vat: float
    incl_vat: Optional[float]

    def __init__(self, excl_vat: float, incl_vat: Optional[float]) -> None:
        self.excl_vat = excl_vat
        self.incl_vat = incl_vat

    @staticmethod
    def from_dict(obj: Any) -> 'Price':
        assert isinstance(obj, dict)
        excl_vat = from_float(obj.get("excl_vat"))
        incl_vat = from_union([from_none, from_float], obj.get("incl_vat"))
        return Price(excl_vat, incl_vat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["excl_vat"] = to_float(self.excl_vat)
        if self.incl_vat is not None:
            result["incl_vat"] = from_union([from_none, to_float], self.incl_vat)
        return result


class TariffType(Enum):
    AD_HOC_PAYMENT = "AD_HOC_PAYMENT"
    PROFILE_CHEAP = "PROFILE_CHEAP"
    PROFILE_FAST = "PROFILE_FAST"
    PROFILE_GREEN = "PROFILE_GREEN"
    REGULAR = "REGULAR"


class Tariff:
    country_code: str
    currency: str
    elements: List[TariffElement]
    end_date_time: Optional[str]
    energy_mix: Optional[EnergyMix]
    id: str
    last_updated: str
    max_price: Optional[Price]
    min_price: Optional[Price]
    party_id: str
    start_date_time: Optional[str]
    tariff_alt_text: Optional[List[DisplayText]]
    tariff_alt_url: Optional[str]
    type: Optional[TariffType]

    def __init__(self, country_code: str, currency: str, elements: List[TariffElement], end_date_time: Optional[str], energy_mix: Optional[EnergyMix], id: str, last_updated: str, max_price: Optional[Price], min_price: Optional[Price], party_id: str, start_date_time: Optional[str], tariff_alt_text: Optional[List[DisplayText]], tariff_alt_url: Optional[str], type: Optional[TariffType]) -> None:
        self.country_code = country_code
        self.currency = currency
        self.elements = elements
        self.end_date_time = end_date_time
        self.energy_mix = energy_mix
        self.id = id
        self.last_updated = last_updated
        self.max_price = max_price
        self.min_price = min_price
        self.party_id = party_id
        self.start_date_time = start_date_time
        self.tariff_alt_text = tariff_alt_text
        self.tariff_alt_url = tariff_alt_url
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Tariff':
        assert isinstance(obj, dict)
        country_code = from_str(obj.get("country_code"))
        currency = from_str(obj.get("currency"))
        elements = from_list(TariffElement.from_dict, obj.get("elements"))
        end_date_time = from_union([from_none, from_str], obj.get("end_date_time"))
        energy_mix = from_union([from_none, EnergyMix.from_dict], obj.get("energy_mix"))
        id = from_str(obj.get("id"))
        last_updated = from_str(obj.get("last_updated"))
        max_price = from_union([from_none, Price.from_dict], obj.get("max_price"))
        min_price = from_union([from_none, Price.from_dict], obj.get("min_price"))
        party_id = from_str(obj.get("party_id"))
        start_date_time = from_union([from_none, from_str], obj.get("start_date_time"))
        tariff_alt_text = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("tariff_alt_text"))
        tariff_alt_url = from_union([from_none, from_str], obj.get("tariff_alt_url"))
        type = from_union([from_none, TariffType], obj.get("type"))
        return Tariff(country_code, currency, elements, end_date_time, energy_mix, id, last_updated, max_price, min_price, party_id, start_date_time, tariff_alt_text, tariff_alt_url, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["country_code"] = from_str(self.country_code)
        result["currency"] = from_str(self.currency)
        result["elements"] = from_list(lambda x: to_class(TariffElement, x), self.elements)
        if self.end_date_time is not None:
            result["end_date_time"] = from_union([from_none, from_str], self.end_date_time)
        if self.energy_mix is not None:
            result["energy_mix"] = from_union([from_none, lambda x: to_class(EnergyMix, x)], self.energy_mix)
        result["id"] = from_str(self.id)
        result["last_updated"] = from_str(self.last_updated)
        if self.max_price is not None:
            result["max_price"] = from_union([from_none, lambda x: to_class(Price, x)], self.max_price)
        if self.min_price is not None:
            result["min_price"] = from_union([from_none, lambda x: to_class(Price, x)], self.min_price)
        result["party_id"] = from_str(self.party_id)
        if self.start_date_time is not None:
            result["start_date_time"] = from_union([from_none, from_str], self.start_date_time)
        if self.tariff_alt_text is not None:
            result["tariff_alt_text"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.tariff_alt_text)
        if self.tariff_alt_url is not None:
            result["tariff_alt_url"] = from_union([from_none, from_str], self.tariff_alt_url)
        if self.type is not None:
            result["type"] = from_union([from_none, lambda x: to_enum(TariffType, x)], self.type)
        return result


class Cdr:
    auth_method: AuthMethod
    authorization_reference: Optional[str]
    cdr_location: CdrLocation
    cdr_token: CdrToken
    charging_periods: List[ChargingPeriod]
    country_code: str
    credit: Optional[bool]
    credit_reference_id: Optional[str]
    currency: str
    end_date_time: str
    home_charging_compensation: Optional[bool]
    id: str
    invoice_reference_id: Optional[str]
    last_updated: str
    meter_id: Optional[str]
    party_id: str
    remark: Optional[str]
    session_id: Optional[str]
    signed_data: Optional[SignedData]
    start_date_time: str
    tariffs: Optional[List[Tariff]]
    total_cost: Price
    total_energy: float
    total_energy_cost: Optional[Price]
    total_fixed_cost: Optional[Price]
    total_parking_cost: Optional[Price]
    total_parking_time: Optional[float]
    total_reservation_cost: Optional[Price]
    total_time: float
    total_time_cost: Optional[Price]

    def __init__(self, auth_method: AuthMethod, authorization_reference: Optional[str], cdr_location: CdrLocation, cdr_token: CdrToken, charging_periods: List[ChargingPeriod], country_code: str, credit: Optional[bool], credit_reference_id: Optional[str], currency: str, end_date_time: str, home_charging_compensation: Optional[bool], id: str, invoice_reference_id: Optional[str], last_updated: str, meter_id: Optional[str], party_id: str, remark: Optional[str], session_id: Optional[str], signed_data: Optional[SignedData], start_date_time: str, tariffs: Optional[List[Tariff]], total_cost: Price, total_energy: float, total_energy_cost: Optional[Price], total_fixed_cost: Optional[Price], total_parking_cost: Optional[Price], total_parking_time: Optional[float], total_reservation_cost: Optional[Price], total_time: float, total_time_cost: Optional[Price]) -> None:
        self.auth_method = auth_method
        self.authorization_reference = authorization_reference
        self.cdr_location = cdr_location
        self.cdr_token = cdr_token
        self.charging_periods = charging_periods
        self.country_code = country_code
        self.credit = credit
        self.credit_reference_id = credit_reference_id
        self.currency = currency
        self.end_date_time = end_date_time
        self.home_charging_compensation = home_charging_compensation
        self.id = id
        self.invoice_reference_id = invoice_reference_id
        self.last_updated = last_updated
        self.meter_id = meter_id
        self.party_id = party_id
        self.remark = remark
        self.session_id = session_id
        self.signed_data = signed_data
        self.start_date_time = start_date_time
        self.tariffs = tariffs
        self.total_cost = total_cost
        self.total_energy = total_energy
        self.total_energy_cost = total_energy_cost
        self.total_fixed_cost = total_fixed_cost
        self.total_parking_cost = total_parking_cost
        self.total_parking_time = total_parking_time
        self.total_reservation_cost = total_reservation_cost
        self.total_time = total_time
        self.total_time_cost = total_time_cost

    @staticmethod
    def from_dict(obj: Any) -> 'Cdr':
        assert isinstance(obj, dict)
        auth_method = AuthMethod(obj.get("auth_method"))
        authorization_reference = from_union([from_none, from_str], obj.get("authorization_reference"))
        cdr_location = CdrLocation.from_dict(obj.get("cdr_location"))
        cdr_token = CdrToken.from_dict(obj.get("cdr_token"))
        charging_periods = from_list(ChargingPeriod.from_dict, obj.get("charging_periods"))
        country_code = from_str(obj.get("country_code"))
        credit = from_union([from_none, from_bool], obj.get("credit"))
        credit_reference_id = from_union([from_none, from_str], obj.get("credit_reference_id"))
        currency = from_str(obj.get("currency"))
        end_date_time = from_str(obj.get("end_date_time"))
        home_charging_compensation = from_union([from_none, from_bool], obj.get("home_charging_compensation"))
        id = from_str(obj.get("id"))
        invoice_reference_id = from_union([from_none, from_str], obj.get("invoice_reference_id"))
        last_updated = from_str(obj.get("last_updated"))
        meter_id = from_union([from_none, from_str], obj.get("meter_id"))
        party_id = from_str(obj.get("party_id"))
        remark = from_union([from_none, from_str], obj.get("remark"))
        session_id = from_union([from_none, from_str], obj.get("session_id"))
        signed_data = from_union([from_none, SignedData.from_dict], obj.get("signed_data"))
        start_date_time = from_str(obj.get("start_date_time"))
        tariffs = from_union([from_none, lambda x: from_list(Tariff.from_dict, x)], obj.get("tariffs"))
        total_cost = Price.from_dict(obj.get("total_cost"))
        total_energy = from_float(obj.get("total_energy"))
        total_energy_cost = from_union([from_none, Price.from_dict], obj.get("total_energy_cost"))
        total_fixed_cost = from_union([from_none, Price.from_dict], obj.get("total_fixed_cost"))
        total_parking_cost = from_union([from_none, Price.from_dict], obj.get("total_parking_cost"))
        total_parking_time = from_union([from_none, from_float], obj.get("total_parking_time"))
        total_reservation_cost = from_union([from_none, Price.from_dict], obj.get("total_reservation_cost"))
        total_time = from_float(obj.get("total_time"))
        total_time_cost = from_union([from_none, Price.from_dict], obj.get("total_time_cost"))
        return Cdr(auth_method, authorization_reference, cdr_location, cdr_token, charging_periods, country_code, credit, credit_reference_id, currency, end_date_time, home_charging_compensation, id, invoice_reference_id, last_updated, meter_id, party_id, remark, session_id, signed_data, start_date_time, tariffs, total_cost, total_energy, total_energy_cost, total_fixed_cost, total_parking_cost, total_parking_time, total_reservation_cost, total_time, total_time_cost)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth_method"] = to_enum(AuthMethod, self.auth_method)
        if self.authorization_reference is not None:
            result["authorization_reference"] = from_union([from_none, from_str], self.authorization_reference)
        result["cdr_location"] = to_class(CdrLocation, self.cdr_location)
        result["cdr_token"] = to_class(CdrToken, self.cdr_token)
        result["charging_periods"] = from_list(lambda x: to_class(ChargingPeriod, x), self.charging_periods)
        result["country_code"] = from_str(self.country_code)
        if self.credit is not None:
            result["credit"] = from_union([from_none, from_bool], self.credit)
        if self.credit_reference_id is not None:
            result["credit_reference_id"] = from_union([from_none, from_str], self.credit_reference_id)
        result["currency"] = from_str(self.currency)
        result["end_date_time"] = from_str(self.end_date_time)
        if self.home_charging_compensation is not None:
            result["home_charging_compensation"] = from_union([from_none, from_bool], self.home_charging_compensation)
        result["id"] = from_str(self.id)
        if self.invoice_reference_id is not None:
            result["invoice_reference_id"] = from_union([from_none, from_str], self.invoice_reference_id)
        result["last_updated"] = from_str(self.last_updated)
        if self.meter_id is not None:
            result["meter_id"] = from_union([from_none, from_str], self.meter_id)
        result["party_id"] = from_str(self.party_id)
        if self.remark is not None:
            result["remark"] = from_union([from_none, from_str], self.remark)
        if self.session_id is not None:
            result["session_id"] = from_union([from_none, from_str], self.session_id)
        if self.signed_data is not None:
            result["signed_data"] = from_union([from_none, lambda x: to_class(SignedData, x)], self.signed_data)
        result["start_date_time"] = from_str(self.start_date_time)
        if self.tariffs is not None:
            result["tariffs"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Tariff, x), x)], self.tariffs)
        result["total_cost"] = to_class(Price, self.total_cost)
        result["total_energy"] = to_float(self.total_energy)
        if self.total_energy_cost is not None:
            result["total_energy_cost"] = from_union([from_none, lambda x: to_class(Price, x)], self.total_energy_cost)
        if self.total_fixed_cost is not None:
            result["total_fixed_cost"] = from_union([from_none, lambda x: to_class(Price, x)], self.total_fixed_cost)
        if self.total_parking_cost is not None:
            result["total_parking_cost"] = from_union([from_none, lambda x: to_class(Price, x)], self.total_parking_cost)
        if self.total_parking_time is not None:
            result["total_parking_time"] = from_union([from_none, to_float], self.total_parking_time)
        if self.total_reservation_cost is not None:
            result["total_reservation_cost"] = from_union([from_none, lambda x: to_class(Price, x)], self.total_reservation_cost)
        result["total_time"] = to_float(self.total_time)
        if self.total_time_cost is not None:
            result["total_time_cost"] = from_union([from_none, lambda x: to_class(Price, x)], self.total_time_cost)
        return result


class ChargingPreferences:
    departure_time: Optional[str]
    discharge_allowed: Optional[bool]
    energy_need: Optional[float]
    profile_type: ProfileType

    def __init__(self, departure_time: Optional[str], discharge_allowed: Optional[bool], energy_need: Optional[float], profile_type: ProfileType) -> None:
        self.departure_time = departure_time
        self.discharge_allowed = discharge_allowed
        self.energy_need = energy_need
        self.profile_type = profile_type

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingPreferences':
        assert isinstance(obj, dict)
        departure_time = from_union([from_none, from_str], obj.get("departure_time"))
        discharge_allowed = from_union([from_none, from_bool], obj.get("discharge_allowed"))
        energy_need = from_union([from_none, from_float], obj.get("energy_need"))
        profile_type = ProfileType(obj.get("profile_type"))
        return ChargingPreferences(departure_time, discharge_allowed, energy_need, profile_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.departure_time is not None:
            result["departure_time"] = from_union([from_none, from_str], self.departure_time)
        if self.discharge_allowed is not None:
            result["discharge_allowed"] = from_union([from_none, from_bool], self.discharge_allowed)
        if self.energy_need is not None:
            result["energy_need"] = from_union([from_none, to_float], self.energy_need)
        result["profile_type"] = to_enum(ProfileType, self.profile_type)
        return result


class ChargingProfileResponseType(Enum):
    ACCEPTED = "ACCEPTED"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    REJECTED = "REJECTED"
    TOO_OFTEN = "TOO_OFTEN"
    UNKNOWN_SESSION = "UNKNOWN_SESSION"


class ChargingProfileResponse:
    result: ChargingProfileResponseType
    timeout: int

    def __init__(self, result: ChargingProfileResponseType, timeout: int) -> None:
        self.result = result
        self.timeout = timeout

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingProfileResponse':
        assert isinstance(obj, dict)
        result = ChargingProfileResponseType(obj.get("result"))
        timeout = from_int(obj.get("timeout"))
        return ChargingProfileResponse(result, timeout)

    def to_dict(self) -> dict:
        result: dict = {}
        result["result"] = to_enum(ChargingProfileResponseType, self.result)
        result["timeout"] = from_int(self.timeout)
        return result


class ChargingProfileResult:
    result: ChargingProfileResultType

    def __init__(self, result: ChargingProfileResultType) -> None:
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'ChargingProfileResult':
        assert isinstance(obj, dict)
        result = ChargingProfileResultType(obj.get("result"))
        return ChargingProfileResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["result"] = to_enum(ChargingProfileResultType, self.result)
        return result


class ClearProfileResult:
    result: ChargingProfileResultType

    def __init__(self, result: ChargingProfileResultType) -> None:
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'ClearProfileResult':
        assert isinstance(obj, dict)
        result = ChargingProfileResultType(obj.get("result"))
        return ClearProfileResult(result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["result"] = to_enum(ChargingProfileResultType, self.result)
        return result


class CommandResponseType(Enum):
    ACCEPTED = "ACCEPTED"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    REJECTED = "REJECTED"
    UNKNOWN_SESSION = "UNKNOWN_SESSION"


class CommandResponse:
    message: Optional[List[DisplayText]]
    result: CommandResponseType
    timeout: int

    def __init__(self, message: Optional[List[DisplayText]], result: CommandResponseType, timeout: int) -> None:
        self.message = message
        self.result = result
        self.timeout = timeout

    @staticmethod
    def from_dict(obj: Any) -> 'CommandResponse':
        assert isinstance(obj, dict)
        message = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("message"))
        result = CommandResponseType(obj.get("result"))
        timeout = from_int(obj.get("timeout"))
        return CommandResponse(message, result, timeout)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.message is not None:
            result["message"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.message)
        result["result"] = to_enum(CommandResponseType, self.result)
        result["timeout"] = from_int(self.timeout)
        return result


class CommandResultType(Enum):
    ACCEPTED = "ACCEPTED"
    CANCELED_RESERVATION = "CANCELED_RESERVATION"
    EVSE_INOPERATIVE = "EVSE_INOPERATIVE"
    EVSE_OCCUPIED = "EVSE_OCCUPIED"
    FAILED = "FAILED"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    REJECTED = "REJECTED"
    TIMEOUT = "TIMEOUT"
    UNKNOWN_RESERVATION = "UNKNOWN_RESERVATION"


class CommandResult:
    message: Optional[List[DisplayText]]
    result: CommandResultType

    def __init__(self, message: Optional[List[DisplayText]], result: CommandResultType) -> None:
        self.message = message
        self.result = result

    @staticmethod
    def from_dict(obj: Any) -> 'CommandResult':
        assert isinstance(obj, dict)
        message = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("message"))
        result = CommandResultType(obj.get("result"))
        return CommandResult(message, result)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.message is not None:
            result["message"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.message)
        result["result"] = to_enum(CommandResultType, self.result)
        return result


class Connector:
    format: ConnectorFormat
    id: str
    last_updated: str
    max_amperage: int
    max_electric_power: Optional[int]
    max_voltage: int
    power_type: PowerType
    standard: ConnectorType
    tariff_ids: Optional[List[str]]
    terms_and_conditions: Optional[str]

    def __init__(self, format: ConnectorFormat, id: str, last_updated: str, max_amperage: int, max_electric_power: Optional[int], max_voltage: int, power_type: PowerType, standard: ConnectorType, tariff_ids: Optional[List[str]], terms_and_conditions: Optional[str]) -> None:
        self.format = format
        self.id = id
        self.last_updated = last_updated
        self.max_amperage = max_amperage
        self.max_electric_power = max_electric_power
        self.max_voltage = max_voltage
        self.power_type = power_type
        self.standard = standard
        self.tariff_ids = tariff_ids
        self.terms_and_conditions = terms_and_conditions

    @staticmethod
    def from_dict(obj: Any) -> 'Connector':
        assert isinstance(obj, dict)
        format = ConnectorFormat(obj.get("format"))
        id = from_str(obj.get("id"))
        last_updated = from_str(obj.get("last_updated"))
        max_amperage = from_int(obj.get("max_amperage"))
        max_electric_power = from_union([from_none, from_int], obj.get("max_electric_power"))
        max_voltage = from_int(obj.get("max_voltage"))
        power_type = PowerType(obj.get("power_type"))
        standard = ConnectorType(obj.get("standard"))
        tariff_ids = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("tariff_ids"))
        terms_and_conditions = from_union([from_none, from_str], obj.get("terms_and_conditions"))
        return Connector(format, id, last_updated, max_amperage, max_electric_power, max_voltage, power_type, standard, tariff_ids, terms_and_conditions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = to_enum(ConnectorFormat, self.format)
        result["id"] = from_str(self.id)
        result["last_updated"] = from_str(self.last_updated)
        result["max_amperage"] = from_int(self.max_amperage)
        if self.max_electric_power is not None:
            result["max_electric_power"] = from_union([from_none, from_int], self.max_electric_power)
        result["max_voltage"] = from_int(self.max_voltage)
        result["power_type"] = to_enum(PowerType, self.power_type)
        result["standard"] = to_enum(ConnectorType, self.standard)
        if self.tariff_ids is not None:
            result["tariff_ids"] = from_union([from_none, lambda x: from_list(from_str, x)], self.tariff_ids)
        if self.terms_and_conditions is not None:
            result["terms_and_conditions"] = from_union([from_none, from_str], self.terms_and_conditions)
        return result


class ImageCategory(Enum):
    CHARGER = "CHARGER"
    ENTRANCE = "ENTRANCE"
    LOCATION = "LOCATION"
    NETWORK = "NETWORK"
    OPERATOR = "OPERATOR"
    OTHER = "OTHER"
    OWNER = "OWNER"


class Image:
    category: ImageCategory
    height: Optional[int]
    thumbnail: Optional[str]
    type: str
    url: str
    width: Optional[int]

    def __init__(self, category: ImageCategory, height: Optional[int], thumbnail: Optional[str], type: str, url: str, width: Optional[int]) -> None:
        self.category = category
        self.height = height
        self.thumbnail = thumbnail
        self.type = type
        self.url = url
        self.width = width

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        category = ImageCategory(obj.get("category"))
        height = from_union([from_none, from_int], obj.get("height"))
        thumbnail = from_union([from_none, from_str], obj.get("thumbnail"))
        type = from_str(obj.get("type"))
        url = from_str(obj.get("url"))
        width = from_union([from_none, from_int], obj.get("width"))
        return Image(category, height, thumbnail, type, url, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category"] = to_enum(ImageCategory, self.category)
        if self.height is not None:
            result["height"] = from_union([from_none, from_int], self.height)
        if self.thumbnail is not None:
            result["thumbnail"] = from_union([from_none, from_str], self.thumbnail)
        result["type"] = from_str(self.type)
        result["url"] = from_str(self.url)
        if self.width is not None:
            result["width"] = from_union([from_none, from_int], self.width)
        return result


class BusinessDetails:
    logo: Optional[Image]
    name: str
    website: Optional[str]

    def __init__(self, logo: Optional[Image], name: str, website: Optional[str]) -> None:
        self.logo = logo
        self.name = name
        self.website = website

    @staticmethod
    def from_dict(obj: Any) -> 'BusinessDetails':
        assert isinstance(obj, dict)
        logo = from_union([from_none, Image.from_dict], obj.get("logo"))
        name = from_str(obj.get("name"))
        website = from_union([from_none, from_str], obj.get("website"))
        return BusinessDetails(logo, name, website)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.logo is not None:
            result["logo"] = from_union([from_none, lambda x: to_class(Image, x)], self.logo)
        result["name"] = from_str(self.name)
        if self.website is not None:
            result["website"] = from_union([from_none, from_str], self.website)
        return result


class Role(Enum):
    CPO = "CPO"
    EMSP = "EMSP"
    HUB = "HUB"
    NAP = "NAP"
    NSP = "NSP"
    OTHER = "OTHER"
    SCSP = "SCSP"


class CredentialsRole:
    business_details: BusinessDetails
    country_code: str
    party_id: str
    role: Role

    def __init__(self, business_details: BusinessDetails, country_code: str, party_id: str, role: Role) -> None:
        self.business_details = business_details
        self.country_code = country_code
        self.party_id = party_id
        self.role = role

    @staticmethod
    def from_dict(obj: Any) -> 'CredentialsRole':
        assert isinstance(obj, dict)
        business_details = BusinessDetails.from_dict(obj.get("business_details"))
        country_code = from_str(obj.get("country_code"))
        party_id = from_str(obj.get("party_id"))
        role = Role(obj.get("role"))
        return CredentialsRole(business_details, country_code, party_id, role)

    def to_dict(self) -> dict:
        result: dict = {}
        result["business_details"] = to_class(BusinessDetails, self.business_details)
        result["country_code"] = from_str(self.country_code)
        result["party_id"] = from_str(self.party_id)
        result["role"] = to_enum(Role, self.role)
        return result


class Credentials:
    roles: List[CredentialsRole]
    token: str
    url: str

    def __init__(self, roles: List[CredentialsRole], token: str, url: str) -> None:
        self.roles = roles
        self.token = token
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Credentials':
        assert isinstance(obj, dict)
        roles = from_list(CredentialsRole.from_dict, obj.get("roles"))
        token = from_str(obj.get("token"))
        url = from_str(obj.get("url"))
        return Credentials(roles, token, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["roles"] = from_list(lambda x: to_class(CredentialsRole, x), self.roles)
        result["token"] = from_str(self.token)
        result["url"] = from_str(self.url)
        return result


class ModuleID(Enum):
    CDRS = "cdrs"
    CHARGINGPROFILES = "chargingprofiles"
    COMMANDS = "commands"
    CREDENTIALS = "credentials"
    HUBCLIENTINFO = "hubclientinfo"
    LOCATIONS = "locations"
    SESSIONS = "sessions"
    TARIFFS = "tariffs"
    TOKENS = "tokens"


class InterfaceRole(Enum):
    RECEIVER = "RECEIVER"
    SENDER = "SENDER"


class Endpoint:
    identifier: ModuleID
    role: InterfaceRole
    url: str

    def __init__(self, identifier: ModuleID, role: InterfaceRole, url: str) -> None:
        self.identifier = identifier
        self.role = role
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Endpoint':
        assert isinstance(obj, dict)
        identifier = ModuleID(obj.get("identifier"))
        role = InterfaceRole(obj.get("role"))
        url = from_str(obj.get("url"))
        return Endpoint(identifier, role, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["identifier"] = to_enum(ModuleID, self.identifier)
        result["role"] = to_enum(InterfaceRole, self.role)
        result["url"] = from_str(self.url)
        return result


class Capability(Enum):
    CHARGING_PREFERENCES_CAPABLE = "CHARGING_PREFERENCES_CAPABLE"
    CHARGING_PROFILE_CAPABLE = "CHARGING_PROFILE_CAPABLE"
    CHIP_CARD_SUPPORT = "CHIP_CARD_SUPPORT"
    CONTACTLESS_CARD_SUPPORT = "CONTACTLESS_CARD_SUPPORT"
    CREDIT_CARD_PAYABLE = "CREDIT_CARD_PAYABLE"
    DEBIT_CARD_PAYABLE = "DEBIT_CARD_PAYABLE"
    PED_TERMINAL = "PED_TERMINAL"
    REMOTE_START_STOP_CAPABLE = "REMOTE_START_STOP_CAPABLE"
    RESERVABLE = "RESERVABLE"
    RFID_READER = "RFID_READER"
    START_SESSION_CONNECTOR_REQUIRED = "START_SESSION_CONNECTOR_REQUIRED"
    TOKEN_GROUP_CAPABLE = "TOKEN_GROUP_CAPABLE"
    UNLOCK_CAPABLE = "UNLOCK_CAPABLE"


class ParkingRestriction(Enum):
    CUSTOMERS = "CUSTOMERS"
    DISABLED = "DISABLED"
    EV_ONLY = "EV_ONLY"
    MOTORCYCLES = "MOTORCYCLES"
    PLUGGED = "PLUGGED"


class Status(Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
    CHARGING = "CHARGING"
    INOPERATIVE = "INOPERATIVE"
    OUTOFORDER = "OUTOFORDER"
    PLANNED = "PLANNED"
    REMOVED = "REMOVED"
    RESERVED = "RESERVED"
    UNKNOWN = "UNKNOWN"


class StatusSchedule:
    period_begin: str
    period_end: Optional[str]
    status: Status

    def __init__(self, period_begin: str, period_end: Optional[str], status: Status) -> None:
        self.period_begin = period_begin
        self.period_end = period_end
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'StatusSchedule':
        assert isinstance(obj, dict)
        period_begin = from_str(obj.get("period_begin"))
        period_end = from_union([from_none, from_str], obj.get("period_end"))
        status = Status(obj.get("status"))
        return StatusSchedule(period_begin, period_end, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["period_begin"] = from_str(self.period_begin)
        if self.period_end is not None:
            result["period_end"] = from_union([from_none, from_str], self.period_end)
        result["status"] = to_enum(Status, self.status)
        return result


class Evse:
    capabilities: Optional[List[Capability]]
    connectors: List[Connector]
    coordinates: Optional[GeoLocation]
    directions: Optional[List[DisplayText]]
    evse_id: Optional[str]
    floor_level: Optional[str]
    images: Optional[List[Image]]
    last_updated: str
    parking_restrictions: Optional[List[ParkingRestriction]]
    physical_reference: Optional[str]
    status: Status
    status_schedule: Optional[List[StatusSchedule]]
    uid: str

    def __init__(self, capabilities: Optional[List[Capability]], connectors: List[Connector], coordinates: Optional[GeoLocation], directions: Optional[List[DisplayText]], evse_id: Optional[str], floor_level: Optional[str], images: Optional[List[Image]], last_updated: str, parking_restrictions: Optional[List[ParkingRestriction]], physical_reference: Optional[str], status: Status, status_schedule: Optional[List[StatusSchedule]], uid: str) -> None:
        self.capabilities = capabilities
        self.connectors = connectors
        self.coordinates = coordinates
        self.directions = directions
        self.evse_id = evse_id
        self.floor_level = floor_level
        self.images = images
        self.last_updated = last_updated
        self.parking_restrictions = parking_restrictions
        self.physical_reference = physical_reference
        self.status = status
        self.status_schedule = status_schedule
        self.uid = uid

    @staticmethod
    def from_dict(obj: Any) -> 'Evse':
        assert isinstance(obj, dict)
        capabilities = from_union([from_none, lambda x: from_list(Capability, x)], obj.get("capabilities"))
        connectors = from_list(Connector.from_dict, obj.get("connectors"))
        coordinates = from_union([from_none, GeoLocation.from_dict], obj.get("coordinates"))
        directions = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("directions"))
        evse_id = from_union([from_none, from_str], obj.get("evse_id"))
        floor_level = from_union([from_none, from_str], obj.get("floor_level"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        last_updated = from_str(obj.get("last_updated"))
        parking_restrictions = from_union([from_none, lambda x: from_list(ParkingRestriction, x)], obj.get("parking_restrictions"))
        physical_reference = from_union([from_none, from_str], obj.get("physical_reference"))
        status = Status(obj.get("status"))
        status_schedule = from_union([from_none, lambda x: from_list(StatusSchedule.from_dict, x)], obj.get("status_schedule"))
        uid = from_str(obj.get("uid"))
        return Evse(capabilities, connectors, coordinates, directions, evse_id, floor_level, images, last_updated, parking_restrictions, physical_reference, status, status_schedule, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.capabilities is not None:
            result["capabilities"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(Capability, x), x)], self.capabilities)
        result["connectors"] = from_list(lambda x: to_class(Connector, x), self.connectors)
        if self.coordinates is not None:
            result["coordinates"] = from_union([from_none, lambda x: to_class(GeoLocation, x)], self.coordinates)
        if self.directions is not None:
            result["directions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.directions)
        if self.evse_id is not None:
            result["evse_id"] = from_union([from_none, from_str], self.evse_id)
        if self.floor_level is not None:
            result["floor_level"] = from_union([from_none, from_str], self.floor_level)
        if self.images is not None:
            result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        result["last_updated"] = from_str(self.last_updated)
        if self.parking_restrictions is not None:
            result["parking_restrictions"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(ParkingRestriction, x), x)], self.parking_restrictions)
        if self.physical_reference is not None:
            result["physical_reference"] = from_union([from_none, from_str], self.physical_reference)
        result["status"] = to_enum(Status, self.status)
        if self.status_schedule is not None:
            result["status_schedule"] = from_union([from_none, lambda x: from_list(lambda x: to_class(StatusSchedule, x), x)], self.status_schedule)
        result["uid"] = from_str(self.uid)
        return result


class ConnectionStatus(Enum):
    CONNECTED = "CONNECTED"
    OFFLINE = "OFFLINE"
    PLANNED = "PLANNED"
    SUSPENDED = "SUSPENDED"


class HubClientInfo:
    country_code: str
    last_updated: str
    party_id: str
    role: Role
    status: ConnectionStatus

    def __init__(self, country_code: str, last_updated: str, party_id: str, role: Role, status: ConnectionStatus) -> None:
        self.country_code = country_code
        self.last_updated = last_updated
        self.party_id = party_id
        self.role = role
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'HubClientInfo':
        assert isinstance(obj, dict)
        country_code = from_str(obj.get("country_code"))
        last_updated = from_str(obj.get("last_updated"))
        party_id = from_str(obj.get("party_id"))
        role = Role(obj.get("role"))
        status = ConnectionStatus(obj.get("status"))
        return HubClientInfo(country_code, last_updated, party_id, role, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["country_code"] = from_str(self.country_code)
        result["last_updated"] = from_str(self.last_updated)
        result["party_id"] = from_str(self.party_id)
        result["role"] = to_enum(Role, self.role)
        result["status"] = to_enum(ConnectionStatus, self.status)
        return result


class Facility(Enum):
    AIRPORT = "AIRPORT"
    BIKE_SHARING = "BIKE_SHARING"
    BUS_STOP = "BUS_STOP"
    CAFE = "CAFE"
    CARPOOL_PARKING = "CARPOOL_PARKING"
    FUEL_STATION = "FUEL_STATION"
    HOTEL = "HOTEL"
    MALL = "MALL"
    METRO_STATION = "METRO_STATION"
    MUSEUM = "MUSEUM"
    NATURE = "NATURE"
    PARKING_LOT = "PARKING_LOT"
    RECREATION_AREA = "RECREATION_AREA"
    RESTAURANT = "RESTAURANT"
    SPORT = "SPORT"
    SUPERMARKET = "SUPERMARKET"
    TAXI_STAND = "TAXI_STAND"
    TRAIN_STATION = "TRAIN_STATION"
    TRAM_STOP = "TRAM_STOP"
    WIFI = "WIFI"


class ExceptionalPeriod:
    period_begin: str
    period_end: str

    def __init__(self, period_begin: str, period_end: str) -> None:
        self.period_begin = period_begin
        self.period_end = period_end

    @staticmethod
    def from_dict(obj: Any) -> 'ExceptionalPeriod':
        assert isinstance(obj, dict)
        period_begin = from_str(obj.get("period_begin"))
        period_end = from_str(obj.get("period_end"))
        return ExceptionalPeriod(period_begin, period_end)

    def to_dict(self) -> dict:
        result: dict = {}
        result["period_begin"] = from_str(self.period_begin)
        result["period_end"] = from_str(self.period_end)
        return result


class RegularHours:
    period_begin: str
    period_end: str
    weekday: int

    def __init__(self, period_begin: str, period_end: str, weekday: int) -> None:
        self.period_begin = period_begin
        self.period_end = period_end
        self.weekday = weekday

    @staticmethod
    def from_dict(obj: Any) -> 'RegularHours':
        assert isinstance(obj, dict)
        period_begin = from_str(obj.get("period_begin"))
        period_end = from_str(obj.get("period_end"))
        weekday = from_int(obj.get("weekday"))
        return RegularHours(period_begin, period_end, weekday)

    def to_dict(self) -> dict:
        result: dict = {}
        result["period_begin"] = from_str(self.period_begin)
        result["period_end"] = from_str(self.period_end)
        result["weekday"] = from_int(self.weekday)
        return result


class Hours:
    exceptional_closings: Optional[List[ExceptionalPeriod]]
    exceptional_openings: Optional[List[ExceptionalPeriod]]
    regular_hours: Optional[List[RegularHours]]
    twentyfourseven: bool

    def __init__(self, exceptional_closings: Optional[List[ExceptionalPeriod]], exceptional_openings: Optional[List[ExceptionalPeriod]], regular_hours: Optional[List[RegularHours]], twentyfourseven: bool) -> None:
        self.exceptional_closings = exceptional_closings
        self.exceptional_openings = exceptional_openings
        self.regular_hours = regular_hours
        self.twentyfourseven = twentyfourseven

    @staticmethod
    def from_dict(obj: Any) -> 'Hours':
        assert isinstance(obj, dict)
        exceptional_closings = from_union([from_none, lambda x: from_list(ExceptionalPeriod.from_dict, x)], obj.get("exceptional_closings"))
        exceptional_openings = from_union([from_none, lambda x: from_list(ExceptionalPeriod.from_dict, x)], obj.get("exceptional_openings"))
        regular_hours = from_union([from_none, lambda x: from_list(RegularHours.from_dict, x)], obj.get("regular_hours"))
        twentyfourseven = from_bool(obj.get("twentyfourseven"))
        return Hours(exceptional_closings, exceptional_openings, regular_hours, twentyfourseven)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.exceptional_closings is not None:
            result["exceptional_closings"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ExceptionalPeriod, x), x)], self.exceptional_closings)
        if self.exceptional_openings is not None:
            result["exceptional_openings"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ExceptionalPeriod, x), x)], self.exceptional_openings)
        if self.regular_hours is not None:
            result["regular_hours"] = from_union([from_none, lambda x: from_list(lambda x: to_class(RegularHours, x), x)], self.regular_hours)
        result["twentyfourseven"] = from_bool(self.twentyfourseven)
        return result


class ParkingType(Enum):
    ALONG_MOTORWAY = "ALONG_MOTORWAY"
    ON_DRIVEWAY = "ON_DRIVEWAY"
    ON_STREET = "ON_STREET"
    PARKING_GARAGE = "PARKING_GARAGE"
    PARKING_LOT = "PARKING_LOT"
    UNDERGROUND_GARAGE = "UNDERGROUND_GARAGE"


class PublishTokenType:
    group_id: Optional[str]
    issuer: Optional[str]
    type: Optional[TokenType]
    uid: Optional[str]
    visual_number: Optional[str]

    def __init__(self, group_id: Optional[str], issuer: Optional[str], type: Optional[TokenType], uid: Optional[str], visual_number: Optional[str]) -> None:
        self.group_id = group_id
        self.issuer = issuer
        self.type = type
        self.uid = uid
        self.visual_number = visual_number

    @staticmethod
    def from_dict(obj: Any) -> 'PublishTokenType':
        assert isinstance(obj, dict)
        group_id = from_union([from_none, from_str], obj.get("group_id"))
        issuer = from_union([from_none, from_str], obj.get("issuer"))
        type = from_union([from_none, TokenType], obj.get("type"))
        uid = from_union([from_none, from_str], obj.get("uid"))
        visual_number = from_union([from_none, from_str], obj.get("visual_number"))
        return PublishTokenType(group_id, issuer, type, uid, visual_number)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.group_id is not None:
            result["group_id"] = from_union([from_none, from_str], self.group_id)
        if self.issuer is not None:
            result["issuer"] = from_union([from_none, from_str], self.issuer)
        if self.type is not None:
            result["type"] = from_union([from_none, lambda x: to_enum(TokenType, x)], self.type)
        if self.uid is not None:
            result["uid"] = from_union([from_none, from_str], self.uid)
        if self.visual_number is not None:
            result["visual_number"] = from_union([from_none, from_str], self.visual_number)
        return result


class AdditionalGeoLocation:
    latitude: str
    longitude: str
    name: Optional[DisplayText]

    def __init__(self, latitude: str, longitude: str, name: Optional[DisplayText]) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'AdditionalGeoLocation':
        assert isinstance(obj, dict)
        latitude = from_str(obj.get("latitude"))
        longitude = from_str(obj.get("longitude"))
        name = from_union([from_none, DisplayText.from_dict], obj.get("name"))
        return AdditionalGeoLocation(latitude, longitude, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["latitude"] = from_str(self.latitude)
        result["longitude"] = from_str(self.longitude)
        if self.name is not None:
            result["name"] = from_union([from_none, lambda x: to_class(DisplayText, x)], self.name)
        return result


class Location:
    address: str
    charging_when_closed: Optional[bool]
    city: str
    coordinates: GeoLocation
    country: str
    country_code: str
    directions: Optional[List[DisplayText]]
    energy_mix: Optional[EnergyMix]
    evses: Optional[List[Evse]]
    facilities: Optional[List[Facility]]
    id: str
    images: Optional[List[Image]]
    last_updated: str
    name: Optional[str]
    opening_times: Optional[Hours]
    operator: Optional[BusinessDetails]
    owner: Optional[BusinessDetails]
    parking_type: Optional[ParkingType]
    party_id: str
    postal_code: Optional[str]
    publish: bool
    publish_allowed_to: Optional[List[PublishTokenType]]
    related_locations: Optional[List[AdditionalGeoLocation]]
    state: Optional[str]
    suboperator: Optional[BusinessDetails]
    time_zone: str

    def __init__(self, address: str, charging_when_closed: Optional[bool], city: str, coordinates: GeoLocation, country: str, country_code: str, directions: Optional[List[DisplayText]], energy_mix: Optional[EnergyMix], evses: Optional[List[Evse]], facilities: Optional[List[Facility]], id: str, images: Optional[List[Image]], last_updated: str, name: Optional[str], opening_times: Optional[Hours], operator: Optional[BusinessDetails], owner: Optional[BusinessDetails], parking_type: Optional[ParkingType], party_id: str, postal_code: Optional[str], publish: bool, publish_allowed_to: Optional[List[PublishTokenType]], related_locations: Optional[List[AdditionalGeoLocation]], state: Optional[str], suboperator: Optional[BusinessDetails], time_zone: str) -> None:
        self.address = address
        self.charging_when_closed = charging_when_closed
        self.city = city
        self.coordinates = coordinates
        self.country = country
        self.country_code = country_code
        self.directions = directions
        self.energy_mix = energy_mix
        self.evses = evses
        self.facilities = facilities
        self.id = id
        self.images = images
        self.last_updated = last_updated
        self.name = name
        self.opening_times = opening_times
        self.operator = operator
        self.owner = owner
        self.parking_type = parking_type
        self.party_id = party_id
        self.postal_code = postal_code
        self.publish = publish
        self.publish_allowed_to = publish_allowed_to
        self.related_locations = related_locations
        self.state = state
        self.suboperator = suboperator
        self.time_zone = time_zone

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        charging_when_closed = from_union([from_none, from_bool], obj.get("charging_when_closed"))
        city = from_str(obj.get("city"))
        coordinates = GeoLocation.from_dict(obj.get("coordinates"))
        country = from_str(obj.get("country"))
        country_code = from_str(obj.get("country_code"))
        directions = from_union([from_none, lambda x: from_list(DisplayText.from_dict, x)], obj.get("directions"))
        energy_mix = from_union([from_none, EnergyMix.from_dict], obj.get("energy_mix"))
        evses = from_union([from_none, lambda x: from_list(Evse.from_dict, x)], obj.get("evses"))
        facilities = from_union([from_none, lambda x: from_list(Facility, x)], obj.get("facilities"))
        id = from_str(obj.get("id"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        last_updated = from_str(obj.get("last_updated"))
        name = from_union([from_none, from_str], obj.get("name"))
        opening_times = from_union([from_none, Hours.from_dict], obj.get("opening_times"))
        operator = from_union([from_none, BusinessDetails.from_dict], obj.get("operator"))
        owner = from_union([from_none, BusinessDetails.from_dict], obj.get("owner"))
        parking_type = from_union([from_none, ParkingType], obj.get("parking_type"))
        party_id = from_str(obj.get("party_id"))
        postal_code = from_union([from_none, from_str], obj.get("postal_code"))
        publish = from_bool(obj.get("publish"))
        publish_allowed_to = from_union([from_none, lambda x: from_list(PublishTokenType.from_dict, x)], obj.get("publish_allowed_to"))
        related_locations = from_union([from_none, lambda x: from_list(AdditionalGeoLocation.from_dict, x)], obj.get("related_locations"))
        state = from_union([from_none, from_str], obj.get("state"))
        suboperator = from_union([from_none, BusinessDetails.from_dict], obj.get("suboperator"))
        time_zone = from_str(obj.get("time_zone"))
        return Location(address, charging_when_closed, city, coordinates, country, country_code, directions, energy_mix, evses, facilities, id, images, last_updated, name, opening_times, operator, owner, parking_type, party_id, postal_code, publish, publish_allowed_to, related_locations, state, suboperator, time_zone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        if self.charging_when_closed is not None:
            result["charging_when_closed"] = from_union([from_none, from_bool], self.charging_when_closed)
        result["city"] = from_str(self.city)
        result["coordinates"] = to_class(GeoLocation, self.coordinates)
        result["country"] = from_str(self.country)
        result["country_code"] = from_str(self.country_code)
        if self.directions is not None:
            result["directions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DisplayText, x), x)], self.directions)
        if self.energy_mix is not None:
            result["energy_mix"] = from_union([from_none, lambda x: to_class(EnergyMix, x)], self.energy_mix)
        if self.evses is not None:
            result["evses"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Evse, x), x)], self.evses)
        if self.facilities is not None:
            result["facilities"] = from_union([from_none, lambda x: from_list(lambda x: to_enum(Facility, x), x)], self.facilities)
        result["id"] = from_str(self.id)
        if self.images is not None:
            result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        result["last_updated"] = from_str(self.last_updated)
        if self.name is not None:
            result["name"] = from_union([from_none, from_str], self.name)
        if self.opening_times is not None:
            result["opening_times"] = from_union([from_none, lambda x: to_class(Hours, x)], self.opening_times)
        if self.operator is not None:
            result["operator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.operator)
        if self.owner is not None:
            result["owner"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.owner)
        if self.parking_type is not None:
            result["parking_type"] = from_union([from_none, lambda x: to_enum(ParkingType, x)], self.parking_type)
        result["party_id"] = from_str(self.party_id)
        if self.postal_code is not None:
            result["postal_code"] = from_union([from_none, from_str], self.postal_code)
        result["publish"] = from_bool(self.publish)
        if self.publish_allowed_to is not None:
            result["publish_allowed_to"] = from_union([from_none, lambda x: from_list(lambda x: to_class(PublishTokenType, x), x)], self.publish_allowed_to)
        if self.related_locations is not None:
            result["related_locations"] = from_union([from_none, lambda x: from_list(lambda x: to_class(AdditionalGeoLocation, x), x)], self.related_locations)
        if self.state is not None:
            result["state"] = from_union([from_none, from_str], self.state)
        if self.suboperator is not None:
            result["suboperator"] = from_union([from_none, lambda x: to_class(BusinessDetails, x)], self.suboperator)
        result["time_zone"] = from_str(self.time_zone)
        return result


class ReserveNow:
    authorization_reference: Optional[str]
    evse_uid: Optional[str]
    expiry_date: str
    location_id: str
    reservation_id: str
    response_url: str
    token: Token

    def __init__(self, authorization_reference: Optional[str], evse_uid: Optional[str], expiry_date: str, location_id: str, reservation_id: str, response_url: str, token: Token) -> None:
        self.authorization_reference = authorization_reference
        self.evse_uid = evse_uid
        self.expiry_date = expiry_date
        self.location_id = location_id
        self.reservation_id = reservation_id
        self.response_url = response_url
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'ReserveNow':
        assert isinstance(obj, dict)
        authorization_reference = from_union([from_none, from_str], obj.get("authorization_reference"))
        evse_uid = from_union([from_none, from_str], obj.get("evse_uid"))
        expiry_date = from_str(obj.get("expiry_date"))
        location_id = from_str(obj.get("location_id"))
        reservation_id = from_str(obj.get("reservation_id"))
        response_url = from_str(obj.get("response_url"))
        token = Token.from_dict(obj.get("token"))
        return ReserveNow(authorization_reference, evse_uid, expiry_date, location_id, reservation_id, response_url, token)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.authorization_reference is not None:
            result["authorization_reference"] = from_union([from_none, from_str], self.authorization_reference)
        if self.evse_uid is not None:
            result["evse_uid"] = from_union([from_none, from_str], self.evse_uid)
        result["expiry_date"] = from_str(self.expiry_date)
        result["location_id"] = from_str(self.location_id)
        result["reservation_id"] = from_str(self.reservation_id)
        result["response_url"] = from_str(self.response_url)
        result["token"] = to_class(Token, self.token)
        return result


class SessionStatus(Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    INVALID = "INVALID"
    PENDING = "PENDING"
    RESERVATION = "RESERVATION"


class Session:
    auth_method: AuthMethod
    authorization_reference: Optional[str]
    cdr_token: CdrToken
    charging_periods: Optional[List[ChargingPeriod]]
    connector_id: str
    country_code: str
    currency: str
    end_date_time: Optional[str]
    evse_uid: str
    id: str
    kwh: float
    last_updated: str
    location_id: str
    meter_id: Optional[str]
    party_id: str
    start_date_time: str
    status: SessionStatus
    total_cost: Optional[Price]

    def __init__(self, auth_method: AuthMethod, authorization_reference: Optional[str], cdr_token: CdrToken, charging_periods: Optional[List[ChargingPeriod]], connector_id: str, country_code: str, currency: str, end_date_time: Optional[str], evse_uid: str, id: str, kwh: float, last_updated: str, location_id: str, meter_id: Optional[str], party_id: str, start_date_time: str, status: SessionStatus, total_cost: Optional[Price]) -> None:
        self.auth_method = auth_method
        self.authorization_reference = authorization_reference
        self.cdr_token = cdr_token
        self.charging_periods = charging_periods
        self.connector_id = connector_id
        self.country_code = country_code
        self.currency = currency
        self.end_date_time = end_date_time
        self.evse_uid = evse_uid
        self.id = id
        self.kwh = kwh
        self.last_updated = last_updated
        self.location_id = location_id
        self.meter_id = meter_id
        self.party_id = party_id
        self.start_date_time = start_date_time
        self.status = status
        self.total_cost = total_cost

    @staticmethod
    def from_dict(obj: Any) -> 'Session':
        assert isinstance(obj, dict)
        auth_method = AuthMethod(obj.get("auth_method"))
        authorization_reference = from_union([from_none, from_str], obj.get("authorization_reference"))
        cdr_token = CdrToken.from_dict(obj.get("cdr_token"))
        charging_periods = from_union([from_none, lambda x: from_list(ChargingPeriod.from_dict, x)], obj.get("charging_periods"))
        connector_id = from_str(obj.get("connector_id"))
        country_code = from_str(obj.get("country_code"))
        currency = from_str(obj.get("currency"))
        end_date_time = from_union([from_none, from_str], obj.get("end_date_time"))
        evse_uid = from_str(obj.get("evse_uid"))
        id = from_str(obj.get("id"))
        kwh = from_float(obj.get("kwh"))
        last_updated = from_str(obj.get("last_updated"))
        location_id = from_str(obj.get("location_id"))
        meter_id = from_union([from_none, from_str], obj.get("meter_id"))
        party_id = from_str(obj.get("party_id"))
        start_date_time = from_str(obj.get("start_date_time"))
        status = SessionStatus(obj.get("status"))
        total_cost = from_union([from_none, Price.from_dict], obj.get("total_cost"))
        return Session(auth_method, authorization_reference, cdr_token, charging_periods, connector_id, country_code, currency, end_date_time, evse_uid, id, kwh, last_updated, location_id, meter_id, party_id, start_date_time, status, total_cost)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth_method"] = to_enum(AuthMethod, self.auth_method)
        if self.authorization_reference is not None:
            result["authorization_reference"] = from_union([from_none, from_str], self.authorization_reference)
        result["cdr_token"] = to_class(CdrToken, self.cdr_token)
        if self.charging_periods is not None:
            result["charging_periods"] = from_union([from_none, lambda x: from_list(lambda x: to_class(ChargingPeriod, x), x)], self.charging_periods)
        result["connector_id"] = from_str(self.connector_id)
        result["country_code"] = from_str(self.country_code)
        result["currency"] = from_str(self.currency)
        if self.end_date_time is not None:
            result["end_date_time"] = from_union([from_none, from_str], self.end_date_time)
        result["evse_uid"] = from_str(self.evse_uid)
        result["id"] = from_str(self.id)
        result["kwh"] = to_float(self.kwh)
        result["last_updated"] = from_str(self.last_updated)
        result["location_id"] = from_str(self.location_id)
        if self.meter_id is not None:
            result["meter_id"] = from_union([from_none, from_str], self.meter_id)
        result["party_id"] = from_str(self.party_id)
        result["start_date_time"] = from_str(self.start_date_time)
        result["status"] = to_enum(SessionStatus, self.status)
        if self.total_cost is not None:
            result["total_cost"] = from_union([from_none, lambda x: to_class(Price, x)], self.total_cost)
        return result


class SetChargingProfile:
    charging_profile: ChargingProfile
    response_url: str

    def __init__(self, charging_profile: ChargingProfile, response_url: str) -> None:
        self.charging_profile = charging_profile
        self.response_url = response_url

    @staticmethod
    def from_dict(obj: Any) -> 'SetChargingProfile':
        assert isinstance(obj, dict)
        charging_profile = ChargingProfile.from_dict(obj.get("charging_profile"))
        response_url = from_str(obj.get("response_url"))
        return SetChargingProfile(charging_profile, response_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["charging_profile"] = to_class(ChargingProfile, self.charging_profile)
        result["response_url"] = from_str(self.response_url)
        return result


class StartSession:
    authorization_reference: Optional[str]
    connector_id: Optional[str]
    evse_uid: Optional[str]
    location_id: str
    response_url: str
    token: Token

    def __init__(self, authorization_reference: Optional[str], connector_id: Optional[str], evse_uid: Optional[str], location_id: str, response_url: str, token: Token) -> None:
        self.authorization_reference = authorization_reference
        self.connector_id = connector_id
        self.evse_uid = evse_uid
        self.location_id = location_id
        self.response_url = response_url
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'StartSession':
        assert isinstance(obj, dict)
        authorization_reference = from_union([from_none, from_str], obj.get("authorization_reference"))
        connector_id = from_union([from_none, from_str], obj.get("connector_id"))
        evse_uid = from_union([from_none, from_str], obj.get("evse_uid"))
        location_id = from_str(obj.get("location_id"))
        response_url = from_str(obj.get("response_url"))
        token = Token.from_dict(obj.get("token"))
        return StartSession(authorization_reference, connector_id, evse_uid, location_id, response_url, token)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.authorization_reference is not None:
            result["authorization_reference"] = from_union([from_none, from_str], self.authorization_reference)
        if self.connector_id is not None:
            result["connector_id"] = from_union([from_none, from_str], self.connector_id)
        if self.evse_uid is not None:
            result["evse_uid"] = from_union([from_none, from_str], self.evse_uid)
        result["location_id"] = from_str(self.location_id)
        result["response_url"] = from_str(self.response_url)
        result["token"] = to_class(Token, self.token)
        return result


class StopSession:
    response_url: str
    session_id: str

    def __init__(self, response_url: str, session_id: str) -> None:
        self.response_url = response_url
        self.session_id = session_id

    @staticmethod
    def from_dict(obj: Any) -> 'StopSession':
        assert isinstance(obj, dict)
        response_url = from_str(obj.get("response_url"))
        session_id = from_str(obj.get("session_id"))
        return StopSession(response_url, session_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["response_url"] = from_str(self.response_url)
        result["session_id"] = from_str(self.session_id)
        return result


class UnlockConnector:
    connector_id: str
    evse_uid: str
    location_id: str
    response_url: str

    def __init__(self, connector_id: str, evse_uid: str, location_id: str, response_url: str) -> None:
        self.connector_id = connector_id
        self.evse_uid = evse_uid
        self.location_id = location_id
        self.response_url = response_url

    @staticmethod
    def from_dict(obj: Any) -> 'UnlockConnector':
        assert isinstance(obj, dict)
        connector_id = from_str(obj.get("connector_id"))
        evse_uid = from_str(obj.get("evse_uid"))
        location_id = from_str(obj.get("location_id"))
        response_url = from_str(obj.get("response_url"))
        return UnlockConnector(connector_id, evse_uid, location_id, response_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["connector_id"] = from_str(self.connector_id)
        result["evse_uid"] = from_str(self.evse_uid)
        result["location_id"] = from_str(self.location_id)
        result["response_url"] = from_str(self.response_url)
        return result


class VersionNumber(Enum):
    THE_20 = "2.0"
    THE_21 = "2.1"
    THE_211 = "2.1.1"
    THE_22 = "2.2"
    THE_221 = "2.2.1"


class Version:
    url: str
    version: VersionNumber

    def __init__(self, url: str, version: VersionNumber) -> None:
        self.url = url
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'Version':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        version = VersionNumber(obj.get("version"))
        return Version(url, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["version"] = to_enum(VersionNumber, self.version)
        return result


class VersionDetails:
    endpoints: List[Endpoint]
    version: VersionNumber

    def __init__(self, endpoints: List[Endpoint], version: VersionNumber) -> None:
        self.endpoints = endpoints
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'VersionDetails':
        assert isinstance(obj, dict)
        endpoints = from_list(Endpoint.from_dict, obj.get("endpoints"))
        version = VersionNumber(obj.get("version"))
        return VersionDetails(endpoints, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endpoints"] = from_list(lambda x: to_class(Endpoint, x), self.endpoints)
        result["version"] = to_enum(VersionNumber, self.version)
        return result


class V221:
    active_charging_profile: Optional[ActiveChargingProfile]
    active_charging_profile_result: Optional[ActiveChargingProfileResult]
    authorization_info: Optional[AuthorizationInfo]
    cancel_reservation: Optional[CancelReservation]
    cdr: Optional[Cdr]
    charging_preferences: Optional[ChargingPreferences]
    charging_profile: Optional[ChargingProfile]
    charging_profile_response: Optional[ChargingProfileResponse]
    charging_profile_result: Optional[ChargingProfileResult]
    clear_profile_result: Optional[ClearProfileResult]
    command_response: Optional[CommandResponse]
    command_result: Optional[CommandResult]
    connector: Optional[Connector]
    credentials: Optional[Credentials]
    endpoint: Optional[Endpoint]
    evse: Optional[Evse]
    hub_client_info: Optional[HubClientInfo]
    location: Optional[Location]
    location_references: Optional[LocationReferences]
    reserve_now: Optional[ReserveNow]
    session: Optional[Session]
    set_charging_profile: Optional[SetChargingProfile]
    start_session: Optional[StartSession]
    stop_session: Optional[StopSession]
    tariff: Optional[Tariff]
    token: Optional[Token]
    unlock_connector: Optional[UnlockConnector]
    version: Optional[Version]
    version_details: Optional[VersionDetails]

    def __init__(self, active_charging_profile: Optional[ActiveChargingProfile], active_charging_profile_result: Optional[ActiveChargingProfileResult], authorization_info: Optional[AuthorizationInfo], cancel_reservation: Optional[CancelReservation], cdr: Optional[Cdr], charging_preferences: Optional[ChargingPreferences], charging_profile: Optional[ChargingProfile], charging_profile_response: Optional[ChargingProfileResponse], charging_profile_result: Optional[ChargingProfileResult], clear_profile_result: Optional[ClearProfileResult], command_response: Optional[CommandResponse], command_result: Optional[CommandResult], connector: Optional[Connector], credentials: Optional[Credentials], endpoint: Optional[Endpoint], evse: Optional[Evse], hub_client_info: Optional[HubClientInfo], location: Optional[Location], location_references: Optional[LocationReferences], reserve_now: Optional[ReserveNow], session: Optional[Session], set_charging_profile: Optional[SetChargingProfile], start_session: Optional[StartSession], stop_session: Optional[StopSession], tariff: Optional[Tariff], token: Optional[Token], unlock_connector: Optional[UnlockConnector], version: Optional[Version], version_details: Optional[VersionDetails]) -> None:
        self.active_charging_profile = active_charging_profile
        self.active_charging_profile_result = active_charging_profile_result
        self.authorization_info = authorization_info
        self.cancel_reservation = cancel_reservation
        self.cdr = cdr
        self.charging_preferences = charging_preferences
        self.charging_profile = charging_profile
        self.charging_profile_response = charging_profile_response
        self.charging_profile_result = charging_profile_result
        self.clear_profile_result = clear_profile_result
        self.command_response = command_response
        self.command_result = command_result
        self.connector = connector
        self.credentials = credentials
        self.endpoint = endpoint
        self.evse = evse
        self.hub_client_info = hub_client_info
        self.location = location
        self.location_references = location_references
        self.reserve_now = reserve_now
        self.session = session
        self.set_charging_profile = set_charging_profile
        self.start_session = start_session
        self.stop_session = stop_session
        self.tariff = tariff
        self.token = token
        self.unlock_connector = unlock_connector
        self.version = version
        self.version_details = version_details

    @staticmethod
    def from_dict(obj: Any) -> 'V221':
        assert isinstance(obj, dict)
        active_charging_profile = from_union([ActiveChargingProfile.from_dict, from_none], obj.get("active_charging_profile"))
        active_charging_profile_result = from_union([ActiveChargingProfileResult.from_dict, from_none], obj.get("active_charging_profile_result"))
        authorization_info = from_union([AuthorizationInfo.from_dict, from_none], obj.get("authorization_info"))
        cancel_reservation = from_union([CancelReservation.from_dict, from_none], obj.get("cancel_reservation"))
        cdr = from_union([Cdr.from_dict, from_none], obj.get("cdr"))
        charging_preferences = from_union([ChargingPreferences.from_dict, from_none], obj.get("charging_preferences"))
        charging_profile = from_union([ChargingProfile.from_dict, from_none], obj.get("charging_profile"))
        charging_profile_response = from_union([ChargingProfileResponse.from_dict, from_none], obj.get("charging_profile_response"))
        charging_profile_result = from_union([ChargingProfileResult.from_dict, from_none], obj.get("charging_profile_result"))
        clear_profile_result = from_union([ClearProfileResult.from_dict, from_none], obj.get("clear_profile_result"))
        command_response = from_union([CommandResponse.from_dict, from_none], obj.get("command_response"))
        command_result = from_union([CommandResult.from_dict, from_none], obj.get("command_result"))
        connector = from_union([Connector.from_dict, from_none], obj.get("connector"))
        credentials = from_union([Credentials.from_dict, from_none], obj.get("credentials"))
        endpoint = from_union([Endpoint.from_dict, from_none], obj.get("endpoint"))
        evse = from_union([Evse.from_dict, from_none], obj.get("evse"))
        hub_client_info = from_union([HubClientInfo.from_dict, from_none], obj.get("hub_client_info"))
        location = from_union([Location.from_dict, from_none], obj.get("location"))
        location_references = from_union([from_none, LocationReferences.from_dict], obj.get("location_references"))
        reserve_now = from_union([ReserveNow.from_dict, from_none], obj.get("reserve_now"))
        session = from_union([Session.from_dict, from_none], obj.get("session"))
        set_charging_profile = from_union([SetChargingProfile.from_dict, from_none], obj.get("set_charging_profile"))
        start_session = from_union([StartSession.from_dict, from_none], obj.get("start_session"))
        stop_session = from_union([StopSession.from_dict, from_none], obj.get("stop_session"))
        tariff = from_union([Tariff.from_dict, from_none], obj.get("tariff"))
        token = from_union([Token.from_dict, from_none], obj.get("token"))
        unlock_connector = from_union([UnlockConnector.from_dict, from_none], obj.get("unlock_connector"))
        version = from_union([Version.from_dict, from_none], obj.get("version"))
        version_details = from_union([VersionDetails.from_dict, from_none], obj.get("version_details"))
        return V221(active_charging_profile, active_charging_profile_result, authorization_info, cancel_reservation, cdr, charging_preferences, charging_profile, charging_profile_response, charging_profile_result, clear_profile_result, command_response, command_result, connector, credentials, endpoint, evse, hub_client_info, location, location_references, reserve_now, session, set_charging_profile, start_session, stop_session, tariff, token, unlock_connector, version, version_details)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.active_charging_profile is not None:
            result["active_charging_profile"] = from_union([lambda x: to_class(ActiveChargingProfile, x), from_none], self.active_charging_profile)
        if self.active_charging_profile_result is not None:
            result["active_charging_profile_result"] = from_union([lambda x: to_class(ActiveChargingProfileResult, x), from_none], self.active_charging_profile_result)
        if self.authorization_info is not None:
            result["authorization_info"] = from_union([lambda x: to_class(AuthorizationInfo, x), from_none], self.authorization_info)
        if self.cancel_reservation is not None:
            result["cancel_reservation"] = from_union([lambda x: to_class(CancelReservation, x), from_none], self.cancel_reservation)
        if self.cdr is not None:
            result["cdr"] = from_union([lambda x: to_class(Cdr, x), from_none], self.cdr)
        if self.charging_preferences is not None:
            result["charging_preferences"] = from_union([lambda x: to_class(ChargingPreferences, x), from_none], self.charging_preferences)
        if self.charging_profile is not None:
            result["charging_profile"] = from_union([lambda x: to_class(ChargingProfile, x), from_none], self.charging_profile)
        if self.charging_profile_response is not None:
            result["charging_profile_response"] = from_union([lambda x: to_class(ChargingProfileResponse, x), from_none], self.charging_profile_response)
        if self.charging_profile_result is not None:
            result["charging_profile_result"] = from_union([lambda x: to_class(ChargingProfileResult, x), from_none], self.charging_profile_result)
        if self.clear_profile_result is not None:
            result["clear_profile_result"] = from_union([lambda x: to_class(ClearProfileResult, x), from_none], self.clear_profile_result)
        if self.command_response is not None:
            result["command_response"] = from_union([lambda x: to_class(CommandResponse, x), from_none], self.command_response)
        if self.command_result is not None:
            result["command_result"] = from_union([lambda x: to_class(CommandResult, x), from_none], self.command_result)
        if self.connector is not None:
            result["connector"] = from_union([lambda x: to_class(Connector, x), from_none], self.connector)
        if self.credentials is not None:
            result["credentials"] = from_union([lambda x: to_class(Credentials, x), from_none], self.credentials)
        if self.endpoint is not None:
            result["endpoint"] = from_union([lambda x: to_class(Endpoint, x), from_none], self.endpoint)
        if self.evse is not None:
            result["evse"] = from_union([lambda x: to_class(Evse, x), from_none], self.evse)
        if self.hub_client_info is not None:
            result["hub_client_info"] = from_union([lambda x: to_class(HubClientInfo, x), from_none], self.hub_client_info)
        if self.location is not None:
            result["location"] = from_union([lambda x: to_class(Location, x), from_none], self.location)
        if self.location_references is not None:
            result["location_references"] = from_union([from_none, lambda x: to_class(LocationReferences, x)], self.location_references)
        if self.reserve_now is not None:
            result["reserve_now"] = from_union([lambda x: to_class(ReserveNow, x), from_none], self.reserve_now)
        if self.session is not None:
            result["session"] = from_union([lambda x: to_class(Session, x), from_none], self.session)
        if self.set_charging_profile is not None:
            result["set_charging_profile"] = from_union([lambda x: to_class(SetChargingProfile, x), from_none], self.set_charging_profile)
        if self.start_session is not None:
            result["start_session"] = from_union([lambda x: to_class(StartSession, x), from_none], self.start_session)
        if self.stop_session is not None:
            result["stop_session"] = from_union([lambda x: to_class(StopSession, x), from_none], self.stop_session)
        if self.tariff is not None:
            result["tariff"] = from_union([lambda x: to_class(Tariff, x), from_none], self.tariff)
        if self.token is not None:
            result["token"] = from_union([lambda x: to_class(Token, x), from_none], self.token)
        if self.unlock_connector is not None:
            result["unlock_connector"] = from_union([lambda x: to_class(UnlockConnector, x), from_none], self.unlock_connector)
        if self.version is not None:
            result["version"] = from_union([lambda x: to_class(Version, x), from_none], self.version)
        if self.version_details is not None:
            result["version_details"] = from_union([lambda x: to_class(VersionDetails, x), from_none], self.version_details)
        return result


def v221_from_dict(s: Any) -> V221:
    return V221.from_dict(s)


def v221_to_dict(x: V221) -> Any:
    return to_class(V221, x)
