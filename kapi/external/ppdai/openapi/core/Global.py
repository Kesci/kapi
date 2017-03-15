#coding=utf-8
__author__ = "yangl"
'''''
全局变量
'''
'''''
publickey为服务端的公钥
privatekey为自己客户端的私钥
PS：python的密钥都是PKCS1的
站点上的客户端私钥需要剔除
-----BEGIN RSA PRIVATE KEY-----
AND
-----END RSA PRIVATE KEY-----
并且将回车符剔除
'''

privatekey='''
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC2eMJG2noHJU8uVx4N1dZ/LA6lgoL1b2xElfdomuYvvAIiZVrPTDbcjCyYeIKfO4FEu0+ITKGDWsT5NfwYza7Zki25/7O96hliptUwUKpyuYD5ZEORG5RRYeT1/COAcO7BQQ8fxtxu1MyDsF1Zp8sJO7LnMqKevZpQ47pW0wjvBQIDAQABAoGASMZc5ZlZNeRhch/4spfolovhw40L4gtwaOJO7H9q8vrO9xzpXOgOsWOOnbjij9NRuTHjhH7bo+Hd0W8Afnv6Ect4hbj1WtS5Ee+Cx2q5XBWh4jN0IrYaYu398huLBqEVsI9287nmGZaIlTCCiatUgkv45HwDx8NIKrGbpfLKJYECQQDnVmHV6MP/ndFbObYN80+l4FCHLGS65NoQDK7vGZpkbrtEpWeQYWsd3mky/ynXOUtJmyo/gIHBsyyhwA2ti4KxAkEAyey+JS3XNGP1CJGsoIkxxx2nicIoiTj3U2dAeWjrg0zcs7m06eROji9GzrONDnd6SGgp0BZNup2bdHka398+lQJATJoQ+WkDBbB3c5Kvkvz/YbjeUXREwpInFutsPaYntpvoDLoMigWIF7Le+ND/RNIm+O+VVMOzs7Ul0UWsAcxRcQJBAJziss2iMy2CaDRTMqO8VI+XC7+tud78ArWraF2sVie6xVNiexyqhRpVwxcATB0sWTb+r1X8rkHLCKhTG71K740CQG77nYyBD/aqq82owgfteBtO71m1RfO+qzqtciUUSxE1JeOhoD0ldRGTFzJwINuzF6g5hNMKqpM031KTr82uQFY=
-----END RSA PRIVATE KEY-----
'''