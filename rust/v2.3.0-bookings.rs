// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::v2.3.0-bookings;
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: v2.3.0-bookings = serde_json::from_str(&json).unwrap();
// }

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct V230Bookings {
    active_charging_profile: Option<ActiveChargingProfile>,

    active_charging_profile_result: Option<ActiveChargingProfileResult>,

    authorization_info: Option<AuthorizationInfo>,

    booking: Option<Booking>,

    booking_location: Option<BookingLocation>,

    booking_request: Option<BookingRequest>,

    calendar: Option<Calendar>,

    cancel_reservation: Option<CancelReservation>,

    cdr: Option<Cdr>,

    charging_preferences: Option<ChargingPreferences>,

    charging_profile: Option<ChargingProfile>,

    charging_profile_response: Option<ChargingProfileResponse>,

    charging_profile_result: Option<ChargingProfileResult>,

    clear_profile_result: Option<ClearProfileResult>,

    command_response: Option<CommandResponse>,

    command_result: Option<CommandResult>,

    connector: Option<Connector>,

    credentials: Option<Credentials>,

    endpoint: Option<Endpoint>,

    evse: Option<Evse>,

    hub_client_info: Option<HubClientInfo>,

    location: Option<Location>,

    location_references: Option<LocationReferences>,

    reserve_now: Option<ReserveNow>,

    session: Option<Session>,

    set_charging_profile: Option<SetChargingProfile>,

    start_session: Option<StartSession>,

    stop_session: Option<StopSession>,

    tariff: Option<Tariff>,

    token: Option<Token>,

    unlock_connector: Option<UnlockConnector>,

    version: Option<Version>,

    version_details: Option<VersionDetails>,
}

#[derive(Serialize, Deserialize)]
pub struct ActiveChargingProfile {
    charging_profile: ChargingProfile,

    start_date_time: String,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingProfile {
    charging_profile_period: Option<Vec<ChargingProfilePeriod>>,

    charging_rate_unit: ChargingRateUnit,

    duration: Option<i64>,

    min_charging_rate: Option<f64>,

    start_date_time: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingProfilePeriod {
    limit: f64,

    start_period: i64,
}

#[derive(Serialize, Deserialize)]
pub enum ChargingRateUnit {
    A,

    W,
}

#[derive(Serialize, Deserialize)]
pub struct ActiveChargingProfileResult {
    profile: Option<ActiveChargingProfile>,

    result: ChargingProfileResultType,
}

#[derive(Serialize, Deserialize)]
pub enum ChargingProfileResultType {
    #[serde(rename = "ACCEPTED")]
    Accepted,

    #[serde(rename = "REJECTED")]
    Rejected,

    #[serde(rename = "UNKNOWN")]
    Unknown,
}

#[derive(Serialize, Deserialize)]
pub struct AuthorizationInfo {
    allowed: AllowedType,

    authorization_reference: Option<String>,

    info: Option<DisplayText>,

    location: Option<LocationReferences>,

    token: Token,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum AllowedType {
    Allowed,

    Blocked,

    Expired,

    #[serde(rename = "NO_CREDIT")]
    NoCredit,

    #[serde(rename = "NOT_ALLOWED")]
    NotAllowed,
}

#[derive(Serialize, Deserialize)]
pub struct DisplayText {
    language: String,

    text: String,
}

#[derive(Serialize, Deserialize)]
pub struct LocationReferences {
    evse_uids: Option<Vec<String>>,

    location_id: String,
}

#[derive(Serialize, Deserialize)]
pub struct Token {
    contract_id: String,

    country_code: String,

    default_profile_type: Option<ProfileType>,

    energy_contract: Option<EnergyContract>,

    group_id: Option<String>,

    issuer: String,

    language: Option<String>,

    last_updated: String,

    party_id: String,

    #[serde(rename = "type")]
    token_type: TokenType,

    uid: String,

    valid: bool,

    visual_number: Option<String>,

    whitelist: WhitelistType,
}

#[derive(Serialize, Deserialize)]
pub enum ProfileType {
    #[serde(rename = "CHEAP")]
    Cheap,

    #[serde(rename = "FAST")]
    Fast,

    #[serde(rename = "GREEN")]
    Green,

    #[serde(rename = "REGULAR")]
    Regular,
}

#[derive(Serialize, Deserialize)]
pub struct EnergyContract {
    contract_id: Option<String>,

    supplier_name: String,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum TokenType {
    #[serde(rename = "AD_HOC_USER")]
    AdHocUser,

    #[serde(rename = "APP_USER")]
    AppUser,

    Emaid,

    #[serde(rename = "LICENSE_PLATE")]
    LicensePlate,

    Other,

    Rfid,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum WhitelistType {
    Allowed,

    #[serde(rename = "ALLOWED_OFFLINE")]
    AllowedOffline,

    Always,

    Never,
}

#[derive(Serialize, Deserialize)]
pub struct Booking {
    access_methods: Option<Vec<AccessMethod>>,

    authorization_reference: String,

    bookable_parking_option: Option<BookableParkingOptions>,

    booking_requests: Vec<BookingRequestStatus>,

    booking_terms: BookingTerms,

    booking_tokens: Option<Vec<BookingToken>>,

    canceled: Option<Cancellation>,

    connector_id: Option<String>,

    country_code: String,

    evse_uid: Option<String>,

    id: String,

    last_updated: String,

    location_id: String,

    parking_id: Option<String>,

    party_id: String,

    period: Timeslot,

    request_id: String,

    reservation_status: ReservationStatus,

    tariff_id: Option<Vec<String>>,
}

#[derive(Serialize, Deserialize)]
pub struct AccessMethod {
    location_access: LocationAccess,

    value: Option<String>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum LocationAccess {
    #[serde(rename = "ACCESS_CODE")]
    AccessCode,

    Intercom,

    #[serde(rename = "LICENSE_PLATE")]
    LicensePlate,

    Open,

    #[serde(rename = "PARKING_TICKET")]
    ParkingTicket,

    Token,
}

#[derive(Serialize, Deserialize)]
pub struct BookableParkingOptions {
    dangerous_goods_allowed: Option<bool>,

    drive_through: Option<bool>,

    evse_position: Option<EvsePosition>,

    format: ConnectorFormat,

    max_vehicle_height: Option<f64>,

    max_vehicle_length: Option<f64>,

    max_vehicle_weight: Option<f64>,

    max_vehicle_width: Option<f64>,

    parking_space_length: Option<f64>,

    parking_space_width: Option<f64>,

    refrigeration_outlet: Option<bool>,

    restricted_to_type: bool,

    vehicle_types: Vec<VehicleType>,
}

#[derive(Serialize, Deserialize)]
pub enum EvsePosition {
    #[serde(rename = "CENTER")]
    Center,

    #[serde(rename = "LEFT")]
    Left,

    #[serde(rename = "RIGHT")]
    Right,
}

#[derive(Serialize, Deserialize)]
pub enum ConnectorFormat {
    #[serde(rename = "CABLE")]
    Cable,

    #[serde(rename = "SOCKET")]
    Socket,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum VehicleType {
    Bus,

    Disabled,

    Motorcycle,

    #[serde(rename = "PERSONAL_VEHICLE")]
    PersonalVehicle,

    #[serde(rename = "PERSONAL_VEHICLE_WITH_TRAILER")]
    PersonalVehicleWithTrailer,

    Rigid,

    #[serde(rename = "SEMI_TRACTOR")]
    SemiTractor,

    #[serde(rename = "TRUCK_WITH_TRAILER")]
    TruckWithTrailer,

    Van,
}

#[derive(Serialize, Deserialize)]
pub struct BookingRequestStatus {
    booking_request: BookingRequest,

    request_received: String,

    request_status: ReservationRequestStatus,
}

#[derive(Serialize, Deserialize)]
pub struct BookingRequest {
    authorization_reference: String,

    bookable_parking_option: Option<BookableParkingOptions>,

    canceled: Option<Cancellation>,

    connector_id: Option<String>,

    country_code: String,

    evse_uid: Option<String>,

    location_id: String,

    party_id: String,

    period: Timeslot,

    power_required: Option<i64>,

    request_id: String,

    tokens: Option<Vec<BookingToken>>,
}

#[derive(Serialize, Deserialize)]
pub struct Cancellation {
    cancellation_reason: CanceledReason,

    who_canceled: Role,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CanceledReason {
    Blocked,

    #[serde(rename = "BROKEN_CHARGER")]
    BrokenCharger,

    #[serde(rename = "BROKEN_VEHICLE")]
    BrokenVehicle,

    Full,

    #[serde(rename = "NO_CANCELED")]
    NoCanceled,

    #[serde(rename = "POWER_OUTAGE")]
    PowerOutage,

    Traffic,

    Unknown,
}

#[derive(Serialize, Deserialize)]
pub enum Role {
    #[serde(rename = "CPO")]
    Cpo,

    #[serde(rename = "EMSP")]
    Emsp,

    #[serde(rename = "NAP")]
    Nap,

    #[serde(rename = "NSP")]
    Nsp,

    #[serde(rename = "OTHER")]
    Other,

    #[serde(rename = "SCSP")]
    Scsp,
}

#[derive(Serialize, Deserialize)]
pub struct Timeslot {
    end_before: String,

    green_energy_support: Option<bool>,

    max_power: Option<f64>,

    min_power: Option<f64>,

    start_from: String,
}

#[derive(Serialize, Deserialize)]
pub struct BookingToken {
    contract_id: String,

    country_code: String,

    party_id: String,

    #[serde(rename = "type")]
    booking_token_type: TokenType,

    uid: String,
}

#[derive(Serialize, Deserialize)]
pub enum ReservationRequestStatus {
    #[serde(rename = "ACCEPTED")]
    Accepted,

    #[serde(rename = "DECLINED")]
    Declined,

    #[serde(rename = "FAILED")]
    Failed,

    #[serde(rename = "PENDING")]
    Pending,
}

#[derive(Serialize, Deserialize)]
pub struct BookingTerms {
    booking_terms: Option<String>,

    cancel_until_minutes: f64,

    change_not_allowed: Option<bool>,

    change_until_minutes: f64,

    early_start_allowed: Option<bool>,

    early_start_time: Option<f64>,

    late_stop_allowed: Option<bool>,

    late_stop_time: Option<f64>,

    noshow_fee: Option<bool>,

    noshow_timeout: Option<f64>,

    overlapping_bookings_allowed: Option<bool>,

    remote_auth_supported: Option<bool>,

    #[serde(rename = "RFID_auth_required")]
    rfid_auth_required: Option<bool>,

    supported_access_methods: Vec<LocationAccess>,

    token_groups_supported: Option<bool>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ReservationStatus {
    Canceled,

    Failed,

    Fulfilled,

    #[serde(rename = "NO_SHOW")]
    NoShow,

    Pending,

    Rejected,

    Reserved,

    Unknown,
}

#[derive(Serialize, Deserialize)]
pub struct BookingLocation {
    bookable: Option<Bookable>,

    bookable_parking_options: Option<Vec<BookableParkingOptions>>,

    booking_terms: Option<Vec<BookingTerms>>,

    calendars: Option<Vec<Calendar>>,

    connector_id: Option<String>,

    country_code: String,

    evse_uid: Option<String>,

    id: String,

    last_updated: String,

    location_id: String,

    party_id: String,

    tariff_id: Option<Vec<String>>,
}

#[derive(Serialize, Deserialize)]
pub struct Bookable {
    ad_hoc: Option<f64>,

    reservation_required: bool,
}

#[derive(Serialize, Deserialize)]
pub struct Calendar {
    available_timeslots: Vec<Timeslot>,

    begin_from: String,

    end_before: String,

    id: String,

    last_updated: String,

    step_size: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub struct CancelReservation {
    reservation_id: String,

    response_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct Cdr {
    auth_method: AuthMethod,

    authorization_reference: Option<String>,

    booking_id: Option<String>,

    cdr_location: CdrLocation,

    cdr_token: CdrToken,

    charging_periods: Vec<ChargingPeriod>,

    country_code: String,

    credit: Option<bool>,

    credit_reference_id: Option<String>,

    currency: String,

    end_date_time: String,

    home_charging_compensation: Option<bool>,

    id: String,

    invoice_reference_id: Option<String>,

    last_updated: String,

    meter_id: Option<String>,

    party_id: String,

    remark: Option<String>,

    session_id: Option<String>,

    signed_data: Option<SignedData>,

    start_date_time: String,

    tariffs: Option<Vec<Tariff>>,

    total_cost: Price,

    total_energy: f64,

    total_energy_cost: Option<Price>,

    total_fixed_cost: Option<Price>,

    total_parking_cost: Option<Price>,

    total_parking_time: Option<f64>,

    total_reservation_cost: Option<Price>,

    total_time: f64,

    total_time_cost: Option<Price>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum AuthMethod {
    #[serde(rename = "AUTH_REQUEST")]
    AuthRequest,

    Command,

    Whitelist,
}

#[derive(Serialize, Deserialize)]
pub struct CdrLocation {
    address: String,

    city: String,

    connector_format: ConnectorFormat,

    connector_id: String,

    connector_power_type: PowerType,

    connector_standard: ConnectorType,

    coordinates: GeoLocation,

    country: String,

    evse_id: String,

    evse_uid: String,

    id: String,

    name: Option<String>,

    postal_code: Option<String>,

    state: Option<String>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum PowerType {
    #[serde(rename = "AC_1_PHASE")]
    Ac1_Phase,

    #[serde(rename = "AC_2_PHASE")]
    Ac2_Phase,

    #[serde(rename = "AC_2_PHASE_SPLIT")]
    Ac2_PhaseSplit,

    #[serde(rename = "AC_3_PHASE")]
    Ac3_Phase,

    Dc,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ConnectorType {
    Chademo,

    Chaoji,

    #[serde(rename = "DOMESTIC_A")]
    DomesticA,

    #[serde(rename = "DOMESTIC_B")]
    DomesticB,

    #[serde(rename = "DOMESTIC_C")]
    DomesticC,

    #[serde(rename = "DOMESTIC_D")]
    DomesticD,

    #[serde(rename = "DOMESTIC_E")]
    DomesticE,

    #[serde(rename = "DOMESTIC_F")]
    DomesticF,

    #[serde(rename = "DOMESTIC_G")]
    DomesticG,

    #[serde(rename = "DOMESTIC_H")]
    DomesticH,

    #[serde(rename = "DOMESTIC_I")]
    DomesticI,

    #[serde(rename = "DOMESTIC_J")]
    DomesticJ,

    #[serde(rename = "DOMESTIC_K")]
    DomesticK,

    #[serde(rename = "DOMESTIC_L")]
    DomesticL,

    #[serde(rename = "DOMESTIC_M")]
    DomesticM,

    #[serde(rename = "DOMESTIC_N")]
    DomesticN,

    #[serde(rename = "DOMESTIC_O")]
    DomesticO,

    #[serde(rename = "GBT_AC")]
    GbtAc,

    #[serde(rename = "GBT_DC")]
    GbtDc,

    #[serde(rename = "IEC_60309_2_single_16")]
    Iec60309_2_Single16,

    #[serde(rename = "IEC_60309_2_three_16")]
    Iec60309_2_Three16,

    #[serde(rename = "IEC_60309_2_three_32")]
    Iec60309_2_Three32,

    #[serde(rename = "IEC_60309_2_three_64")]
    Iec60309_2_Three64,

    #[serde(rename = "IEC_62196_T1")]
    Iec62196_T1,

    #[serde(rename = "IEC_62196_T1_COMBO")]
    Iec62196_T1Combo,

    #[serde(rename = "IEC_62196_T2")]
    Iec62196_T2,

    #[serde(rename = "IEC_62196_T2_COMBO")]
    Iec62196_T2Combo,

    #[serde(rename = "IEC_62196_T3A")]
    Iec62196_T3A,

    #[serde(rename = "IEC_62196_T3C")]
    Iec62196_T3C,

    Mcs,

    #[serde(rename = "NEMA_10_30")]
    Nema10_30,

    #[serde(rename = "NEMA_10_50")]
    Nema10_50,

    #[serde(rename = "NEMA_14_30")]
    Nema14_30,

    #[serde(rename = "NEMA_14_50")]
    Nema14_50,

    #[serde(rename = "NEMA_5_20")]
    Nema5_20,

    #[serde(rename = "NEMA_6_30")]
    Nema6_30,

    #[serde(rename = "NEMA_6_50")]
    Nema6_50,

    #[serde(rename = "PANTOGRAPH_BOTTOM_UP")]
    PantographBottomUp,

    #[serde(rename = "PANTOGRAPH_TOP_DOWN")]
    PantographTopDown,

    #[serde(rename = "SAE_J3400")]
    SaeJ3400,

    #[serde(rename = "TESLA_R")]
    TeslaR,

    #[serde(rename = "TESLA_S")]
    TeslaS,
}

#[derive(Serialize, Deserialize)]
pub struct GeoLocation {
    latitude: String,

    longitude: String,
}

#[derive(Serialize, Deserialize)]
pub struct CdrToken {
    contract_id: String,

    country_code: String,

    party_id: String,

    #[serde(rename = "type")]
    cdr_token_type: TokenType,

    uid: String,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingPeriod {
    dimensions: Vec<CdrDimension>,

    start_date_time: String,

    tariff_id: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct CdrDimension {
    #[serde(rename = "type")]
    cdr_dimension_type: CdrDimensionType,

    volume: f64,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CdrDimensionType {
    Current,

    Energy,

    #[serde(rename = "ENERGY_EXPORT")]
    EnergyExport,

    #[serde(rename = "ENERGY_IMPORT")]
    EnergyImport,

    #[serde(rename = "MAX_CURRENT")]
    MaxCurrent,

    #[serde(rename = "MAX_POWER")]
    MaxPower,

    #[serde(rename = "MIN_CURRENT")]
    MinCurrent,

    #[serde(rename = "MIN_POWER")]
    MinPower,

    #[serde(rename = "PARKING_TIME")]
    ParkingTime,

    Power,

    #[serde(rename = "RESERVATION_EXPIRES")]
    ReservationExpires,

    #[serde(rename = "RESERVATION_OVERTIME")]
    ReservationOvertime,

    #[serde(rename = "RESERVATION_TIME")]
    ReservationTime,

    #[serde(rename = "STATE_OF_CHARGE")]
    StateOfCharge,

    Time,
}

#[derive(Serialize, Deserialize)]
pub struct SignedData {
    encoding_method: String,

    encoding_method_version: Option<i64>,

    public_key: Option<String>,

    signed_values: Vec<SignedValue>,

    url: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct SignedValue {
    nature: String,

    plain_data: String,

    signed_data: String,
}

#[derive(Serialize, Deserialize)]
pub struct Tariff {
    country_code: String,

    currency: String,

    elements: Vec<TariffElement>,

    end_date_time: Option<String>,

    energy_mix: Option<EnergyMix>,

    id: String,

    last_updated: String,

    max_price: Option<PriceLimit>,

    min_price: Option<PriceLimit>,

    party_id: String,

    start_date_time: Option<String>,

    tariff_alt_text: Option<Vec<DisplayText>>,

    tariff_alt_url: Option<String>,

    tax_included: TaxIncluded,

    #[serde(rename = "type")]
    tariff_type: Option<TariffType>,
}

#[derive(Serialize, Deserialize)]
pub struct TariffElement {
    price_components: Vec<PriceComponent>,

    restrictions: Option<TariffRestrictions>,
}

#[derive(Serialize, Deserialize)]
pub struct PriceComponent {
    price: f64,

    step_size: i64,

    #[serde(rename = "type")]
    price_component_type: TariffDimensionType,

    vat: Option<f64>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum TariffDimensionType {
    Energy,

    Flat,

    #[serde(rename = "PARKING_TIME")]
    ParkingTime,

    Time,
}

#[derive(Serialize, Deserialize)]
pub struct TariffRestrictions {
    day_of_week: Option<Vec<DayOfWeek>>,

    end_date: Option<String>,

    end_time: Option<String>,

    max_current: Option<f64>,

    max_duration: Option<i64>,

    max_kwh: Option<f64>,

    max_power: Option<f64>,

    min_current: Option<f64>,

    min_duration: Option<i64>,

    min_kwh: Option<f64>,

    min_power: Option<f64>,

    reservation: Option<ReservationRestrictionType>,

    start_date: Option<String>,

    start_time: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub enum DayOfWeek {
    #[serde(rename = "FRIDAY")]
    Friday,

    #[serde(rename = "MONDAY")]
    Monday,

    #[serde(rename = "SATURDAY")]
    Saturday,

    #[serde(rename = "SUNDAY")]
    Sunday,

    #[serde(rename = "THURSDAY")]
    Thursday,

    #[serde(rename = "TUESDAY")]
    Tuesday,

    #[serde(rename = "WEDNESDAY")]
    Wednesday,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ReservationRestrictionType {
    Reservation,

    #[serde(rename = "RESERVATION_CANCELLATION_FEES")]
    ReservationCancellationFees,

    #[serde(rename = "RESERVATION_EXPIRES")]
    ReservationExpires,

    #[serde(rename = "RESERVATION_OVERTIME")]
    ReservationOvertime,
}

#[derive(Serialize, Deserialize)]
pub struct EnergyMix {
    energy_product_name: Option<String>,

    energy_sources: Option<Vec<EnergySource>>,

    environ_impact: Option<Vec<EnvironmentalImpact>>,

    is_green_energy: bool,

    supplier_name: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct EnergySource {
    percentage: f64,

    source: EnergySourceCategory,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum EnergySourceCategory {
    Coal,

    Gas,

    #[serde(rename = "GENERAL_FOSSIL")]
    GeneralFossil,

    #[serde(rename = "GENERAL_GREEN")]
    GeneralGreen,

    Nuclear,

    Solar,

    Water,

    Wind,
}

#[derive(Serialize, Deserialize)]
pub struct EnvironmentalImpact {
    amount: f64,

    category: EnvironmentalImpactCategory,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum EnvironmentalImpactCategory {
    #[serde(rename = "CARBON_DIOXIDE")]
    CarbonDioxide,

    #[serde(rename = "NUCLEAR_WASTE")]
    NuclearWaste,
}

#[derive(Serialize, Deserialize)]
pub struct PriceLimit {
    after_taxes: Option<f64>,

    before_taxes: f64,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum TariffType {
    #[serde(rename = "AD_HOC_PAYMENT")]
    AdHocPayment,

    #[serde(rename = "PROFILE_CHEAP")]
    ProfileCheap,

    #[serde(rename = "PROFILE_FAST")]
    ProfileFast,

    #[serde(rename = "PROFILE_GREEN")]
    ProfileGreen,

    Regular,
}

#[derive(Serialize, Deserialize)]
pub enum TaxIncluded {
    #[serde(rename = "N/A")]
    NA,

    #[serde(rename = "NO")]
    No,

    #[serde(rename = "YES")]
    Yes,
}

#[derive(Serialize, Deserialize)]
pub struct Price {
    before_taxes: f64,

    taxes: Option<Vec<TaxAmount>>,
}

#[derive(Serialize, Deserialize)]
pub struct TaxAmount {
    account_number: Option<String>,

    amount: f64,

    name: String,

    percentage: Option<f64>,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingPreferences {
    departure_time: Option<String>,

    discharge_allowed: Option<bool>,

    energy_need: Option<f64>,

    profile_type: ProfileType,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingProfileResponse {
    result: ChargingProfileResponseType,

    timeout: i64,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ChargingProfileResponseType {
    Accepted,

    #[serde(rename = "NOT_SUPPORTED")]
    NotSupported,

    Rejected,

    #[serde(rename = "TOO_OFTEN")]
    TooOften,

    #[serde(rename = "UNKNOWN_SESSION")]
    UnknownSession,
}

#[derive(Serialize, Deserialize)]
pub struct ChargingProfileResult {
    result: ChargingProfileResultType,
}

#[derive(Serialize, Deserialize)]
pub struct ClearProfileResult {
    result: ChargingProfileResultType,
}

#[derive(Serialize, Deserialize)]
pub struct CommandResponse {
    message: Option<Vec<DisplayText>>,

    result: CommandResponseType,

    timeout: i64,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CommandResponseType {
    Accepted,

    #[serde(rename = "NOT_SUPPORTED")]
    NotSupported,

    Rejected,

    #[serde(rename = "UNKNOWN_SESSION")]
    UnknownSession,
}

#[derive(Serialize, Deserialize)]
pub struct CommandResult {
    message: Option<Vec<DisplayText>>,

    result: CommandResultType,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CommandResultType {
    Accepted,

    #[serde(rename = "CANCELED_RESERVATION")]
    CanceledReservation,

    #[serde(rename = "EVSE_INOPERATIVE")]
    EvseInoperative,

    #[serde(rename = "EVSE_OCCUPIED")]
    EvseOccupied,

    Failed,

    #[serde(rename = "NOT_SUPPORTED")]
    NotSupported,

    Rejected,

    Timeout,

    #[serde(rename = "UNKNOWN_RESERVATION")]
    UnknownReservation,
}

#[derive(Serialize, Deserialize)]
pub struct Connector {
    capabilities: Option<Vec<ConnectorCapability>>,

    format: ConnectorFormat,

    id: String,

    last_updated: String,

    max_amperage: i64,

    max_electric_power: Option<i64>,

    max_voltage: i64,

    power_type: PowerType,

    standard: ConnectorType,

    tariff_ids: Option<Vec<String>>,

    terms_and_conditions: Option<String>,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ConnectorCapability {
    #[serde(rename = "ISO_15118_20_PLUG_AND_CHARGE")]
    Iso15118_20_PlugAndCharge,

    #[serde(rename = "ISO_15118_2_PLUG_AND_CHARGE")]
    Iso15118_2_PlugAndCharge,
}

#[derive(Serialize, Deserialize)]
pub struct Credentials {
    hub_party_id: Option<String>,

    roles: Vec<CredentialsRole>,

    token: String,

    url: String,
}

#[derive(Serialize, Deserialize)]
pub struct CredentialsRole {
    business_details: BusinessDetails,

    country_code: String,

    party_id: String,

    role: Role,
}

#[derive(Serialize, Deserialize)]
pub struct BusinessDetails {
    logo: Option<Image>,

    name: String,

    website: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Image {
    category: ImageCategory,

    height: Option<i64>,

    thumbnail: Option<String>,

    #[serde(rename = "type")]
    image_type: String,

    url: String,

    width: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub enum ImageCategory {
    #[serde(rename = "CHARGER")]
    Charger,

    #[serde(rename = "ENTRANCE")]
    Entrance,

    #[serde(rename = "LOCATION")]
    Location,

    #[serde(rename = "NETWORK")]
    Network,

    #[serde(rename = "OPERATOR")]
    Operator,

    #[serde(rename = "OTHER")]
    Other,

    #[serde(rename = "OWNER")]
    Owner,
}

#[derive(Serialize, Deserialize)]
pub struct Endpoint {
    identifier: ModuleId,

    role: InterfaceRole,

    url: String,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ModuleId {
    #[serde(rename = "Booking")]
    Booking,

    Cdrs,

    Chargingprofiles,

    Commands,

    Credentials,

    Hubclientinfo,

    Locations,

    Sessions,

    Tariffs,

    Tokens,
}

#[derive(Serialize, Deserialize)]
pub enum InterfaceRole {
    #[serde(rename = "RECEIVER")]
    Receiver,

    #[serde(rename = "SENDER")]
    Sender,
}

#[derive(Serialize, Deserialize)]
pub struct Evse {
    accepted_service_providers: Option<Vec<String>>,

    capabilities: Option<Vec<Capability>>,

    connectors: Vec<Connector>,

    coordinates: Option<GeoLocation>,

    directions: Option<Vec<DisplayText>>,

    evse_id: Option<String>,

    floor_level: Option<String>,

    images: Option<Vec<Image>>,

    last_updated: String,

    parking: Option<Vec<EvseParking>>,

    parking_restrictions: Option<Vec<ParkingRestriction>>,

    physical_reference: Option<String>,

    status: Status,

    status_schedule: Option<Vec<StatusSchedule>>,

    uid: String,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Capability {
    #[serde(rename = "CHARGING_PREFERENCES_CAPABLE")]
    ChargingPreferencesCapable,

    #[serde(rename = "CHARGING_PROFILE_CAPABLE")]
    ChargingProfileCapable,

    #[serde(rename = "CHIP_CARD_SUPPORT")]
    ChipCardSupport,

    #[serde(rename = "CONTACTLESS_CARD_SUPPORT")]
    ContactlessCardSupport,

    #[serde(rename = "CREDIT_CARD_PAYABLE")]
    CreditCardPayable,

    #[serde(rename = "DEBIT_CARD_PAYABLE")]
    DebitCardPayable,

    #[serde(rename = "PED_TERMINAL")]
    PedTerminal,

    #[serde(rename = "REMOTE_START_STOP_CAPABLE")]
    RemoteStartStopCapable,

    Reservable,

    #[serde(rename = "RFID_READER")]
    RfidReader,

    #[serde(rename = "START_SESSION_CONNECTOR_REQUIRED")]
    StartSessionConnectorRequired,

    #[serde(rename = "TOKEN_GROUP_CAPABLE")]
    TokenGroupCapable,

    #[serde(rename = "UNLOCK_CAPABLE")]
    UnlockCapable,
}

#[derive(Serialize, Deserialize)]
pub struct EvseParking {
    evse_position: Option<EvsePosition>,

    parking_id: String,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ParkingRestriction {
    Customers,

    Disabled,

    Employees,

    #[serde(rename = "EV_ONLY")]
    EvOnly,

    Motorcycles,

    Plugged,

    Taxis,

    Tenants,
}

#[derive(Serialize, Deserialize)]
pub enum Status {
    #[serde(rename = "AVAILABLE")]
    Available,

    #[serde(rename = "BLOCKED")]
    Blocked,

    #[serde(rename = "CHARGING")]
    Charging,

    #[serde(rename = "INOPERATIVE")]
    Inoperative,

    #[serde(rename = "OUTOFORDER")]
    Outoforder,

    #[serde(rename = "PLANNED")]
    Planned,

    #[serde(rename = "REMOVED")]
    Removed,

    #[serde(rename = "RESERVED")]
    Reserved,

    #[serde(rename = "UNKNOWN")]
    Unknown,
}

#[derive(Serialize, Deserialize)]
pub struct StatusSchedule {
    period_begin: String,

    period_end: Option<String>,

    status: Status,
}

#[derive(Serialize, Deserialize)]
pub struct HubClientInfo {
    country_code: String,

    last_updated: String,

    party_id: String,

    role: Role,

    status: ConnectionStatus,
}

#[derive(Serialize, Deserialize)]
pub enum ConnectionStatus {
    #[serde(rename = "CONNECTED")]
    Connected,

    #[serde(rename = "OFFLINE")]
    Offline,

    #[serde(rename = "PLANNED")]
    Planned,

    #[serde(rename = "SUSPENDED")]
    Suspended,
}

#[derive(Serialize, Deserialize)]
pub struct Location {
    address: String,

    charging_when_closed: Option<bool>,

    city: String,

    coordinates: GeoLocation,

    country: String,

    country_code: String,

    directions: Option<Vec<DisplayText>>,

    energy_mix: Option<EnergyMix>,

    evses: Option<Vec<Evse>>,

    facilities: Option<Vec<Facility>>,

    help_phone: Option<String>,

    id: String,

    images: Option<Vec<Image>>,

    last_updated: String,

    name: Option<String>,

    opening_times: Option<Hours>,

    operator: Option<BusinessDetails>,

    owner: Option<BusinessDetails>,

    parking_places: Option<Vec<Parking>>,

    parking_type: Option<ParkingType>,

    party_id: String,

    postal_code: Option<String>,

    publish: bool,

    publish_allowed_to: Option<Vec<PublishTokenType>>,

    related_locations: Option<Vec<AdditionalGeoLocation>>,

    state: Option<String>,

    suboperator: Option<BusinessDetails>,

    time_zone: String,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Facility {
    Airport,

    #[serde(rename = "BIKE_SHARING")]
    BikeSharing,

    #[serde(rename = "BUS_STOP")]
    BusStop,

    Cafe,

    #[serde(rename = "CARPOOL_PARKING")]
    CarpoolParking,

    #[serde(rename = "FUEL_STATION")]
    FuelStation,

    Hotel,

    Mall,

    #[serde(rename = "METRO_STATION")]
    MetroStation,

    Museum,

    Nature,

    #[serde(rename = "PARKING_LOT")]
    ParkingLot,

    #[serde(rename = "RECREATION_AREA")]
    RecreationArea,

    Restaurant,

    Sport,

    Supermarket,

    #[serde(rename = "TAXI_STAND")]
    TaxiStand,

    #[serde(rename = "TRAIN_STATION")]
    TrainStation,

    #[serde(rename = "TRAM_STOP")]
    TramStop,

    Wifi,
}

#[derive(Serialize, Deserialize)]
pub struct Hours {
    exceptional_closings: Option<Vec<ExceptionalPeriod>>,

    exceptional_openings: Option<Vec<ExceptionalPeriod>>,

    regular_hours: Option<Vec<RegularHours>>,

    twentyfourseven: bool,
}

#[derive(Serialize, Deserialize)]
pub struct ExceptionalPeriod {
    period_begin: String,

    period_end: String,
}

#[derive(Serialize, Deserialize)]
pub struct RegularHours {
    period_begin: String,

    period_end: String,

    weekday: i64,
}

#[derive(Serialize, Deserialize)]
pub struct Parking {
    apds_reference: Option<String>,

    dangerous_goods_allowed: Option<bool>,

    direction: Option<ParkingDirection>,

    drive_through: Option<bool>,

    id: String,

    images: Option<Vec<Image>>,

    lighting: Option<bool>,

    max_vehicle_height: Option<f64>,

    max_vehicle_length: Option<f64>,

    max_vehicle_weight: Option<f64>,

    max_vehicle_width: Option<f64>,

    parking_space_length: Option<f64>,

    parking_space_width: Option<f64>,

    physical_reference: Option<String>,

    refrigeration_outlet: Option<bool>,

    reservation_required: bool,

    restricted_to_type: bool,

    roofed: Option<bool>,

    standards: Option<Vec<String>>,

    time_limit: Option<f64>,

    vehicle_types: Vec<VehicleType>,
}

#[derive(Serialize, Deserialize)]
pub enum ParkingDirection {
    #[serde(rename = "ANGLE")]
    Angle,

    #[serde(rename = "PARALLEL")]
    Parallel,

    #[serde(rename = "PERPENDICULAR")]
    Perpendicular,
}

#[derive(Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum ParkingType {
    #[serde(rename = "ALONG_MOTORWAY")]
    AlongMotorway,

    #[serde(rename = "ON_DRIVEWAY")]
    OnDriveway,

    #[serde(rename = "ON_STREET")]
    OnStreet,

    #[serde(rename = "PARKING_GARAGE")]
    ParkingGarage,

    #[serde(rename = "PARKING_LOT")]
    ParkingLot,

    #[serde(rename = "UNDERGROUND_GARAGE")]
    UndergroundGarage,
}

#[derive(Serialize, Deserialize)]
pub struct PublishTokenType {
    group_id: Option<String>,

    issuer: Option<String>,

    #[serde(rename = "type")]
    publish_token_type_type: Option<TokenType>,

    uid: Option<String>,

    visual_number: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct AdditionalGeoLocation {
    latitude: String,

    longitude: String,

    name: Option<DisplayText>,
}

#[derive(Serialize, Deserialize)]
pub struct ReserveNow {
    authorization_reference: Option<String>,

    evse_uid: Option<String>,

    expiry_date: String,

    location_id: String,

    reservation_id: String,

    response_url: String,

    token: Token,
}

#[derive(Serialize, Deserialize)]
pub struct Session {
    auth_method: AuthMethod,

    authorization_reference: Option<String>,

    cdr_token: CdrToken,

    charging_periods: Option<Vec<ChargingPeriod>>,

    connector_id: String,

    country_code: String,

    currency: String,

    end_date_time: Option<String>,

    evse_uid: String,

    id: String,

    kwh: f64,

    last_updated: String,

    location_id: String,

    meter_id: Option<String>,

    party_id: String,

    start_date_time: String,

    status: SessionStatus,

    total_cost: Option<Price>,
}

#[derive(Serialize, Deserialize)]
pub enum SessionStatus {
    #[serde(rename = "ACTIVE")]
    Active,

    #[serde(rename = "COMPLETED")]
    Completed,

    #[serde(rename = "INVALID")]
    Invalid,

    #[serde(rename = "PENDING")]
    Pending,

    #[serde(rename = "RESERVATION")]
    Reservation,
}

#[derive(Serialize, Deserialize)]
pub struct SetChargingProfile {
    charging_profile: ChargingProfile,

    response_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct StartSession {
    authorization_reference: Option<String>,

    connector_id: Option<String>,

    evse_uid: Option<String>,

    location_id: String,

    response_url: String,

    token: Token,
}

#[derive(Serialize, Deserialize)]
pub struct StopSession {
    response_url: String,

    session_id: String,
}

#[derive(Serialize, Deserialize)]
pub struct UnlockConnector {
    connector_id: String,

    evse_uid: String,

    location_id: String,

    response_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct Version {
    url: String,

    version: VersionNumber,
}

#[derive(Serialize, Deserialize)]
pub enum VersionNumber {
    #[serde(rename = "2.0")]
    The20,

    #[serde(rename = "2.1")]
    The21,

    #[serde(rename = "2.1.1")]
    The211,

    #[serde(rename = "2.2")]
    The22,

    #[serde(rename = "2.2.1")]
    The221,

    #[serde(rename = "2.3.0")]
    The230,
}

#[derive(Serialize, Deserialize)]
pub struct VersionDetails {
    endpoints: Vec<Endpoint>,

    version: VersionNumber,
}
