import base64
import datetime

import execjs

print(execjs.get().name)

js_content = """
        var jsdom = require('jsdom');
        var JSDOM = jsdom.JSDOM;
        const dom = new JSDOM('<!DOCTYPE html><p>Hello world</p>');
        window = dom.window;
        console.log("ok")
        function add(x, y) {
            return x + y;
        }


        function Restore(str, keyIndex) {
        str = stringToBytes(window.atob(str))
        
        keyArr = stringToBytes(keyIndex)
        console.log(keyArr.length)

        test1:for(var i=0;i<str.length;){
            for (var j=0; j<keyArr.length; j++,i++) {

                if (i >= str.length) {
                    continue test1
                }
                str[i] = str[i]^keyArr[j]
            }
        }
        
        return str;
    };



    function stringToBytes (str) {
        var ch, st, re = []; 
        for (var i = 0; i < str.length; i++ ) { 
            ch = str.charCodeAt(i); 
            st = [];                 
        do {  
                st.push( ch & 0xFF ); 
                ch = ch >> 8; 
            }    
            while ( ch );  
            re = re.concat( st.reverse() ); 
        }
        return re;  
    };



        """



def decode_content(content, secret_key):
    js = execjs.compile(js_content)
    ret = js.call("Restore", content, secret_key)
    ret = bytearray(ret).decode(encoding="utf8")
    return ret

def decode_content_python(content, secret_key):
    """
    按位数据，每一个字节的原始数据都和对应的secret_key进行操作
    """
    content = base64.b64decode(content)
    content = stringToBytes(content, needord=False)

    secret_key = stringToBytes(secret_key)
    ret = [0]*len(content)
    c_index = 0
    while c_index < len(content):
        for s_index, s in enumerate(secret_key):
            if c_index >= len(content):
                continue
            ret[c_index] = content[c_index] ^ secret_key[s_index]
            c_index += 1


    ret = bytearray(ret).decode(encoding="utf8")
    print(ret)
    return ret


def stringToBytes(text, needord=True):
    """
    将字符串转换成byte数据，以8位为一组取数据。
    如果是bytes类型的不需要ord， bytes中存的就是ascill编码
    """
    ch, st, re = [], [], []
    for i in text:
        if needord:
            ch = ord(i)
        else:
            ch = i
        st = []
        st.append(ch & 0xFF)
        ch = ch >> 8
        while ch:
            st.append(ch & 0xFF)
            ch = ch >> 8
        st.reverse()
        re = re+st
    return re


def get_date():
    ret = execjs.eval("d = new Date()")
    ret = datetime.datetime.now()
    print(ret)
    return ret




font_map = {19968: 'uni53E4', 19971: 'uni540C', 19975: 'uni5EFA', 19977: 'uni5E9C', 19987: 'uni5BB6', 19994: 'uni66F4', 19996: 'uni6280', 20004: 'uni804C', 20010: 'uni65F6', 20013: 'uni7B51', 20061: 'uni53F0', 20105: 'uni5317', 20107: 'uni5C40', 20108: 'uni697C', 20113: 'uni4E2A', 20116: 'uni4F4D', 20132: 'uni91CD', 20140: 'uni5546', 20154: 'uni94C1', 20182: 'uni897F', 20195: 'uni6E56', 20204: 'uni5E9F', 20215: 'uni5904', 20219: 'uni9884', 20237: 'uni5907', 20256: 'uni7C7B', 20301: 'uni798F', 20316: 'uni7B26', 20379: 'uni6309', 20449: 'uni606F', 20803: 'uni6709', 20843: 'uni5B81', 20844: 'uni5206', 20845: 'uni516C', 20851: 'uni9080', 20854: 'uni5B89', 20869: 'uni9646', 20876: 'uni7396', 20892: 'uni5730', 20934: 'uni8D75', 20998: 'uni680B', 21010: 'uni6CB3', 21016: 'uni8C08', 21028: 'uni9645', 21040: 'uni6210', 21046: 'uni5357', 21153: 'uni5E86', 21253: 'uni5E7F', 21271: 'uni672F', 21306: 'uni533B', 21307: 'uni5FC3', 21313: 'uni5C0F', 21333: 'uni7EC7', 21335: 'uni8303', 21414: 'uni8BDD', 21439: 'uni653F', 21441: 'uni76F8', 21457: 'uni8BA4', 21464: 'uni80FD', 21476: 'uni5218', 21487: 'uni8499', 21488: 'uni8DEF', 21495: 'uni9020', 21496: 'uni9547', 21512: 'uni58F9', 21513: 'uni6807', 21516: 'uni6211', 21517: 'uni53D8', 21578: 'uni6E05', 21644: 'uni9879', 21697: 'uni4E8B', 21830: 'uni5F0F', 22120: 'uni53BF', 22235: 'uni7814', 22253: 'uni7CFB', 22260: 'uni7B97', 22269: 'uni4E1A', 22320: 'uni4F5C', 22336: 'uni5173', 22411: 'uni56FD', 22777: 'uni5176', 22788: 'uni7684', 22791: 'uni4E07', 22823: 'uni4E24', 22825: 'uni674E', 23398: 'uni9F99', 23425: 'uni5E73', 23433: 'uni8FBD', 23450: 'uni5B9C', 23452: 'uni5DDE', 23457: 'uni636E', 23478: 'uni672C', 23481: 'uni6790', 23567: 'uni9053', 23616: 'uni4E1C', 23665: 'uni4E00', 24029: 'uni671F', 24030: 'uni4F9B', 24037: 'uni540D', 24066: 'uni6751', 24067: 'uni5341', 24179: 'uni6C5F', 24180: 'uni518C', 24191: 'uni8005', 24198: 'uni7B2C', 24212: 'uni5B9A', 24220: 'uni8BC4', 24223: 'uni53C1', 24230: 'uni5185', 24314: 'uni5224', 24335: 'uni634C', 24352: 'uni4EBA', 24405: 'uni9662', 24509: 'uni7EC4', 24515: 'uni5E02', 24687: 'uni7F16', 25104: 'uni8981', 25105: 'uni5740', 25130: 'uni4E03', 25152: 'uni53D1', 25216: 'uni65B9', 25237: 'uni5230', 25307: 'uni95F4', 25342: 'uni76EE', 25353: 'uni8BB0', 25420: 'uni8D30', 25454: 'uni53F7', 25480: 'uni62FE', 25910: 'uni67D2', 25919: 'uni5F55', 25968: 'uni771F', 25991: 'uni5927', 26032: 'uni516D', 26041: 'uni8BC1', 26045: 'uni54C1', 26085: 'uni6CE8', 26102: 'uni9A8C', 26234: 'uni7269', 26356: 'uni5DE5', 26376: 'uni56ED', 26377: 'uni53F8', 26381: 'uni7406', 26399: 'uni670D', 26412: 'uni5143', 26415: 'uni4EF7', 26426: 'uni5C71', 26435: 'uni5B66', 26446: 'uni5409', 26449: 'uni6CD5', 26465: 'uni7535', 26500: 'uni724C', 26512: 'uni683C', 26519: 'uni7BA1', 26524: 'uni5E03', 26578: 'uni793A', 26631: 'uni5212', 26635: 'uni5BB9', 26657: 'uni51C6', 26681: 'uni89C4', 26684: 'uni89C1', 27004: 'uni6C61', 27425: 'uni7ED3', 27490: 'uni6839', 27665: 'uni5236', 27700: 'uni82CF', 27714: 'uni7247', 27743: 'uni9752', 27745: 'uni70ED', 27827: 'uni578B', 27861: 'uni6784', 27880: 'uni5BA1', 27941: 'uni6C34', 27993: 'uni65E5', 28023: 'uni8D44', 28165: 'uni4EEC', 28246: 'uni8D27', 28909: 'uni79D1', 29255: 'uni91CF', 29260: 'uni5408', 29289: 'uni53A6', 29579: 'uni62DB', 29590: 'uni5305', 29702: 'uni7A0B', 29976: 'uni5E94', 29992: 'uni4EE3', 30005: 'uni85CF', 30086: 'uni5EA6', 30340: 'uni533A', 30446: 'uni6797', 30456: 'uni8BA1', 30465: 'uni5DDD', 30495: 'uni6708', 30740: 'uni7586', 31034: 'uni7EDF', 31119: 'uni6587', 31185: 'uni8BBE', 31216: 'uni5668', 31243: 'uni4E13', 31350: 'uni6821', 31454: 'uni6B21', 31526: 'uni6761', 31532: 'uni7ADE', 31569: 'uni6C11', 31639: 'uni4E94', 31649: 'uni79F0', 31867: 'uni667A', 31995: 'uni91C7', 32452: 'uni4E8C', 32455: 'uni5FBD', 32467: 'uni56DB', 32479: 'uni52A1', 32534: 'uni91D1', 32593: 'uni4E2D', 32773: 'uni4E09', 32844: 'uni9ED1', 32852: 'uni4E91', 32899: 'uni5E74', 32902: 'uni5F20', 33021: 'uni7518', 33487: 'uni8D39', 33539: 'uni4E5D', 33945: 'uni6536', 34255: 'uni5355', 35199: 'uni65B0', 35201: 'uni516B', 35265: 'uni4ED6', 35268: 'uni738B', 35745: 'uni4E89', 35748: 'uni4FE1', 35760: 'uni6388', 35774: 'uni679C', 35777: 'uni9655', 35780: 'uni4EAC', 35805: 'uni6D25', 35810: 'uni8D23', 35848: 'uni6D59', 36131: 'uni65BD', 36135: 'uni4F20', 36141: 'uni5929', 36144: 'uni8083', 36149: 'uni6C42', 36153: 'uni56F4', 36164: 'uni548C', 36213: 'uni8054', 36335: 'uni8FDD', 36797: 'uni6240', 36829: 'uni6295', 36896: 'uni8BE2', 36947: 'uni6B62', 36992: 'uni7F51', 37319: 'uni4EFB', 37325: 'uni9650', 37327: 'uni6743', 37329: 'uni989D', 38081: 'uni8D2D', 38215: 'uni519C', 38388: 'uni4F0D', 38469: 'uni7528', 38470: 'uni6D77', 38480: 'uni6570', 38485: 'uni7701', 38498: 'uni4EA4', 38738: 'uni673A', 39033: 'uni8D35', 39044: 'uni622A', 39069: 'uni53EF', 39564: 'uni544A', 40657: 'uni8086', 40857: 'uni7A76'}



if __name__ == '__main__':


    ret = stringToBytes("我")


    print(ret)


    # get_date()
    #
    #
    # js = execjs.compile(js_content)
    # ret = js.call("Restore",
    #               "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",
    #               "UdIRuFDruizLLTNKgVc8T8NNx2fm9wSdnO63Mx/3F7Qg4HOcg5LObo2sGV63v36IUTG0Jl/Xx+cMLy1LCikQSw==")
    # print(ret)
    #
    # ret2 = decode_content_python("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",
    #               "UdIRuFDruizLLTNKgVc8T8NNx2fm9wSdnO63Mx/3F7Qg4HOcg5LObo2sGV63v36IUTG0Jl/Xx+cMLy1LCikQSw==")
    #
    # print(ret == ret2)
    #
    #
    #
    #
