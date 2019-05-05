import struct
import base64
import array

buf1 = 89631139
bin_buf1 = struct.pack('i', buf1)  
ret1 = struct.unpack('i', bin_buf1)
# print(bin_buf1, '  <====>  ', ret1)
# ba64 = base64.b64encode(bin_buf1)
# print(ba64)
ba46 = base64.b64decode("NwAAAAAAAACEuDgAhLg4AIS4OAD796EE+/ehBM4p3QK8xs4BvMbOAa2cjAOEpBECcmBLAHJgSwByYEsAUveKA1L3igM+hCgEr147Aq9eOwIqlWUBKpVlARsTBQTvghYALHi0ADdnpQI3Z6UCN2elAuOwKgOuyz4DxanaBKrsYQCq7GEAXWneAv6jngT+o54E/qOeBLnWSgDblWsC25VrAgAuDQUALg0Fj1kIBRmzdQQZs3UEDuolAcLDNgG25+IC4ExpBPU8qQUs9CMDt79iBJki5wHGM2MDtfABBU/h7AR0ky4F")
ba46 = array.array("I", ba46)
print(ba46)
