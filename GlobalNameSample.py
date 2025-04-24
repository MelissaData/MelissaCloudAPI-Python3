from melissadatacloudapi.RecordRequests import GlobalNameRecordRequest
from melissadatacloudapi.cloudapis.GlobalName import GlobalName
from melissadatacloudapi.apiresponse import GlobalNameResponse
from melissadatacloudapi.PostReqestBase import GlobalNamePostRequest

def global_name_sample(license_key):
        """
        This function uses the Global Name Cloud API object to make a GET request
        """
        global_name = GlobalName(license_key)
        global_name.set_full_name("Raymond Melissa")

        response = global_name.get()
        response_object = global_name.get(GlobalNameResponse)

        print(response)

        print(f"\nVersion: {response_object.version}")
        print(f"TransmissionReference: {response_object.transmission_reference}")
        print(f"TransmissionResults: {response_object.transmission_results}")
        print(f"TotalRecords: {response_object.total_records}\n")

        for record in response_object.records:
            print(f"RecordID: {record.record_id}")
            print(f"Results: {record.results}")
            print(f"Company: {record.company}")
            print(f"NamePrefix: {record.name_prefix}")
            print(f"NameFirst: {record.name_first}")
            print(f"NameMiddle: {record.name_middle}")
            print(f"NameLast: {record.name_last}")
            print(f"NameSuffix: {record.name_suffix}")
            print(f"NameNickname: {record.name_nickname}")
            print(f"NameProfTitle: {record.name_prof_title}")
            print(f"Gender: {record.gender}")
            print(f"NamePrefix2: {record.name_prefix2}")
            print(f"NameFirst2: {record.name_first2}")
            print(f"NameMiddle2: {record.name_middle2}")
            print(f"NameLast2: {record.name_last2}")
            print(f"NameSuffix2: {record.name_suffix2}")
            print(f"NameNickname2: {record.name_nickname2}")
            print(f"NameProfTitle2: {record.name_prof_title2}")
            print(f"Gender2: {record.gender2}")
            print(f"Salutation: {record.salutation}")
            print(f"Extras: {record.extras}")



def global_name_batch_1_sample(license_key):
    """
    This function uses the Global Name Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective BatchRequest class
    """
    global_name = GlobalName()
    global_name.set_post_body(GlobalNamePostRequest(
        customer_id=license_key,
        records=[
            GlobalNameRecordRequest(record_id="1", full_name="Raymond Melissa"),
            GlobalNameRecordRequest(record_id="2", full_name="Daniel Kha Le")
        ]
    ))

    response = global_name.post()
    response_object = global_name.post(GlobalNameResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print(f"RecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"Company: {record.company}")
        print(f"NamePrefix: {record.name_prefix}")
        print(f"NameFirst: {record.name_first}")
        print(f"NameMiddle: {record.name_middle}")
        print(f"NameLast: {record.name_last}")
        print(f"NameSuffix: {record.name_suffix}")
        print(f"NameNickname: {record.name_nickname}")
        print(f"NameProfTitle: {record.name_prof_title}")
        print(f"Gender: {record.gender}")
        print(f"NamePrefix2: {record.name_prefix2}")
        print(f"NameFirst2: {record.name_first2}")
        print(f"NameMiddle2: {record.name_middle2}")
        print(f"NameLast2: {record.name_last2}")
        print(f"NameSuffix2: {record.name_suffix2}")
        print(f"NameNickname2: {record.name_nickname2}")
        print(f"NameProfTitle2: {record.name_prof_title2}")
        print(f"Gender2: {record.gender2}")
        print(f"Salutation: {record.salutation}")
        print(f"Extras: {record.extras}\n\n")

def global_name_batch_2_sample(license_key):
    """
    This function uses the Global Name Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    global_name = GlobalName(license_key)
    global_name.add_record(GlobalNameRecordRequest(record_id="1", full_name="Raymond Melissa"))
    global_name.add_record(GlobalNameRecordRequest(record_id="2", full_name="Daniel Kha Le"))

    response = global_name.post()
    response_object = global_name.post(GlobalNameResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print(f"RecordID: {record.record_id}")
        print(f"Results: {record.results}")
        print(f"Company: {record.company}")
        print(f"NamePrefix: {record.name_prefix}")
        print(f"NameFirst: {record.name_first}")
        print(f"NameMiddle: {record.name_middle}")
        print(f"NameLast: {record.name_last}")
        print(f"NameSuffix: {record.name_suffix}")
        print(f"NameNickname: {record.name_nickname}")
        print(f"NameProfTitle: {record.name_prof_title}")
        print(f"Gender: {record.gender}")
        print(f"NamePrefix2: {record.name_prefix2}")
        print(f"NameFirst2: {record.name_first2}")
        print(f"NameMiddle2: {record.name_middle2}")
        print(f"NameLast2: {record.name_last2}")
        print(f"NameSuffix2: {record.name_suffix2}")
        print(f"NameNickname2: {record.name_nickname2}")
        print(f"NameProfTitle2: {record.name_prof_title2}")
        print(f"Gender2: {record.gender2}")
        print(f"Salutation: {record.salutation}")
        print(f"Extras: {record.extras}\n\n")
