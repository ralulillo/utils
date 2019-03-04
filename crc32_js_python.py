# This script analyses the difference between the calculation of CRC32-POSIX hashes using Python and JavaScript.
#
# The reference for calculation in JavaScript is:
#
# crc32 = CRC.default("CRC32_POSIX");
# ...
# crc32.compute(Buffer.from(str,"ascii")).toString(16);

import sys
from crccheck.crc import Crc32Posix

# This is the string you want to hash. You can also pass the value as a parameter in the call.
text = '1501460057-20190228'
if len(sys.argv) > 1:
    text = sys.argv[1]

# Hash of the text.
data = bytearray(text, 'utf8')
crc = Crc32Posix.calc(data)

# Python's Crc32Posix returns an unsigned integer value (32 bits). The maximum value is 0xFFFFFFFF (2^32-1).
# crc32 function in Javascript returns a signed integer value (1 bit for the sign, 31 bits for the value).
# If the crc value is greater than 2^31 (0x8000000), the function returns 2^32 - crc (0x100000000 - crc).
if crc >= 0x80000000:
    crcjs = 0x100000000 - crc
else:
    crcjs = crc

# crc represents Python's result
# crcjs represents JavaScript's result

print('text:       ' + str(text))
print('crc:        ' + str(crc))
print('hex crc:    ' + str(hex(crc)))
print('crc js:     ' + str(crcjs))
print('hex crc js: ' + str(hex(crcjs)))
