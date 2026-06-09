// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    v221, err := UnmarshalV221(bytes)
//    bytes, err = v221.Marshal()

package main

import "encoding/json"

func UnmarshalV221(data []byte) (V221, error) {
	var r V221
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *V221) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type V221 struct {
	ActiveChargingProfile       *ActiveChargingProfile       `json:"active_charging_profile,omitempty"`
	ActiveChargingProfileResult *ActiveChargingProfileResult `json:"active_charging_profile_result,omitempty"`
	AuthorizationInfo           *AuthorizationInfo           `json:"authorization_info,omitempty"`
	CancelReservation           *CancelReservation           `json:"cancel_reservation,omitempty"`
	Cdr                         *Cdr                         `json:"cdr,omitempty"`
	ChargingPreferences         *ChargingPreferences         `json:"charging_preferences,omitempty"`
	ChargingProfile             *ChargingProfile             `json:"charging_profile,omitempty"`
	ChargingProfileResponse     *ChargingProfileResponse     `json:"charging_profile_response,omitempty"`
	ChargingProfileResult       *ChargingProfileResult       `json:"charging_profile_result,omitempty"`
	ClearProfileResult          *ClearProfileResult          `json:"clear_profile_result,omitempty"`
	CommandResponse             *CommandResponse             `json:"command_response,omitempty"`
	CommandResult               *CommandResult               `json:"command_result,omitempty"`
	Connector                   *Connector                   `json:"connector,omitempty"`
	Credentials                 *CredentialsClass            `json:"credentials,omitempty"`
	Endpoint                    *Endpoint                    `json:"endpoint,omitempty"`
	Evse                        *Evse                        `json:"evse,omitempty"`
	HubClientInfo               *HubClientInfo               `json:"hub_client_info,omitempty"`
	Location                    *LocationClass               `json:"location,omitempty"`
	LocationReferences          *LocationReferences          `json:"location_references,omitempty"`
	ReserveNow                  *ReserveNow                  `json:"reserve_now,omitempty"`
	Session                     *Session                     `json:"session,omitempty"`
	SetChargingProfile          *SetChargingProfile          `json:"set_charging_profile,omitempty"`
	StartSession                *StartSession                `json:"start_session,omitempty"`
	StopSession                 *StopSession                 `json:"stop_session,omitempty"`
	Tariff                      *Tariff                      `json:"tariff,omitempty"`
	Token                       *Token                       `json:"token,omitempty"`
	UnlockConnector             *UnlockConnector             `json:"unlock_connector,omitempty"`
	Version                     *Version                     `json:"version,omitempty"`
	VersionDetails              *VersionDetails              `json:"version_details,omitempty"`
}

type ActiveChargingProfile struct {
	ChargingProfile ChargingProfile `json:"charging_profile"`
	StartDateTime   string          `json:"start_date_time"`
}

type ChargingProfile struct {
	ChargingProfilePeriod []ChargingProfilePeriod `json:"charging_profile_period"`
	ChargingRateUnit      ChargingRateUnit        `json:"charging_rate_unit"`
	Duration              *int64                  `json:"duration"`
	MinChargingRate       *float64                `json:"min_charging_rate"`
	StartDateTime         *string                 `json:"start_date_time"`
}

type ChargingProfilePeriod struct {
	Limit       float64 `json:"limit"`
	StartPeriod int64   `json:"start_period"`
}

type ActiveChargingProfileResult struct {
	Profile *ActiveChargingProfile    `json:"profile"`
	Result  ChargingProfileResultType `json:"result"`
}

type AuthorizationInfo struct {
	Allowed                AllowedType         `json:"allowed"`
	AuthorizationReference *string             `json:"authorization_reference"`
	Info                   *DisplayText        `json:"info"`
	Location               *LocationReferences `json:"location"`
	Token                  Token               `json:"token"`
}

type DisplayText struct {
	Language string `json:"language"`
	Text     string `json:"text"`
}

type LocationReferences struct {
	EvseUids   []string `json:"evse_uids"`
	LocationID string   `json:"location_id"`
}

type Token struct {
	ContractID         string          `json:"contract_id"`
	CountryCode        string          `json:"country_code"`
	DefaultProfileType *ProfileType    `json:"default_profile_type"`
	EnergyContract     *EnergyContract `json:"energy_contract"`
	GroupID            *string         `json:"group_id"`
	Issuer             string          `json:"issuer"`
	Language           *string         `json:"language"`
	LastUpdated        string          `json:"last_updated"`
	PartyID            string          `json:"party_id"`
	Type               TokenType       `json:"type"`
	Uid                string          `json:"uid"`
	Valid              bool            `json:"valid"`
	VisualNumber       *string         `json:"visual_number"`
	Whitelist          WhitelistType   `json:"whitelist"`
}

type EnergyContract struct {
	ContractID   *string `json:"contract_id"`
	SupplierName string  `json:"supplier_name"`
}

type CancelReservation struct {
	ReservationID string `json:"reservation_id"`
	ResponseURL   string `json:"response_url"`
}

type Cdr struct {
	AuthMethod               AuthMethod       `json:"auth_method"`
	AuthorizationReference   *string          `json:"authorization_reference"`
	CdrLocation              CdrLocation      `json:"cdr_location"`
	CdrToken                 CdrToken         `json:"cdr_token"`
	ChargingPeriods          []ChargingPeriod `json:"charging_periods"`
	CountryCode              string           `json:"country_code"`
	Credit                   *bool            `json:"credit"`
	CreditReferenceID        *string          `json:"credit_reference_id"`
	Currency                 string           `json:"currency"`
	EndDateTime              string           `json:"end_date_time"`
	HomeChargingCompensation *bool            `json:"home_charging_compensation"`
	ID                       string           `json:"id"`
	InvoiceReferenceID       *string          `json:"invoice_reference_id"`
	LastUpdated              string           `json:"last_updated"`
	MeterID                  *string          `json:"meter_id"`
	PartyID                  string           `json:"party_id"`
	Remark                   *string          `json:"remark"`
	SessionID                *string          `json:"session_id"`
	SignedData               *SignedData      `json:"signed_data"`
	StartDateTime            string           `json:"start_date_time"`
	Tariffs                  []Tariff         `json:"tariffs"`
	TotalCost                Price            `json:"total_cost"`
	TotalEnergy              float64          `json:"total_energy"`
	TotalEnergyCost          *Price           `json:"total_energy_cost"`
	TotalFixedCost           *Price           `json:"total_fixed_cost"`
	TotalParkingCost         *Price           `json:"total_parking_cost"`
	TotalParkingTime         *float64         `json:"total_parking_time"`
	TotalReservationCost     *Price           `json:"total_reservation_cost"`
	TotalTime                float64          `json:"total_time"`
	TotalTimeCost            *Price           `json:"total_time_cost"`
}

type CdrLocation struct {
	Address            string          `json:"address"`
	City               string          `json:"city"`
	ConnectorFormat    ConnectorFormat `json:"connector_format"`
	ConnectorID        string          `json:"connector_id"`
	ConnectorPowerType PowerType       `json:"connector_power_type"`
	ConnectorStandard  ConnectorType   `json:"connector_standard"`
	Coordinates        GeoLocation     `json:"coordinates"`
	Country            string          `json:"country"`
	EvseID             string          `json:"evse_id"`
	EvseUid            string          `json:"evse_uid"`
	ID                 string          `json:"id"`
	Name               *string         `json:"name"`
	PostalCode         *string         `json:"postal_code"`
	State              *string         `json:"state"`
}

type GeoLocation struct {
	Latitude  string `json:"latitude"`
	Longitude string `json:"longitude"`
}

type CdrToken struct {
	ContractID  string    `json:"contract_id"`
	CountryCode string    `json:"country_code"`
	PartyID     string    `json:"party_id"`
	Type        TokenType `json:"type"`
	Uid         string    `json:"uid"`
}

type ChargingPeriod struct {
	Dimensions    []CdrDimension `json:"dimensions"`
	StartDateTime string         `json:"start_date_time"`
	TariffID      *string        `json:"tariff_id"`
}

type CdrDimension struct {
	Type   CdrDimensionType `json:"type"`
	Volume float64          `json:"volume"`
}

type SignedData struct {
	EncodingMethod        string        `json:"encoding_method"`
	EncodingMethodVersion *int64        `json:"encoding_method_version"`
	PublicKey             *string       `json:"public_key"`
	SignedValues          []SignedValue `json:"signed_values"`
	URL                   *string       `json:"url"`
}

type SignedValue struct {
	Nature     string `json:"nature"`
	PlainData  string `json:"plain_data"`
	SignedData string `json:"signed_data"`
}

type Tariff struct {
	CountryCode   string          `json:"country_code"`
	Currency      string          `json:"currency"`
	Elements      []TariffElement `json:"elements"`
	EndDateTime   *string         `json:"end_date_time"`
	EnergyMix     *EnergyMix      `json:"energy_mix"`
	ID            string          `json:"id"`
	LastUpdated   string          `json:"last_updated"`
	MaxPrice      *Price          `json:"max_price"`
	MinPrice      *Price          `json:"min_price"`
	PartyID       string          `json:"party_id"`
	StartDateTime *string         `json:"start_date_time"`
	TariffAltText []DisplayText   `json:"tariff_alt_text"`
	TariffAltURL  *string         `json:"tariff_alt_url"`
	Type          *TariffType     `json:"type"`
}

type TariffElement struct {
	PriceComponents []PriceComponent    `json:"price_components"`
	Restrictions    *TariffRestrictions `json:"restrictions"`
}

type PriceComponent struct {
	Price    float64             `json:"price"`
	StepSize int64               `json:"step_size"`
	Type     TariffDimensionType `json:"type"`
	Vat      *float64            `json:"vat"`
}

type TariffRestrictions struct {
	DayOfWeek   []DayOfWeek                 `json:"day_of_week"`
	EndDate     *string                     `json:"end_date"`
	EndTime     *string                     `json:"end_time"`
	MaxCurrent  *float64                    `json:"max_current"`
	MaxDuration *int64                      `json:"max_duration"`
	MaxKwh      *float64                    `json:"max_kwh"`
	MaxPower    *float64                    `json:"max_power"`
	MinCurrent  *float64                    `json:"min_current"`
	MinDuration *int64                      `json:"min_duration"`
	MinKwh      *float64                    `json:"min_kwh"`
	MinPower    *float64                    `json:"min_power"`
	Reservation *ReservationRestrictionType `json:"reservation"`
	StartDate   *string                     `json:"start_date"`
	StartTime   *string                     `json:"start_time"`
}

type EnergyMix struct {
	EnergyProductName *string               `json:"energy_product_name"`
	EnergySources     []EnergySource        `json:"energy_sources"`
	EnvironImpact     []EnvironmentalImpact `json:"environ_impact"`
	IsGreenEnergy     bool                  `json:"is_green_energy"`
	SupplierName      *string               `json:"supplier_name"`
}

type EnergySource struct {
	Percentage float64              `json:"percentage"`
	Source     EnergySourceCategory `json:"source"`
}

type EnvironmentalImpact struct {
	Amount   float64                     `json:"amount"`
	Category EnvironmentalImpactCategory `json:"category"`
}

type Price struct {
	ExclVat float64  `json:"excl_vat"`
	InclVat *float64 `json:"incl_vat"`
}

type ChargingPreferences struct {
	DepartureTime    *string     `json:"departure_time"`
	DischargeAllowed *bool       `json:"discharge_allowed"`
	EnergyNeed       *float64    `json:"energy_need"`
	ProfileType      ProfileType `json:"profile_type"`
}

type ChargingProfileResponse struct {
	Result  ChargingProfileResponseType `json:"result"`
	Timeout int64                       `json:"timeout"`
}

type ChargingProfileResult struct {
	Result ChargingProfileResultType `json:"result"`
}

type ClearProfileResult struct {
	Result ChargingProfileResultType `json:"result"`
}

type CommandResponse struct {
	Message []DisplayText       `json:"message"`
	Result  CommandResponseType `json:"result"`
	Timeout int64               `json:"timeout"`
}

type CommandResult struct {
	Message []DisplayText     `json:"message"`
	Result  CommandResultType `json:"result"`
}

type Connector struct {
	Format             ConnectorFormat `json:"format"`
	ID                 string          `json:"id"`
	LastUpdated        string          `json:"last_updated"`
	MaxAmperage        int64           `json:"max_amperage"`
	MaxElectricPower   *int64          `json:"max_electric_power"`
	MaxVoltage         int64           `json:"max_voltage"`
	PowerType          PowerType       `json:"power_type"`
	Standard           ConnectorType   `json:"standard"`
	TariffIDS          []string        `json:"tariff_ids"`
	TermsAndConditions *string         `json:"terms_and_conditions"`
}

type CredentialsClass struct {
	Roles []CredentialsRole `json:"roles"`
	Token string            `json:"token"`
	URL   string            `json:"url"`
}

type CredentialsRole struct {
	BusinessDetails BusinessDetails `json:"business_details"`
	CountryCode     string          `json:"country_code"`
	PartyID         string          `json:"party_id"`
	Role            Role            `json:"role"`
}

type BusinessDetails struct {
	Logo    *Image  `json:"logo"`
	Name    string  `json:"name"`
	Website *string `json:"website"`
}

type Image struct {
	Category  ImageCategory `json:"category"`
	Height    *int64        `json:"height"`
	Thumbnail *string       `json:"thumbnail"`
	Type      string        `json:"type"`
	URL       string        `json:"url"`
	Width     *int64        `json:"width"`
}

type Endpoint struct {
	Identifier ModuleID      `json:"identifier"`
	Role       InterfaceRole `json:"role"`
	URL        string        `json:"url"`
}

type Evse struct {
	Capabilities        []Capability         `json:"capabilities"`
	Connectors          []Connector          `json:"connectors"`
	Coordinates         *GeoLocation         `json:"coordinates"`
	Directions          []DisplayText        `json:"directions"`
	EvseID              *string              `json:"evse_id"`
	FloorLevel          *string              `json:"floor_level"`
	Images              []Image              `json:"images"`
	LastUpdated         string               `json:"last_updated"`
	ParkingRestrictions []ParkingRestriction `json:"parking_restrictions"`
	PhysicalReference   *string              `json:"physical_reference"`
	Status              Status               `json:"status"`
	StatusSchedule      []StatusSchedule     `json:"status_schedule"`
	Uid                 string               `json:"uid"`
}

type StatusSchedule struct {
	PeriodBegin string  `json:"period_begin"`
	PeriodEnd   *string `json:"period_end"`
	Status      Status  `json:"status"`
}

type HubClientInfo struct {
	CountryCode string           `json:"country_code"`
	LastUpdated string           `json:"last_updated"`
	PartyID     string           `json:"party_id"`
	Role        Role             `json:"role"`
	Status      ConnectionStatus `json:"status"`
}

type LocationClass struct {
	Address            string                  `json:"address"`
	ChargingWhenClosed *bool                   `json:"charging_when_closed"`
	City               string                  `json:"city"`
	Coordinates        GeoLocation             `json:"coordinates"`
	Country            string                  `json:"country"`
	CountryCode        string                  `json:"country_code"`
	Directions         []DisplayText           `json:"directions"`
	EnergyMix          *EnergyMix              `json:"energy_mix"`
	Evses              []Evse                  `json:"evses"`
	Facilities         []Facility              `json:"facilities"`
	ID                 string                  `json:"id"`
	Images             []Image                 `json:"images"`
	LastUpdated        string                  `json:"last_updated"`
	Name               *string                 `json:"name"`
	OpeningTimes       *Hours                  `json:"opening_times"`
	Operator           *BusinessDetails        `json:"operator"`
	Owner              *BusinessDetails        `json:"owner"`
	ParkingType        *ParkingType            `json:"parking_type"`
	PartyID            string                  `json:"party_id"`
	PostalCode         *string                 `json:"postal_code"`
	Publish            bool                    `json:"publish"`
	PublishAllowedTo   []PublishTokenType      `json:"publish_allowed_to"`
	RelatedLocations   []AdditionalGeoLocation `json:"related_locations"`
	State              *string                 `json:"state"`
	Suboperator        *BusinessDetails        `json:"suboperator"`
	TimeZone           string                  `json:"time_zone"`
}

type Hours struct {
	ExceptionalClosings []ExceptionalPeriod `json:"exceptional_closings"`
	ExceptionalOpenings []ExceptionalPeriod `json:"exceptional_openings"`
	RegularHours        []RegularHours      `json:"regular_hours"`
	Twentyfourseven     bool                `json:"twentyfourseven"`
}

type ExceptionalPeriod struct {
	PeriodBegin string `json:"period_begin"`
	PeriodEnd   string `json:"period_end"`
}

type RegularHours struct {
	PeriodBegin string `json:"period_begin"`
	PeriodEnd   string `json:"period_end"`
	Weekday     int64  `json:"weekday"`
}

type PublishTokenType struct {
	GroupID      *string    `json:"group_id"`
	Issuer       *string    `json:"issuer"`
	Type         *TokenType `json:"type"`
	Uid          *string    `json:"uid"`
	VisualNumber *string    `json:"visual_number"`
}

type AdditionalGeoLocation struct {
	Latitude  string       `json:"latitude"`
	Longitude string       `json:"longitude"`
	Name      *DisplayText `json:"name"`
}

type ReserveNow struct {
	AuthorizationReference *string `json:"authorization_reference"`
	EvseUid                *string `json:"evse_uid"`
	ExpiryDate             string  `json:"expiry_date"`
	LocationID             string  `json:"location_id"`
	ReservationID          string  `json:"reservation_id"`
	ResponseURL            string  `json:"response_url"`
	Token                  Token   `json:"token"`
}

type Session struct {
	AuthMethod             AuthMethod       `json:"auth_method"`
	AuthorizationReference *string          `json:"authorization_reference"`
	CdrToken               CdrToken         `json:"cdr_token"`
	ChargingPeriods        []ChargingPeriod `json:"charging_periods"`
	ConnectorID            string           `json:"connector_id"`
	CountryCode            string           `json:"country_code"`
	Currency               string           `json:"currency"`
	EndDateTime            *string          `json:"end_date_time"`
	EvseUid                string           `json:"evse_uid"`
	ID                     string           `json:"id"`
	Kwh                    float64          `json:"kwh"`
	LastUpdated            string           `json:"last_updated"`
	LocationID             string           `json:"location_id"`
	MeterID                *string          `json:"meter_id"`
	PartyID                string           `json:"party_id"`
	StartDateTime          string           `json:"start_date_time"`
	Status                 SessionStatus    `json:"status"`
	TotalCost              *Price           `json:"total_cost"`
}

type SetChargingProfile struct {
	ChargingProfile ChargingProfile `json:"charging_profile"`
	ResponseURL     string          `json:"response_url"`
}

type StartSession struct {
	AuthorizationReference *string `json:"authorization_reference"`
	ConnectorID            *string `json:"connector_id"`
	EvseUid                *string `json:"evse_uid"`
	LocationID             string  `json:"location_id"`
	ResponseURL            string  `json:"response_url"`
	Token                  Token   `json:"token"`
}

type StopSession struct {
	ResponseURL string `json:"response_url"`
	SessionID   string `json:"session_id"`
}

type UnlockConnector struct {
	ConnectorID string `json:"connector_id"`
	EvseUid     string `json:"evse_uid"`
	LocationID  string `json:"location_id"`
	ResponseURL string `json:"response_url"`
}

type Version struct {
	URL     string        `json:"url"`
	Version VersionNumber `json:"version"`
}

type VersionDetails struct {
	Endpoints []Endpoint    `json:"endpoints"`
	Version   VersionNumber `json:"version"`
}

type ChargingRateUnit string

const (
	A ChargingRateUnit = "A"
	W ChargingRateUnit = "W"
)

type ChargingProfileResultType string

const (
	ChargingProfileResultTypeACCEPTED ChargingProfileResultType = "ACCEPTED"
	ChargingProfileResultTypeREJECTED ChargingProfileResultType = "REJECTED"
	ChargingProfileResultTypeUNKNOWN  ChargingProfileResultType = "UNKNOWN"
)

type AllowedType string

const (
	AllowedTypeALLOWED AllowedType = "ALLOWED"
	AllowedTypeBLOCKED AllowedType = "BLOCKED"
	Expired            AllowedType = "EXPIRED"
	NoCredit           AllowedType = "NO_CREDIT"
	NotAllowed         AllowedType = "NOT_ALLOWED"
)

type ProfileType string

const (
	Cheap              ProfileType = "CHEAP"
	Fast               ProfileType = "FAST"
	Green              ProfileType = "GREEN"
	ProfileTypeREGULAR ProfileType = "REGULAR"
)

type TokenType string

const (
	AdHocUser      TokenType = "AD_HOC_USER"
	AppUser        TokenType = "APP_USER"
	RFID           TokenType = "RFID"
	TokenTypeOTHER TokenType = "OTHER"
)

type WhitelistType string

const (
	AllowedOffline       WhitelistType = "ALLOWED_OFFLINE"
	Always               WhitelistType = "ALWAYS"
	Never                WhitelistType = "NEVER"
	WhitelistTypeALLOWED WhitelistType = "ALLOWED"
)

type AuthMethod string

const (
	AuthRequest AuthMethod = "AUTH_REQUEST"
	Command     AuthMethod = "COMMAND"
	Whitelist   AuthMethod = "WHITELIST"
)

type ConnectorFormat string

const (
	Cable  ConnectorFormat = "CABLE"
	Socket ConnectorFormat = "SOCKET"
)

type PowerType string

const (
	AC1_Phase      PowerType = "AC_1_PHASE"
	AC2_Phase      PowerType = "AC_2_PHASE"
	AC2_PhaseSplit PowerType = "AC_2_PHASE_SPLIT"
	AC3_Phase      PowerType = "AC_3_PHASE"
	Dc             PowerType = "DC"
)

type ConnectorType string

const (
	Chademo             ConnectorType = "CHADEMO"
	Chaoji              ConnectorType = "CHAOJI"
	DomesticA           ConnectorType = "DOMESTIC_A"
	DomesticB           ConnectorType = "DOMESTIC_B"
	DomesticC           ConnectorType = "DOMESTIC_C"
	DomesticD           ConnectorType = "DOMESTIC_D"
	DomesticE           ConnectorType = "DOMESTIC_E"
	DomesticF           ConnectorType = "DOMESTIC_F"
	DomesticG           ConnectorType = "DOMESTIC_G"
	DomesticH           ConnectorType = "DOMESTIC_H"
	DomesticI           ConnectorType = "DOMESTIC_I"
	DomesticJ           ConnectorType = "DOMESTIC_J"
	DomesticK           ConnectorType = "DOMESTIC_K"
	DomesticL           ConnectorType = "DOMESTIC_L"
	DomesticM           ConnectorType = "DOMESTIC_M"
	DomesticN           ConnectorType = "DOMESTIC_N"
	DomesticO           ConnectorType = "DOMESTIC_O"
	GbtAC               ConnectorType = "GBT_AC"
	GbtDc               ConnectorType = "GBT_DC"
	IEC60309_2_Single16 ConnectorType = "IEC_60309_2_single_16"
	IEC60309_2_Three16  ConnectorType = "IEC_60309_2_three_16"
	IEC60309_2_Three32  ConnectorType = "IEC_60309_2_three_32"
	IEC60309_2_Three64  ConnectorType = "IEC_60309_2_three_64"
	IEC62196_T1         ConnectorType = "IEC_62196_T1"
	IEC62196_T1Combo    ConnectorType = "IEC_62196_T1_COMBO"
	IEC62196_T2         ConnectorType = "IEC_62196_T2"
	IEC62196_T2Combo    ConnectorType = "IEC_62196_T2_COMBO"
	IEC62196_T3A        ConnectorType = "IEC_62196_T3A"
	IEC62196_T3C        ConnectorType = "IEC_62196_T3C"
	Nema10_30           ConnectorType = "NEMA_10_30"
	Nema10_50           ConnectorType = "NEMA_10_50"
	Nema14_30           ConnectorType = "NEMA_14_30"
	Nema14_50           ConnectorType = "NEMA_14_50"
	Nema5_20            ConnectorType = "NEMA_5_20"
	Nema6_30            ConnectorType = "NEMA_6_30"
	Nema6_50            ConnectorType = "NEMA_6_50"
	PantographBottomUp  ConnectorType = "PANTOGRAPH_BOTTOM_UP"
	PantographTopDown   ConnectorType = "PANTOGRAPH_TOP_DOWN"
	TeslaR              ConnectorType = "TESLA_R"
	TeslaS              ConnectorType = "TESLA_S"
)

type CdrDimensionType string

const (
	CdrDimensionTypeENERGY      CdrDimensionType = "ENERGY"
	CdrDimensionTypePARKINGTIME CdrDimensionType = "PARKING_TIME"
	CdrDimensionTypeTIME        CdrDimensionType = "TIME"
	Current                     CdrDimensionType = "CURRENT"
	EnergyExport                CdrDimensionType = "ENERGY_EXPORT"
	EnergyImport                CdrDimensionType = "ENERGY_IMPORT"
	MaxCurrent                  CdrDimensionType = "MAX_CURRENT"
	MaxPower                    CdrDimensionType = "MAX_POWER"
	MinCurrent                  CdrDimensionType = "MIN_CURRENT"
	MinPower                    CdrDimensionType = "MIN_POWER"
	Power                       CdrDimensionType = "POWER"
	ReservationTime             CdrDimensionType = "RESERVATION_TIME"
	StateOfCharge               CdrDimensionType = "STATE_OF_CHARGE"
)

type TariffDimensionType string

const (
	Flat                           TariffDimensionType = "FLAT"
	TariffDimensionTypeENERGY      TariffDimensionType = "ENERGY"
	TariffDimensionTypePARKINGTIME TariffDimensionType = "PARKING_TIME"
	TariffDimensionTypeTIME        TariffDimensionType = "TIME"
)

type DayOfWeek string

const (
	Friday    DayOfWeek = "FRIDAY"
	Monday    DayOfWeek = "MONDAY"
	Saturday  DayOfWeek = "SATURDAY"
	Sunday    DayOfWeek = "SUNDAY"
	Thursday  DayOfWeek = "THURSDAY"
	Tuesday   DayOfWeek = "TUESDAY"
	Wednesday DayOfWeek = "WEDNESDAY"
)

type ReservationRestrictionType string

const (
	ReservationExpires                    ReservationRestrictionType = "RESERVATION_EXPIRES"
	ReservationRestrictionTypeRESERVATION ReservationRestrictionType = "RESERVATION"
)

type EnergySourceCategory string

const (
	Coal          EnergySourceCategory = "COAL"
	Gas           EnergySourceCategory = "GAS"
	GeneralFossil EnergySourceCategory = "GENERAL_FOSSIL"
	GeneralGreen  EnergySourceCategory = "GENERAL_GREEN"
	Nuclear       EnergySourceCategory = "NUCLEAR"
	Solar         EnergySourceCategory = "SOLAR"
	Water         EnergySourceCategory = "WATER"
	Wind          EnergySourceCategory = "WIND"
)

type EnvironmentalImpactCategory string

const (
	CarbonDioxide EnvironmentalImpactCategory = "CARBON_DIOXIDE"
	NuclearWaste  EnvironmentalImpactCategory = "NUCLEAR_WASTE"
)

type TariffType string

const (
	AdHocPayment      TariffType = "AD_HOC_PAYMENT"
	ProfileCheap      TariffType = "PROFILE_CHEAP"
	ProfileFast       TariffType = "PROFILE_FAST"
	ProfileGreen      TariffType = "PROFILE_GREEN"
	TariffTypeREGULAR TariffType = "REGULAR"
)

type ChargingProfileResponseType string

const (
	ChargingProfileResponseTypeACCEPTED       ChargingProfileResponseType = "ACCEPTED"
	ChargingProfileResponseTypeNOTSUPPORTED   ChargingProfileResponseType = "NOT_SUPPORTED"
	ChargingProfileResponseTypeREJECTED       ChargingProfileResponseType = "REJECTED"
	ChargingProfileResponseTypeUNKNOWNSESSION ChargingProfileResponseType = "UNKNOWN_SESSION"
	TooOften                                  ChargingProfileResponseType = "TOO_OFTEN"
)

type CommandResponseType string

const (
	CommandResponseTypeACCEPTED       CommandResponseType = "ACCEPTED"
	CommandResponseTypeNOTSUPPORTED   CommandResponseType = "NOT_SUPPORTED"
	CommandResponseTypeREJECTED       CommandResponseType = "REJECTED"
	CommandResponseTypeUNKNOWNSESSION CommandResponseType = "UNKNOWN_SESSION"
)

type CommandResultType string

const (
	CanceledReservation           CommandResultType = "CANCELED_RESERVATION"
	CommandResultTypeACCEPTED     CommandResultType = "ACCEPTED"
	CommandResultTypeNOTSUPPORTED CommandResultType = "NOT_SUPPORTED"
	CommandResultTypeREJECTED     CommandResultType = "REJECTED"
	EvseInoperative               CommandResultType = "EVSE_INOPERATIVE"
	EvseOccupied                  CommandResultType = "EVSE_OCCUPIED"
	Failed                        CommandResultType = "FAILED"
	Timeout                       CommandResultType = "TIMEOUT"
	UnknownReservation            CommandResultType = "UNKNOWN_RESERVATION"
)

type ImageCategory string

const (
	Charger            ImageCategory = "CHARGER"
	Entrance           ImageCategory = "ENTRANCE"
	ImageCategoryOTHER ImageCategory = "OTHER"
	Location           ImageCategory = "LOCATION"
	Network            ImageCategory = "NETWORK"
	Operator           ImageCategory = "OPERATOR"
	Owner              ImageCategory = "OWNER"
)

type Role string

const (
	Cpo       Role = "CPO"
	Emsp      Role = "EMSP"
	Hub       Role = "HUB"
	Nap       Role = "NAP"
	Nsp       Role = "NSP"
	RoleOTHER Role = "OTHER"
	Scsp      Role = "SCSP"
)

type ModuleID string

const (
	Cdrs             ModuleID = "cdrs"
	Chargingprofiles ModuleID = "chargingprofiles"
	Commands         ModuleID = "commands"
	Credentials      ModuleID = "credentials"
	Hubclientinfo    ModuleID = "hubclientinfo"
	Locations        ModuleID = "locations"
	Sessions         ModuleID = "sessions"
	Tariffs          ModuleID = "tariffs"
	Tokens           ModuleID = "tokens"
)

type InterfaceRole string

const (
	Receiver InterfaceRole = "RECEIVER"
	Sender   InterfaceRole = "SENDER"
)

type Capability string

const (
	ChargingPreferencesCapable    Capability = "CHARGING_PREFERENCES_CAPABLE"
	ChargingProfileCapable        Capability = "CHARGING_PROFILE_CAPABLE"
	ChipCardSupport               Capability = "CHIP_CARD_SUPPORT"
	ContactlessCardSupport        Capability = "CONTACTLESS_CARD_SUPPORT"
	CreditCardPayable             Capability = "CREDIT_CARD_PAYABLE"
	DebitCardPayable              Capability = "DEBIT_CARD_PAYABLE"
	PedTerminal                   Capability = "PED_TERMINAL"
	RFIDReader                    Capability = "RFID_READER"
	RemoteStartStopCapable        Capability = "REMOTE_START_STOP_CAPABLE"
	Reservable                    Capability = "RESERVABLE"
	StartSessionConnectorRequired Capability = "START_SESSION_CONNECTOR_REQUIRED"
	TokenGroupCapable             Capability = "TOKEN_GROUP_CAPABLE"
	UnlockCapable                 Capability = "UNLOCK_CAPABLE"
)

type ParkingRestriction string

const (
	Customers   ParkingRestriction = "CUSTOMERS"
	Disabled    ParkingRestriction = "DISABLED"
	EvOnly      ParkingRestriction = "EV_ONLY"
	Motorcycles ParkingRestriction = "MOTORCYCLES"
	Plugged     ParkingRestriction = "PLUGGED"
)

type Status string

const (
	Available     Status = "AVAILABLE"
	Charging      Status = "CHARGING"
	Inoperative   Status = "INOPERATIVE"
	Outoforder    Status = "OUTOFORDER"
	Removed       Status = "REMOVED"
	Reserved      Status = "RESERVED"
	StatusBLOCKED Status = "BLOCKED"
	StatusPLANNED Status = "PLANNED"
	StatusUNKNOWN Status = "UNKNOWN"
)

type ConnectionStatus string

const (
	Connected               ConnectionStatus = "CONNECTED"
	ConnectionStatusPLANNED ConnectionStatus = "PLANNED"
	Offline                 ConnectionStatus = "OFFLINE"
	Suspended               ConnectionStatus = "SUSPENDED"
)

type Facility string

const (
	Airport            Facility = "AIRPORT"
	BikeSharing        Facility = "BIKE_SHARING"
	BusStop            Facility = "BUS_STOP"
	Cafe               Facility = "CAFE"
	CarpoolParking     Facility = "CARPOOL_PARKING"
	FacilityPARKINGLOT Facility = "PARKING_LOT"
	FuelStation        Facility = "FUEL_STATION"
	Hotel              Facility = "HOTEL"
	Mall               Facility = "MALL"
	MetroStation       Facility = "METRO_STATION"
	Museum             Facility = "MUSEUM"
	Nature             Facility = "NATURE"
	RecreationArea     Facility = "RECREATION_AREA"
	Restaurant         Facility = "RESTAURANT"
	Sport              Facility = "SPORT"
	Supermarket        Facility = "SUPERMARKET"
	TaxiStand          Facility = "TAXI_STAND"
	TrainStation       Facility = "TRAIN_STATION"
	TramStop           Facility = "TRAM_STOP"
	Wifi               Facility = "WIFI"
)

type ParkingType string

const (
	AlongMotorway         ParkingType = "ALONG_MOTORWAY"
	OnDriveway            ParkingType = "ON_DRIVEWAY"
	OnStreet              ParkingType = "ON_STREET"
	ParkingGarage         ParkingType = "PARKING_GARAGE"
	ParkingTypePARKINGLOT ParkingType = "PARKING_LOT"
	UndergroundGarage     ParkingType = "UNDERGROUND_GARAGE"
)

type SessionStatus string

const (
	Active                   SessionStatus = "ACTIVE"
	Completed                SessionStatus = "COMPLETED"
	Invalid                  SessionStatus = "INVALID"
	Pending                  SessionStatus = "PENDING"
	SessionStatusRESERVATION SessionStatus = "RESERVATION"
)

type VersionNumber string

const (
	The20  VersionNumber = "2.0"
	The21  VersionNumber = "2.1"
	The211 VersionNumber = "2.1.1"
	The22  VersionNumber = "2.2"
	The221 VersionNumber = "2.2.1"
)
