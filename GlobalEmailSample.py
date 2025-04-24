from melissadatacloudapi.RecordRequests import GlobalEmailRecordRequest
from melissadatacloudapi.cloudapis.GlobalEmail import GlobalEmail
from melissadatacloudapi.apiresponse import GlobalEmailResponse
from melissadatacloudapi.PostReqestBase import GlobalEmailPostRequest

def global_email_sample(license_key):
        """
        This function uses the Global Email Cloud API object to make a GET request
        """
        global_email = GlobalEmail(license_key)
        global_email.set_email("info@melissa.com")

        global_email.set_value("email", "info@melissa.com")

        response = global_email.get(str)

        response_objectect = global_email.get(GlobalEmailResponse)

        print(response)

        print(f"\nVersion: {response_objectect.get_value('Version')}")
        print(f"TransmissionReference: {response_objectect.transmission_reference}")
        print(f"TotalRecords: {response_objectect.total_records}\n")
        for record in response_objectect.records:
            print("RecordID: " + record.get_value("RecordID"))
            print("DeliverabilityConfidenceScore: " + record.get_value("DeliverabilityConfidenceScore"))
            print("Results: " + record.get_value("Results"))
            print("EmailAddress: " + record.get_value("EmailAddress"))
            print("MailboxName: " + record.get_value("MailboxName"))
            print("DomainName: " + record.get_value("DomainName"))
            print("DomainAuthenticationStatus: " + record.get_value("DomainAuthenticationStatus"))
            print("TopLevelDomain: " + record.get_value("TopLevelDomain"))
            print("TopLevelDomainName: " + record.get_value("TopLevelDomainName"))
            print("DateChecked: " + record.date_checked)
            print("EmailAgeEstimated: " + record.email_age_estimated)
            print("DomainAgeEstimated: " + record.domain_age_estimated)
            print("DomainExpirationDate: " + record.domain_expiration_date)
            print("DomainCreatedDate: " + record.domain_created_date)
            print("DomainUpdatedDate: " + record.domain_updated_date)
            print("DomainEmail: " + record.domain_email)
            print("DomainOrganization: " + record.domain_organization)
            print("DomainAddress1: " + record.domain_address1)
            print("DomainLocality: " + record.domain_locality)
            print("DomainAdministrativeArea: " + record.domain_administrative_area)
            print("DomainPostalCode: " + record.get_domain_postal_code())
            print("DomainCountry: " + record.get_domain_country())
            print("DomainCountryCode: " + record.get_domain_country())
            print("DomainAvailability: " + record.get_domain_availability())
            print("DomainPrivateProxy: " + record.get_domain_private_proxy())
            print("PrivacyFlag: " + record.get_privacy_flag())
            print("MXServer: " + record.get_mx_server())
            print("DomainTypeIndicator: " + record.get_domain_type_indicator())
            print("BreachCount: " + record.get_breach_count())

def global_email_batch_1_sample(license_key):
    """
    This function uses the Global Email Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    global_email = GlobalEmail(license_key)

    global_email.set_post_body(GlobalEmailPostRequest(
        customer_id=license_key, 
        records=[
            GlobalEmailRecordRequest(record_id="1", email="info@melissa.com"),
            GlobalEmailRecordRequest(record_id="2", email="test@melissa.com"),
        ]
    ))

    response = global_email.post(str)

    response_object = global_email.post(GlobalEmailResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print("RecordID: " + record.record_id)
        print("Results: " + record.results)
        print("EmailAddress: " + record.email_address)
        print("MailboxName: " + record.mailbox_name)
        print("DomainName: " + record.domain_name)
        print("DomainAuthenticationStatus: " + record.domain_authentication_status)
        print("TopLevelDomain: " + record.top_level_domain)
        print("TopLevelDomainName: " + record.top_level_domain_name)
        print("DateChecked: " + record.date_checked)
        print("EmailAgeEstimated: " + record.email_age_estimated)
        print("DeliverabilityConfidenceScore: " + record.deliverability_confidence_score)
        print("DomainAgeEstimated: " + record.domain_age_estimated)
        print("DomainExpirationDate: " + record.domain_expiration_date)
        print("DomainCreatedDate: " + record.domain_created_date)
        print("DomainUpdatedDate: " + record.domain_updated_date)
        print("DomainEmail: " + record.domain_email)
        print("DomainOrganization: " + record.domain_organization)
        print("DomainAddress1: " + record.domain_address1)
        print("DomainLocality: " + record.domain_locality)
        print("DomainAdministrativeArea: " + record.domain_administrative_area)
        print("DomainPostalCode: " + record.domain_postal_code)
        print("DomainCountry: " + record.domain_country)
        print("DomainCountryCode: " + record.domain_country_code)
        print("DomainAvailability: " + record.domain_availability)
        print("DomainPrivateProxy: " + record.domain_private_proxy)
        print("PrivacyFlag: " + record.privacy_flag)
        print("MXServer: " + record.mx_server)
        print("DomainTypeIndicator: " + record.domain_type_indicator)
        print("BreachCount: " + record.breach_count + "\n\n")

def global_email_batch_2_sample(license_key):
    """
    This function uses the Global Email Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    global_email = GlobalEmail(license_key)
    global_email.add_record(GlobalEmailRecordRequest(record_id="1", email="info@melissa.com"))
    global_email.add_record(GlobalEmailRecordRequest(record_id="2", email="test@melissa.com"))

    response = global_email.post(str)
    response_object = global_email.post(GlobalEmailResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionReference: {response_object.transmission_reference}")
    print(f"TotalRecords: {response_object.total_records}\n")

    for record in response_object.records:
        print("RecordID: " + record.record_id)
        print("Results: " + record.results)
        print("EmailAddress: " + record.email_address)
        print("MailboxName: " + record.mailbox_name)
        print("DomainName: " + record.domain_name)
        print("DomainAuthenticationStatus: " + record.domain_authentication_status)
        print("TopLevelDomain: " + record.top_level_domain)
        print("TopLevelDomainName: " + record.top_level_domain_name)
        print("DateChecked: " + record.date_checked)
        print("EmailAgeEstimated: " + record.email_age_estimated)
        print("DeliverabilityConfidenceScore: " + record.deliverability_confidence_score)
        print("DomainAgeEstimated: " + record.domain_age_estimated)
        print("DomainExpirationDate: " + record.domain_expiration_date)
        print("DomainCreatedDate: " + record.domain_created_date)
        print("DomainUpdatedDate: " + record.domain_updated_date)
        print("DomainEmail: " + record.domain_email)
        print("DomainOrganization: " + record.domain_organization)
        print("DomainAddress1: " + record.domain_address1)
        print("DomainLocality: " + record.domain_locality)
        print("DomainAdministrativeArea: " + record.domain_administrative_area)
        print("DomainPostalCode: " + record.domain_postal_code)
        print("DomainCountry: " + record.domain_country)
        print("DomainCountryCode: " + record.domain_country_code)
        print("DomainAvailability: " + record.domain_availability)
        print("DomainPrivateProxy: " + record.domain_private_proxy)
        print("PrivacyFlag: " + record.privacy_flag)
        print("MXServer: " + record.mx_server)
        print("DomainTypeIndicator: " + record.domain_type_indicator)
        print("BreachCount: " + record.breach_count + "\n\n")
