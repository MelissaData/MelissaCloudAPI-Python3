from melissadatacloudapi.RecordRequests import PersonatorConsumerRecordRequest
from melissadatacloudapi.cloudapis.PersonatorConsumer import PersonatorConsumer
from melissadatacloudapi.apiresponse import PersonatorConsumerResponse
from melissadatacloudapi.PostReqestBase import PersonatorConsumerPostRequest



def personator_consumer_sample(license_key):
    """
    This function uses the Personator Consumer Cloud API object to make a GET request
    """
    personator = PersonatorConsumer(license_key)
    personator.set_full_name("Ray Melissa")
    personator.set_address_line_1("22382 Avenida Empresa")
    personator.set_city("Rancho Santa Margarita")
    personator.set_state("CA")
    personator.set_postal("92688")
    personator.set_country("United States")
    personator.set_email("info@melissa.com")
    personator.set_phone("800-635-4772")

    response = personator.get(str)
    response_object = personator.get(PersonatorConsumerResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print(f"RecordID: {record.record_id}")
        print(f"AddressKey: {record.address_key}")
        print(f"AddressLine1: {record.address_line_1}")
        print(f"AddressLine2: {record.address_line_2}")
        print(f"City: {record.city}")
        print(f"CompanyName: {record.company_name}")
        print(f"EmailAddress: {record.email_address}")
        print(f"MelissaAddressKey: {record.melissa_address_key}")
        print(f"MelissaAddressKeyBase: {record.melissa_address_key_base}")
        print(f"NameFull: {record.name_full}")
        print(f"PhoneNumber: {record.phone_number}")
        print(f"PostalCode: {record.postal_code}")
        print(f"RecordExtras: {record.record_extras}")
        print(f"Reserved: {record.reserved}")
        print(f"Results: {record.results}")
        print(f"State: {record.state}")


def personator_consumer_batch_1_sample(license_key):
    """
    This function uses the Personator Consumer Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class

    """
    personator_consumer = PersonatorConsumer()
    post_request = PersonatorConsumerPostRequest(
        customer_id=license_key,
        records=[
            PersonatorConsumerRecordRequest(
                record_id="1",
                full_name="Raymond Melissa",
                address_line_1="22382 Avenida Empresa",
                city="Rancho Santa Margarita",
                state="CA",
                postal_code="92688"
            ),
            PersonatorConsumerRecordRequest(
                record_id="2",
                full_name="John Melissa",
                address_line_1="22382 Avenida Empresa",
                city="Rancho Santa Margarita",
                state="CA",
                postal_code="92688"
            )
        ]
    )
    personator_consumer.set_post_body(post_request)

    response = personator_consumer.post(str)
    response_object = personator_consumer.post(PersonatorConsumerResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print(f"AddressExtras: {record.record_id}")
        print(f"AddressKey: {record.address_key}")
        print(f"AddressLine1: {record.address_line_1}")
        print(f"AddressLine2: {record.address_line_2}")
        print(f"City: {record.city}")
        print(f"CompanyName: {record.company_name}")
        print(f"EmailAddress: {record.email_address}")
        print(f"MelissaAddressKey: {record.melissa_address_key}")
        print(f"MelissaAddressKeyBase: {record.melissa_address_key_base}")
        print(f"NameFull: {record.name_full}")
        print(f"PhoneNumber: {record.phone_number}")
        print(f"PostalCode: {record.postal_code}")
        print(f"RecordExtras: {record.record_extras}")
        print(f"RecordID: {record.record_id}")
        print(f"Reserved: {record.reserved}")
        print(f"Results: {record.results}")
        print(f"State: {record.state}\n\n")


def personator_consumer_batch_2_sample(license_key):
    """    
    This function uses the Personator Consumer Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """

    personator_consumer = PersonatorConsumer(license_key)
    personator_consumer.add_record(
        PersonatorConsumerRecordRequest(
            record_id="1",
            full_name="Raymond Melissa",
            address_line_1="22382 Avenida Empresa",
            city="Rancho Santa Margarita",
            state="CA",
            postal_code="92688"
        )
    )
    personator_consumer.add_record(
        PersonatorConsumerRecordRequest(
            record_id="2",
            full_name="John Melissa",
            address_line_1="22382 Avenida Empresa",
            city="Rancho Santa Margarita",
            state="CA",
            postal_code="92688"
        )
    )

    response = personator_consumer.post(str)
    response_object = personator_consumer.post(PersonatorConsumerResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print(f"AddressExtras: {record.record_id}")
        print(f"AddressKey: {record.address_key}")
        print(f"AddressLine1: {record.address_line_1}")
        print(f"AddressLine2: {record.address_line_2}")
        print(f"City: {record.city}")
        print(f"CompanyName: {record.company_name}")
        print(f"EmailAddress: {record.email_address}")
        print(f"MelissaAddressKey: {record.melissa_address_key}")
        print(f"MelissaAddressKeyBase: {record.melissa_address_key_base}")
        print(f"NameFull: {record.name_full}")
        print(f"PhoneNumber: {record.phone_number}")
        print(f"PostalCode: {record.postal_code}")
        print(f"RecordExtras: {record.record_extras}")
        print(f"RecordID: {record.record_id}")
        print(f"Reserved: {record.reserved}")
        print(f"Results: {record.results}")
        print(f"State: {record.state}\n\n")
