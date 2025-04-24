from melissadatacloudapi.RecordRequests import PeopleBusinessSearchRecordRequest
from melissadatacloudapi.cloudapis.PeopleBusinessSearch import PeopleBusinessSearch
from melissadatacloudapi.apiresponse import PeopleBusinessSearchResponse

def people_business_search_sample(license_key):
    """
    This function uses the People Business Search Cloud API object to test both GET and POST
    """
    people_business = PeopleBusinessSearch(license_key)
    people_business.set_max_records("10")
    people_business.set_match_level("10")
    people_business.set_address_line_1("22382 Avenida Empresa")
    people_business.set_locality("RSM")
    people_business.set_administrative_area("CA")
    people_business.set_postal("92688")
    people_business.set_any_name("Melissa Data")

    response = people_business.get(str)
    response_object = people_business.get(PeopleBusinessSearchResponse)
    
    print(response)
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"Version: {response_object.version}")
    print(f"ResultCode: {response_object.result_code}")
    print(f"TotalRecords: {response_object.total_records}")
    
    for record in response_object.results:
        print(f"\nMatchLevel: {record.match_level}")
        print(f"Address:")
        print(f"\tAddress1: {record.address.address1}")
        print(f"\tLocality: {record.address.locality}")
        print(f"\tLocalityAlternates: {record.address.locality_alternates}")
        print(f"\tAdministrativeArea: {record.address.administrative_area}")
        print(f"\tCountryCode: {record.address.country_code}")
        print(f"\tCountryName: {record.address.country_name}")
        print(f"\tThoroughfare: {record.address.thoroughfare}")
        print(f"\tThoroughfareName: {record.address.thoroughfare_name}")
        print(f"\tPremises: {record.address.premises}")
        print(f"\tPremiseNumber: {record.address.premise_number}")
        print(f"\tPostalCode: {record.address.postal_code}")
        print(f"\tPostalCodeSecondary: {record.address.postal_code_secondary}")
        print(f"\tMelissaAddressKey: {record.address.melissa_address_key}")
        
        print(f"Consumer:")
        print(f"\tFullName: {record.consumer.full_name}")
        print(f"\tFirstName: {record.consumer.first_name}")
        print(f"\tLastName: {record.consumer.last_name}")
        print(f"\tMelissaIdentityKey: {record.consumer.melissa_identity_key}")
        
        print(f"Phone:")
        print(f"\tPhone: {record.phone.phone}")
    
    # POST request
    post_body = PeopleBusinessSearchRecordRequest()
    post_body.customer_id = license_key
    post_body.max_records = "10"
    post_body.match_level = "10"
    post_body.address_line_1 = "22382 Avenida Empresa"
    post_body.locality = "RSM"
    post_body.administrative_area = "CA"
    post_body.postal_code = "92688"
    post_body.any_name = "Melissa Data"
    
    people_business.set_post_body(post_body)
    
    response = people_business.post(str)
    response_object = people_business.post(PeopleBusinessSearchResponse)
    
    print(response)
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"Version: {response_object.version}")
    print(f"ResultCode: {response_object.result_code}")
    print(f"TotalRecords: {response_object.total_records}")
    
    for record in response_object.results:
        print(f"\nMatchLevel: {record.match_level}")
        print(f"Address:")
        print(f"\tAddress1: {record.address.address1}")
        print(f"\tLocality: {record.address.locality}")
        print(f"\tLocalityAlternates: {record.address.locality_alternates}")
        print(f"\tAdministrativeArea: {record.address.administrative_area}")
        print(f"\tCountryCode: {record.address.country_code}")
        print(f"\tCountryName: {record.address.country_name}")
        print(f"\tThoroughfare: {record.address.thoroughfare}")
        print(f"\tThoroughfareName: {record.address.thoroughfare_name}")
        print(f"\tPremises: {record.address.premises}")
        print(f"\tPremiseNumber: {record.address.premise_number}")
        print(f"\tPostalCode: {record.address.postal_code}")
        print(f"\tPostalCodeSecondary: {record.address.postal_code_secondary}")
        print(f"\tMelissaAddressKey: {record.address.melissa_address_key}")
        
        print(f"Consumer:")
        print(f"\tFullName: {record.consumer.full_name}")
        print(f"\tFirstName: {record.consumer.first_name}")
        print(f"\tLastName: {record.consumer.last_name}")
        print(f"\tMelissaIdentityKey: {record.consumer.melissa_identity_key}")
        
        print(f"Phone:")
        print(f"\tPhone: {record.phone.phone}")

