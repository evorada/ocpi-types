// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    v230Bookings, err := UnmarshalV230Bookings(bytes)
//    bytes, err = v230Bookings.Marshal()

package v230bookings

import "encoding/json"

func UnmarshalV230Bookings(data []byte) (V230Bookings, error) {
	var r V230Bookings
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *V230Bookings) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type V230Bookings struct {
	ActiveChargingProfile       *ActiveChargingProfile       `json:"active_charging_profile,omitempty"`
	ActiveChargingProfileResult *ActiveChargingProfileResult `json:"active_charging_profile_result,omitempty"`
	AuthorizationInfo           *AuthorizationInfo           `json:"authorization_info,omitempty"`
	Booking                     *BookingClass                `json:"booking,omitempty"`
	BookingLocation             *BookingLocation             `json:"booking_location,omitempty"`
	BookingRequest              *BookingRequest              `json:"booking_request,omitempty"`
	Calendar                    *Calendar                    `json:"calendar,omitempty"`
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
	Token                       *TokenClass                  `json:"token,omitempty"`
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
	Token                  TokenClass          `json:"token"`
}

type DisplayText struct {
	Language string `json:"language"`
	Text     string `json:"text"`
}

type LocationReferences struct {
	EvseUids   []string `json:"evse_uids"`
	LocationID string   `json:"location_id"`
}

type TokenClass struct {
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

type BookingClass struct {
	AccessMethods          []AccessMethod          `json:"access_methods"`
	AuthorizationReference string                  `json:"authorization_reference"`
	BookableParkingOption  *BookableParkingOptions `json:"bookable_parking_option"`
	BookingRequests        []BookingRequestStatus  `json:"booking_requests"`
	BookingTerms           BookingTerms            `json:"booking_terms"`
	BookingTokens          []BookingToken          `json:"booking_tokens"`
	Canceled               *Cancellation           `json:"canceled"`
	ConnectorID            *string                 `json:"connector_id"`
	CountryCode            string                  `json:"country_code"`
	EvseUid                *string                 `json:"evse_uid"`
	ID                     string                  `json:"id"`
	LastUpdated            string                  `json:"last_updated"`
	LocationID             string                  `json:"location_id"`
	ParkingID              *string                 `json:"parking_id"`
	PartyID                string                  `json:"party_id"`
	Period                 Timeslot                `json:"period"`
	RequestID              string                  `json:"request_id"`
	ReservationStatus      ReservationStatus       `json:"reservation_status"`
	TariffID               []string                `json:"tariff_id"`
}

type AccessMethod struct {
	LocationAccess LocationAccess `json:"location_access"`
	Value          *string        `json:"value"`
}

type BookableParkingOptions struct {
	DangerousGoodsAllowed *bool           `json:"dangerous_goods_allowed"`
	DriveThrough          *bool           `json:"drive_through"`
	EvsePosition          *EvsePosition   `json:"evse_position"`
	Format                ConnectorFormat `json:"format"`
	MaxVehicleHeight      *float64        `json:"max_vehicle_height"`
	MaxVehicleLength      *float64        `json:"max_vehicle_length"`
	MaxVehicleWeight      *float64        `json:"max_vehicle_weight"`
	MaxVehicleWidth       *float64        `json:"max_vehicle_width"`
	ParkingSpaceLength    *float64        `json:"parking_space_length"`
	ParkingSpaceWidth     *float64        `json:"parking_space_width"`
	RefrigerationOutlet   *bool           `json:"refrigeration_outlet"`
	RestrictedToType      bool            `json:"restricted_to_type"`
	VehicleTypes          []VehicleType   `json:"vehicle_types"`
}

type BookingRequestStatus struct {
	BookingRequest  BookingRequest           `json:"booking_request"`
	RequestReceived string                   `json:"request_received"`
	RequestStatus   ReservationRequestStatus `json:"request_status"`
}

type BookingRequest struct {
	AuthorizationReference string                  `json:"authorization_reference"`
	BookableParkingOption  *BookableParkingOptions `json:"bookable_parking_option"`
	Canceled               *Cancellation           `json:"canceled"`
	ConnectorID            *string                 `json:"connector_id"`
	CountryCode            string                  `json:"country_code"`
	EvseUid                *string                 `json:"evse_uid"`
	LocationID             string                  `json:"location_id"`
	PartyID                string                  `json:"party_id"`
	Period                 Timeslot                `json:"period"`
	PowerRequired          *int64                  `json:"power_required"`
	RequestID              string                  `json:"request_id"`
	Tokens                 []BookingToken          `json:"tokens"`
}

type Cancellation struct {
	CancellationReason CanceledReason `json:"cancellation_reason"`
	WhoCanceled        Role           `json:"who_canceled"`
}

type Timeslot struct {
	EndBefore          string   `json:"end_before"`
	GreenEnergySupport *bool    `json:"green_energy_support"`
	MaxPower           *float64 `json:"max_power"`
	MinPower           *float64 `json:"min_power"`
	StartFrom          string   `json:"start_from"`
}

type BookingToken struct {
	ContractID  string    `json:"contract_id"`
	CountryCode string    `json:"country_code"`
	PartyID     string    `json:"party_id"`
	Type        TokenType `json:"type"`
	Uid         string    `json:"uid"`
}

type BookingTerms struct {
	BookingTerms               *string          `json:"booking_terms"`
	CancelUntilMinutes         float64          `json:"cancel_until_minutes"`
	ChangeNotAllowed           *bool            `json:"change_not_allowed"`
	ChangeUntilMinutes         float64          `json:"change_until_minutes"`
	EarlyStartAllowed          *bool            `json:"early_start_allowed"`
	EarlyStartTime             *float64         `json:"early_start_time"`
	LateStopAllowed            *bool            `json:"late_stop_allowed"`
	LateStopTime               *float64         `json:"late_stop_time"`
	NoshowFee                  *bool            `json:"noshow_fee"`
	NoshowTimeout              *float64         `json:"noshow_timeout"`
	OverlappingBookingsAllowed *bool            `json:"overlapping_bookings_allowed"`
	RemoteAuthSupported        *bool            `json:"remote_auth_supported"`
	RFIDAuthRequired           *bool            `json:"RFID_auth_required"`
	SupportedAccessMethods     []LocationAccess `json:"supported_access_methods"`
	TokenGroupsSupported       *bool            `json:"token_groups_supported"`
}

type BookingLocation struct {
	Bookable               *Bookable                `json:"bookable"`
	BookableParkingOptions []BookableParkingOptions `json:"bookable_parking_options"`
	BookingTerms           []BookingTerms           `json:"booking_terms"`
	Calendars              []Calendar               `json:"calendars"`
	ConnectorID            *string                  `json:"connector_id"`
	CountryCode            string                   `json:"country_code"`
	EvseUid                *string                  `json:"evse_uid"`
	ID                     string                   `json:"id"`
	LastUpdated            string                   `json:"last_updated"`
	LocationID             string                   `json:"location_id"`
	PartyID                string                   `json:"party_id"`
	TariffID               []string                 `json:"tariff_id"`
}

type Bookable struct {
	AdHoc               *float64 `json:"ad_hoc"`
	ReservationRequired bool     `json:"reservation_required"`
}

type Calendar struct {
	AvailableTimeslots []Timeslot `json:"available_timeslots"`
	BeginFrom          string     `json:"begin_from"`
	EndBefore          string     `json:"end_before"`
	ID                 string     `json:"id"`
	LastUpdated        string     `json:"last_updated"`
	StepSize           *int64     `json:"step_size"`
}

type CancelReservation struct {
	ReservationID string `json:"reservation_id"`
	ResponseURL   string `json:"response_url"`
}

type Cdr struct {
	AuthMethod               AuthMethod       `json:"auth_method"`
	AuthorizationReference   *string          `json:"authorization_reference"`
	BookingID                *string          `json:"booking_id"`
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
	MaxPrice      *PriceLimit     `json:"max_price"`
	MinPrice      *PriceLimit     `json:"min_price"`
	PartyID       string          `json:"party_id"`
	StartDateTime *string         `json:"start_date_time"`
	TariffAltText []DisplayText   `json:"tariff_alt_text"`
	TariffAltURL  *string         `json:"tariff_alt_url"`
	TaxIncluded   TaxIncluded     `json:"tax_included"`
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

type PriceLimit struct {
	AfterTaxes  *float64 `json:"after_taxes"`
	BeforeTaxes float64  `json:"before_taxes"`
}

type Price struct {
	BeforeTaxes float64     `json:"before_taxes"`
	Taxes       []TaxAmount `json:"taxes"`
}

type TaxAmount struct {
	AccountNumber *string  `json:"account_number"`
	Amount        float64  `json:"amount"`
	Name          string   `json:"name"`
	Percentage    *float64 `json:"percentage"`
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
	Capabilities       []ConnectorCapability `json:"capabilities"`
	Format             ConnectorFormat       `json:"format"`
	ID                 string                `json:"id"`
	LastUpdated        string                `json:"last_updated"`
	MaxAmperage        int64                 `json:"max_amperage"`
	MaxElectricPower   *int64                `json:"max_electric_power"`
	MaxVoltage         int64                 `json:"max_voltage"`
	PowerType          PowerType             `json:"power_type"`
	Standard           ConnectorType         `json:"standard"`
	TariffIDS          []string              `json:"tariff_ids"`
	TermsAndConditions *string               `json:"terms_and_conditions"`
}

type CredentialsClass struct {
	HubPartyID *string           `json:"hub_party_id"`
	Roles      []CredentialsRole `json:"roles"`
	Token      string            `json:"token"`
	URL        string            `json:"url"`
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
	AcceptedServiceProviders []string             `json:"accepted_service_providers"`
	Capabilities             []Capability         `json:"capabilities"`
	Connectors               []Connector          `json:"connectors"`
	Coordinates              *GeoLocation         `json:"coordinates"`
	Directions               []DisplayText        `json:"directions"`
	EvseID                   *string              `json:"evse_id"`
	FloorLevel               *string              `json:"floor_level"`
	Images                   []Image              `json:"images"`
	LastUpdated              string               `json:"last_updated"`
	Parking                  []EvseParking        `json:"parking"`
	ParkingRestrictions      []ParkingRestriction `json:"parking_restrictions"`
	PhysicalReference        *string              `json:"physical_reference"`
	Status                   Status               `json:"status"`
	StatusSchedule           []StatusSchedule     `json:"status_schedule"`
	Uid                      string               `json:"uid"`
}

type EvseParking struct {
	EvsePosition *EvsePosition `json:"evse_position"`
	ParkingID    string        `json:"parking_id"`
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
	HelpPhone          *string                 `json:"help_phone"`
	ID                 string                  `json:"id"`
	Images             []Image                 `json:"images"`
	LastUpdated        string                  `json:"last_updated"`
	Name               *string                 `json:"name"`
	OpeningTimes       *Hours                  `json:"opening_times"`
	Operator           *BusinessDetails        `json:"operator"`
	Owner              *BusinessDetails        `json:"owner"`
	ParkingPlaces      []Parking               `json:"parking_places"`
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

type Parking struct {
	ApdsReference         *string           `json:"apds_reference"`
	DangerousGoodsAllowed *bool             `json:"dangerous_goods_allowed"`
	Direction             *ParkingDirection `json:"direction"`
	DriveThrough          *bool             `json:"drive_through"`
	ID                    string            `json:"id"`
	Images                []Image           `json:"images"`
	Lighting              *bool             `json:"lighting"`
	MaxVehicleHeight      *float64          `json:"max_vehicle_height"`
	MaxVehicleLength      *float64          `json:"max_vehicle_length"`
	MaxVehicleWeight      *float64          `json:"max_vehicle_weight"`
	MaxVehicleWidth       *float64          `json:"max_vehicle_width"`
	ParkingSpaceLength    *float64          `json:"parking_space_length"`
	ParkingSpaceWidth     *float64          `json:"parking_space_width"`
	PhysicalReference     *string           `json:"physical_reference"`
	RefrigerationOutlet   *bool             `json:"refrigeration_outlet"`
	ReservationRequired   bool              `json:"reservation_required"`
	RestrictedToType      bool              `json:"restricted_to_type"`
	Roofed                *bool             `json:"roofed"`
	Standards             []string          `json:"standards"`
	TimeLimit             *float64          `json:"time_limit"`
	VehicleTypes          []VehicleType     `json:"vehicle_types"`
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
	AuthorizationReference *string    `json:"authorization_reference"`
	EvseUid                *string    `json:"evse_uid"`
	ExpiryDate             string     `json:"expiry_date"`
	LocationID             string     `json:"location_id"`
	ReservationID          string     `json:"reservation_id"`
	ResponseURL            string     `json:"response_url"`
	Token                  TokenClass `json:"token"`
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
	AuthorizationReference *string    `json:"authorization_reference"`
	ConnectorID            *string    `json:"connector_id"`
	EvseUid                *string    `json:"evse_uid"`
	LocationID             string     `json:"location_id"`
	ResponseURL            string     `json:"response_url"`
	Token                  TokenClass `json:"token"`
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
	AdHocUser             TokenType = "AD_HOC_USER"
	AppUser               TokenType = "APP_USER"
	Emaid                 TokenType = "EMAID"
	RFID                  TokenType = "RFID"
	TokenTypeLICENSEPLATE TokenType = "LICENSE_PLATE"
	TokenTypeOTHER        TokenType = "OTHER"
)

type WhitelistType string

const (
	AllowedOffline       WhitelistType = "ALLOWED_OFFLINE"
	Always               WhitelistType = "ALWAYS"
	Never                WhitelistType = "NEVER"
	WhitelistTypeALLOWED WhitelistType = "ALLOWED"
)

type LocationAccess string

const (
	AccessCode                 LocationAccess = "ACCESS_CODE"
	Intercom                   LocationAccess = "INTERCOM"
	LocationAccessLICENSEPLATE LocationAccess = "LICENSE_PLATE"
	Open                       LocationAccess = "OPEN"
	ParkingTicket              LocationAccess = "PARKING_TICKET"
	Token                      LocationAccess = "TOKEN"
)

type EvsePosition string

const (
	Center EvsePosition = "CENTER"
	Left   EvsePosition = "LEFT"
	Right  EvsePosition = "RIGHT"
)

type ConnectorFormat string

const (
	Cable  ConnectorFormat = "CABLE"
	Socket ConnectorFormat = "SOCKET"
)

type VehicleType string

const (
	Bus                        VehicleType = "BUS"
	Motorcycle                 VehicleType = "MOTORCYCLE"
	PersonalVehicle            VehicleType = "PERSONAL_VEHICLE"
	PersonalVehicleWithTrailer VehicleType = "PERSONAL_VEHICLE_WITH_TRAILER"
	Rigid                      VehicleType = "RIGID"
	SemiTractor                VehicleType = "SEMI_TRACTOR"
	TruckWithTrailer           VehicleType = "TRUCK_WITH_TRAILER"
	Van                        VehicleType = "VAN"
	VehicleTypeDISABLED        VehicleType = "DISABLED"
)

type CanceledReason string

const (
	BrokenCharger         CanceledReason = "BROKEN_CHARGER"
	BrokenVehicle         CanceledReason = "BROKEN_VEHICLE"
	CanceledReasonBLOCKED CanceledReason = "BLOCKED"
	CanceledReasonUNKNOWN CanceledReason = "UNKNOWN"
	Full                  CanceledReason = "FULL"
	NoCanceled            CanceledReason = "NO_CANCELED"
	PowerOutage           CanceledReason = "POWER_OUTAGE"
	Traffic               CanceledReason = "TRAFFIC"
)

type Role string

const (
	Cpo       Role = "CPO"
	Emsp      Role = "EMSP"
	Nap       Role = "NAP"
	Nsp       Role = "NSP"
	RoleOTHER Role = "OTHER"
	Scsp      Role = "SCSP"
)

type ReservationRequestStatus string

const (
	Declined                         ReservationRequestStatus = "DECLINED"
	ReservationRequestStatusACCEPTED ReservationRequestStatus = "ACCEPTED"
	ReservationRequestStatusFAILED   ReservationRequestStatus = "FAILED"
	ReservationRequestStatusPENDING  ReservationRequestStatus = "PENDING"
)

type ReservationStatus string

const (
	Canceled                  ReservationStatus = "CANCELED"
	Fulfilled                 ReservationStatus = "FULFILLED"
	NoShow                    ReservationStatus = "NO_SHOW"
	ReservationStatusFAILED   ReservationStatus = "FAILED"
	ReservationStatusPENDING  ReservationStatus = "PENDING"
	ReservationStatusREJECTED ReservationStatus = "REJECTED"
	ReservationStatusRESERVED ReservationStatus = "RESERVED"
	ReservationStatusUNKNOWN  ReservationStatus = "UNKNOWN"
)

type AuthMethod string

const (
	AuthRequest AuthMethod = "AUTH_REQUEST"
	Command     AuthMethod = "COMMAND"
	Whitelist   AuthMethod = "WHITELIST"
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
	Mcs                 ConnectorType = "MCS"
	Nema10_30           ConnectorType = "NEMA_10_30"
	Nema10_50           ConnectorType = "NEMA_10_50"
	Nema14_30           ConnectorType = "NEMA_14_30"
	Nema14_50           ConnectorType = "NEMA_14_50"
	Nema5_20            ConnectorType = "NEMA_5_20"
	Nema6_30            ConnectorType = "NEMA_6_30"
	Nema6_50            ConnectorType = "NEMA_6_50"
	PantographBottomUp  ConnectorType = "PANTOGRAPH_BOTTOM_UP"
	PantographTopDown   ConnectorType = "PANTOGRAPH_TOP_DOWN"
	SaeJ3400            ConnectorType = "SAE_J3400"
	TeslaR              ConnectorType = "TESLA_R"
	TeslaS              ConnectorType = "TESLA_S"
)

type CdrDimensionType string

const (
	CdrDimensionTypeENERGY              CdrDimensionType = "ENERGY"
	CdrDimensionTypePARKINGTIME         CdrDimensionType = "PARKING_TIME"
	CdrDimensionTypeRESERVATIONEXPIRES  CdrDimensionType = "RESERVATION_EXPIRES"
	CdrDimensionTypeRESERVATIONOVERTIME CdrDimensionType = "RESERVATION_OVERTIME"
	CdrDimensionTypeTIME                CdrDimensionType = "TIME"
	Current                             CdrDimensionType = "CURRENT"
	EnergyExport                        CdrDimensionType = "ENERGY_EXPORT"
	EnergyImport                        CdrDimensionType = "ENERGY_IMPORT"
	MaxCurrent                          CdrDimensionType = "MAX_CURRENT"
	MaxPower                            CdrDimensionType = "MAX_POWER"
	MinCurrent                          CdrDimensionType = "MIN_CURRENT"
	MinPower                            CdrDimensionType = "MIN_POWER"
	Power                               CdrDimensionType = "POWER"
	ReservationTime                     CdrDimensionType = "RESERVATION_TIME"
	StateOfCharge                       CdrDimensionType = "STATE_OF_CHARGE"
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
	ReservationCancellationFees                   ReservationRestrictionType = "RESERVATION_CANCELLATION_FEES"
	ReservationRestrictionTypeRESERVATION         ReservationRestrictionType = "RESERVATION"
	ReservationRestrictionTypeRESERVATIONEXPIRES  ReservationRestrictionType = "RESERVATION_EXPIRES"
	ReservationRestrictionTypeRESERVATIONOVERTIME ReservationRestrictionType = "RESERVATION_OVERTIME"
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

type TaxIncluded string

const (
	NA  TaxIncluded = "N/A"
	No  TaxIncluded = "NO"
	Yes TaxIncluded = "YES"
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
	CommandResultTypeFAILED       CommandResultType = "FAILED"
	CommandResultTypeNOTSUPPORTED CommandResultType = "NOT_SUPPORTED"
	CommandResultTypeREJECTED     CommandResultType = "REJECTED"
	EvseInoperative               CommandResultType = "EVSE_INOPERATIVE"
	EvseOccupied                  CommandResultType = "EVSE_OCCUPIED"
	Timeout                       CommandResultType = "TIMEOUT"
	UnknownReservation            CommandResultType = "UNKNOWN_RESERVATION"
)

type ConnectorCapability string

const (
	ISO15118_20_PlugAndCharge ConnectorCapability = "ISO_15118_20_PLUG_AND_CHARGE"
	ISO15118_2_PlugAndCharge  ConnectorCapability = "ISO_15118_2_PLUG_AND_CHARGE"
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

type ModuleID string

const (
	Booking          ModuleID = "Booking"
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
	Customers                  ParkingRestriction = "CUSTOMERS"
	Employees                  ParkingRestriction = "EMPLOYEES"
	EvOnly                     ParkingRestriction = "EV_ONLY"
	Motorcycles                ParkingRestriction = "MOTORCYCLES"
	ParkingRestrictionDISABLED ParkingRestriction = "DISABLED"
	Plugged                    ParkingRestriction = "PLUGGED"
	Taxis                      ParkingRestriction = "TAXIS"
	Tenants                    ParkingRestriction = "TENANTS"
)

type Status string

const (
	Available      Status = "AVAILABLE"
	Charging       Status = "CHARGING"
	Inoperative    Status = "INOPERATIVE"
	Outoforder     Status = "OUTOFORDER"
	Removed        Status = "REMOVED"
	StatusBLOCKED  Status = "BLOCKED"
	StatusPLANNED  Status = "PLANNED"
	StatusRESERVED Status = "RESERVED"
	StatusUNKNOWN  Status = "UNKNOWN"
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

type ParkingDirection string

const (
	Angle         ParkingDirection = "ANGLE"
	Parallel      ParkingDirection = "PARALLEL"
	Perpendicular ParkingDirection = "PERPENDICULAR"
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
	SessionStatusPENDING     SessionStatus = "PENDING"
	SessionStatusRESERVATION SessionStatus = "RESERVATION"
)

type VersionNumber string

const (
	The20  VersionNumber = "2.0"
	The21  VersionNumber = "2.1"
	The211 VersionNumber = "2.1.1"
	The22  VersionNumber = "2.2"
	The221 VersionNumber = "2.2.1"
	The230 VersionNumber = "2.3.0"
)
