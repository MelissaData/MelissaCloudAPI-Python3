from melissadatacloudapi.cloudapis import BusinessCoder
from melissadatacloudapi.apiresponse import BusinessCoderResponse
from melissadatacloudapi.PostReqestBase import BusinessCoderPostRequest
from melissadatacloudapi.RecordRequests import BusinessCoderRecordRequest


def business_coder_sample(license_key):
    """
    This function uses the Business Coder Cloud API object to make a GET request
    """
    business_coder = BusinessCoder(license_key)
    business_coder.set_company("Melissa")
    business_coder.set_address_line_1("22382 Avenida Empresa")
    business_coder.set_city("Rancho Santa Margarita")
    business_coder.set_state("CA")
    business_coder.set_postal("92688")
    business_coder.set_country("United States")
    # business_coder.set_cols("GrpAddressDetails,GrpBusinessCodes,Contacts")

    response = business_coder.get(str)
    response_object = business_coder.get(BusinessCoderResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print("AddressLine1: " + record.address_line_1)
        print("City: " + record.city)
        print("CompanyName: " + record.company_name)
        print("CurrentCompanyName: " + record.current_company_name)
        print("MelissaEnterpriseKey: " + record.melissa_enterprise_key)
        print("PostalCode: " + record.postal_code)
        print("RecordID: " + record.record_id)
        print("Results: " + record.results)
        print("State: " + record.state)
        print("Suite: " + record.suite)
        print("TotalContacts: " + record.total_contacts)

def business_coder_batch_1_sample(license_key):
    """
    This function uses the Business Coder Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    business_coder =  BusinessCoder()
    business_coder.set_post_body(BusinessCoderPostRequest(
        id=license_key,
        records=[
            BusinessCoderRecordRequest(
                a1="22382 Avenida Empresa",
                city="Rancho Santa Margarita",
                postal="92688",
                state="California"
            ),
            BusinessCoderRecordRequest(
                a1="1 Microsoft Way",
                city="Redmond",
                postal="98052",
                state="Washington"
            )
        ]
    ))

    response = business_coder.post(str)
    response_object = business_coder.post(BusinessCoderResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print("AddressLine1: " + record.address_line_1)
        print("City: " + record.city)
        print("CompanyName: " + record.company_name)
        print("CurrentCompanyName: " + record.current_company_name)
        print("MelissaEnterpriseKey: " + record.melissa_enterprise_key)
        print("PostalCode: " + record.postal_code)
        print("RecordID: " + record.record_id)
        print("Results: " + record.results)
        print("State: " + record.state)
        print("Suite: " + record.suite)
        print("TotalContacts: " + record.total_contacts + "\n")

