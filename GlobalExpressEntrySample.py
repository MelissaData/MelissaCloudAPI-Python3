from melissadatacloudapi.cloudapis.GlobalExpressEntry import GlobalExpressEntry
from melissadatacloudapi.apiresponse import GlobalExpressEntryResponse
from melissadatacloudapi.apiresponse import ExpressEntryResponse



def global_express_entry_sample(license_key):
    """
    This function uses the Global Express Entry Cloud API object to make a GET request
    Multiple endpoints are tested
    """
    global_express_entry = GlobalExpressEntry(license_key)
    global_express_entry.set_address_line_1("22382 Avenida Empresa")
    global_express_entry.set_city("RSM")
    global_express_entry.set_state("CA")
    global_express_entry.set_postal("92688")

    response = global_express_entry.get_express_address(str)
    response_object = global_express_entry.get_express_address(ExpressEntryResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"ResultCode: {response_object.result_code}")
    print(f"ErrorString: {response_object.error_string}\n")

    for record in response_object.results:
        address = record.address
        print(f"Address: \n"
              f"  AddressLine1: {address.address_line_1}\n"
              f"  City: {address.city}\n"
              f"  CityAccepted: {address.city_accepted}\n"
              f"  State: {address.state}\n"
              f"  PostalCode: {address.postal_code}\n"
              f"  CountrySubdivisionCode: {address.country_subdivision_code}\n"
              f"  AddressKey: {address.address_key}\n"
              f"  SuiteCount: {address.suite_count}\n"
              f"  Plus4: {address.plus_four[0] if address.plus_four else ''}\n"
              f"  MAK: {address.mak}\n")

    global_express_entry.clear()

    global_express_entry.set_city("RSM")
    global_express_entry.set_state("CA")

    response = global_express_entry.get_express_city_state(str)
    response_object = global_express_entry.get_express_city_state(ExpressEntryResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"ResultCode: {response_object.result_code}")
    print(f"ErrorString: {response_object.error_string}\n")

    for record in response_object.results:
        address = record.address
        print(f"Address: \n"
              f"  City: {address.city}\n"
              f"  CityAccepted: {address.city_accepted}\n"
              f"  State: {address.state}\n"
              f"  PostalCode: {address.postal_code}\n"
              f"  CountrySubdivisionCode: {address.country_subdivision_code}\n"
              f"  SuiteCount: {address.suite_count}\n"
              )

    global_express_entry.clear()

    global_express_entry.set_postal("92688")

    response = global_express_entry.get_express_postal_code(str)
    response_object = global_express_entry.get_express_postal_code(ExpressEntryResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"ResultCode: {response_object.result_code}")
    print(f"ErrorString: {response_object.error_string}\n")

    for record in response_object.results:
        address = record.address
        print(f"Address: \n"
              f"  City: {address.city}\n"
              f"  CityAccepted: {address.city_accepted}\n"
              f"  State: {address.state}\n"
              f"  PostalCode: {address.postal_code}\n"
              f"  CountrySubdivisionCode: {address.country_subdivision_code}\n"
              f"  SuiteCount: {address.suite_count}\n"
              )

    global_express_entry.clear()

    global_express_entry.set_address_line_1("Avenida")
    global_express_entry.set_postal("92688")

    response = global_express_entry.get_express_street(str)
    response_object = global_express_entry.get_express_street(ExpressEntryResponse)

    print(response)

    print(f"\nVersion: {response_object.version}")
    print(f"ResultCode: {response_object.result_code}")
    print(f"ErrorString: {response_object.error_string}\n")

    for record in response_object.results:
        address = record.address
        print(f"Address: \n"
              f"  AddressLine1: {address.address_line_1}\n"
              f"  City: {address.city}\n"
              f"  CityAccepted: {address.city_accepted}\n"
              f"  State: {address.state}\n"
              f"  PostalCode: {address.postal_code}\n"
              f"  CountrySubdivisionCode: {address.country_subdivision_code}\n"
              f"  SuiteCount: {address.suite_count}\n"
              )

    global_express_entry.clear()

    global_express_entry.set_address_line_1("Avenida Empresa, Rancho Santa Margarita, CA")
    global_express_entry.set_locality("Rancho Santa Margarita")
    global_express_entry.set_administrative_area("CA")
    global_express_entry.set_postal("92688")
    global_express_entry.set_country("United States")
    global_express_entry.set_max_records("2")

    response = global_express_entry.get_global_express_address(str)
    global_response_object = global_express_entry.get_global_express_address(GlobalExpressEntryResponse)

    print(response)

    print(f"\nVersion: {global_response_object.version}")
    print(f"ResultCode: {global_response_object.result_code}")
    print(f"ErrorString: {global_response_object.error_string}\n")

    for record in global_response_object.results:
        address = record.address
        print(f"Address: \n"
              f"  Address: {address.address}\n"
              f"  Address1: {address.address1}\n"
              f"  Address2: {address.address2}\n"
              f"  DeliveryAddress: {address.delivery_address}\n"
              f"  DeliveryAddress1: {address.delivery_address1}\n"
              f"  CountryName: {address.country_name}\n"
              f"  ISO3166_2: {address.iso3166_2}\n"
              f"  ISO3166_3: {address.iso3166_3}\n"
              f"  ISO3166_N: {address.iso3166_n}\n"
              f"  AdministrativeArea: {address.administrative_area}\n"
              f"  SubAdministrativeArea: {address.sub_administrative_area}\n"
              f"  Locality: {address.locality}\n"
              f"  CityAccepted: {address.city_accepted}\n"
              f"  Thoroughfare: {address.thoroughfare}\n"
              f"  Premise: {address.premise}\n"
              f"  SubBuilding: {address.sub_building}\n"
              f"  PostalCode: {address.postal_code}\n"
              f"  PostalCodePrimary: {address.postal_code_primary}\n"
              f"  PostalCodeSecondary: {address.postal_code_secondary}\n"
              f"  CountrySubdivisionCode: {address.country_subdivision_code}\n"
              f"  MAK: {address.mak}\n"
              f"  BaseMAK: {address.base_mak}\n"
              f"  DistanceFromPoint: {address.distance_from_point}\n")

    global_express_entry.clear()

    global_express_entry.set_country("France")

    response = global_express_entry.get_global_express_country(str)
    global_response_object = global_express_entry.get_global_express_country(GlobalExpressEntryResponse)

    print(response)

    print(f"\nVersion: {global_response_object.version}")
    print(f"ResultCode: {global_response_object.result_code}")
    print(f"ErrorString: {global_response_object.error_string}\n")

    for record in global_response_object.results:
        print(f"Address: \n"
              f"  Country: {record.country}\n"
              f"  English: {record.english}\n"
              f"  Spanish: {record.spanish}\n"
              f"  French: {record.french}\n"
              f"  German: {record.german}\n"
              f"  SimplifiedChinese: {record.simplified_chinese}\n"
              f"  Char2ISO: {record.char2_iso}\n"
              f"  Char3ISO: {record.char3_iso}\n"
              f"  ISONumeric: {record.iso_numeric}\n")

    global_express_entry.clear()

    global_express_entry.set_free_form("22382 Avenida Empresa, RSM, CA, 92688")
    global_express_entry.set_country("United States")

    response = global_express_entry.get_global_express_free_form(str)
    global_response_object = global_express_entry.get_global_express_free_form(GlobalExpressEntryResponse)

    print(response)

    print(f"\nVersion: {global_response_object.version}")
    print(f"ResultCode: {global_response_object.result_code}")
    print(f"ErrorString: {global_response_object.error_string}\n")

    for record in global_response_object.results:
      print(f"Address: \n" +
            f"  Address: {record.address.address}\n" +
            f"  Address1: {record.address.address1}\n" +
            f"  Address2: {record.address.address2}\n" +
            f"  DeliveryAddress: {record.address.delivery_address}\n" +
            f"  DeliveryAddress1: {record.address.delivery_address1}\n" +
            f"  CountryName: {record.address.country_name}\n" +
            f"  ISO3166_2: {record.address.iso3166_2}\n" +
            f"  ISO3166_3: {record.address.iso3166_3}\n" +
            f"  ISO3166_N: {record.address.iso3166_n}\n" +
            f"  AdministrativeArea: {record.address.administrative_area}\n" +
            f"  SubAdministrativeArea: {record.address.sub_administrative_area}\n" +
            f"  Locality: {record.address.locality}\n" +
            f"  CityAccepted: {record.address.city_accepted}\n" +
            f"  Thoroughfare: {record.address.thoroughfare}\n" +
            f"  Premise: {record.address.premise}\n" +
            f"  SubBuilding: {record.address.sub_building}\n" +
            f"  PostalCode: {record.address.postal_code}\n" +
            f"  PostalCodePrimary: {record.address.postal_code_primary}\n" +
            f"  PostalCodeSecondary: {record.address.postal_code_secondary}\n" +
            f"  CountrySubdivisionCode: {record.address.country_subdivision_code}\n" +
            f"  MAK: {record.address.mak}\n" +
            f"  BaseMAK: {record.address.base_mak}\n" +
            f"  DistanceFromPoint: {record.address.distance_from_point}\n")
      

    global_express_entry.set_postal("92688")
    global_express_entry.set_country("United States")

    response = global_express_entry.get_global_express_postal_code(str)
    global_response_objectect = global_express_entry.get_global_express_postal_code(GlobalExpressEntryResponse)

    print(response)

    print(f"\nVersion: {global_response_objectect.version}")
    print(f"ResultCode: {global_response_objectect.result_code}")
    print(f"ErrorString: {global_response_objectect.error_string}\n")

    for record in global_response_objectect.results:
        print(f"Address: \n" +
              f"  Address: {record.address.address}\n" +
              f"  Address1: {record.address.address1}\n" +
              f"  Address2: {record.address.address2}\n" +
              f"  DeliveryAddress: {record.address.delivery_address}\n" +
              f"  DeliveryAddress1: {record.address.delivery_address1}\n" +
              f"  CountryName: {record.address.country_name}\n" +
              f"  ISO3166_2: {record.address.iso3166_2}\n" +
              f"  ISO3166_3: {record.address.iso3166_3}\n" +
              f"  ISO3166_N: {record.address.iso3166_n}\n" +
              f"  AdministrativeArea: {record.address.administrative_area}\n" +
              f"  SubAdministrativeArea: {record.address.sub_administrative_area}\n" +
              f"  Locality: {record.address.locality}\n" +
              f"  CityAccepted: {record.address.city_accepted}\n" +
              f"  Thoroughfare: {record.address.thoroughfare}\n" +
              f"  Premise: {record.address.premise}\n" +
              f"  SubBuilding: {record.address.sub_building}\n" +
              f"  PostalCode: {record.address.postal_code}\n" +
              f"  PostalCodePrimary: {record.address.postal_code_primary}\n" +
              f"  PostalCodeSecondary: {record.address.postal_code_secondary}\n" +
              f"  CountrySubdivisionCode: {record.address.country_subdivision_code}\n" +
              f"  MAK: {record.address.mak}\n" +
              f"  BaseMAK: {record.address.base_mak}\n" +
              f"  DistanceFromPoint: {record.address.distance_from_point}\n")
    
    global_express_entry.clear()

    global_express_entry.set_thoroughfare("avenida empresa")
    global_express_entry.set_postal("92688")
    global_express_entry.set_country("united states")

    response = global_express_entry.get_global_express_thoroughfare(str)
    global_response_object = global_express_entry.get_global_express_thoroughfare(GlobalExpressEntryResponse)

    print(response)


    print(f"\nVersion: {global_response_objectect.version}")
    print(f"ResultCode: {global_response_objectect.result_code}")
    print(f"ErrorString: {global_response_objectect.error_string}\n")

    for record in global_response_objectect.results:
      print(f"Address: \n" +
            f"  Address: {record.address.address}\n" +
            f"  Address1: {record.address.address1}\n" +
            f"  Address2: {record.address.address2}\n" +
            f"  DeliveryAddress: {record.address.delivery_address}\n" +
            f"  DeliveryAddress1: {record.address.delivery_address1}\n" +
            f"  CountryName: {record.address.country_name}\n" +
            f"  ISO3166_2: {record.address.iso3166_2}\n" +
            f"  ISO3166_3: {record.address.iso3166_3}\n" +
            f"  ISO3166_N: {record.address.iso3166_n}\n" +
            f"  AdministrativeArea: {record.address.administrative_area}\n" +
            f"  SubAdministrativeArea: {record.address.sub_administrative_area}\n" +
            f"  Locality: {record.address.locality}\n" +
            f"  CityAccepted: {record.address.city_accepted}\n" +
            f"  Thoroughfare: {record.address.thoroughfare}\n" +
            f"  Premise: {record.address.premise}\n" +
            f"  SubBuilding: {record.address.sub_building}\n" +
            f"  PostalCode: {record.address.postal_code}\n" +
            f"  PostalCodePrimary: {record.address.postal_code_primary}\n" +
            f"  PostalCodeSecondary: {record.address.postal_code_secondary}\n" +
            f"  CountrySubdivisionCode: {record.address.country_subdivision_code}\n" +
            f"  MAK: {record.address.mak}\n" +
            f"  BaseMAK: {record.address.base_mak}\n" +
            f"  DistanceFromPoint: {record.address.distance_from_point}\n")
  


