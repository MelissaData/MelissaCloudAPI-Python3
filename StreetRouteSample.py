from melissadatacloudapi.RecordRequests import StreetRouteRecordRequest
from melissadatacloudapi.cloudapis.StreetRoute import StreetRoute
from melissadatacloudapi.apiresponse import StreetRouteResponse
from melissadatacloudapi.PostReqestBase import StreetRoutePostRequest

def street_route_sample(license_key):
    """
    This function uses the Street Route Cloud API object to make a GET request
    """
    street_route = StreetRoute(license_key)
    street_route.set_start_latitude("33.637520")
    street_route.set_start_longitude("-117.606920")
    street_route.set_end_latitude("33.649870")
    street_route.set_end_longitude("-117.582960")

    response = street_route.get(str)
    response_object = street_route.get(StreetRouteResponse)

    print(response)

    print(f"\nResults: {response_object.results}")
    print(f"Units: {response_object.units}")
    print(f"TransmissionResult: {response_object.transmission_result}")
    print(f"TravelTime: {response_object.travel_time}")
    print(f"TotalDrivingDistance: {response_object.total_driving_distance}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"Version: {response_object.version}")


def street_route_batch_1_sample(license_key):
    """
    This function uses the Street Route Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    street_route = StreetRoute()

    post_body = StreetRoutePostRequest(
        customer_id=license_key,
        records=[
            StreetRouteRecordRequest(
                record_id="1",
                start_latitude="33.637520",
                start_longitude="-117.606920",
                end_latitude="33.649870",
                end_longitude="-117.582960"
            ),
            StreetRouteRecordRequest(
                record_id="2",
                start_latitude="33.637520",
                start_longitude="-117.606920",
                end_latitude="33.6328945",
                end_longitude="-117.61098"
            )
        ]
    )

    street_route.set_post_body(post_body)

    response = street_route.post(str)
    response_object = street_route.post(StreetRouteResponse)

    print(response)

    for record in response_object.records:
        print(f"\nRecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"TravelTime: {record.travel_time}")
        print(f"TotalDrivingDistance: {record.total_driving_distance}")


def street_route_batch_2_sample(license_key):
    """
    This function uses the Street Route Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    street_route = StreetRoute(license_key)
    
    street_route.add_record(StreetRouteRecordRequest(
        record_id="1",
        start_latitude="33.637520",
        start_longitude="-117.606920",
        end_latitude="33.649870",
        end_longitude="-117.582960"
    ))
    
    street_route.add_record(StreetRouteRecordRequest(
        record_id="2",
        start_latitude="33.637520",
        start_longitude="-117.606920",
        end_latitude="33.6328945",
        end_longitude="-117.61098"
    ))

    response = street_route.post(str)
    response_object = street_route.post(StreetRouteResponse)

    print(response)

    for record in response_object.records:
        print(f"\nRecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"TravelTime: {record.travel_time}")
        print(f"TotalDrivingDistance: {record.total_driving_distance}")
