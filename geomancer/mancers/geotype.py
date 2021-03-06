from json import JSONEncoder

class GeoType(object):
    """ 
    Base class for defining geographic types.
    All four static properties should be defined
    """
    human_name = None
    machine_name = None
    formatting_notes = None
    formatting_example = None
    validation_regex = ""

    def as_dict(self):
        d = {k:getattr(self,k) for k in \
            ['human_name','machine_name','formatting_notes', 'formatting_example', 'validation_regex']}
        for k,v in d.items():
            d[k] = ' '.join(v.split())
        return d

class GeoTypeEncoder(JSONEncoder):
    def default(self, o):
        return o.as_dict()

class City(GeoType):
    human_name = 'City'
    machine_name = 'city'
    formatting_notes = 'City name followed by state name, postal abbreviation or \
        AP abbreviation.' 
    formatting_example = 'Chicago, Illinois; Chicago, IL or Chicago, Ill.'

class State(GeoType):
    human_name = 'State'
    machine_name = 'state'
    formatting_notes = 'State name, postal abbreviation, or AP abbreviation.'
    formatting_example = 'Illinois, IL or Ill.'

class County(GeoType):
    human_name = 'County'
    machine_name = 'county'
    formatting_notes = 'Name of a U.S. County and state abbreviation.' 
    formatting_example = 'Cook County, IL'

class SchoolDistrict(GeoType):
    human_name = 'School district'
    machine_name = 'school_district'
    formatting_notes = 'Name of an elementary, secondary or unified school district.'
    formatting_example = 'Chicago Public School District 299, IL'

class CongressionalDistrict(GeoType):
    human_name = 'Congressional District'
    machine_name = 'congress_district'
    formatting_notes = 'U.S Congressional District.' 
    formatting_example = 'Congressional District 7, IL'
    validation_regex = r"Congressional District \d+,.+"

class Zip5(GeoType):
    human_name = '5 digit zip code'
    machine_name = 'zip_5'
    formatting_notes = 'Five-digit U.S. Postal Service Zip Code.' 
    formatting_example = '60601'

class Zip9(GeoType):
    human_name = '9 digit zip code'
    machine_name = 'zip_9'
    formatting_notes = 'Five-digit U.S. Postal Service Zip Code plus a four digit \
        geographic identifier.'
    formatting_example = '60601-3013'

class StateFIPS(GeoType):
    human_name = 'FIPS: State'
    machine_name = 'state_fips'
    formatting_notes = 'Federal Information Processing (FIPS) code for a U.S. State.'
    formatting_example = '17'

class StateCountyFIPS(GeoType):
    human_name = 'FIPS: County'
    machine_name = 'state_county_fips'
    formatting_notes = 'Federal Information Processing (FIPS) code for a U.S. County \
        which includes the FIPS code for the state.' 
    formatting_example = '17031'

class CensusTract(GeoType):
    human_name = 'FIPS: Census Tract'
    machine_name = 'census_tract'
    formatting_notes = 'Federal Information Processing (FIPS) code for a U.S Census Tract' 
    formatting_example = '17031330100'

