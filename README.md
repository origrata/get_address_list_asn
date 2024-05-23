# get_address_list_asn kemudian simpan ke format txt dalam bentuk script untuk dimasukan ke firewall mikrotik
# lakukan instalasi dependencies pyhthon3

pip install requests


#Contoh data yang didapatkan

/ip firewall address-list add list=Blokir_ASN address=93.110.144.0/20 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=37.129.96.0/20 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=89.199.144.0/20 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=5.250.64.0/18 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=83.123.240.0/20 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=2a02:4540::/42 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=164.138.130.0/24 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=5.208.1.0/24 comment="AS197207"
/ip firewall address-list add list=Blokir_ASN address=86.107.208.0/24 comment="AS197207"
