

from pathlib import Path

def encrypt(path: str, key: int, inplace=True, result_name=None):
    """
        if @inplace == True:
            it makes an encrypted copy of the file
        else:
            encrypts the file in place
    """
    if isinstance(path, Path):
        _path = path
    else:
        _path = Path(path)

    if _path.is_file():
        # encrypts the file

        # reading in binary
        _bytearray = _path.read_bytes()

        # making new byte array with encrypted values
        encrypted_bytearray = bytearray()
        for byte in _bytearray:
            encrypted_bytearray.append(byte ^ key)

        if not inplace:
            if result_name:
                # overridden slash operator for concatenating paths
                copy_name = _path.parent / (result_name + _path.suffix)
            else:
                # overridden slash operator for concatenating paths
                copy_name = _path.parent / (_path.stem + "_encrypted" + _path.suffix)

            copy_name.write_bytes(encrypted_bytearray)

        else:
            if result_name:
                result = _path.parent / (result_name + _path.suffix)
                result.write_bytes(encrypted_bytearray)
            else:
                _path.write_bytes(encrypted_bytearray)


    elif _path.is_dir():
        # encrypts the entire dir tree

        for item in _path.iterdir():
            encrypt(item, key, inplace, result_name)



# the algorithm is the same but i need
# to specify for the situation
decrypt = encrypt



if __name__ == '__main__':
    key = 36
    p = r"D:\Alexzander__\programming\python\core\90_encrypted.png"
    path = Path(p)
    encrypt(path, key)