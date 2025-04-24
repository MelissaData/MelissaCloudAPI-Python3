from melissadatacloudapi.RecordRequests import PropertyRecordRequest
from melissadatacloudapi.cloudapis.Property import Property
from melissadatacloudapi.apiresponse import PropertyResponse
from melissadatacloudapi.PostReqestBase import PropertyPostRequest


def property_sample(license_key):
    """
    This function uses the Property Cloud API object to make a GET request
    Multiple endpoints are tested 
    """
    property_instance = Property(license_key)
    property_instance.set_address_line_1("22382 Avenida Empresa")
    property_instance.set_city("Rancho Santa Margarita")
    property_instance.set_state("CA")

    response = property_instance.get_lookup_property(str)
    response_object = property_instance.get_lookup_property(PropertyResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"Results: {record.results}")
        print(f"Parcel: \n" +
                f"  FIPSCode: {record.parcel.fips_code}\n" +
                f"  UnformattedAPN: {record.parcel.unformatted_apn}\n" +
                f"  FormattedAPN: {record.parcel.formatted_apn}\n")
        print(f"PrimaryOwner: \n" +
                f"  Name1Full: {record.primary_owner.name1_full}\n")
        print(f"Tax: \n" +
                f"  AssessedValueTotal: {record.tax.assessed_value_total}\n" +
                f"  MarketValueTotal: {record.tax.market_value_total}\n" +
                f"  TaxFiscalYear: {record.tax.tax_fiscal_year}\n" +
                f"  TaxBilledAmount: {record.tax.tax_billed_amount}\n")
        print(f"SaleInfo: \n" +
                f"  AssessorLastSaleDate: {record.sale_info.assessor_last_sale_date}\n" +
                f"  AssessorLastSaleAmount: {record.sale_info.assessor_last_sale_amount}\n" +
                f"  AssessorPriorSaleDate: {record.sale_info.assessor_prior_sale_date}\n" +
                f"  AssessorPriorSaleAmount: {record.sale_info.assessor_prior_sale_amount}\n" +
                f"  DeedLastSaleDate: {record.sale_info.deed_last_sale_date}\n" +
                f"  DeedLastSalePrice: {record.sale_info.deed_last_sale_price}\n")
        print(f"PropertySize: \n" +
                f"  AreaBuilding: {record.property_size.area_building}\n" +
                f"  AreaLotAcres: {record.property_size.area_lot_acres}\n" +
                f"  AreaLotSF: {record.property_size.area_lot_sf}\n")
        print(f"IntRoomInfo: \n" +
                f"  BathCount: {record.int_room_info.bath_count}\n" +
                f"  BedroomsCount: {record.int_room_info.bedrooms_count}\n" +
                f"  RoomsCount: {record.int_room_info.rooms_count}\n")

    property_instance.clear()

    property_instance.set_fips("06059")
    property_instance.set_apn("80505208")

    response = property_instance.get_lookup_deeds(str)
    response_object = property_instance.get_lookup_deeds(PropertyResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"DocInfo: \n" +
                f"  RecordingDate: {record.doc_info.get_recording_date()}")
        print(f"TxDefInfo: \n" +
                f"  TransactionType: {record.tx_def_info.get_transaction_type()}")
        print(f"TxAmtInfo: \n" +
                f"  TransferAmount: {record.tx_amt_info.get_transfer_amount()}")
        print(f"PrimaryGrantor: \n" +
                f"  Name1Full: {record.primary_grantor.get_name1_full()}\n" +
                f"  Name2Full: {record.primary_grantor.get_name2_full()}")
        print(f"PrimaryGrantee: \n" +
                f"  Name1Full: {record.primary_grantee.get_name1_full()}\n" +
                f"  Name2Full: {record.primary_grantee.get_name2_full()}")
        print(f"TitleCompInfo: \n" +
                f"  StandardizedName: {record.title_comp_info.get_standardized_name()}")
        print(f"Mortgage1: \n" +
                f"  RecordingDate: {record.mortgage1.get_recording_date()}\n" +
                f"  Amount: {record.mortgage1.amount}\n" +
                f"  InterestRate {record.mortgage1.get_interest_rate()}\n")

    property_instance.clear()

    property_instance.set_mak("9005381555")

    response = property_instance.get_lookup_homes_by_owner(str)
    response_object = property_instance.get_lookup_homes_by_owner(PropertyResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"  MAK: {record.mak}\n" +
                f"  BaseMAK: {record.base_mak}\n" +
                f"  FIPS: {record.fips}\n" +
                f"  APN: {record.apn}\n" +
                f"  PropertyAddress: {record.property_address}\n" +
                f"  PropertyCity: {record.property_city}\n" +
                f"  PropertyState: {record.property_state}\n" +
                f"  PropertyZip: {record.property_zip}\n" +
                f"  PropertyPlus4: {record.property_plus4}\n")

        
def property_post_1_sample(license_key):
    """
    This function uses the Property Cloud API object to make a POST request
    This tests the lookuphomesbyowner and lookupdeeds endpoints that have a different request structure than the lookupproperty endpoint
    Use PropertyPostRequest for these endpoints even though they do not work with BATCH 
    """
    property_instance = Property(license_key)
    property_instance.set_post_body(PropertyPostRequest(
        customer_id=license_key,
        free_form="1 Microsoft Way, Redmond, WA 98052"
    ))
    

    response = property_instance.post_lookup_homes_by_owner(str)
    response_object = property_instance.post_lookup_homes_by_owner(PropertyResponse)

    print(response)

   
    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"  MAK: {record.mak}\n" +
                f"  BaseMAK: {record.base_mak}\n" +
                f"  FIPS: {record.fips}\n" +
                f"  APN: {record.apn}\n" +
                f"  PropertyAddress: {record.property_address}\n" +
                f"  PropertyCity: {record.property_city}\n" +
                f"  PropertyState: {record.property_state}\n" +
                f"  PropertyZip: {record.property_zip}\n" +
                f"  PropertyPlus4: {record.property_plus4}\n")

    property_instance.set_post_body(PropertyPostRequest(
        customer_id=license_key,
        fips="06059",
        apn="14312308"
    ))

    response = property_instance.post_lookup_deeds(str)
    response_object = property_instance.post_lookup_deeds(PropertyResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"DocInfo: \n" +
                f"  RecordingDate: {record.doc_info.get_recording_date()}")
        print(f"TxDefInfo: \n" +
                f"  TransactionType: {record.tx_def_info.get_transaction_type()}")
        print(f"TxAmtInfo: \n" +
                f"  TransferAmount: {record.tx_amt_info.get_transfer_amount()}")
        print(f"PrimaryGrantor: \n" +
                f"  Name1Full: {record.primary_grantor.get_name1_full()}\n" +
                f"  Name2Full: {record.primary_grantor.get_name2_full()}")
        print(f"PrimaryGrantee: \n" +
                f"  Name1Full: {record.primary_grantee.get_name1_full()}\n" +
                f"  Name2Full: {record.primary_grantee.get_name2_full()}")
        print(f"TitleCompInfo: \n" +
                f"  StandardizedName: {record.title_comp_info.get_standardized_name()}")
        print(f"Mortgage1: \n" +
                f"  RecordingDate: {record.mortgage1.get_recording_date()}\n" +
                f"  Amount: {record.mortgage1.amount}\n" +
                f"  InterestRate {record.mortgage1.get_interest_rate()}\n")


def property_post_2_sample(license_key):
    """
    This function uses the Property Cloud API object to make a POST BATCH request
    This function showcases method 1 of setting and making POST requests: construct the POST body structure using the Cloud API's respective PostRequest class
    """
    property_instance = Property(license_key)
    
    property_instance.set_post_body(PropertyPostRequest(
        customer_id=license_key,
        total_records="2",
        records=[
            PropertyRecordRequest(
                record_id="1",
                address_line_1="22382 Avenida Empresa",
                city="RSM",
                state="CA",
                postal_code="92688"
            ),
            PropertyRecordRequest(
                record_id="2",
                address_line_1="710 Winston Ln",
                city="Sugar Land",
                state="TX",
                postal_code="77479"
            )
        ]
    ))

    response = property_instance.post_lookup_property(str)
    response_object = property_instance.post_lookup_property(PropertyResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"Results: {record.results}")
        print(f"Parcel: \n" +
                f"  FIPSCode: {record.parcel.fips_code}\n" +
                f"  UnformattedAPN: {record.parcel.unformatted_apn}\n" +
                f"  FormattedAPN: {record.parcel.formatted_apn}\n")
        print(f"PrimaryOwner: \n" +
                f"  Name1Full: {record.primary_owner.name1_full}\n")
        print(f"Tax: \n" +
                f"  AssessedValueTotal: {record.tax.assessed_value_total}\n" +
                f"  MarketValueTotal: {record.tax.market_value_total}\n" +
                f"  TaxFiscalYear: {record.tax.tax_fiscal_year}\n" +
                f"  TaxBilledAmount: {record.tax.tax_billed_amount}\n")
        print(f"SaleInfo: \n" +
                f"  AssessorLastSaleDate: {record.sale_info.assessor_last_sale_date}\n" +
                f"  AssessorLastSaleAmount: {record.sale_info.assessor_last_sale_amount}\n" +
                f"  AssessorPriorSaleDate: {record.sale_info.assessor_prior_sale_date}\n" +
                f"  AssessorPriorSaleAmount: {record.sale_info.assessor_prior_sale_amount}\n" +
                f"  DeedLastSaleDate: {record.sale_info.deed_last_sale_date}\n" +
                f"  DeedLastSalePrice: {record.sale_info.deed_last_sale_price}\n")
        print(f"PropertySize: \n" +
                f"  AreaBuilding: {record.property_size.area_building}\n" +
                f"  AreaLotAcres: {record.property_size.area_lot_acres}\n" +
                f"  AreaLotSF: {record.property_size.area_lot_sf}\n")
        print(f"IntRoomInfo: \n" +
                f"  BathCount: {record.int_room_info.bath_count}\n" +
                f"  BedroomsCount: {record.int_room_info.bedrooms_count}\n" +
                f"  RoomsCount: {record.int_room_info.rooms_count}\n")


def property_post_3_sample(license_key):
    """
    This function uses the Property Cloud API object to make a POST BATCH request
    This function showcases method 2 of setting and making POST requests: construct the POST body record by using the Cloud API's respective RecordRequest class
    """
    property_instance = Property(license_key)
    
    property_instance.add_record(
        PropertyRecordRequest(
            record_id="1",
            address_line_1="22382 Avenida Empresa",
            city="RSM",
            state="CA",
            postal_code="92688"
            )
    )
    property_instance.add_record(
        PropertyRecordRequest(
            record_id="2",
            address_line_1="710 Winston Ln",
            city="Sugar Land",
            state="TX",
        )
    )

    property_instance.set_total_records("2")

    response = property_instance.post_lookup_property(str)
    response_object = property_instance.post_lookup_property(PropertyResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"TransmissionResults: {response_object.transmission_results}")
    print(f"TotalRecords: {response_object.total_records}\n")
    for record in response_object.records:
        print(f"Results: {record.results}")
        print(f"Parcel: \n" +
                f"  FIPSCode: {record.parcel.fips_code}\n" +
                f"  UnformattedAPN: {record.parcel.unformatted_apn}\n" +
                f"  FormattedAPN: {record.parcel.formatted_apn}\n")
        print(f"PrimaryOwner: \n" +
                f"  Name1Full: {record.primary_owner.name1_full}\n")
        print(f"Tax: \n" +
                f"  AssessedValueTotal: {record.tax.assessed_value_total}\n" +
                f"  MarketValueTotal: {record.tax.market_value_total}\n" +
                f"  TaxFiscalYear: {record.tax.tax_fiscal_year}\n" +
                f"  TaxBilledAmount: {record.tax.tax_billed_amount}\n")
        print(f"SaleInfo: \n" +
                f"  AssessorLastSaleDate: {record.sale_info.assessor_last_sale_date}\n" +
                f"  AssessorLastSaleAmount: {record.sale_info.assessor_last_sale_amount}\n" +
                f"  AssessorPriorSaleDate: {record.sale_info.assessor_prior_sale_date}\n" +
                f"  AssessorPriorSaleAmount: {record.sale_info.assessor_prior_sale_amount}\n" +
                f"  DeedLastSaleDate: {record.sale_info.deed_last_sale_date}\n" +
                f"  DeedLastSalePrice: {record.sale_info.deed_last_sale_price}\n")
        print(f"PropertySize: \n" +
                f"  AreaBuilding: {record.property_size.area_building}\n" +
                f"  AreaLotAcres: {record.property_size.area_lot_acres}\n" +
                f"  AreaLotSF: {record.property_size.area_lot_sf}\n")
        print(f"IntRoomInfo: \n" +
                f"  BathCount: {record.int_room_info.bath_count}\n" +
                f"  BedroomsCount: {record.int_room_info.bedrooms_count}\n" +
                f"  RoomsCount: {record.int_room_info.rooms_count}\n")

