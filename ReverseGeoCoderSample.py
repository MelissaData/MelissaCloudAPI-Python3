from melissadatacloudapi.RecordRequests import ReverseGeoCoderRecordRequest
from melissadatacloudapi.cloudapis.ReverseGeoCoder import ReverseGeoCoder
from melissadatacloudapi.apiresponse import ReverseGeoCoderResponse



def reverse_geo_coder_sample(license_key):
    """
    This function uses the Reverse GeoCoder Cloud API object to make a GET request
    Multiple endpoints are tested
    """
    reverse_geo_coder = ReverseGeoCoder(license_key)
    reverse_geo_coder.set_latitude("33.637520")
    reverse_geo_coder.set_longitude("-117.606920")
    reverse_geo_coder.set_max_records("3")

    response = reverse_geo_coder.get_do_lookup(str)
    response_object = reverse_geo_coder.get_do_lookup(ReverseGeoCoderResponse)

    print(response)
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Results: {response_object.results}")
    print(f"TotalRecords: {response_object.total_records}")
    for record in response_object.records:
        print(f"  AddressLine1: {record.address_line1}")
        print(f"  SuiteName: {record.suite_name}")
        print(f"  SuiteCount: {record.suite_count}")
        print(f"  City: {record.city}")
        print(f"  State: {record.state}")
        print(f"  PostalCode: {record.postal_code}")
        print(f"  AddressKey: {record.address_key}")
        print(f"  Latitude: {record.latitude}")
        print(f"  Longitude: {record.longitude}")
        print(f"  Distance: {record.distance}")
        print(f"  MelissaAddressKey: {record.melissa_address_key}")
        print(f"  MelissaAddressKeyBase: {record.melissa_address_key_base}")

    reverse_geo_coder.clear()

    reverse_geo_coder.set_latitude("33.637520")
    reverse_geo_coder.set_longitude("-117.606920")
    reverse_geo_coder.set_max_records("3")

    response = reverse_geo_coder.get_do_lookup_postal_codes(str)
    response_object = reverse_geo_coder.get_do_lookup_postal_codes(ReverseGeoCoderResponse)

    print(response)
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Results: {response_object.results}")
    print(f"TotalRecords: {response_object.total_records}")
    for record in response_object.records:
        print(f"  City: {record.city}")
        print(f"  State: {record.state}")
        print(f"  PostalCode: {record.postal_code}")
        print(f"  Latitude: {record.latitude}")
        print(f"  Longitude: {record.longitude}")
        print(f"  Distance: {record.distance}")


def reverse_geo_coder_post_sample(license_key):
    """
    This function uses the Reverse GeoCoder Cloud API object to make a POST request
    Multiple endpoints are tested
    """
    reverse_geo_coder = ReverseGeoCoder(license_key)
    reverse_geo_coder.set_post_body(ReverseGeoCoderRecordRequest(
        customer_id=license_key,
        latitude="33.63756710910554",
        longitude="-117.60695049134513",
        max_records="2"
    ))

    response = reverse_geo_coder.post_do_lookup(str)
    response_object = reverse_geo_coder.post_do_lookup(ReverseGeoCoderResponse)

    print(response)
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Results: {response_object.results}")
    print(f"TotalRecords: {response_object.total_records}")
    for record in response_object.records:
        print(f"  AddressLine1: {record.address_line1}")
        print(f"  SuiteName: {record.suite_name}")
        print(f"  SuiteCount: {record.suite_count}")
        print(f"  City: {record.city}")
        print(f"  State: {record.state}")
        print(f"  PostalCode: {record.postal_code}")
        print(f"  AddressKey: {record.address_key}")
        print(f"  Latitude: {record.latitude}")
        print(f"  Longitude: {record.longitude}")
        print(f"  Distance: {record.distance}")
        print(f"  MelissaAddressKey: {record.melissa_address_key}")
        print(f"  MelissaAddressKeyBase: {record.melissa_address_key_base}")

    reverse_geo_coder.clear()

    reverse_geo_coder.set_post_body(ReverseGeoCoderRecordRequest(
        customer_id=license_key,
        latitude="33.63756710910554",
        longitude="-117.60695049134513",
        max_records="2"
    ))

    response = reverse_geo_coder.post_do_lookup_postal_codes(str)
    response_object = reverse_geo_coder.post_do_lookup_postal_codes(ReverseGeoCoderResponse)

    print(response)
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"Results: {response_object.results}")
    print(f"TotalRecords: {response_object.total_records}")
    for record in response_object.records:
        print(f"  City: {record.city}")
        print(f"  State: {record.state}")
        print(f"  PostalCode: {record.postal_code}")
        print(f"  Latitude: {record.latitude}")
        print(f"  Longitude: {record.longitude}")
        print(f"  Distance: {record.distance}")

