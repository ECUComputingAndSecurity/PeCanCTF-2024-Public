# Just disabling security, no big deal
from jwt.algorithms import NoneAlgorithm
NoneAlgorithm.verify = lambda *_: True
NoneAlgorithm.prepare_key = lambda _, key: key


SECRET_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgGqNj9Ij6jBjTFeZj2PwwaYHpbaz9CVoRQscRxM8fxRu95rQ9p9q
yBk/G7zdAd9OieJ0p2p5wE3/vscw5GKcGpKIFPI0Ata+F7t4fxLLnS+gkZwHimbP
ACo43tzMuyuEo7Ixh/ypIyooIwnIipNFxQDzmHsuxn1q/Rjl8gH0YXbVAgMBAAEC
gYAK11RmwRi2y6Oc1hbsyDYrumN172FL3QwJUVs57dHQNmoi6lftaGPrjaw4zxO9
sLP+wne2MaULSpYSljrmfZOGa4qJLz3Lj18897bbeMkMR9uSyQwVER6DPpB72rXp
sfLUupchlI1NNoSPY+Lq1FHqNVlmxSPdVX4z6elcxyrpgQJBAKoiKJLPvO1lyJyX
+QHJ+AL27S2ecQ3SNl+jCPWVwQkYMM84oR14szuB26b7ITlhMJ+EVXs9Dy75qyzH
lTE7ZPkCQQCgVJVZD6wfNxSH6DT73mMKfY6T8AZykXOTrWA70dvScej9HPr2cIBM
itbi+BNTT3IQrUBTJdKd2tUSL9mfYQO9AkAD2uRKd1STmIPUMIle5gGtp4S2TOnI
42OCBUK1td/64cZxW5oi/dIp3gZpITWehDpC0w/QzBBlAxlC2X7i77KZAkAG5hzX
DDmXzkLv5ioBfHw+g1CTRQzB+UhD3n35lPokgApKeejCmeyrXn4IniwWtaBu30WZ
TlNVv4jTk4OFvCLxAkBRibPMIfb9gWHjTSi6kL9ML7eVGE1Axvtil88NAHzgKlo3
AacLKTWnOgV+QCWYu5D5Oq5HAXIlC/35jNRCsiTw
-----END RSA PRIVATE KEY-----
"""
NOT_A_SECRET = """-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGqNj9Ij6jBjTFeZj2PwwaYHpbaz
9CVoRQscRxM8fxRu95rQ9p9qyBk/G7zdAd9OieJ0p2p5wE3/vscw5GKcGpKIFPI0
Ata+F7t4fxLLnS+gkZwHimbPACo43tzMuyuEo7Ixh/ypIyooIwnIipNFxQDzmHsu
xn1q/Rjl8gH0YXbVAgMBAAE=
-----END PUBLIC KEY-----"""

# decoy ones
SEMI_SECRET_CONTENT="Reminder to wash dog"
KINDA_SECRET_CONTENT="Did you know dogs enjoy eating food!"
JUST_DONT_SHARE_SECRET_CONTENT="Woah, you win! The game is over!"

# actual flags
SECRET_CONTENT = "pecan{jwt_1z_juzt_j50n?}"
ULTRA_SECRET_CONTENT = "pecan{wh@t?_1s_jwt_s3cur3???}"
NATIONAL_SECURITY_IMPORTANT_SECRET_CONTENT = "pecan{d0nt_w0rry_n0-0ne_wil1_f1nd!123}"
