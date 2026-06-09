// To parse this data:
//
//   import { Convert, V230Payments } from "./file";
//
//   const v230Payments = Convert.toV230Payments(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface V230Payments {
    active_charging_profile?:        ActiveChargingProfile;
    active_charging_profile_result?: ActiveChargingProfileResult;
    authorization_info?:             AuthorizationInfo;
    cancel_reservation?:             CancelReservation;
    cdr?:                            Cdr;
    charging_preferences?:           ChargingPreferences;
    charging_profile?:               ChargingProfile;
    charging_profile_response?:      ChargingProfileResponse;
    charging_profile_result?:        ChargingProfileResult;
    clear_profile_result?:           ClearProfileResult;
    command_response?:               CommandResponse;
    command_result?:                 CommandResult;
    connector?:                      Connector;
    credentials?:                    Credentials;
    endpoint?:                       Endpoint;
    evse?:                           Evse;
    financial_advice_confirmation?:  FinancialAdviceConfirmation;
    hub_client_info?:                HubClientInfo;
    location?:                       Location;
    location_references?:            LocationReferences;
    reserve_now?:                    ReserveNow;
    session?:                        Session;
    set_charging_profile?:           SetChargingProfile;
    start_session?:                  StartSession;
    stop_session?:                   StopSession;
    tariff?:                         Tariff;
    terminal?:                       Terminal;
    token?:                          Token;
    unlock_connector?:               UnlockConnector;
    version?:                        Version;
    version_details?:                VersionDetails;
    [property: string]: any;
}

export interface ActiveChargingProfile {
    charging_profile: ChargingProfile;
    start_date_time:  string;
}

export interface ChargingProfile {
    charging_profile_period?: ChargingProfilePeriod[] | null;
    charging_rate_unit:       ChargingRateUnit;
    duration?:                number | null;
    min_charging_rate?:       number | null;
    start_date_time?:         null | string;
}

export interface ChargingProfilePeriod {
    limit:        number;
    start_period: number;
}

export enum ChargingRateUnit {
    A = "A",
    W = "W",
}

export interface ActiveChargingProfileResult {
    profile?: ActiveChargingProfile | null;
    result:   ChargingProfileResultType;
}

export enum ChargingProfileResultType {
    Accepted = "ACCEPTED",
    Rejected = "REJECTED",
    Unknown = "UNKNOWN",
}

export interface AuthorizationInfo {
    allowed:                  AllowedType;
    authorization_reference?: null | string;
    info?:                    DisplayText | null;
    location?:                LocationReferences | null;
    token:                    Token;
}

export enum AllowedType {
    Allowed = "ALLOWED",
    Blocked = "BLOCKED",
    Expired = "EXPIRED",
    NoCredit = "NO_CREDIT",
    NotAllowed = "NOT_ALLOWED",
}

export interface DisplayText {
    language: string;
    text:     string;
}

export interface LocationReferences {
    evse_uids?:  string[] | null;
    location_id: string;
}

export interface Token {
    contract_id:           string;
    country_code:          string;
    default_profile_type?: ProfileType | null;
    energy_contract?:      EnergyContract | null;
    group_id?:             null | string;
    issuer:                string;
    language?:             null | string;
    last_updated:          string;
    party_id:              string;
    type:                  TokenType;
    uid:                   string;
    valid:                 boolean;
    visual_number?:        null | string;
    whitelist:             WhitelistType;
}

export enum ProfileType {
    Cheap = "CHEAP",
    Fast = "FAST",
    Green = "GREEN",
    Regular = "REGULAR",
}

export interface EnergyContract {
    contract_id?:  null | string;
    supplier_name: string;
}

export enum TokenType {
    AdHocUser = "AD_HOC_USER",
    AppUser = "APP_USER",
    Emaid = "EMAID",
    Other = "OTHER",
    RFID = "RFID",
}

export enum WhitelistType {
    Allowed = "ALLOWED",
    AllowedOffline = "ALLOWED_OFFLINE",
    Always = "ALWAYS",
    Never = "NEVER",
}

export interface CancelReservation {
    reservation_id: string;
    response_url:   string;
}

export interface Cdr {
    auth_method:                 AuthMethod;
    authorization_reference?:    null | string;
    cdr_location:                CdrLocation;
    cdr_token:                   CdrToken;
    charging_periods:            ChargingPeriod[];
    country_code:                string;
    credit?:                     boolean | null;
    credit_reference_id?:        null | string;
    currency:                    string;
    end_date_time:               string;
    home_charging_compensation?: boolean | null;
    id:                          string;
    invoice_reference_id?:       null | string;
    last_updated:                string;
    meter_id?:                   null | string;
    party_id:                    string;
    remark?:                     null | string;
    session_id?:                 null | string;
    signed_data?:                SignedData | null;
    start_date_time:             string;
    tariffs?:                    Tariff[] | null;
    total_cost:                  Price;
    total_energy:                number;
    total_energy_cost?:          Price | null;
    total_fixed_cost?:           Price | null;
    total_parking_cost?:         Price | null;
    total_parking_time?:         number | null;
    total_reservation_cost?:     Price | null;
    total_time:                  number;
    total_time_cost?:            Price | null;
}

export enum AuthMethod {
    AuthRequest = "AUTH_REQUEST",
    Command = "COMMAND",
    Whitelist = "WHITELIST",
}

export interface CdrLocation {
    address:              string;
    city:                 string;
    connector_format:     ConnectorFormat;
    connector_id:         string;
    connector_power_type: PowerType;
    connector_standard:   ConnectorType;
    coordinates:          GeoLocation;
    country:              string;
    evse_id:              string;
    evse_uid:             string;
    id:                   string;
    name?:                null | string;
    postal_code?:         null | string;
    state?:               null | string;
}

export enum ConnectorFormat {
    Cable = "CABLE",
    Socket = "SOCKET",
}

export enum PowerType {
    AC1_Phase = "AC_1_PHASE",
    AC2_Phase = "AC_2_PHASE",
    AC2_PhaseSplit = "AC_2_PHASE_SPLIT",
    AC3_Phase = "AC_3_PHASE",
    Dc = "DC",
}

export enum ConnectorType {
    Chademo = "CHADEMO",
    Chaoji = "CHAOJI",
    DomesticA = "DOMESTIC_A",
    DomesticB = "DOMESTIC_B",
    DomesticC = "DOMESTIC_C",
    DomesticD = "DOMESTIC_D",
    DomesticE = "DOMESTIC_E",
    DomesticF = "DOMESTIC_F",
    DomesticG = "DOMESTIC_G",
    DomesticH = "DOMESTIC_H",
    DomesticI = "DOMESTIC_I",
    DomesticJ = "DOMESTIC_J",
    DomesticK = "DOMESTIC_K",
    DomesticL = "DOMESTIC_L",
    DomesticM = "DOMESTIC_M",
    DomesticN = "DOMESTIC_N",
    DomesticO = "DOMESTIC_O",
    GbtAC = "GBT_AC",
    GbtDc = "GBT_DC",
    IEC60309_2_Single16 = "IEC_60309_2_single_16",
    IEC60309_2_Three16 = "IEC_60309_2_three_16",
    IEC60309_2_Three32 = "IEC_60309_2_three_32",
    IEC60309_2_Three64 = "IEC_60309_2_three_64",
    IEC62196_T1 = "IEC_62196_T1",
    IEC62196_T1Combo = "IEC_62196_T1_COMBO",
    IEC62196_T2 = "IEC_62196_T2",
    IEC62196_T2Combo = "IEC_62196_T2_COMBO",
    IEC62196_T3A = "IEC_62196_T3A",
    IEC62196_T3C = "IEC_62196_T3C",
    Mcs = "MCS",
    Nema10_30 = "NEMA_10_30",
    Nema10_50 = "NEMA_10_50",
    Nema14_30 = "NEMA_14_30",
    Nema14_50 = "NEMA_14_50",
    Nema5_20 = "NEMA_5_20",
    Nema6_30 = "NEMA_6_30",
    Nema6_50 = "NEMA_6_50",
    PantographBottomUp = "PANTOGRAPH_BOTTOM_UP",
    PantographTopDown = "PANTOGRAPH_TOP_DOWN",
    SaeJ3400 = "SAE_J3400",
    TeslaR = "TESLA_R",
    TeslaS = "TESLA_S",
}

export interface GeoLocation {
    latitude:  string;
    longitude: string;
}

export interface CdrToken {
    contract_id:  string;
    country_code: string;
    party_id:     string;
    type:         TokenType;
    uid:          string;
}

export interface ChargingPeriod {
    dimensions:      CdrDimension[];
    start_date_time: string;
    tariff_id?:      null | string;
}

export interface CdrDimension {
    type:   CdrDimensionType;
    volume: number;
}

export enum CdrDimensionType {
    Current = "CURRENT",
    Energy = "ENERGY",
    EnergyExport = "ENERGY_EXPORT",
    EnergyImport = "ENERGY_IMPORT",
    MaxCurrent = "MAX_CURRENT",
    MaxPower = "MAX_POWER",
    MinCurrent = "MIN_CURRENT",
    MinPower = "MIN_POWER",
    ParkingTime = "PARKING_TIME",
    Power = "POWER",
    ReservationTime = "RESERVATION_TIME",
    StateOfCharge = "STATE_OF_CHARGE",
    Time = "TIME",
}

export interface SignedData {
    encoding_method:          string;
    encoding_method_version?: number | null;
    public_key?:              null | string;
    signed_values:            SignedValue[];
    url?:                     null | string;
}

export interface SignedValue {
    nature:      string;
    plain_data:  string;
    signed_data: string;
}

export interface Tariff {
    country_code:         string;
    currency:             string;
    elements:             TariffElement[];
    end_date_time?:       null | string;
    energy_mix?:          EnergyMix | null;
    id:                   string;
    last_updated:         string;
    max_price?:           PriceLimit | null;
    min_price?:           PriceLimit | null;
    party_id:             string;
    preauthorize_amount?: number | null;
    start_date_time?:     null | string;
    tariff_alt_text?:     DisplayText[] | null;
    tariff_alt_url?:      null | string;
    tax_included:         TaxIncluded;
    type?:                TariffType | null;
}

export interface TariffElement {
    price_components: PriceComponent[];
    restrictions?:    TariffRestrictions | null;
}

export interface PriceComponent {
    price:     number;
    step_size: number;
    type:      TariffDimensionType;
    vat?:      number | null;
}

export enum TariffDimensionType {
    Energy = "ENERGY",
    Flat = "FLAT",
    ParkingTime = "PARKING_TIME",
    Time = "TIME",
}

export interface TariffRestrictions {
    day_of_week?:  DayOfWeek[] | null;
    end_date?:     null | string;
    end_time?:     null | string;
    max_current?:  number | null;
    max_duration?: number | null;
    max_kwh?:      number | null;
    max_power?:    number | null;
    min_current?:  number | null;
    min_duration?: number | null;
    min_kwh?:      number | null;
    min_power?:    number | null;
    reservation?:  ReservationRestrictionType | null;
    start_date?:   null | string;
    start_time?:   null | string;
}

export enum DayOfWeek {
    Friday = "FRIDAY",
    Monday = "MONDAY",
    Saturday = "SATURDAY",
    Sunday = "SUNDAY",
    Thursday = "THURSDAY",
    Tuesday = "TUESDAY",
    Wednesday = "WEDNESDAY",
}

export enum ReservationRestrictionType {
    Reservation = "RESERVATION",
    ReservationExpires = "RESERVATION_EXPIRES",
}

export interface EnergyMix {
    energy_product_name?: null | string;
    energy_sources?:      EnergySource[] | null;
    environ_impact?:      EnvironmentalImpact[] | null;
    is_green_energy:      boolean;
    supplier_name?:       null | string;
}

export interface EnergySource {
    percentage: number;
    source:     EnergySourceCategory;
}

export enum EnergySourceCategory {
    Coal = "COAL",
    Gas = "GAS",
    GeneralFossil = "GENERAL_FOSSIL",
    GeneralGreen = "GENERAL_GREEN",
    Nuclear = "NUCLEAR",
    Solar = "SOLAR",
    Water = "WATER",
    Wind = "WIND",
}

export interface EnvironmentalImpact {
    amount:   number;
    category: EnvironmentalImpactCategory;
}

export enum EnvironmentalImpactCategory {
    CarbonDioxide = "CARBON_DIOXIDE",
    NuclearWaste = "NUCLEAR_WASTE",
}

export interface PriceLimit {
    after_taxes?: number | null;
    before_taxes: number;
}

export enum TaxIncluded {
    NA = "N/A",
    No = "NO",
    Yes = "YES",
}

export enum TariffType {
    AdHocPayment = "AD_HOC_PAYMENT",
    ProfileCheap = "PROFILE_CHEAP",
    ProfileFast = "PROFILE_FAST",
    ProfileGreen = "PROFILE_GREEN",
    Regular = "REGULAR",
}

export interface Price {
    before_taxes: number;
    taxes?:       TaxAmount[] | null;
}

export interface TaxAmount {
    account_number?: null | string;
    amount:          number;
    name:            string;
    percentage?:     number | null;
}

export interface ChargingPreferences {
    departure_time?:    null | string;
    discharge_allowed?: boolean | null;
    energy_need?:       number | null;
    profile_type:       ProfileType;
}

export interface ChargingProfileResponse {
    result:  ChargingProfileResponseType;
    timeout: number;
}

export enum ChargingProfileResponseType {
    Accepted = "ACCEPTED",
    NotSupported = "NOT_SUPPORTED",
    Rejected = "REJECTED",
    TooOften = "TOO_OFTEN",
    UnknownSession = "UNKNOWN_SESSION",
}

export interface ChargingProfileResult {
    result: ChargingProfileResultType;
}

export interface ClearProfileResult {
    result: ChargingProfileResultType;
}

export interface CommandResponse {
    message?: DisplayText[] | null;
    result:   CommandResponseType;
    timeout:  number;
}

export enum CommandResponseType {
    Accepted = "ACCEPTED",
    NotSupported = "NOT_SUPPORTED",
    Rejected = "REJECTED",
    UnknownSession = "UNKNOWN_SESSION",
}

export interface CommandResult {
    message?: DisplayText[] | null;
    result:   CommandResultType;
}

export enum CommandResultType {
    Accepted = "ACCEPTED",
    CanceledReservation = "CANCELED_RESERVATION",
    EvseInoperative = "EVSE_INOPERATIVE",
    EvseOccupied = "EVSE_OCCUPIED",
    Failed = "FAILED",
    NotSupported = "NOT_SUPPORTED",
    Rejected = "REJECTED",
    Timeout = "TIMEOUT",
    UnknownReservation = "UNKNOWN_RESERVATION",
}

export interface Connector {
    capabilities?:         ConnectorCapability[] | null;
    format:                ConnectorFormat;
    id:                    string;
    last_updated:          string;
    max_amperage:          number;
    max_electric_power?:   number | null;
    max_voltage:           number;
    power_type:            PowerType;
    standard:              ConnectorType;
    tariff_ids?:           string[] | null;
    terms_and_conditions?: null | string;
}

export enum ConnectorCapability {
    ISO15118_20_PlugAndCharge = "ISO_15118_20_PLUG_AND_CHARGE",
    ISO15118_2_PlugAndCharge = "ISO_15118_2_PLUG_AND_CHARGE",
}

export interface Credentials {
    hub_party_id?: null | string;
    roles:         CredentialsRole[];
    token:         string;
    url:           string;
}

export interface CredentialsRole {
    business_details: BusinessDetails;
    country_code:     string;
    party_id:         string;
    role:             Role;
}

export interface BusinessDetails {
    logo?:    Image | null;
    name:     string;
    website?: null | string;
}

export interface Image {
    category:   ImageCategory;
    height?:    number | null;
    thumbnail?: null | string;
    type:       string;
    url:        string;
    width?:     number | null;
}

export enum ImageCategory {
    Charger = "CHARGER",
    Entrance = "ENTRANCE",
    Location = "LOCATION",
    Network = "NETWORK",
    Operator = "OPERATOR",
    Other = "OTHER",
    Owner = "OWNER",
}

export enum Role {
    Cpo = "CPO",
    Emsp = "EMSP",
    Nap = "NAP",
    Nsp = "NSP",
    Other = "OTHER",
    Scsp = "SCSP",
}

export interface Endpoint {
    identifier: ModuleID;
    role:       InterfaceRole;
    url:        string;
}

export enum ModuleID {
    Cdrs = "cdrs",
    Chargingprofiles = "chargingprofiles",
    Commands = "commands",
    Credentials = "credentials",
    Hubclientinfo = "hubclientinfo",
    Locations = "locations",
    Payments = "payments",
    Sessions = "sessions",
    Tariffs = "tariffs",
    Tokens = "tokens",
}

export enum InterfaceRole {
    Receiver = "RECEIVER",
    Sender = "SENDER",
}

export interface Evse {
    accepted_service_providers?: string[] | null;
    capabilities?:               Capability[] | null;
    connectors:                  Connector[];
    coordinates?:                GeoLocation | null;
    directions?:                 DisplayText[] | null;
    evse_id?:                    null | string;
    floor_level?:                null | string;
    images?:                     Image[] | null;
    last_updated:                string;
    parking?:                    EvseParking[] | null;
    parking_restrictions?:       ParkingRestriction[] | null;
    physical_reference?:         null | string;
    status:                      Status;
    status_schedule?:            StatusSchedule[] | null;
    uid:                         string;
}

export enum Capability {
    ChargingPreferencesCapable = "CHARGING_PREFERENCES_CAPABLE",
    ChargingProfileCapable = "CHARGING_PROFILE_CAPABLE",
    ChipCardSupport = "CHIP_CARD_SUPPORT",
    ContactlessCardSupport = "CONTACTLESS_CARD_SUPPORT",
    CreditCardPayable = "CREDIT_CARD_PAYABLE",
    DebitCardPayable = "DEBIT_CARD_PAYABLE",
    PedTerminal = "PED_TERMINAL",
    RFIDReader = "RFID_READER",
    RemoteStartStopCapable = "REMOTE_START_STOP_CAPABLE",
    Reservable = "RESERVABLE",
    StartSessionConnectorRequired = "START_SESSION_CONNECTOR_REQUIRED",
    TokenGroupCapable = "TOKEN_GROUP_CAPABLE",
    UnlockCapable = "UNLOCK_CAPABLE",
}

export interface EvseParking {
    evse_position?: EvsePosition | null;
    parking_id:     string;
}

export enum EvsePosition {
    Center = "CENTER",
    Left = "LEFT",
    Right = "RIGHT",
}

export enum ParkingRestriction {
    Customers = "CUSTOMERS",
    Disabled = "DISABLED",
    Employees = "EMPLOYEES",
    EvOnly = "EV_ONLY",
    Motorcycles = "MOTORCYCLES",
    Plugged = "PLUGGED",
    Taxis = "TAXIS",
    Tenants = "TENANTS",
}

export enum Status {
    Available = "AVAILABLE",
    Blocked = "BLOCKED",
    Charging = "CHARGING",
    Inoperative = "INOPERATIVE",
    Outoforder = "OUTOFORDER",
    Planned = "PLANNED",
    Removed = "REMOVED",
    Reserved = "RESERVED",
    Unknown = "UNKNOWN",
}

export interface StatusSchedule {
    period_begin: string;
    period_end?:  null | string;
    status:       Status;
}

export interface FinancialAdviceConfirmation {
    authorization_reference: string;
    capture_status_code:     CaptureStatusCode;
    capture_status_message?: null | string;
    currency:                string;
    eft_data:                string[];
    id:                      string;
    last_updated:            string;
    total_costs:             Price;
}

export enum CaptureStatusCode {
    Failed = "FAILED",
    PartialSuccess = "PARTIAL_SUCCESS",
    Success = "SUCCESS",
}

export interface HubClientInfo {
    country_code: string;
    last_updated: string;
    party_id:     string;
    role:         Role;
    status:       ConnectionStatus;
}

export enum ConnectionStatus {
    Connected = "CONNECTED",
    Offline = "OFFLINE",
    Planned = "PLANNED",
    Suspended = "SUSPENDED",
}

export interface Location {
    address:               string;
    charging_when_closed?: boolean | null;
    city:                  string;
    coordinates:           GeoLocation;
    country:               string;
    country_code:          string;
    directions?:           DisplayText[] | null;
    energy_mix?:           EnergyMix | null;
    evses?:                Evse[] | null;
    facilities?:           Facility[] | null;
    help_phone?:           null | string;
    id:                    string;
    images?:               Image[] | null;
    last_updated:          string;
    name?:                 null | string;
    opening_times?:        Hours | null;
    operator?:             BusinessDetails | null;
    owner?:                BusinessDetails | null;
    parking_places?:       Parking[] | null;
    parking_type?:         ParkingType | null;
    party_id:              string;
    postal_code?:          null | string;
    publish:               boolean;
    publish_allowed_to?:   PublishTokenType[] | null;
    related_locations?:    AdditionalGeoLocation[] | null;
    state?:                null | string;
    suboperator?:          BusinessDetails | null;
    time_zone:             string;
}

export enum Facility {
    Airport = "AIRPORT",
    BikeSharing = "BIKE_SHARING",
    BusStop = "BUS_STOP",
    Cafe = "CAFE",
    CarpoolParking = "CARPOOL_PARKING",
    FuelStation = "FUEL_STATION",
    Hotel = "HOTEL",
    Mall = "MALL",
    MetroStation = "METRO_STATION",
    Museum = "MUSEUM",
    Nature = "NATURE",
    ParkingLot = "PARKING_LOT",
    RecreationArea = "RECREATION_AREA",
    Restaurant = "RESTAURANT",
    Sport = "SPORT",
    Supermarket = "SUPERMARKET",
    TaxiStand = "TAXI_STAND",
    TrainStation = "TRAIN_STATION",
    TramStop = "TRAM_STOP",
    Wifi = "WIFI",
}

export interface Hours {
    exceptional_closings?: ExceptionalPeriod[] | null;
    exceptional_openings?: ExceptionalPeriod[] | null;
    regular_hours?:        RegularHours[] | null;
    twentyfourseven:       boolean;
}

export interface ExceptionalPeriod {
    period_begin: string;
    period_end:   string;
}

export interface RegularHours {
    period_begin: string;
    period_end:   string;
    weekday:      number;
}

export interface Parking {
    apds_reference?:          null | string;
    dangerous_goods_allowed?: boolean | null;
    direction?:               ParkingDirection | null;
    drive_through?:           boolean | null;
    id:                       string;
    images?:                  Image[] | null;
    lighting?:                boolean | null;
    max_vehicle_height?:      number | null;
    max_vehicle_length?:      number | null;
    max_vehicle_weight?:      number | null;
    max_vehicle_width?:       number | null;
    parking_space_length?:    number | null;
    parking_space_width?:     number | null;
    physical_reference?:      null | string;
    refrigeration_outlet?:    boolean | null;
    reservation_required:     boolean;
    restricted_to_type:       boolean;
    roofed?:                  boolean | null;
    standards?:               string[] | null;
    time_limit?:              number | null;
    vehicle_types:            VehicleType[];
}

export enum ParkingDirection {
    Angle = "ANGLE",
    Parallel = "PARALLEL",
    Perpendicular = "PERPENDICULAR",
}

export enum VehicleType {
    Bus = "BUS",
    Disabled = "DISABLED",
    Motorcycle = "MOTORCYCLE",
    PersonalVehicle = "PERSONAL_VEHICLE",
    PersonalVehicleWithTrailer = "PERSONAL_VEHICLE_WITH_TRAILER",
    Rigid = "RIGID",
    SemiTractor = "SEMI_TRACTOR",
    TruckWithTrailer = "TRUCK_WITH_TRAILER",
    Van = "VAN",
}

export enum ParkingType {
    AlongMotorway = "ALONG_MOTORWAY",
    OnDriveway = "ON_DRIVEWAY",
    OnStreet = "ON_STREET",
    ParkingGarage = "PARKING_GARAGE",
    ParkingLot = "PARKING_LOT",
    UndergroundGarage = "UNDERGROUND_GARAGE",
}

export interface PublishTokenType {
    group_id?:      null | string;
    issuer?:        null | string;
    type?:          TokenType | null;
    uid?:           null | string;
    visual_number?: null | string;
}

export interface AdditionalGeoLocation {
    latitude:  string;
    longitude: string;
    name?:     DisplayText | null;
}

export interface ReserveNow {
    authorization_reference?: null | string;
    evse_uid?:                null | string;
    expiry_date:              string;
    location_id:              string;
    reservation_id:           string;
    response_url:             string;
    token:                    Token;
}

export interface Session {
    auth_method:              AuthMethod;
    authorization_reference?: null | string;
    cdr_token:                CdrToken;
    charging_periods?:        ChargingPeriod[] | null;
    connector_id:             string;
    country_code:             string;
    currency:                 string;
    end_date_time?:           null | string;
    evse_uid:                 string;
    id:                       string;
    kwh:                      number;
    last_updated:             string;
    location_id:              string;
    meter_id?:                null | string;
    party_id:                 string;
    start_date_time:          string;
    status:                   SessionStatus;
    total_cost?:              Price | null;
}

export enum SessionStatus {
    Active = "ACTIVE",
    Completed = "COMPLETED",
    Invalid = "INVALID",
    Pending = "PENDING",
    Reservation = "RESERVATION",
}

export interface SetChargingProfile {
    charging_profile: ChargingProfile;
    response_url:     string;
}

export interface StartSession {
    authorization_reference?: null | string;
    connector_id?:            null | string;
    evse_uid?:                null | string;
    location_id:              string;
    response_url:             string;
    token:                    Token;
}

export interface StopSession {
    response_url: string;
    session_id:   string;
}

export interface Terminal {
    address?:            null | string;
    city?:               null | string;
    coordinates?:        GeoLocation | null;
    country?:            null | string;
    country_code?:       null | string;
    customer_reference?: null | string;
    evse_uids?:          string[] | null;
    invoice_base_url?:   null | string;
    invoice_creator?:    InvoiceCreator | null;
    last_updated:        string;
    location_ids?:       string[] | null;
    party_id?:           null | string;
    postal_code?:        null | string;
    reference?:          null | string;
    state?:              null | string;
    terminal_id:         string;
}

export enum InvoiceCreator {
    Cpo = "CPO",
    Ptp = "PTP",
}

export interface UnlockConnector {
    connector_id: string;
    evse_uid:     string;
    location_id:  string;
    response_url: string;
}

export interface Version {
    url:     string;
    version: VersionNumber;
}

export enum VersionNumber {
    The20 = "2.0",
    The21 = "2.1",
    The211 = "2.1.1",
    The22 = "2.2",
    The221 = "2.2.1",
    The230 = "2.3.0",
}

export interface VersionDetails {
    endpoints: Endpoint[];
    version:   VersionNumber;
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toV230Payments(json: string): V230Payments {
        return cast(JSON.parse(json), r("V230Payments"));
    }

    public static v230PaymentsToJson(value: V230Payments): string {
        return JSON.stringify(uncast(value, r("V230Payments")), null, 2);
    }
}

function invalidValue(typ: any, val: any, key: any, parent: any = ''): never {
    const prettyTyp = prettyTypeName(typ);
    const parentText = parent ? ` on ${parent}` : '';
    const keyText = key ? ` for key "${key}"` : '';
    throw Error(`Invalid value${keyText}${parentText}. Expected ${prettyTyp} but got ${JSON.stringify(val)}`);
}

function prettyTypeName(typ: any): string {
    if (Array.isArray(typ)) {
        if (typ.length === 2 && typ[0] === undefined) {
            return `an optional ${prettyTypeName(typ[1])}`;
        } else {
            return `one of [${typ.map(a => { return prettyTypeName(a); }).join(", ")}]`;
        }
    } else if (typeof typ === "object" && typ.literal !== undefined) {
        return typ.literal;
    } else {
        return typeof typ;
    }
}

function jsonToJSProps(typ: any): any {
    if (typ.jsonToJS === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.json] = { key: p.js, typ: p.typ });
        typ.jsonToJS = map;
    }
    return typ.jsonToJS;
}

function jsToJSONProps(typ: any): any {
    if (typ.jsToJSON === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.js] = { key: p.json, typ: p.typ });
        typ.jsToJSON = map;
    }
    return typ.jsToJSON;
}

function transform(val: any, typ: any, getProps: any, key: any = '', parent: any = ''): any {
    function transformPrimitive(typ: string, val: any): any {
        if (typeof typ === typeof val) return val;
        return invalidValue(typ, val, key, parent);
    }

    function transformUnion(typs: any[], val: any): any {
        // val must validate against one typ in typs
        const l = typs.length;
        for (let i = 0; i < l; i++) {
            const typ = typs[i];
            try {
                return transform(val, typ, getProps);
            } catch (_) {}
        }
        return invalidValue(typs, val, key, parent);
    }

    function transformEnum(cases: string[], val: any): any {
        if (cases.indexOf(val) !== -1) return val;
        return invalidValue(cases.map(a => { return l(a); }), val, key, parent);
    }

    function transformArray(typ: any, val: any): any {
        // val must be an array with no invalid elements
        if (!Array.isArray(val)) return invalidValue(l("array"), val, key, parent);
        return val.map(el => transform(el, typ, getProps));
    }

    function transformDate(val: any): any {
        if (val === null) {
            return null;
        }
        const d = new Date(val);
        if (isNaN(d.valueOf())) {
            return invalidValue(l("Date"), val, key, parent);
        }
        return d;
    }

    function transformObject(props: { [k: string]: any }, additional: any, val: any): any {
        if (val === null || typeof val !== "object" || Array.isArray(val)) {
            return invalidValue(l(ref || "object"), val, key, parent);
        }
        const result: any = {};
        Object.getOwnPropertyNames(props).forEach(key => {
            const prop = props[key];
            const v = Object.prototype.hasOwnProperty.call(val, key) ? val[key] : undefined;
            result[prop.key] = transform(v, prop.typ, getProps, key, ref);
        });
        Object.getOwnPropertyNames(val).forEach(key => {
            if (!Object.prototype.hasOwnProperty.call(props, key)) {
                result[key] = transform(val[key], additional, getProps, key, ref);
            }
        });
        return result;
    }

    if (typ === "any") return val;
    if (typ === null) {
        if (val === null) return val;
        return invalidValue(typ, val, key, parent);
    }
    if (typ === false) return invalidValue(typ, val, key, parent);
    let ref: any = undefined;
    while (typeof typ === "object" && typ.ref !== undefined) {
        ref = typ.ref;
        typ = typeMap[typ.ref];
    }
    if (Array.isArray(typ)) return transformEnum(typ, val);
    if (typeof typ === "object") {
        return typ.hasOwnProperty("unionMembers") ? transformUnion(typ.unionMembers, val)
            : typ.hasOwnProperty("arrayItems")    ? transformArray(typ.arrayItems, val)
            : typ.hasOwnProperty("props")         ? transformObject(getProps(typ), typ.additional, val)
            : invalidValue(typ, val, key, parent);
    }
    // Numbers can be parsed by Date but shouldn't be.
    if (typ === Date && typeof val !== "number") return transformDate(val);
    return transformPrimitive(typ, val);
}

function cast<T>(val: any, typ: any): T {
    return transform(val, typ, jsonToJSProps);
}

function uncast<T>(val: T, typ: any): any {
    return transform(val, typ, jsToJSONProps);
}

function l(typ: any) {
    return { literal: typ };
}

function a(typ: any) {
    return { arrayItems: typ };
}

function u(...typs: any[]) {
    return { unionMembers: typs };
}

function o(props: any[], additional: any) {
    return { props, additional };
}

function m(additional: any) {
    return { props: [], additional };
}

function r(name: string) {
    return { ref: name };
}

const typeMap: any = {
    "V230Payments": o([
        { json: "active_charging_profile", js: "active_charging_profile", typ: u(undefined, r("ActiveChargingProfile")) },
        { json: "active_charging_profile_result", js: "active_charging_profile_result", typ: u(undefined, r("ActiveChargingProfileResult")) },
        { json: "authorization_info", js: "authorization_info", typ: u(undefined, r("AuthorizationInfo")) },
        { json: "cancel_reservation", js: "cancel_reservation", typ: u(undefined, r("CancelReservation")) },
        { json: "cdr", js: "cdr", typ: u(undefined, r("Cdr")) },
        { json: "charging_preferences", js: "charging_preferences", typ: u(undefined, r("ChargingPreferences")) },
        { json: "charging_profile", js: "charging_profile", typ: u(undefined, r("ChargingProfile")) },
        { json: "charging_profile_response", js: "charging_profile_response", typ: u(undefined, r("ChargingProfileResponse")) },
        { json: "charging_profile_result", js: "charging_profile_result", typ: u(undefined, r("ChargingProfileResult")) },
        { json: "clear_profile_result", js: "clear_profile_result", typ: u(undefined, r("ClearProfileResult")) },
        { json: "command_response", js: "command_response", typ: u(undefined, r("CommandResponse")) },
        { json: "command_result", js: "command_result", typ: u(undefined, r("CommandResult")) },
        { json: "connector", js: "connector", typ: u(undefined, r("Connector")) },
        { json: "credentials", js: "credentials", typ: u(undefined, r("Credentials")) },
        { json: "endpoint", js: "endpoint", typ: u(undefined, r("Endpoint")) },
        { json: "evse", js: "evse", typ: u(undefined, r("Evse")) },
        { json: "financial_advice_confirmation", js: "financial_advice_confirmation", typ: u(undefined, r("FinancialAdviceConfirmation")) },
        { json: "hub_client_info", js: "hub_client_info", typ: u(undefined, r("HubClientInfo")) },
        { json: "location", js: "location", typ: u(undefined, r("Location")) },
        { json: "location_references", js: "location_references", typ: u(undefined, r("LocationReferences")) },
        { json: "reserve_now", js: "reserve_now", typ: u(undefined, r("ReserveNow")) },
        { json: "session", js: "session", typ: u(undefined, r("Session")) },
        { json: "set_charging_profile", js: "set_charging_profile", typ: u(undefined, r("SetChargingProfile")) },
        { json: "start_session", js: "start_session", typ: u(undefined, r("StartSession")) },
        { json: "stop_session", js: "stop_session", typ: u(undefined, r("StopSession")) },
        { json: "tariff", js: "tariff", typ: u(undefined, r("Tariff")) },
        { json: "terminal", js: "terminal", typ: u(undefined, r("Terminal")) },
        { json: "token", js: "token", typ: u(undefined, r("Token")) },
        { json: "unlock_connector", js: "unlock_connector", typ: u(undefined, r("UnlockConnector")) },
        { json: "version", js: "version", typ: u(undefined, r("Version")) },
        { json: "version_details", js: "version_details", typ: u(undefined, r("VersionDetails")) },
    ], "any"),
    "ActiveChargingProfile": o([
        { json: "charging_profile", js: "charging_profile", typ: r("ChargingProfile") },
        { json: "start_date_time", js: "start_date_time", typ: "" },
    ], false),
    "ChargingProfile": o([
        { json: "charging_profile_period", js: "charging_profile_period", typ: u(undefined, u(a(r("ChargingProfilePeriod")), null)) },
        { json: "charging_rate_unit", js: "charging_rate_unit", typ: r("ChargingRateUnit") },
        { json: "duration", js: "duration", typ: u(undefined, u(0, null)) },
        { json: "min_charging_rate", js: "min_charging_rate", typ: u(undefined, u(3.14, null)) },
        { json: "start_date_time", js: "start_date_time", typ: u(undefined, u(null, "")) },
    ], false),
    "ChargingProfilePeriod": o([
        { json: "limit", js: "limit", typ: 3.14 },
        { json: "start_period", js: "start_period", typ: 0 },
    ], false),
    "ActiveChargingProfileResult": o([
        { json: "profile", js: "profile", typ: u(undefined, u(r("ActiveChargingProfile"), null)) },
        { json: "result", js: "result", typ: r("ChargingProfileResultType") },
    ], false),
    "AuthorizationInfo": o([
        { json: "allowed", js: "allowed", typ: r("AllowedType") },
        { json: "authorization_reference", js: "authorization_reference", typ: u(undefined, u(null, "")) },
        { json: "info", js: "info", typ: u(undefined, u(r("DisplayText"), null)) },
        { json: "location", js: "location", typ: u(undefined, u(r("LocationReferences"), null)) },
        { json: "token", js: "token", typ: r("Token") },
    ], false),
    "DisplayText": o([
        { json: "language", js: "language", typ: "" },
        { json: "text", js: "text", typ: "" },
    ], false),
    "LocationReferences": o([
        { json: "evse_uids", js: "evse_uids", typ: u(undefined, u(a(""), null)) },
        { json: "location_id", js: "location_id", typ: "" },
    ], false),
    "Token": o([
        { json: "contract_id", js: "contract_id", typ: "" },
        { json: "country_code", js: "country_code", typ: "" },
        { json: "default_profile_type", js: "default_profile_type", typ: u(undefined, u(r("ProfileType"), null)) },
        { json: "energy_contract", js: "energy_contract", typ: u(undefined, u(r("EnergyContract"), null)) },
        { json: "group_id", js: "group_id", typ: u(undefined, u(null, "")) },
        { json: "issuer", js: "issuer", typ: "" },
        { json: "language", js: "language", typ: u(undefined, u(null, "")) },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "type", js: "type", typ: r("TokenType") },
        { json: "uid", js: "uid", typ: "" },
        { json: "valid", js: "valid", typ: true },
        { json: "visual_number", js: "visual_number", typ: u(undefined, u(null, "")) },
        { json: "whitelist", js: "whitelist", typ: r("WhitelistType") },
    ], false),
    "EnergyContract": o([
        { json: "contract_id", js: "contract_id", typ: u(undefined, u(null, "")) },
        { json: "supplier_name", js: "supplier_name", typ: "" },
    ], false),
    "CancelReservation": o([
        { json: "reservation_id", js: "reservation_id", typ: "" },
        { json: "response_url", js: "response_url", typ: "" },
    ], false),
    "Cdr": o([
        { json: "auth_method", js: "auth_method", typ: r("AuthMethod") },
        { json: "authorization_reference", js: "authorization_reference", typ: u(undefined, u(null, "")) },
        { json: "cdr_location", js: "cdr_location", typ: r("CdrLocation") },
        { json: "cdr_token", js: "cdr_token", typ: r("CdrToken") },
        { json: "charging_periods", js: "charging_periods", typ: a(r("ChargingPeriod")) },
        { json: "country_code", js: "country_code", typ: "" },
        { json: "credit", js: "credit", typ: u(undefined, u(true, null)) },
        { json: "credit_reference_id", js: "credit_reference_id", typ: u(undefined, u(null, "")) },
        { json: "currency", js: "currency", typ: "" },
        { json: "end_date_time", js: "end_date_time", typ: "" },
        { json: "home_charging_compensation", js: "home_charging_compensation", typ: u(undefined, u(true, null)) },
        { json: "id", js: "id", typ: "" },
        { json: "invoice_reference_id", js: "invoice_reference_id", typ: u(undefined, u(null, "")) },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "meter_id", js: "meter_id", typ: u(undefined, u(null, "")) },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "remark", js: "remark", typ: u(undefined, u(null, "")) },
        { json: "session_id", js: "session_id", typ: u(undefined, u(null, "")) },
        { json: "signed_data", js: "signed_data", typ: u(undefined, u(r("SignedData"), null)) },
        { json: "start_date_time", js: "start_date_time", typ: "" },
        { json: "tariffs", js: "tariffs", typ: u(undefined, u(a(r("Tariff")), null)) },
        { json: "total_cost", js: "total_cost", typ: r("Price") },
        { json: "total_energy", js: "total_energy", typ: 3.14 },
        { json: "total_energy_cost", js: "total_energy_cost", typ: u(undefined, u(r("Price"), null)) },
        { json: "total_fixed_cost", js: "total_fixed_cost", typ: u(undefined, u(r("Price"), null)) },
        { json: "total_parking_cost", js: "total_parking_cost", typ: u(undefined, u(r("Price"), null)) },
        { json: "total_parking_time", js: "total_parking_time", typ: u(undefined, u(3.14, null)) },
        { json: "total_reservation_cost", js: "total_reservation_cost", typ: u(undefined, u(r("Price"), null)) },
        { json: "total_time", js: "total_time", typ: 3.14 },
        { json: "total_time_cost", js: "total_time_cost", typ: u(undefined, u(r("Price"), null)) },
    ], false),
    "CdrLocation": o([
        { json: "address", js: "address", typ: "" },
        { json: "city", js: "city", typ: "" },
        { json: "connector_format", js: "connector_format", typ: r("ConnectorFormat") },
        { json: "connector_id", js: "connector_id", typ: "" },
        { json: "connector_power_type", js: "connector_power_type", typ: r("PowerType") },
        { json: "connector_standard", js: "connector_standard", typ: r("ConnectorType") },
        { json: "coordinates", js: "coordinates", typ: r("GeoLocation") },
        { json: "country", js: "country", typ: "" },
        { json: "evse_id", js: "evse_id", typ: "" },
        { json: "evse_uid", js: "evse_uid", typ: "" },
        { json: "id", js: "id", typ: "" },
        { json: "name", js: "name", typ: u(undefined, u(null, "")) },
        { json: "postal_code", js: "postal_code", typ: u(undefined, u(null, "")) },
        { json: "state", js: "state", typ: u(undefined, u(null, "")) },
    ], false),
    "GeoLocation": o([
        { json: "latitude", js: "latitude", typ: "" },
        { json: "longitude", js: "longitude", typ: "" },
    ], false),
    "CdrToken": o([
        { json: "contract_id", js: "contract_id", typ: "" },
        { json: "country_code", js: "country_code", typ: "" },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "type", js: "type", typ: r("TokenType") },
        { json: "uid", js: "uid", typ: "" },
    ], false),
    "ChargingPeriod": o([
        { json: "dimensions", js: "dimensions", typ: a(r("CdrDimension")) },
        { json: "start_date_time", js: "start_date_time", typ: "" },
        { json: "tariff_id", js: "tariff_id", typ: u(undefined, u(null, "")) },
    ], false),
    "CdrDimension": o([
        { json: "type", js: "type", typ: r("CdrDimensionType") },
        { json: "volume", js: "volume", typ: 3.14 },
    ], false),
    "SignedData": o([
        { json: "encoding_method", js: "encoding_method", typ: "" },
        { json: "encoding_method_version", js: "encoding_method_version", typ: u(undefined, u(0, null)) },
        { json: "public_key", js: "public_key", typ: u(undefined, u(null, "")) },
        { json: "signed_values", js: "signed_values", typ: a(r("SignedValue")) },
        { json: "url", js: "url", typ: u(undefined, u(null, "")) },
    ], false),
    "SignedValue": o([
        { json: "nature", js: "nature", typ: "" },
        { json: "plain_data", js: "plain_data", typ: "" },
        { json: "signed_data", js: "signed_data", typ: "" },
    ], false),
    "Tariff": o([
        { json: "country_code", js: "country_code", typ: "" },
        { json: "currency", js: "currency", typ: "" },
        { json: "elements", js: "elements", typ: a(r("TariffElement")) },
        { json: "end_date_time", js: "end_date_time", typ: u(undefined, u(null, "")) },
        { json: "energy_mix", js: "energy_mix", typ: u(undefined, u(r("EnergyMix"), null)) },
        { json: "id", js: "id", typ: "" },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "max_price", js: "max_price", typ: u(undefined, u(r("PriceLimit"), null)) },
        { json: "min_price", js: "min_price", typ: u(undefined, u(r("PriceLimit"), null)) },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "preauthorize_amount", js: "preauthorize_amount", typ: u(undefined, u(3.14, null)) },
        { json: "start_date_time", js: "start_date_time", typ: u(undefined, u(null, "")) },
        { json: "tariff_alt_text", js: "tariff_alt_text", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "tariff_alt_url", js: "tariff_alt_url", typ: u(undefined, u(null, "")) },
        { json: "tax_included", js: "tax_included", typ: r("TaxIncluded") },
        { json: "type", js: "type", typ: u(undefined, u(r("TariffType"), null)) },
    ], false),
    "TariffElement": o([
        { json: "price_components", js: "price_components", typ: a(r("PriceComponent")) },
        { json: "restrictions", js: "restrictions", typ: u(undefined, u(r("TariffRestrictions"), null)) },
    ], false),
    "PriceComponent": o([
        { json: "price", js: "price", typ: 3.14 },
        { json: "step_size", js: "step_size", typ: 0 },
        { json: "type", js: "type", typ: r("TariffDimensionType") },
        { json: "vat", js: "vat", typ: u(undefined, u(3.14, null)) },
    ], false),
    "TariffRestrictions": o([
        { json: "day_of_week", js: "day_of_week", typ: u(undefined, u(a(r("DayOfWeek")), null)) },
        { json: "end_date", js: "end_date", typ: u(undefined, u(null, "")) },
        { json: "end_time", js: "end_time", typ: u(undefined, u(null, "")) },
        { json: "max_current", js: "max_current", typ: u(undefined, u(3.14, null)) },
        { json: "max_duration", js: "max_duration", typ: u(undefined, u(0, null)) },
        { json: "max_kwh", js: "max_kwh", typ: u(undefined, u(3.14, null)) },
        { json: "max_power", js: "max_power", typ: u(undefined, u(3.14, null)) },
        { json: "min_current", js: "min_current", typ: u(undefined, u(3.14, null)) },
        { json: "min_duration", js: "min_duration", typ: u(undefined, u(0, null)) },
        { json: "min_kwh", js: "min_kwh", typ: u(undefined, u(3.14, null)) },
        { json: "min_power", js: "min_power", typ: u(undefined, u(3.14, null)) },
        { json: "reservation", js: "reservation", typ: u(undefined, u(r("ReservationRestrictionType"), null)) },
        { json: "start_date", js: "start_date", typ: u(undefined, u(null, "")) },
        { json: "start_time", js: "start_time", typ: u(undefined, u(null, "")) },
    ], false),
    "EnergyMix": o([
        { json: "energy_product_name", js: "energy_product_name", typ: u(undefined, u(null, "")) },
        { json: "energy_sources", js: "energy_sources", typ: u(undefined, u(a(r("EnergySource")), null)) },
        { json: "environ_impact", js: "environ_impact", typ: u(undefined, u(a(r("EnvironmentalImpact")), null)) },
        { json: "is_green_energy", js: "is_green_energy", typ: true },
        { json: "supplier_name", js: "supplier_name", typ: u(undefined, u(null, "")) },
    ], false),
    "EnergySource": o([
        { json: "percentage", js: "percentage", typ: 3.14 },
        { json: "source", js: "source", typ: r("EnergySourceCategory") },
    ], false),
    "EnvironmentalImpact": o([
        { json: "amount", js: "amount", typ: 3.14 },
        { json: "category", js: "category", typ: r("EnvironmentalImpactCategory") },
    ], false),
    "PriceLimit": o([
        { json: "after_taxes", js: "after_taxes", typ: u(undefined, u(3.14, null)) },
        { json: "before_taxes", js: "before_taxes", typ: 3.14 },
    ], false),
    "Price": o([
        { json: "before_taxes", js: "before_taxes", typ: 3.14 },
        { json: "taxes", js: "taxes", typ: u(undefined, u(a(r("TaxAmount")), null)) },
    ], false),
    "TaxAmount": o([
        { json: "account_number", js: "account_number", typ: u(undefined, u(null, "")) },
        { json: "amount", js: "amount", typ: 3.14 },
        { json: "name", js: "name", typ: "" },
        { json: "percentage", js: "percentage", typ: u(undefined, u(3.14, null)) },
    ], false),
    "ChargingPreferences": o([
        { json: "departure_time", js: "departure_time", typ: u(undefined, u(null, "")) },
        { json: "discharge_allowed", js: "discharge_allowed", typ: u(undefined, u(true, null)) },
        { json: "energy_need", js: "energy_need", typ: u(undefined, u(3.14, null)) },
        { json: "profile_type", js: "profile_type", typ: r("ProfileType") },
    ], false),
    "ChargingProfileResponse": o([
        { json: "result", js: "result", typ: r("ChargingProfileResponseType") },
        { json: "timeout", js: "timeout", typ: 0 },
    ], false),
    "ChargingProfileResult": o([
        { json: "result", js: "result", typ: r("ChargingProfileResultType") },
    ], false),
    "ClearProfileResult": o([
        { json: "result", js: "result", typ: r("ChargingProfileResultType") },
    ], false),
    "CommandResponse": o([
        { json: "message", js: "message", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "result", js: "result", typ: r("CommandResponseType") },
        { json: "timeout", js: "timeout", typ: 0 },
    ], false),
    "CommandResult": o([
        { json: "message", js: "message", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "result", js: "result", typ: r("CommandResultType") },
    ], false),
    "Connector": o([
        { json: "capabilities", js: "capabilities", typ: u(undefined, u(a(r("ConnectorCapability")), null)) },
        { json: "format", js: "format", typ: r("ConnectorFormat") },
        { json: "id", js: "id", typ: "" },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "max_amperage", js: "max_amperage", typ: 0 },
        { json: "max_electric_power", js: "max_electric_power", typ: u(undefined, u(0, null)) },
        { json: "max_voltage", js: "max_voltage", typ: 0 },
        { json: "power_type", js: "power_type", typ: r("PowerType") },
        { json: "standard", js: "standard", typ: r("ConnectorType") },
        { json: "tariff_ids", js: "tariff_ids", typ: u(undefined, u(a(""), null)) },
        { json: "terms_and_conditions", js: "terms_and_conditions", typ: u(undefined, u(null, "")) },
    ], false),
    "Credentials": o([
        { json: "hub_party_id", js: "hub_party_id", typ: u(undefined, u(null, "")) },
        { json: "roles", js: "roles", typ: a(r("CredentialsRole")) },
        { json: "token", js: "token", typ: "" },
        { json: "url", js: "url", typ: "" },
    ], false),
    "CredentialsRole": o([
        { json: "business_details", js: "business_details", typ: r("BusinessDetails") },
        { json: "country_code", js: "country_code", typ: "" },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "role", js: "role", typ: r("Role") },
    ], false),
    "BusinessDetails": o([
        { json: "logo", js: "logo", typ: u(undefined, u(r("Image"), null)) },
        { json: "name", js: "name", typ: "" },
        { json: "website", js: "website", typ: u(undefined, u(null, "")) },
    ], false),
    "Image": o([
        { json: "category", js: "category", typ: r("ImageCategory") },
        { json: "height", js: "height", typ: u(undefined, u(0, null)) },
        { json: "thumbnail", js: "thumbnail", typ: u(undefined, u(null, "")) },
        { json: "type", js: "type", typ: "" },
        { json: "url", js: "url", typ: "" },
        { json: "width", js: "width", typ: u(undefined, u(0, null)) },
    ], false),
    "Endpoint": o([
        { json: "identifier", js: "identifier", typ: r("ModuleID") },
        { json: "role", js: "role", typ: r("InterfaceRole") },
        { json: "url", js: "url", typ: "" },
    ], false),
    "Evse": o([
        { json: "accepted_service_providers", js: "accepted_service_providers", typ: u(undefined, u(a(""), null)) },
        { json: "capabilities", js: "capabilities", typ: u(undefined, u(a(r("Capability")), null)) },
        { json: "connectors", js: "connectors", typ: a(r("Connector")) },
        { json: "coordinates", js: "coordinates", typ: u(undefined, u(r("GeoLocation"), null)) },
        { json: "directions", js: "directions", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "evse_id", js: "evse_id", typ: u(undefined, u(null, "")) },
        { json: "floor_level", js: "floor_level", typ: u(undefined, u(null, "")) },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "parking", js: "parking", typ: u(undefined, u(a(r("EvseParking")), null)) },
        { json: "parking_restrictions", js: "parking_restrictions", typ: u(undefined, u(a(r("ParkingRestriction")), null)) },
        { json: "physical_reference", js: "physical_reference", typ: u(undefined, u(null, "")) },
        { json: "status", js: "status", typ: r("Status") },
        { json: "status_schedule", js: "status_schedule", typ: u(undefined, u(a(r("StatusSchedule")), null)) },
        { json: "uid", js: "uid", typ: "" },
    ], false),
    "EvseParking": o([
        { json: "evse_position", js: "evse_position", typ: u(undefined, u(r("EvsePosition"), null)) },
        { json: "parking_id", js: "parking_id", typ: "" },
    ], false),
    "StatusSchedule": o([
        { json: "period_begin", js: "period_begin", typ: "" },
        { json: "period_end", js: "period_end", typ: u(undefined, u(null, "")) },
        { json: "status", js: "status", typ: r("Status") },
    ], false),
    "FinancialAdviceConfirmation": o([
        { json: "authorization_reference", js: "authorization_reference", typ: "" },
        { json: "capture_status_code", js: "capture_status_code", typ: r("CaptureStatusCode") },
        { json: "capture_status_message", js: "capture_status_message", typ: u(undefined, u(null, "")) },
        { json: "currency", js: "currency", typ: "" },
        { json: "eft_data", js: "eft_data", typ: a("") },
        { json: "id", js: "id", typ: "" },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "total_costs", js: "total_costs", typ: r("Price") },
    ], false),
    "HubClientInfo": o([
        { json: "country_code", js: "country_code", typ: "" },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "role", js: "role", typ: r("Role") },
        { json: "status", js: "status", typ: r("ConnectionStatus") },
    ], false),
    "Location": o([
        { json: "address", js: "address", typ: "" },
        { json: "charging_when_closed", js: "charging_when_closed", typ: u(undefined, u(true, null)) },
        { json: "city", js: "city", typ: "" },
        { json: "coordinates", js: "coordinates", typ: r("GeoLocation") },
        { json: "country", js: "country", typ: "" },
        { json: "country_code", js: "country_code", typ: "" },
        { json: "directions", js: "directions", typ: u(undefined, u(a(r("DisplayText")), null)) },
        { json: "energy_mix", js: "energy_mix", typ: u(undefined, u(r("EnergyMix"), null)) },
        { json: "evses", js: "evses", typ: u(undefined, u(a(r("Evse")), null)) },
        { json: "facilities", js: "facilities", typ: u(undefined, u(a(r("Facility")), null)) },
        { json: "help_phone", js: "help_phone", typ: u(undefined, u(null, "")) },
        { json: "id", js: "id", typ: "" },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "name", js: "name", typ: u(undefined, u(null, "")) },
        { json: "opening_times", js: "opening_times", typ: u(undefined, u(r("Hours"), null)) },
        { json: "operator", js: "operator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "owner", js: "owner", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "parking_places", js: "parking_places", typ: u(undefined, u(a(r("Parking")), null)) },
        { json: "parking_type", js: "parking_type", typ: u(undefined, u(r("ParkingType"), null)) },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "postal_code", js: "postal_code", typ: u(undefined, u(null, "")) },
        { json: "publish", js: "publish", typ: true },
        { json: "publish_allowed_to", js: "publish_allowed_to", typ: u(undefined, u(a(r("PublishTokenType")), null)) },
        { json: "related_locations", js: "related_locations", typ: u(undefined, u(a(r("AdditionalGeoLocation")), null)) },
        { json: "state", js: "state", typ: u(undefined, u(null, "")) },
        { json: "suboperator", js: "suboperator", typ: u(undefined, u(r("BusinessDetails"), null)) },
        { json: "time_zone", js: "time_zone", typ: "" },
    ], false),
    "Hours": o([
        { json: "exceptional_closings", js: "exceptional_closings", typ: u(undefined, u(a(r("ExceptionalPeriod")), null)) },
        { json: "exceptional_openings", js: "exceptional_openings", typ: u(undefined, u(a(r("ExceptionalPeriod")), null)) },
        { json: "regular_hours", js: "regular_hours", typ: u(undefined, u(a(r("RegularHours")), null)) },
        { json: "twentyfourseven", js: "twentyfourseven", typ: true },
    ], false),
    "ExceptionalPeriod": o([
        { json: "period_begin", js: "period_begin", typ: "" },
        { json: "period_end", js: "period_end", typ: "" },
    ], false),
    "RegularHours": o([
        { json: "period_begin", js: "period_begin", typ: "" },
        { json: "period_end", js: "period_end", typ: "" },
        { json: "weekday", js: "weekday", typ: 0 },
    ], false),
    "Parking": o([
        { json: "apds_reference", js: "apds_reference", typ: u(undefined, u(null, "")) },
        { json: "dangerous_goods_allowed", js: "dangerous_goods_allowed", typ: u(undefined, u(true, null)) },
        { json: "direction", js: "direction", typ: u(undefined, u(r("ParkingDirection"), null)) },
        { json: "drive_through", js: "drive_through", typ: u(undefined, u(true, null)) },
        { json: "id", js: "id", typ: "" },
        { json: "images", js: "images", typ: u(undefined, u(a(r("Image")), null)) },
        { json: "lighting", js: "lighting", typ: u(undefined, u(true, null)) },
        { json: "max_vehicle_height", js: "max_vehicle_height", typ: u(undefined, u(3.14, null)) },
        { json: "max_vehicle_length", js: "max_vehicle_length", typ: u(undefined, u(3.14, null)) },
        { json: "max_vehicle_weight", js: "max_vehicle_weight", typ: u(undefined, u(3.14, null)) },
        { json: "max_vehicle_width", js: "max_vehicle_width", typ: u(undefined, u(3.14, null)) },
        { json: "parking_space_length", js: "parking_space_length", typ: u(undefined, u(3.14, null)) },
        { json: "parking_space_width", js: "parking_space_width", typ: u(undefined, u(3.14, null)) },
        { json: "physical_reference", js: "physical_reference", typ: u(undefined, u(null, "")) },
        { json: "refrigeration_outlet", js: "refrigeration_outlet", typ: u(undefined, u(true, null)) },
        { json: "reservation_required", js: "reservation_required", typ: true },
        { json: "restricted_to_type", js: "restricted_to_type", typ: true },
        { json: "roofed", js: "roofed", typ: u(undefined, u(true, null)) },
        { json: "standards", js: "standards", typ: u(undefined, u(a(""), null)) },
        { json: "time_limit", js: "time_limit", typ: u(undefined, u(3.14, null)) },
        { json: "vehicle_types", js: "vehicle_types", typ: a(r("VehicleType")) },
    ], false),
    "PublishTokenType": o([
        { json: "group_id", js: "group_id", typ: u(undefined, u(null, "")) },
        { json: "issuer", js: "issuer", typ: u(undefined, u(null, "")) },
        { json: "type", js: "type", typ: u(undefined, u(r("TokenType"), null)) },
        { json: "uid", js: "uid", typ: u(undefined, u(null, "")) },
        { json: "visual_number", js: "visual_number", typ: u(undefined, u(null, "")) },
    ], false),
    "AdditionalGeoLocation": o([
        { json: "latitude", js: "latitude", typ: "" },
        { json: "longitude", js: "longitude", typ: "" },
        { json: "name", js: "name", typ: u(undefined, u(r("DisplayText"), null)) },
    ], false),
    "ReserveNow": o([
        { json: "authorization_reference", js: "authorization_reference", typ: u(undefined, u(null, "")) },
        { json: "evse_uid", js: "evse_uid", typ: u(undefined, u(null, "")) },
        { json: "expiry_date", js: "expiry_date", typ: "" },
        { json: "location_id", js: "location_id", typ: "" },
        { json: "reservation_id", js: "reservation_id", typ: "" },
        { json: "response_url", js: "response_url", typ: "" },
        { json: "token", js: "token", typ: r("Token") },
    ], false),
    "Session": o([
        { json: "auth_method", js: "auth_method", typ: r("AuthMethod") },
        { json: "authorization_reference", js: "authorization_reference", typ: u(undefined, u(null, "")) },
        { json: "cdr_token", js: "cdr_token", typ: r("CdrToken") },
        { json: "charging_periods", js: "charging_periods", typ: u(undefined, u(a(r("ChargingPeriod")), null)) },
        { json: "connector_id", js: "connector_id", typ: "" },
        { json: "country_code", js: "country_code", typ: "" },
        { json: "currency", js: "currency", typ: "" },
        { json: "end_date_time", js: "end_date_time", typ: u(undefined, u(null, "")) },
        { json: "evse_uid", js: "evse_uid", typ: "" },
        { json: "id", js: "id", typ: "" },
        { json: "kwh", js: "kwh", typ: 3.14 },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "location_id", js: "location_id", typ: "" },
        { json: "meter_id", js: "meter_id", typ: u(undefined, u(null, "")) },
        { json: "party_id", js: "party_id", typ: "" },
        { json: "start_date_time", js: "start_date_time", typ: "" },
        { json: "status", js: "status", typ: r("SessionStatus") },
        { json: "total_cost", js: "total_cost", typ: u(undefined, u(r("Price"), null)) },
    ], false),
    "SetChargingProfile": o([
        { json: "charging_profile", js: "charging_profile", typ: r("ChargingProfile") },
        { json: "response_url", js: "response_url", typ: "" },
    ], false),
    "StartSession": o([
        { json: "authorization_reference", js: "authorization_reference", typ: u(undefined, u(null, "")) },
        { json: "connector_id", js: "connector_id", typ: u(undefined, u(null, "")) },
        { json: "evse_uid", js: "evse_uid", typ: u(undefined, u(null, "")) },
        { json: "location_id", js: "location_id", typ: "" },
        { json: "response_url", js: "response_url", typ: "" },
        { json: "token", js: "token", typ: r("Token") },
    ], false),
    "StopSession": o([
        { json: "response_url", js: "response_url", typ: "" },
        { json: "session_id", js: "session_id", typ: "" },
    ], false),
    "Terminal": o([
        { json: "address", js: "address", typ: u(undefined, u(null, "")) },
        { json: "city", js: "city", typ: u(undefined, u(null, "")) },
        { json: "coordinates", js: "coordinates", typ: u(undefined, u(r("GeoLocation"), null)) },
        { json: "country", js: "country", typ: u(undefined, u(null, "")) },
        { json: "country_code", js: "country_code", typ: u(undefined, u(null, "")) },
        { json: "customer_reference", js: "customer_reference", typ: u(undefined, u(null, "")) },
        { json: "evse_uids", js: "evse_uids", typ: u(undefined, u(a(""), null)) },
        { json: "invoice_base_url", js: "invoice_base_url", typ: u(undefined, u(null, "")) },
        { json: "invoice_creator", js: "invoice_creator", typ: u(undefined, u(r("InvoiceCreator"), null)) },
        { json: "last_updated", js: "last_updated", typ: "" },
        { json: "location_ids", js: "location_ids", typ: u(undefined, u(a(""), null)) },
        { json: "party_id", js: "party_id", typ: u(undefined, u(null, "")) },
        { json: "postal_code", js: "postal_code", typ: u(undefined, u(null, "")) },
        { json: "reference", js: "reference", typ: u(undefined, u(null, "")) },
        { json: "state", js: "state", typ: u(undefined, u(null, "")) },
        { json: "terminal_id", js: "terminal_id", typ: "" },
    ], false),
    "UnlockConnector": o([
        { json: "connector_id", js: "connector_id", typ: "" },
        { json: "evse_uid", js: "evse_uid", typ: "" },
        { json: "location_id", js: "location_id", typ: "" },
        { json: "response_url", js: "response_url", typ: "" },
    ], false),
    "Version": o([
        { json: "url", js: "url", typ: "" },
        { json: "version", js: "version", typ: r("VersionNumber") },
    ], false),
    "VersionDetails": o([
        { json: "endpoints", js: "endpoints", typ: a(r("Endpoint")) },
        { json: "version", js: "version", typ: r("VersionNumber") },
    ], false),
    "ChargingRateUnit": [
        "A",
        "W",
    ],
    "ChargingProfileResultType": [
        "ACCEPTED",
        "REJECTED",
        "UNKNOWN",
    ],
    "AllowedType": [
        "ALLOWED",
        "BLOCKED",
        "EXPIRED",
        "NO_CREDIT",
        "NOT_ALLOWED",
    ],
    "ProfileType": [
        "CHEAP",
        "FAST",
        "GREEN",
        "REGULAR",
    ],
    "TokenType": [
        "AD_HOC_USER",
        "APP_USER",
        "EMAID",
        "OTHER",
        "RFID",
    ],
    "WhitelistType": [
        "ALLOWED",
        "ALLOWED_OFFLINE",
        "ALWAYS",
        "NEVER",
    ],
    "AuthMethod": [
        "AUTH_REQUEST",
        "COMMAND",
        "WHITELIST",
    ],
    "ConnectorFormat": [
        "CABLE",
        "SOCKET",
    ],
    "PowerType": [
        "AC_1_PHASE",
        "AC_2_PHASE",
        "AC_2_PHASE_SPLIT",
        "AC_3_PHASE",
        "DC",
    ],
    "ConnectorType": [
        "CHADEMO",
        "CHAOJI",
        "DOMESTIC_A",
        "DOMESTIC_B",
        "DOMESTIC_C",
        "DOMESTIC_D",
        "DOMESTIC_E",
        "DOMESTIC_F",
        "DOMESTIC_G",
        "DOMESTIC_H",
        "DOMESTIC_I",
        "DOMESTIC_J",
        "DOMESTIC_K",
        "DOMESTIC_L",
        "DOMESTIC_M",
        "DOMESTIC_N",
        "DOMESTIC_O",
        "GBT_AC",
        "GBT_DC",
        "IEC_60309_2_single_16",
        "IEC_60309_2_three_16",
        "IEC_60309_2_three_32",
        "IEC_60309_2_three_64",
        "IEC_62196_T1",
        "IEC_62196_T1_COMBO",
        "IEC_62196_T2",
        "IEC_62196_T2_COMBO",
        "IEC_62196_T3A",
        "IEC_62196_T3C",
        "MCS",
        "NEMA_10_30",
        "NEMA_10_50",
        "NEMA_14_30",
        "NEMA_14_50",
        "NEMA_5_20",
        "NEMA_6_30",
        "NEMA_6_50",
        "PANTOGRAPH_BOTTOM_UP",
        "PANTOGRAPH_TOP_DOWN",
        "SAE_J3400",
        "TESLA_R",
        "TESLA_S",
    ],
    "CdrDimensionType": [
        "CURRENT",
        "ENERGY",
        "ENERGY_EXPORT",
        "ENERGY_IMPORT",
        "MAX_CURRENT",
        "MAX_POWER",
        "MIN_CURRENT",
        "MIN_POWER",
        "PARKING_TIME",
        "POWER",
        "RESERVATION_TIME",
        "STATE_OF_CHARGE",
        "TIME",
    ],
    "TariffDimensionType": [
        "ENERGY",
        "FLAT",
        "PARKING_TIME",
        "TIME",
    ],
    "DayOfWeek": [
        "FRIDAY",
        "MONDAY",
        "SATURDAY",
        "SUNDAY",
        "THURSDAY",
        "TUESDAY",
        "WEDNESDAY",
    ],
    "ReservationRestrictionType": [
        "RESERVATION",
        "RESERVATION_EXPIRES",
    ],
    "EnergySourceCategory": [
        "COAL",
        "GAS",
        "GENERAL_FOSSIL",
        "GENERAL_GREEN",
        "NUCLEAR",
        "SOLAR",
        "WATER",
        "WIND",
    ],
    "EnvironmentalImpactCategory": [
        "CARBON_DIOXIDE",
        "NUCLEAR_WASTE",
    ],
    "TaxIncluded": [
        "N/A",
        "NO",
        "YES",
    ],
    "TariffType": [
        "AD_HOC_PAYMENT",
        "PROFILE_CHEAP",
        "PROFILE_FAST",
        "PROFILE_GREEN",
        "REGULAR",
    ],
    "ChargingProfileResponseType": [
        "ACCEPTED",
        "NOT_SUPPORTED",
        "REJECTED",
        "TOO_OFTEN",
        "UNKNOWN_SESSION",
    ],
    "CommandResponseType": [
        "ACCEPTED",
        "NOT_SUPPORTED",
        "REJECTED",
        "UNKNOWN_SESSION",
    ],
    "CommandResultType": [
        "ACCEPTED",
        "CANCELED_RESERVATION",
        "EVSE_INOPERATIVE",
        "EVSE_OCCUPIED",
        "FAILED",
        "NOT_SUPPORTED",
        "REJECTED",
        "TIMEOUT",
        "UNKNOWN_RESERVATION",
    ],
    "ConnectorCapability": [
        "ISO_15118_20_PLUG_AND_CHARGE",
        "ISO_15118_2_PLUG_AND_CHARGE",
    ],
    "ImageCategory": [
        "CHARGER",
        "ENTRANCE",
        "LOCATION",
        "NETWORK",
        "OPERATOR",
        "OTHER",
        "OWNER",
    ],
    "Role": [
        "CPO",
        "EMSP",
        "NAP",
        "NSP",
        "OTHER",
        "SCSP",
    ],
    "ModuleID": [
        "cdrs",
        "chargingprofiles",
        "commands",
        "credentials",
        "hubclientinfo",
        "locations",
        "payments",
        "sessions",
        "tariffs",
        "tokens",
    ],
    "InterfaceRole": [
        "RECEIVER",
        "SENDER",
    ],
    "Capability": [
        "CHARGING_PREFERENCES_CAPABLE",
        "CHARGING_PROFILE_CAPABLE",
        "CHIP_CARD_SUPPORT",
        "CONTACTLESS_CARD_SUPPORT",
        "CREDIT_CARD_PAYABLE",
        "DEBIT_CARD_PAYABLE",
        "PED_TERMINAL",
        "RFID_READER",
        "REMOTE_START_STOP_CAPABLE",
        "RESERVABLE",
        "START_SESSION_CONNECTOR_REQUIRED",
        "TOKEN_GROUP_CAPABLE",
        "UNLOCK_CAPABLE",
    ],
    "EvsePosition": [
        "CENTER",
        "LEFT",
        "RIGHT",
    ],
    "ParkingRestriction": [
        "CUSTOMERS",
        "DISABLED",
        "EMPLOYEES",
        "EV_ONLY",
        "MOTORCYCLES",
        "PLUGGED",
        "TAXIS",
        "TENANTS",
    ],
    "Status": [
        "AVAILABLE",
        "BLOCKED",
        "CHARGING",
        "INOPERATIVE",
        "OUTOFORDER",
        "PLANNED",
        "REMOVED",
        "RESERVED",
        "UNKNOWN",
    ],
    "CaptureStatusCode": [
        "FAILED",
        "PARTIAL_SUCCESS",
        "SUCCESS",
    ],
    "ConnectionStatus": [
        "CONNECTED",
        "OFFLINE",
        "PLANNED",
        "SUSPENDED",
    ],
    "Facility": [
        "AIRPORT",
        "BIKE_SHARING",
        "BUS_STOP",
        "CAFE",
        "CARPOOL_PARKING",
        "FUEL_STATION",
        "HOTEL",
        "MALL",
        "METRO_STATION",
        "MUSEUM",
        "NATURE",
        "PARKING_LOT",
        "RECREATION_AREA",
        "RESTAURANT",
        "SPORT",
        "SUPERMARKET",
        "TAXI_STAND",
        "TRAIN_STATION",
        "TRAM_STOP",
        "WIFI",
    ],
    "ParkingDirection": [
        "ANGLE",
        "PARALLEL",
        "PERPENDICULAR",
    ],
    "VehicleType": [
        "BUS",
        "DISABLED",
        "MOTORCYCLE",
        "PERSONAL_VEHICLE",
        "PERSONAL_VEHICLE_WITH_TRAILER",
        "RIGID",
        "SEMI_TRACTOR",
        "TRUCK_WITH_TRAILER",
        "VAN",
    ],
    "ParkingType": [
        "ALONG_MOTORWAY",
        "ON_DRIVEWAY",
        "ON_STREET",
        "PARKING_GARAGE",
        "PARKING_LOT",
        "UNDERGROUND_GARAGE",
    ],
    "SessionStatus": [
        "ACTIVE",
        "COMPLETED",
        "INVALID",
        "PENDING",
        "RESERVATION",
    ],
    "InvoiceCreator": [
        "CPO",
        "PTP",
    ],
    "VersionNumber": [
        "2.0",
        "2.1",
        "2.1.1",
        "2.2",
        "2.2.1",
        "2.3.0",
    ],
};
