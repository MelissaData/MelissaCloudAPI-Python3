from melissadatacloudapi.RecordRequests import GlobalPhoneRecordRequest
from melissadatacloudapi.cloudapis.GlobalPhone import GlobalPhone
from melissadatacloudapi.apiresponse import GlobalPhoneResponse
from melissadatacloudapi.PostReqestBase import GlobalPhonePostRequest

def global_phone_sample(license_key):
    """
    This function uses the Global Phone Cloud API object to make a GET request
    """
    global_phone = GlobalPhone(license_key)
    global_phone.set_phone("800-635-4772")

    response = global_phone.get(str)
    response_object = global_phone.get(GlobalPhoneResponse)

    print(response)
    
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    
    for record in response_object.records:
        print(f"RecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"PhoneNumber: {record.phone_number}")
        print(f"AdministrativeArea: {record.administrative_area}")
        print(f"CountryAbbreviation: {record.country_abbreviation}")
        print(f"CountryName: {record.country_name}")
        print(f"Carrier: {record.carrier}")
        print(f"CallerID: {record.caller_id}")
        print(f"DST: {record.dst}")
        print(f"InternationalPhoneNumber: {record.international_phone_number}")
        print(f"Language: {record.language}")
        print(f"Latitude: {record.latitude}")
        print(f"Locality: {record.locality}")
        print(f"Longitude: {record.longitude}")
        print(f"PhoneInternationalPrefix: {record.phone_international_prefix}")
        print(f"PhoneCountryDialingCode: {record.phone_country_dialing_code}")
        print(f"PhoneNationPrefix: {record.phone_nation_prefix}")
        print(f"PhoneNationalDestinationCode: {record.phone_national_destination_code}")
        print(f"PhoneSubscriberNumber: {record.phone_subscriber_number}")
        print(f"UTC: {record.utc}")
        print(f"TimeZoneCode: {record.time_zone_code}")
        print(f"TimeZoneName: {record.time_zone_name}")
        print(f"PostalCode: {record.postal_code}")
        print(f"Suggestions: {record.suggestions}\n\n")


def global_phone_batch_1_sample(license_key):
    """
    This function uses the Global Phone Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    
    global_phone = GlobalPhone(license_key)
    global_phone.set_post_body(GlobalPhonePostRequest(
        customer_id= license_key,
        records= [
            GlobalPhoneRecordRequest(record_id = 1, phone_number = "800-635-4772"),
            GlobalPhoneRecordRequest(record_id = 2, phone_number = "+49 (0) 221 97 58 92 40")
        ]
    ))

    response = global_phone.post(str)
    response_object = global_phone.post(GlobalPhoneResponse)

    print(response)
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    
    for record in response_object.records:
        print(f"RecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"PhoneNumber: {record.phone_number}")
        print(f"AdministrativeArea: {record.administrative_area}")
        print(f"CountryAbbreviation: {record.country_abbreviation}")
        print(f"CountryName: {record.country_name}")
        print(f"Carrier: {record.carrier}")
        print(f"CallerID: {record.caller_id}")
        print(f"DST: {record.dst}")
        print(f"InternationalPhoneNumber: {record.international_phone_number}")
        print(f"Language: {record.language}")
        print(f"Latitude: {record.latitude}")
        print(f"Locality: {record.locality}")
        print(f"Longitude: {record.longitude}")
        print(f"PhoneInternationalPrefix: {record.phone_international_prefix}")
        print(f"PhoneCountryDialingCode: {record.phone_country_dialing_code}")
        print(f"PhoneNationPrefix: {record.phone_nation_prefix}")
        print(f"PhoneNationalDestinationCode: {record.phone_national_destination_code}")
        print(f"PhoneSubscriberNumber: {record.phone_subscriber_number}")
        print(f"UTC: {record.utc}")
        print(f"TimeZoneCode: {record.time_zone_code}")
        print(f"TimeZoneName: {record.time_zone_name}")
        print(f"PostalCode: {record.postal_code}")
        print(f"Suggestions: {record.suggestions}\n\n")


def global_phone_batch_2_sample(license_key):
    """
    This function uses the Global Phone Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    global_phone = GlobalPhone(license_key)

    global_phone.add_record(GlobalPhoneRecordRequest(record_id = "1", phone_number= "800-635-4772"))
    global_phone.add_record(GlobalPhoneRecordRequest(record_id = "2", phone_number= "+49 (0) 221 97 58 92 40"))

    response = global_phone.post(str)
    response_object = global_phone.post(GlobalPhoneResponse)

    print(response)
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    
    for record in response_object.records:
        print(f"RecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"PhoneNumber: {record.phone_number}")
        print(f"AdministrativeArea: {record.administrative_area}")
        print(f"CountryAbbreviation: {record.country_abbreviation}")
        print(f"CountryName: {record.country_name}")
        print(f"Carrier: {record.carrier}")
        print(f"CallerID: {record.caller_id}")
        print(f"DST: {record.dst}")
        print(f"InternationalPhoneNumber: {record.international_phone_number}")
        print(f"Language: {record.language}")
        print(f"Latitude: {record.latitude}")
        print(f"Locality: {record.locality}")
        print(f"Longitude: {record.longitude}")
        print(f"PhoneInternationalPrefix: {record.phone_international_prefix}")
        print(f"PhoneCountryDialingCode: {record.phone_country_dialing_code}")
        print(f"PhoneNationPrefix: {record.phone_nation_prefix}")
        print(f"PhoneNationalDestinationCode: {record.phone_national_destination_code}")
        print(f"PhoneSubscriberNumber: {record.phone_subscriber_number}")
        print(f"UTC: {record.utc}")
        print(f"TimeZoneCode: {record.time_zone_code}")
        print(f"TimeZoneName: {record.time_zone_name}")
        print(f"PostalCode: {record.postal_code}")
        print(f"Suggestions: {record.suggestions}\n\n")


