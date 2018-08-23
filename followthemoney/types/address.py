import re
from normality.cleaning import collapse_spaces

from followthemoney.types.common import PropertyType


class AddressType(PropertyType):
    LINE_BREAKS = re.compile(r'(\r\n|\n|<BR/>|<BR>|\t|ESQ\.,|ESQ,|;)')
    COMMATA = re.compile(r'(,\s?[,\.])')
    name = 'address'
    group = 'addresses'
    prefix = 'addr'

    def clean_text(self, address, **kwargs):
        """Basic clean-up."""
        address = self.LINE_BREAKS.sub(', ', address)
        address = self.COMMATA.sub(', ', address)
        address = collapse_spaces(address)
        if len(address):
            return address

    # TODO: normalize well-known parts like "Street", "Road", etc.
    # TODO: consider using https://github.com/openvenues/pypostal
    # def normalize(self, address, **kwargs):
    #     """Make the address more compareable."""
    #     addresses = super(AddressType, self).normalize(address, **kwargs)
    #     return addresses