from melissadatacloudapi.cloudapis.PersonatorSearch import PersonatorSearch
from melissadatacloudapi.apiresponse import PersonatorSearchResponse


def personator_search_sample(license_key):
    """
    This function uses the Personator Search Cloud API object to make a GET request
    """
    personator = PersonatorSearch(license_key)
    personator.set_full_name("Raymond Melissa")
    personator.set_address_line_1("22382 Avenida Empresa")
    personator.set_city("RSM")
    personator.set_state("CA")
    personator.set_postal("92688")
    personator.set_cols("GrpAll")

    response = personator.get()
    print(response)

    response_object = personator.get(PersonatorSearchResponse)

    print(f"\nTransmissionResults: {response_object.transmission_results}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TotalPages: {response_object.total_pages}")
    print(f"TotalRecords: {response_object.total_records}")
    print(f"Version: {response_object.version}")

    for record in response_object.records:
        print(f"\nRecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"FullName: {record.full_name}")
        print(f"FirstName: {record.first_name}")
        print(f"LastName: {record.last_name}")
        print(f"DateOfBirth: {record.date_of_birth}")
        print(f"DateOfDeath: {record.date_of_death}")
        print(f"MelissaIdentityKey: {record.melissa_identity_key}")
        print("CurrentAddress:")
        print(f"\tAddressLine1: {record.current_address.address_line_1}")
        print(f"\tCity: {record.current_address.city}")
        print(f"\tState: {record.current_address.state}")
        print(f"\tPostalCode: {record.current_address.postal_code}")
        print(f"\tPlus4: {record.current_address.plus4}")
        print(f"\tMelissaAddressKey: {record.current_address.melissa_address_key}")


