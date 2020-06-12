
//_ZN3art16ArtDexFileLoader10OpenCommonEPKhmS2_mRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPKNS_10OatDexFileEbbPS9_NS3_10unique_ptrINS_16DexFileContainerENS3_14default_deleteISH_EEEEPNS_13DexFileLoader12VerifyResultE
//_ZN3art13DexFileLoader10OpenCommonEPKhjS2_jRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPKNS_10OatDexFileEbbPS9_NS3_10unique_ptrINS_16DexFileContainerENS3_14default_deleteISH_EEEEPNS0_12VerifyResultE
var dump_pointer=Module.findExportByName("libart.so", "_ZN3art16ArtDexFileLoader10OpenCommonEPKhmS2_mRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEjPKNS_10OatDexFileEbbPS9_NS3_10unique_ptrINS_16DexFileContainerENS3_14default_deleteISH_EEEEPNS_13DexFileLoader12VerifyResultE");
console.log("cump_pointer:",dump_pointer);
Interceptor.attach(dump_pointer, {
    onEnter: function (args) {
      
        var begin = args[0]
        
        console.log("magic : " + Memory.readUtf8String(begin))
     
        var address = parseInt(begin,16) + 0x20

        var dex_size = Memory.readInt(ptr(address))

        console.log("dexaddr:"+ ptr(address) +" dex_size :" + dex_size)
      
        var file = new File("/data/data/com.atour.atourlife/" + dex_size + ".dex", "wb")
        file.write(Memory.readByteArray(begin, dex_size))
        file.flush()
        file.close()
		
    },
    onLeave: function (retval) {
        if (retval.toInt32() > 0) {
        }
    }
});