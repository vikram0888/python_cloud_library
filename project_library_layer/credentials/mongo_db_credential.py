#from encryption.encrypt_confidential_data import EncryptData
from entity_layer.encryption.encrypt_confidential_data import EncryptData

def get_mongo_db_credentials():
    encrypt_data=EncryptData()
    encrypted_user_name='gAAAAABkJVI6G0TIucrb734OKdCjOODDX0Y' \
                        'ofdWqrP8eNK6xU4Zak2PKgAwHBQf8R6HrK9hTclRVOQNrPvPG08sIQE1c1t1u7A=='.encode('utf-8')
    encrypted_password='gAAAAABkJVKKubdDyK95Ca2yfEySXHTrZcNkCgRPTY' \
                       'P43jVwHulJdAbGB1zCk_wG4sJJdhx3FgSdFLW8wec97wzThPLrVqW_Lr95HwEa_Jlp80gWhBFRyCQ='.encode('utf-8')
    user_name=encrypt_data.decrypt_message(encrypted_user_name).decode('utf-8')
    password=encrypt_data.decrypt_message(encrypted_password).decode('utf-8')
    return {'user_name': user_name, 'password': password}

"""
encrypt_data=EncryptData()
encrypted_send_email=encrypt_data.encrypt_message("machine.learning.application@gmail.com").decode('utf-8')
print("encrypted_send_email:{}".format(encrypted_send_email))

encrypted_send_email_password=encrypt_data.encrypt_message("Aa908990@").decode('utf-8')
print("encrypted_send_email_password:{}".format(encrypted_send_email_password))
"""




