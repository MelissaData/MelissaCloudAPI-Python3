from melissadatacloudapi.RecordRequests import GlobalIPRecordRequest
from melissadatacloudapi.cloudapis.GlobalIP import GlobalIP
from melissadatacloudapi.apiresponse import GlobalIPResponse
from melissadatacloudapi.PostReqestBase import GlobalIPPostRequest


def global_ip_sample(license_key):
    """
    This function uses the Global IP Cloud API object to make a GET request
    """
    global_ip = GlobalIP(license_key)
    global_ip.set_ip("12.203.219.6")
    
    response = global_ip.get(str)
    response_object = global_ip.get(GlobalIPResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}\n")

    for record in response_object.records:
        print(f"City: {record.city}")
        print(f"ConnectionSpeed: {record.connection_speed}")
        print(f"ConnectionType: {record.connection_type}")
        print(f"Continent: {record.continent}")
        print(f"CountryAbbreviation: {record.country_abbreviation}")
        print(f"CountryName: {record.country_name}")
        print(f"DomainName: {record.domain_name}")
        print(f"DST: {record.dst}")
        print(f"IPAddress: {record.ip_address}")
        print(f"ISPName: {record.isp_name}")
        print(f"Latitude: {record.latitude}")
        print(f"Longitude: {record.longitude}")
        print(f"PostalCode: {record.postal_code}")
        print(f"ProxyDescription: {record.proxy_description}")
        print(f"ProxyType: {record.proxy_type}")
        print(f"RecordID: {record.record_id}")
        print(f"Region: {record.region}")
        print(f"Result: {record.result}")
        print(f"TimeZoneCode: {record.time_zone_code}")
        print(f"TimeZoneName: {record.time_zone_name}")
        print(f"UTC: {record.utc}\n\n")

def global_ip_batch_1_sample(license_key):
    """
    This function uses the Global IP Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective BatchRequest class
    """
    global_ip = GlobalIP()
    global_ip.set_post_body(GlobalIPPostRequest(
        customer_id=license_key,
        records=[
            GlobalIPRecordRequest(
                record_id="1",
                ip_address="12.203.219.6"
            ),
            GlobalIPRecordRequest(
                record_id="2",
                ip_address="139.101.81.42"
            )
        ]
    ))

    response = global_ip.post(str)

    response_object = global_ip.post(GlobalIPResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}\n")
    for record in response_object.records:
        print("City: " + record.city)
        print("ConnectionSpeed: " + record.connection_speed)
        print("ConnectionType: " + record.connection_type)
        print("Continent: " + record.continent)
        print("CountryAbbreviation: " + record.country_abbreviation)
        print("CountryName: " + record.country_name)
        print("DomainName: " + record.domain_name)
        print("DST: " + record.dst)
        print("IPAddress: " + record.ip_address)
        print("ISPName: " + record.isp_name)
        print("Latitude: " + record.latitude)
        print("Longitude: " + record.longitude)
        print("PostalCode: " + record.postal_code)
        print("ProxyDescription: " + record.proxy_description)
        print("ProxyType: " + record.proxy_type)
        print("RecordID: " + record.record_id)
        print("Region: " + record.region)
        print("Result: " + record.result)
        print("TimeZoneCode: " + record.time_zone_code)
        print("TimeZoneName: " + record.time_zone_name)
        print("UTC: " + record.utc + "\n\n")


def global_ip_batch_2_sample(license_key):
    """
    This function uses the Global IP Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    global_ip = GlobalIP(license_key)
    global_ip.add_record(GlobalIPRecordRequest(
        record_id="1",
        ip_address="12.203.219.6"
    ))
    global_ip.add_record(GlobalIPRecordRequest(
        record_id="2",
        ip_address="139.101.81.42"
    ))

    response = global_ip.post(str)
    response_object = global_ip.post(GlobalIPResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}\n")
    for record in response_object.records:
        print("City: " + record.city)
        print("ConnectionSpeed: " + record.connection_speed)
        print("ConnectionType: " + record.connection_type)
        print("Continent: " + record.continent)
        print("CountryAbbreviation: " + record.country_abbreviation)
        print("CountryName: " + record.country_name)
        print("DomainName: " + record.domain_name)
        print("DST: " + record.dst)
        print("IPAddress: " + record.ip_address)
        print("ISPName: " + record.isp_name)
        print("Latitude: " + record.latitude)
        print("Longitude: " + record.longitude)
        print("PostalCode: " + record.postal_code)
        print("ProxyDescription: " + record.proxy_description)
        print("ProxyType: " + record.proxy_type)
        print("RecordID: " + record.record_id)
        print("Region: " + record.region)
        print("Result: " + record.result)
        print("TimeZoneCode: " + record.time_zone_code)
        print("TimeZoneName: " + record.time_zone_name)
        print("UTC: " + record.utc + "\n\n")

