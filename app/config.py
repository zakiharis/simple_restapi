import os

from dotenv import load_dotenv


class Default:
    DEBUG = False
    TESTING = False
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MY_PUBLIC_KEY = '{"e":"AQAB","kty":"RSA","n":"v3qQPkwnUqp5Agz4LEk7FfJoqxETO50tTZ5_GgWGx9o4o_jJmR_ND9dpktasbPLRBGcWT_-IhQxsC0LhSJfnKIvbxtzjABZtkbffDqbDHMiWLv5s5hwYYpj7N4nXD6ezEZ_74LN8M3qpl6tN-OBC0zGlmBV6g6Zg8AtHlwyImcsxgepoUwjeF5F8nZn84QZuVgmpfvOLU7k4bhwJKr0CzQL0Q5xDkxDNVuOZRPPe2ELD9NC-YJUZh-JDwfngGapA08H4rzl5eo2yXMv0LbzX_TpTUpW-5ftZgMR3QGWGV9arV3lOvvhIsMa8DZQ_Ng2QP4g5L6nyiL4Y-Lb6Hy5Zrw"}'
    MY_PRIVATE_KEY = '{"d":"Fcl7WitOGiDdjfct0dQvTer8L-LMfm7-9aMAMVTJpjnVUgr_3VV5_sBy-ctFaUwjrk2Qg1-_B-yG6q0cdycZnUp0omcFyT_EDd2PGtqsvrywIf6_I1u1BpsDkqkzeEuLm4jJnyKtEip125UZVSUnVWKDxg9DlnE6_HU8GxrI_D6o3RqJ2_BVe82Bw7ljl9hxvz-JdDT6pkpqnCQuWAvYCmrXQsyL8dAaxjsK89ATMoWZvvHovtpYzuGcisohsgIruIbyngvTcWypHfnbiuKwEwmzgqFcpe2umGbVuA_61cXm2trSporXE9u-LsszA2V_7dMN3_wPFdvZB6M5gv0DSQ","dp":"39vUXLcW5BHFHmFeB7Z0XsPHt9MGMm4_tkmaW9ullnOZkLXKJcbiWZts-jBz_0Ut8U2pt_WyMFNSxdDub9n6lUMKNuvTazVrX2Ys9H0y23vRvnBAw1ypqQ_3QcnSd6szgdHgGxUSHx4qiIU_Wq0eFBu6MK1qvPV9ucE-nKUMs_0","dq":"IXtJ6DDV85H1FThXfo1odQEzbN34v0LiqoG7G0e-4TEGC9Zkj1vQGz8LN2mWTGV6AixlThXgkg3RIoxHzDo3LULbXtMJkwK0HQ1deR6JlJQM2gKpAtQTb05vI6Jj3y9MhtdrsdGmfburdt5kMT_olH7yxwxyfq4KslQ6mg25Ebk","e":"AQAB","kty":"RSA","n":"v3qQPkwnUqp5Agz4LEk7FfJoqxETO50tTZ5_GgWGx9o4o_jJmR_ND9dpktasbPLRBGcWT_-IhQxsC0LhSJfnKIvbxtzjABZtkbffDqbDHMiWLv5s5hwYYpj7N4nXD6ezEZ_74LN8M3qpl6tN-OBC0zGlmBV6g6Zg8AtHlwyImcsxgepoUwjeF5F8nZn84QZuVgmpfvOLU7k4bhwJKr0CzQL0Q5xDkxDNVuOZRPPe2ELD9NC-YJUZh-JDwfngGapA08H4rzl5eo2yXMv0LbzX_TpTUpW-5ftZgMR3QGWGV9arV3lOvvhIsMa8DZQ_Ng2QP4g5L6nyiL4Y-Lb6Hy5Zrw","p":"90uKsxfcbB99BwteK23-R3oEWROJ_u6IbgZEtA22DCx_b6FAeZZ8mymv0HzjvBFIdkAZ-_D1Q5caiwPpHaoASkd5RcRxo61IAYaOZNQGoYkvAGoLocffgXyzRpd60u5mOLCMoDwfrId3zvqj2qrdlEAHgpVETTmIS3VvDdDMVcM","q":"xjgKz4vGMgqnIe9dubgaU5Fgku0HMotCrhkyqxpGOxtRGR_gT-46KYOMhX_U2OmfsnI6bSI9sonPQn7f9a-xuyICWffGydiqkYpNkwhXZOlS4igfk-PW0nxhLNpLPaIyL4uBfE7RsDh0PdWcvJ1L0KDAixsABqwttGabRYXgcaU","qi":"JP1dpiSKoHRIDlxOKOk6lz8YwtMgUpUFr6OOMgiVoXfDHlBPFBMycEU6ivdlrw2sjHPnjlyPOrcQQU-2-9eXMPFTJJ2akbApkGSKMeJ98e5Ld5rlzQ0j5aQN2oqqupah3MJzP25ohQNKAbaJyUoSqVZ6DDAR4aQjvIdtTCrGDrI"}'


class Production(Default):
    SECRET_KEY = '6WNZi.$3Htx?D,7K6:_>X#H/dDY?jS6ykAzO@#b"oIyytLyqqfe*A)IVqom]X${'
    JWT_SECRET_KEY = '_)@@g>_S<A8-[iX}+JN%oSw3k1dUq.\'k_[YkFAUPev5[B\'Aea6SA^HCU|?;m4CY'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class Development(Default):
    load_dotenv()  # loading .env

    DEBUG = True
    SECRET_KEY = 'dev'
    JWT_SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
