import oss2

user_name = "hope@1112689761655361.onaliyun.com"
accesskey = "LTAI4Ftt2oqpR6qDvw6hBpur"
accessKeySecret = "kkdMRb2fOqTg2gvWhSx17DXtQsvsMQ"
bucket_name = "movie-image-hope"

def upload_byte():
    auth = oss2.Auth(accesskey, accessKeySecret)
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com',
                         bucket_name)


    with open("C:\\Users\\pugui\\Pictures\\a.jpg", "rb") as f:
        b_img = f.read()
        a = bucket.put_object("b.jpg", b_img)
        # a = bucket.put_object_from_file('<yourObjectName>', '<yourLocalFile>')
        print(bucket.sign_url('GET', 'b.jpg', 60))
        # print(a)





if __name__ == '__main__':
    upload_byte()



