from melissadatacloudapi.RecordRequests import GlobalAddressVerificationRecordRequest
from melissadatacloudapi.cloudapis.GlobalAddressVerification import GlobalAddressVerification
from melissadatacloudapi.apiresponse import GlobalAddressVerificationResponse
from melissadatacloudapi.PostReqestBase import GlobalAddressVerificationPostRequest


def global_address_verification_sample(license_key):
    """
    This function uses the Global Address Verification Cloud API object to make a GET request
    """    
    global_address = GlobalAddressVerification(license_key)
    global_address.set_address_line_1("22382 Avenida Empresa")
    global_address.set_locality("Rancho Santa Margarita")
    global_address.set_administrative_area("CA")
    global_address.set_postal("92688")
    global_address.set_country("United States")
    global_address.set_opt("USExtras:ON")

    response = global_address.get(str)
    response_object = global_address.get(GlobalAddressVerificationResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResult: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print("RecordID:", record.record_id)
        print("Results:", record.results)
        print("Formatted:", record.formatted_address)
        print("Organization:", record.organization)
        print("AddressLine1:", record.get_value("AddressLine1"))
        print("AddressLine1:", record.get_address_line_1())
        print("AddressLine1:", record.address_line_1)
        print("AddressLine2:", record.address_line_2)
        print("AddressLine3:", record.address_line_3)
        print("AddressLine4:", record.address_line_4)
        print("AddressLine5:", record.address_line_5)
        print("AddressLine6:", record.address_line_6)
        print("AddressLine7:", record.address_line_7)
        print("AddressLine8:", record.address_line_8)
        print("SubPremises:", record.sub_premises)
        print("DoubleDependentLocality:", record.double_dependent_locality)
        print("DependentLocality:", record.dependent_locality)
        print("Locality:", record.locality)
        print("SubAdministrativeArea:", record.sub_administrative_area)
        print("AdministrativeArea:", record.administrative_area)
        print("PostalCode:", record.postal_code)
        print("PostalCodeType:", record.postal_code_type)
        print("AddressType:", record.address_type)
        print("AddressKey:", record.address_key)
        print("SubNationalArea:", record.sub_national_area)
        print("CountryName:", record.country_name)
        print("CountryISO3166_1_Alpha2:", record.country_iso3166_1_alpha2)
        print("CountryISO3166_1_Alpha3:", record.country_iso3166_1_alpha3)
        print("CountryISO3166_1_Numeric:", record.country_iso3166_1_numeric)
        print("CountrySubdivisionCode:", record.country_subdivision_code)
        print("Thoroughfare:", record.thoroughfare)
        print("ThoroughfarePreDirection:", record.thoroughfare_pre_direction)
        print("ThoroughfareLeadingType:", record.thoroughfare_leading_type)
        print("ThoroughfareName:", record.thoroughfare_name)
        print("ThoroughfareTrailingType:", record.thoroughfare_trailing_type)
        print("ThoroughfarePostDirection:", record.thoroughfare_post_direction)
        print("DependentThoroughfare:", record.dependent_thoroughfare)
        print("DependentThoroughfarePreDirection:", record.dependent_thoroughfare_pre_direction)
        print("DependentThoroughfareLeadingType:", record.dependent_thoroughfare_leading_type)
        print("DependentThoroughfareName:", record.dependent_thoroughfare_name)
        print("DependentThoroughfareTrailingType:", record.dependent_thoroughfare_trailing_type)
        print("DependentThoroughfarePostDirection:", record.dependent_thoroughfare_post_direction)
        print("Building:", record.building)
        print("PremisesType:", record.premises_type)
        print("PremisesNumber:", record.premises_number)
        print("SubPremisesType:", record.sub_premises_type)
        print("SubPremisesNumber:", record.sub_premises_number)
        print("PostBox:", record.post_box)
        print("Latitude:", record.latitude)
        print("Longitude:", record.longitude)
        print("DeliveryIndicator:", record.delivery_indicator)
        print("MelissaAddressKey:", record.melissa_address_key)
        print("MelissaAddressKeyBase:", record.melissa_address_key_base)
        print("PostOfficeLocation:", record.post_office_location)
        print("SubPremiseLevel:", record.sub_premise_level)
        print("SubPremiseLevelType:", record.sub_premise_level_type)
        print("SubPremiseLevelNumber:", record.sub_premise_level_number)
        print("SubBuilding:", record.sub_building)
        print("SubBuildingType:", record.sub_building_type)
        print("SubBuildingNumber:", record.sub_building_number)
        print("UTC:", record.utc)
        print("DST:", record.dst)
        print("DeliveryPointSuffix:", record.delivery_point_suffix)
        print("CensusKey:", record.census_key)

        # Extras
        print("CBSACode:", record.extras.cbsa_code)
        print("CBSACode:", record.extras.get_cbsa_code())
        print("CBSACode:", record.extras.get_value("CBSACode"))
        print("CBSADivisionCode:", record.extras.cbsa_division_code)
        print("CBSADivisionLevel:", record.extras.cbsa_division_level)
        print("CBSADivisionTitle:", record.extras.cbsa_division_title)
        print("CBSALevel:", record.extras.cbsa_level)
        print("CBSATitle:", record.extras.cbsa_title)
        print("CarrierRoute:", record.extras.carrier_route)
        print("CensusBlock:", record.extras.census_block)
        print("CensusTract:", record.extras.census_tract)
        print("CongressionalDistrict:", record.extras.congressional_district)
        print("CountyFIPS:", record.extras.county_fips)
        print("CountySubdivisionCode:", record.extras.county_subdivision_code)
        print("CountySubdivisionName:", record.extras.county_subdivision_name)
        print("DeliveryPointCheckDigit:", record.extras.delivery_point_check_digit)
        print("DeliveryPointCode:", record.extras.delivery_point_code)
        print("PlaceCode:", record.extras.place_code)
        print("PlaceName:", record.extras.place_name)
        print("StateDistrictLower:", record.extras.state_district_lower)
        print("StateDistrictUpper:", record.extras.state_district_upper)
        print("UnifiedSchoolDistrictCode:", record.extras.unified_school_district_code)
        print("UnifiedSchoolDistrictName:" , record.extras.unified_school_district_name)
        print("\n")
          

def global_address_verification_batch_1_sample(license_key):
    """
    This function uses the Global Address Verification Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    global_address = GlobalAddressVerification(license_key)

    global_address.set_post_body(GlobalAddressVerificationPostRequest(
        customer_id=license_key,
        options="USExtras:ON",
        records=[
            GlobalAddressVerificationRecordRequest(
                record_id="1",
                address_line_1="22382 Avenida Empresa",
                locality="Rancho Santa Margarita",
                administrative_area="CA",
                postal_code="92688",
                country="US"
            ),
            GlobalAddressVerificationRecordRequest(
                record_id="2",
                address_line_1="30 Dunn Dr",
                locality="Bay Bulls",
                administrative_area="NL",
                postal_code="A0A1C0",
                country="CA"
            )
        ]
    ))

    response = global_address.post(str)
    
    response_object = global_address.post(GlobalAddressVerificationResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResult: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print("RecordID:", record.record_id)
        print("Results:", record.results)
        print("Formatted:", record.formatted_address)
        print("Organization:", record.organization)
        print("AddressLine1:", record.get_value("AddressLine1"))
        print("AddressLine1:", record.get_address_line_1())
        print("AddressLine1:", record.address_line_1)
        print("AddressLine2:", record.address_line_2)
        print("AddressLine3:", record.address_line_3)
        print("AddressLine4:", record.address_line_4)
        print("AddressLine5:", record.address_line_5)
        print("AddressLine6:", record.address_line_6)
        print("AddressLine7:", record.address_line_7)
        print("AddressLine8:", record.address_line_8)
        print("SubPremises:", record.sub_premises)
        print("DoubleDependentLocality:", record.double_dependent_locality)
        print("DependentLocality:", record.dependent_locality)
        print("Locality:", record.locality)
        print("SubAdministrativeArea:", record.sub_administrative_area)
        print("AdministrativeArea:", record.administrative_area)
        print("PostalCode:", record.postal_code)
        print("PostalCodeType:", record.postal_code_type)
        print("AddressType:", record.address_type)
        print("AddressKey:", record.address_key)
        print("SubNationalArea:", record.sub_national_area)
        print("CountryName:", record.country_name)
        print("CountryISO3166_1_Alpha2:", record.country_iso3166_1_alpha2)
        print("CountryISO3166_1_Alpha3:", record.country_iso3166_1_alpha3)
        print("CountryISO3166_1_Numeric:", record.country_iso3166_1_numeric)
        print("CountrySubdivisionCode:", record.country_subdivision_code)
        print("Thoroughfare:", record.thoroughfare)
        print("ThoroughfarePreDirection:", record.thoroughfare_pre_direction)
        print("ThoroughfareLeadingType:", record.thoroughfare_leading_type)
        print("ThoroughfareName:", record.thoroughfare_name)
        print("ThoroughfareTrailingType:", record.thoroughfare_trailing_type)
        print("ThoroughfarePostDirection:", record.thoroughfare_post_direction)
        print("DependentThoroughfare:", record.dependent_thoroughfare)
        print("DependentThoroughfarePreDirection:", record.dependent_thoroughfare_pre_direction)
        print("DependentThoroughfareLeadingType:", record.dependent_thoroughfare_leading_type)
        print("DependentThoroughfareName:", record.dependent_thoroughfare_name)
        print("DependentThoroughfareTrailingType:", record.dependent_thoroughfare_trailing_type)
        print("DependentThoroughfarePostDirection:", record.dependent_thoroughfare_post_direction)
        print("Building:", record.building)
        print("PremisesType:", record.premises_type)
        print("PremisesNumber:", record.premises_number)
        print("SubPremisesType:", record.sub_premises_type)
        print("SubPremisesNumber:", record.sub_premises_number)
        print("PostBox:", record.post_box)
        print("Latitude:", record.latitude)
        print("Longitude:", record.longitude)
        print("DeliveryIndicator:", record.delivery_indicator)
        print("MelissaAddressKey:", record.melissa_address_key)
        print("MelissaAddressKeyBase:", record.melissa_address_key_base)
        print("PostOfficeLocation:", record.post_office_location)
        print("SubPremiseLevel:", record.sub_premise_level)
        print("SubPremiseLevelType:", record.sub_premise_level_type)
        print("SubPremiseLevelNumber:", record.sub_premise_level_number)
        print("SubBuilding:", record.sub_building)
        print("SubBuildingType:", record.sub_building_type)
        print("SubBuildingNumber:", record.sub_building_number)
        print("UTC:", record.utc)
        print("DST:", record.dst)
        print("DeliveryPointSuffix:", record.delivery_point_suffix)
        print("CensusKey:", record.census_key)

        # Extras
        print("CBSACode:", record.extras.cbsa_code)
        print("CBSACode:", record.extras.get_cbsa_code())
        print("CBSACode:", record.extras.get_value("CBSACode"))
        print("CBSADivisionCode:", record.extras.cbsa_division_code)
        print("CBSADivisionLevel:", record.extras.cbsa_division_level)
        print("CBSADivisionTitle:", record.extras.cbsa_division_title)
        print("CBSALevel:", record.extras.cbsa_level)
        print("CBSATitle:", record.extras.cbsa_title)
        print("CarrierRoute:", record.extras.carrier_route)
        print("CensusBlock:", record.extras.census_block)
        print("CensusTract:", record.extras.census_tract)
        print("CongressionalDistrict:", record.extras.congressional_district)
        print("CountyFIPS:", record.extras.county_fips)
        print("CountySubdivisionCode:", record.extras.county_subdivision_code)
        print("CountySubdivisionName:", record.extras.county_subdivision_name)
        print("DeliveryPointCheckDigit:", record.extras.delivery_point_check_digit)
        print("DeliveryPointCode:", record.extras.delivery_point_code)
        print("PlaceCode:", record.extras.place_code)
        print("PlaceName:", record.extras.place_name)
        print("StateDistrictLower:", record.extras.state_district_lower)
        print("StateDistrictUpper:", record.extras.state_district_upper)
        print("UnifiedSchoolDistrictCode:", record.extras.unified_school_district_code)
        print("UnifiedSchoolDistrictName:" , record.extras.unified_school_district_name)
        print("\n\n")

def global_address_verification_batch_2_sample(license_key):
    """
    This function uses the Global Address Verification Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    global_address = GlobalAddressVerification(license_key)
    global_address.set_opt("USExtras:ON")

    global_address.add_record(GlobalAddressVerificationRecordRequest(
        record_id="1",
        address_line_1="22382 Avenida Empresa",
        locality="Rancho Santa Margarita",
        administrative_area="CA",
        postal_code="92688",
        country="US"
    ))

    global_address.add_record(GlobalAddressVerificationRecordRequest(
        record_id="2",
        address_line_1="30 Dunn Dr",
        locality="Bay Bulls",
        administrative_area="NL",
        postal_code="A0A1C0",
        country="CA"
    ))

    response = global_address.post(str)
    response_object = global_address.post(GlobalAddressVerificationResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResult: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print("RecordID:", record.record_id)
        print("Results:", record.results)
        print("Formatted:", record.formatted_address)
        print("Organization:", record.organization)
        print("AddressLine1:", record.get_value("AddressLine1"))
        print("AddressLine1:", record.get_address_line_1())
        print("AddressLine1:", record.address_line_1)
        print("AddressLine2:", record.address_line_2)
        print("AddressLine3:", record.address_line_3)
        print("AddressLine4:", record.address_line_4)
        print("AddressLine5:", record.address_line_5)
        print("AddressLine6:", record.address_line_6)
        print("AddressLine7:", record.address_line_7)
        print("AddressLine8:", record.address_line_8)
        print("SubPremises:", record.sub_premises)
        print("DoubleDependentLocality:", record.double_dependent_locality)
        print("DependentLocality:", record.dependent_locality)
        print("Locality:", record.locality)
        print("SubAdministrativeArea:", record.sub_administrative_area)
        print("AdministrativeArea:", record.administrative_area)
        print("PostalCode:", record.postal_code)
        print("PostalCodeType:", record.postal_code_type)
        print("AddressType:", record.address_type)
        print("AddressKey:", record.address_key)
        print("SubNationalArea:", record.sub_national_area)
        print("CountryName:", record.country_name)
        print("CountryISO3166_1_Alpha2:", record.country_iso3166_1_alpha2)
        print("CountryISO3166_1_Alpha3:", record.country_iso3166_1_alpha3)
        print("CountryISO3166_1_Numeric:", record.country_iso3166_1_numeric)
        print("CountrySubdivisionCode:", record.country_subdivision_code)
        print("Thoroughfare:", record.thoroughfare)
        print("ThoroughfarePreDirection:", record.thoroughfare_pre_direction)
        print("ThoroughfareLeadingType:", record.thoroughfare_leading_type)
        print("ThoroughfareName:", record.thoroughfare_name)
        print("ThoroughfareTrailingType:", record.thoroughfare_trailing_type)
        print("ThoroughfarePostDirection:", record.thoroughfare_post_direction)
        print("DependentThoroughfare:", record.dependent_thoroughfare)
        print("DependentThoroughfarePreDirection:", record.dependent_thoroughfare_pre_direction)
        print("DependentThoroughfareLeadingType:", record.dependent_thoroughfare_leading_type)
        print("DependentThoroughfareName:", record.dependent_thoroughfare_name)
        print("DependentThoroughfareTrailingType:", record.dependent_thoroughfare_trailing_type)
        print("DependentThoroughfarePostDirection:", record.dependent_thoroughfare_post_direction)
        print("Building:", record.building)
        print("PremisesType:", record.premises_type)
        print("PremisesNumber:", record.premises_number)
        print("SubPremisesType:", record.sub_premises_type)
        print("SubPremisesNumber:", record.sub_premises_number)
        print("PostBox:", record.post_box)
        print("Latitude:", record.latitude)
        print("Longitude:", record.longitude)
        print("DeliveryIndicator:", record.delivery_indicator)
        print("MelissaAddressKey:", record.melissa_address_key)
        print("MelissaAddressKeyBase:", record.melissa_address_key_base)
        print("PostOfficeLocation:", record.post_office_location)
        print("SubPremiseLevel:", record.sub_premise_level)
        print("SubPremiseLevelType:", record.sub_premise_level_type)
        print("SubPremiseLevelNumber:", record.sub_premise_level_number)
        print("SubBuilding:", record.sub_building)
        print("SubBuildingType:", record.sub_building_type)
        print("SubBuildingNumber:", record.sub_building_number)
        print("UTC:", record.utc)
        print("DST:", record.dst)
        print("DeliveryPointSuffix:", record.delivery_point_suffix)
        print("CensusKey:", record.census_key)

        # Extras
        print("CBSACode:", record.extras.cbsa_code)
        print("CBSACode:", record.extras.get_cbsa_code())
        print("CBSACode:", record.extras.get_value("CBSACode"))
        print("CBSADivisionCode:", record.extras.cbsa_division_code)
        print("CBSADivisionLevel:", record.extras.cbsa_division_level)
        print("CBSADivisionTitle:", record.extras.cbsa_division_title)
        print("CBSALevel:", record.extras.cbsa_level)
        print("CBSATitle:", record.extras.cbsa_title)
        print("CarrierRoute:", record.extras.carrier_route)
        print("CensusBlock:", record.extras.census_block)
        print("CensusTract:", record.extras.census_tract)
        print("CongressionalDistrict:", record.extras.congressional_district)
        print("CountyFIPS:", record.extras.county_fips)
        print("CountySubdivisionCode:", record.extras.county_subdivision_code)
        print("CountySubdivisionName:", record.extras.county_subdivision_name)
        print("DeliveryPointCheckDigit:", record.extras.delivery_point_check_digit)
        print("DeliveryPointCode:", record.extras.delivery_point_code)
        print("PlaceCode:", record.extras.place_code)
        print("PlaceName:", record.extras.place_name)
        print("StateDistrictLower:", record.extras.state_district_lower)
        print("StateDistrictUpper:", record.extras.state_district_upper)
        print("UnifiedSchoolDistrictCode:", record.extras.unified_school_district_code)
        print("UnifiedSchoolDistrictName:" , record.extras.unified_school_district_name)
        print("\n\n")




