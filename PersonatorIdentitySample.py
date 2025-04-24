from melissadatacloudapi.RecordRequests import PersonatorIdentityRecordRequest
from melissadatacloudapi.cloudapis.PersonatorIdentity import PersonatorIdentity
from melissadatacloudapi.apiresponse import PersonatorIdentityResponse


def personator_identity_sample(license_key):
    """
    This function uses the Personator Identity Cloud API object to make a GET request
    """
    personator = PersonatorIdentity(license_key)
    personator.set_action("check")
    personator.set_full_name("Raymond Melissa")
    personator.set_address_line_1("22382 Avenida Empresa")
    personator.set_locality("Rancho Santa Margarita")
    personator.set_administrative_area("CA")
    personator.set_postal("92688")
    personator.set_country("United States")

    response = personator.get(str)
    response_object = personator.get(PersonatorIdentityResponse)

    print(response)

    print(f"\nTransactionID: {response_object.transaction_id}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"Results: {response_object.results}")
    print(f"Version: {response_object.version}\n")

    print("Name:")
    print(f"\tResults: {response_object.peronator_identity_name.results}")
    print(f"\tNameFirst: {response_object.peronator_identity_name.name_first}")
    print(f"\tNameLast: {response_object.peronator_identity_name.name_last}")
    print(f"\tGender: {response_object.peronator_identity_name.gender}")

    print("Address:")
    print(f"\tResults: {response_object.peronator_identity_address.results}")
    print(f"\tFormattedAddress: {response_object.peronator_identity_address.formatted_address}")
    print(f"\tAddressLine1: {response_object.peronator_identity_address.address_line_1}")
    print(f"\tAddressLine2: {response_object.peronator_identity_address.address_line_2}")
    print(f"\tLocality: {response_object.peronator_identity_address.locality}")
    print(f"\tSubAdministrativeArea: {response_object.peronator_identity_address.sub_administrative_area}")
    print(f"\tAdministrativeArea: {response_object.peronator_identity_address.administrative_area}")
    print(f"\tPostalCode: {response_object.peronator_identity_address.postal_code}")
    print(f"\tAddressType: {response_object.peronator_identity_address.address_type}")
    print(f"\tAddressKey: {response_object.peronator_identity_address.address_key}")
    print(f"\tCountryName: {response_object.peronator_identity_address.country_name}")
    print(f"\tCountryCode: {response_object.peronator_identity_address.country_code}")
    print(f"\tCountryISO3: {response_object.peronator_identity_address.country_iso3}")
    print(f"\tCountryNumber: {response_object.peronator_identity_address.country_number}")
    print(f"\tCountrySubdivisionCode: {response_object.peronator_identity_address.country_subdivision_code}")
    print(f"\tThoroughfare: {response_object.peronator_identity_address.thoroughfare}")
    print(f"\tThoroughfareName: {response_object.peronator_identity_address.thoroughfare_name}")
    print(f"\tPremisesNumber: {response_object.peronator_identity_address.premises_number}")
    print(f"\tLatitude: {response_object.peronator_identity_address.latitude}")
    print(f"\tLongitude: {response_object.peronator_identity_address.longitude}")


def personator_identity_post_sample(license_key):
    """
    This function uses the Personator Identity Cloud API object to make a POST request
    This function showcases setting and making POST requests: construct the POST body structure using the Cloud API's respective RecordRequest class
    """
    personator = PersonatorIdentity()
    personator.set_post_body(
        PersonatorIdentityRecordRequest(
            customer_id=license_key,
            actions="check",
            full_name="Raymond Melissa",
            address_line_1="22382 Avenida Empresa",
            locality="Rancho Santa Margarita",
            administrative_area="CA",
            postal_code="92688",
            country="United States",
        )
    )

    response = personator.post(str)
    response_object = personator.post(PersonatorIdentityResponse)

    print(response)

    print(f"\nTransactionID: {response_object.transaction_id}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"Results: {response_object.results}")
    print(f"Version: {response_object.version}\n")

    print("Name:")
    print(f"\tResults: {response_object.peronator_identity_name.results}")
    print(f"\tNameFirst: {response_object.peronator_identity_name.name_first}")
    print(f"\tNameLast: {response_object.peronator_identity_name.name_last}")
    print(f"\tGender: {response_object.peronator_identity_name.gender}")

    print("Address:")
    print(f"\tResults: {response_object.peronator_identity_address.results}")
    print(f"\tFormattedAddress: {response_object.peronator_identity_address.formatted_address}")
    print(f"\tAddressLine1: {response_object.peronator_identity_address.address_line_1}")
    print(f"\tAddressLine2: {response_object.peronator_identity_address.address_line_2}")
    print(f"\tLocality: {response_object.peronator_identity_address.locality}")
    print(f"\tSubAdministrativeArea: {response_object.peronator_identity_address.sub_administrative_area}")
    print(f"\tAdministrativeArea: {response_object.peronator_identity_address.administrative_area}")
    print(f"\tPostalCode: {response_object.peronator_identity_address.postal_code}")
    print(f"\tAddressType: {response_object.peronator_identity_address.address_type}")
    print(f"\tAddressKey: {response_object.peronator_identity_address.address_key}")
    print(f"\tCountryName: {response_object.peronator_identity_address.country_name}")
    print(f"\tCountryCode: {response_object.peronator_identity_address.country_code}")
    print(f"\tCountryISO3: {response_object.peronator_identity_address.country_iso3}")
    print(f"\tCountryNumber: {response_object.peronator_identity_address.country_number}")
    print(f"\tCountrySubdivisionCode: {response_object.peronator_identity_address.country_subdivision_code}")
    print(f"\tThoroughfare: {response_object.peronator_identity_address.thoroughfare}")
    print(f"\tThoroughfareName: {response_object.peronator_identity_address.thoroughfare_name}")
    print(f"\tPremisesNumber: {response_object.peronator_identity_address.premises_number}")
    print(f"\tLatitude: {response_object.peronator_identity_address.latitude}")
    print(f"\tLongitude: {response_object.peronator_identity_address.longitude}")
