from melissadatacloudapi.RecordRequests import SmartMoverRecordRequest
from melissadatacloudapi.cloudapis.SmartMover import SmartMover
from melissadatacloudapi.apiresponse import SmartMoverResponse
from melissadatacloudapi.PostReqestBase import SmartMoverPostRequest

def smart_mover_sample(license_key, paf_id):
    """
    This function uses the Smart Mover Cloud API object to make a GET request
    """
    smart_mover = SmartMover(license_key)
    smart_mover.set_paf_id(paf_id)
    smart_mover.set_company("Melissa")
    smart_mover.set_full_name("Ray Melissa")
    smart_mover.set_address_line_1("22382 Avenida Empresa")
    smart_mover.set_city("Rancho Santa Margarita")
    smart_mover.set_state("CA")
    smart_mover.set_postal("92688")
    smart_mover.set_country("US")
    smart_mover.set_cols("grpParsed")

    response = smart_mover.get(str)
    response_object = smart_mover.get(SmartMoverResponse)

    print(response)

    print(f"\nTotalRecords: {response_object.total_records}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Version: {response_object.version}")

    for record in response_object.records:
        print(f"\nAddressHouseNumber: {record.address_house_number}")
        print(f"AddressKey: {record.address_key}")
        print(f"AddressLine1: {record.address_line_1}")
        print(f"AddressStreetName: {record.address_street_name}")
        print(f"AddressTypeCode: {record.address_type_code}")
        print(f"CarrierRoute: {record.carrier_route}")
        print(f"City: {record.city}")
        print(f"CityAbbreviation: {record.city_abbreviation}")
        print(f"CompanyName: {record.company_name}")
        print(f"CountryCode: {record.country_code}")
        print(f"CountryName: {record.country_name}")
        print(f"DeliveryIndicator: {record.delivery_indicator}")
        print(f"DeliveryPointCheckDigit: {record.delivery_point_check_digit}")
        print(f"DeliveryPointCode: {record.delivery_point_code}")
        print(f"MelissaAddressKey: {record.melissa_address_key}")
        print(f"PostalCode: {record.postal_code}")
        print(f"Results: {record.results}")
        print(f"State: {record.state}")
        print(f"StateName: {record.state_name}")


def smart_mover_batch_1_sample(license_key, paf_id):
    """
    This function uses the Smart Mover Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    smart_mover = SmartMover()

    smart_mover.set_post_body(
        SmartMoverPostRequest(
            customer_id=license_key,
            paf_id=paf_id,
            records=[
                SmartMoverRecordRequest(
                    record_id="1",
                    company="Melissa",
                    name_full="Ray Melissa",
                    address_line_1="22382 Avenida Empresa",
                    city="Rancho Santa Margarita",
                    state="CA",
                    postal_code="92688",
                    country="US"
                ),
                SmartMoverRecordRequest(
                    record_id="2",
                    company="Melissa",
                    name_full="John Melissa",
                    address_line_1="22382 Avenida Empresa",
                    city="Rancho Santa Margarita",
                    state="CA",
                    postal_code="92688",
                    country="US"
                )
            ]
        )
    )

    response = smart_mover.post(str)
    response_object = smart_mover.post(SmartMoverResponse)

    print(response)

    print(f"\nTotalRecords: {response_object.total_records}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Version: {response_object.version}")

    for record in response_object.records:
        print(f"\nAddressHouseNumber: {record.address_house_number}")
        print(f"AddressKey: {record.address_key}")
        print(f"AddressLine1: {record.address_line_1}")
        print(f"AddressStreetName: {record.address_street_name}")
        print(f"AddressTypeCode: {record.address_type_code}")
        print(f"CarrierRoute: {record.carrier_route}")
        print(f"City: {record.city}")
        print(f"CityAbbreviation: {record.city_abbreviation}")
        print(f"CompanyName: {record.company_name}")
        print(f"CountryCode: {record.country_code}")
        print(f"CountryName: {record.country_name}")
        print(f"DeliveryIndicator: {record.delivery_indicator}")
        print(f"DeliveryPointCheckDigit: {record.delivery_point_check_digit}")
        print(f"DeliveryPointCode: {record.delivery_point_code}")
        print(f"MelissaAddressKey: {record.melissa_address_key}")
        print(f"PostalCode: {record.postal_code}")
        print(f"Results: {record.results}")
        print(f"State: {record.state}")
        print(f"StateName: {record.state_name}")


def smart_mover_batch_2_sample(license_key, paf_id):
    """
    This function uses the Smart Mover Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    smart_mover = SmartMover(license_key)
    smart_mover.set_paf_id(paf_id)
    
    smart_mover.add_record(
        SmartMoverRecordRequest(
            record_id="1",
            company="Melissa",
            name_full="Ray Melissa",
            address_line_1="22382 Avenida Empresa",
            city="Rancho Santa Margarita",
            state="CA",
            postal_code="92688",
            country="US"
        )
    )
    
    smart_mover.add_record(
        SmartMoverRecordRequest(
            record_id="2",
            company="Melissa",
            name_full="John Melissa",
            address_line_1="22382 Avenida Empresa",
            city="Rancho Santa Margarita",
            state="CA",
            postal_code="92688",
            country="US"
        )
    )

    response = smart_mover.post(str)
    response_object = smart_mover.post(SmartMoverResponse)

    print(response)

    print(f"\nTotalRecords: {response_object.total_records}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Version: {response_object.version}")

    for record in response_object.records:
        print(f"\nAddressHouseNumber: {record.address_house_number}")
        print(f"AddressKey: {record.address_key}")
        print(f"AddressLine1: {record.address_line_1}")
        print(f"AddressStreetName: {record.address_street_name}")
        print(f"AddressTypeCode: {record.address_type_code}")
        print(f"CarrierRoute: {record.carrier_route}")
        print(f"City: {record.city}")
        print(f"CityAbbreviation: {record.city_abbreviation}")
        print(f"CompanyName: {record.company_name}")
        print(f"CountryCode: {record.country_code}")
        print(f"CountryName: {record.country_name}")
        print(f"DeliveryIndicator: {record.delivery_indicator}")
        print(f"DeliveryPointCheckDigit: {record.delivery_point_check_digit}")
        print(f"DeliveryPointCode: {record.delivery_point_code}")
        print(f"MelissaAddressKey: {record.melissa_address_key}")
        print(f"PostalCode: {record.postal_code}")
        print(f"Results: {record.results}")
        print(f"State: {record.state}")
        print(f"StateName: {record.state_name}")

