from melissadatacloudapi.RecordRequests import SSNNameMatchRecordRequest
from melissadatacloudapi.cloudapis.SSNNameMatch import SSNNameMatch
from melissadatacloudapi.apiresponse import SSNNameMatchResponse
from melissadatacloudapi.PostReqestBase import SSNNameMatchPostRequest


def ssn_name_match_sample(license_key):
    """
    This function uses the SSN Name Match Cloud API object to make a GET request
    """
    ssn_name_match = SSNNameMatch(license_key)
    ssn_name_match.set_ssn("111223333")

    response = ssn_name_match.get(str)
    response_object = ssn_name_match.get(SSNNameMatchResponse)

    print(response)

    print(f"\nTransmissionResults: {response_object.get_transmission_results()}")
    print(f"Version: {response_object.get_version()}")
    print(f"TotalRecords: {response_object.get_total_records()}")
    for record in response_object.records:
        print(f"\nRecordID: {record.get_record_id()}")
        print(f"SSN: {record.get_ssn()}")
        print(f"IssuingState: {record.get_issuing_state()}")
        print(f"Results: {record.get_results()}")
        print(f"ResultsFromDataSource: {record.get_results_from_data_source()}")


def ssn_name_match_batch_1_sample(license_key):
    """
    This function uses the SSN Name Match Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    ssn_name_match = SSNNameMatch(license_key)
    ssn_name_match.set_post_body(SSNNameMatchPostRequest(
        customer_id=license_key,
        records=[
            SSNNameMatchRecordRequest(
                record_id="1",
                ssn="111223333"
            ),
            SSNNameMatchRecordRequest(
                record_id="2",
                ssn="419251021",
            )
        ]
    ))
    
    response = ssn_name_match.post(str)
    response_object = ssn_name_match.post(SSNNameMatchResponse)

    print(response)

    print(f"\nTransmissionResults: {response_object.get_transmission_results()}")
    print(f"Version: {response_object.get_version()}")
    print(f"TotalRecords: {response_object.get_total_records()}")
    for record in response_object.records:
        print(f"\nRecordID: {record.get_record_id()}")
        print(f"SSN: {record.get_ssn()}")
        print(f"IssuingState: {record.get_issuing_state()}")
        print(f"Results: {record.get_results()}")
        print(f"ResultsFromDataSource: {record.get_results_from_data_source()}")


def ssn_name_match_batch_2_sample(license_key):
    """
    This function uses the SSN Name Match Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    ssn_name_match = SSNNameMatch(license_key)
    ssn_name_match.add_record(
        SSNNameMatchRecordRequest(
            record_id="1",
            ssn="111223333"
        ))
    
    ssn_name_match.add_record(
        SSNNameMatchRecordRequest(
            record_id="2",
            ssn="419251021",
        ))
       
    response = ssn_name_match.post(str)
    response_object = ssn_name_match.post(SSNNameMatchResponse)

    print(response)

    print(f"\nTransmissionResults: {response_object.get_transmission_results()}")
    print(f"Version: {response_object.get_version()}")
    print(f"TotalRecords: {response_object.get_total_records()}")
    for record in response_object.records:
        print(f"\nRecordID: {record.get_record_id()}")
        print(f"SSN: {record.get_ssn()}")
        print(f"IssuingState: {record.get_issuing_state()}")
        print(f"Results: {record.get_results()}")
        print(f"ResultsFromDataSource: {record.get_results_from_data_source()}")

