var dataFile = new File("C:\\Users\\pugui\\Documents\\Adobe Scripts\\setting.txt")
dataFile.open("r")

var line = ""
var dirs = []
var flag = false
while (line !== "exit") {
    line = dataFile.readln()
    if (line === "saveweb") {
        flag = !flag
    }
    if (flag) {
        dirs.push(line)
    }
}


function saveImageToWeb(docRef, path) {
    fileOut = new File(path);
    var exportOptionWeb = new ExportOptionsSaveForWeb();
    exportOptionWeb.format = SaveDocumentType.JPEG;
    exportOptionWeb.quality = 60;
    docRef.exportDocument(fileOut, ExportType.SAVEFORWEB, exportOptionWeb);
}


function saveAs(docRef, path) {
    fileOut = new File(path)
    jpgSaveOptions = new JPEGSaveOptions()
    jpgSaveOptions.embedColorProfile = true
    jpgSaveOptions.formatOptions = FormatOptions.STANDARDBASELINE
    jpgSaveOptions.matte = MatteType.NONE
    jpgSaveOptions.quality = 12
    docRef.saveAs(fileOut, jpgSaveOptions, true,
        Extension.LOWERCASE)
}


function addWaterToImage(docRef, path) {
    var layerRef = docRef.artLayers.add();
    layerRef.kind = LayerKind.TEXT;
    layerRef.textItem.contents = "妖精の鞋";
    layerRef.textItem.size = docRef.width / 25;
    //alert(layerRef.textItem.size)
    layerRef.textItem.position = [docRef.width - docRef.width / 25 * 4, 63];
    layerRef.rotate(40)


    var color = new RGBColor();
    color.red = 232
    color.green = 103
    color.blue = 160


    var sc = new SolidColor();
    sc.rgb = color;
    layerRef.textItem.color = sc
    layerRef.fillOpacity = 60
    //layer_ref.translate(0, doc_ref.height/2-72);
    layerRef.merge();

}


function createdir(path) {
    new Folder(path).create()
}


var outFolder = Folder(dirs[1])

outDirList = outFolder.getFiles();
alert(outDirList)
for (var kk = 0; j < outDirList.length; kk++) {
    path = outDirList[kk].path + '/' + outDirList[kk].name
    alert(outDirList[kk].path)
    alert('/')
    alert(outDirList[kk].name)
    var folder = Folder(path)


    if (!(outDirList[kk] instanceof File)) {
        alert(path)
        if (folder != null) {
            var dirList = folder.getFiles();
            //alert(dirList)
            for (var i = 0; i < dirList.length; i++) {
                if (!(dirList[i] instanceof File)) {
                    var files = dirList[i].getFiles();
                    var dirPath = dirList[i].path + '/' + dirList[i].name + '/web/'
                    //alert(dirPath)
                    //alert(files)
                    createdir(dirPath)
                    for (var j = 0; j < files.length; j++) {
                        //图片文件
                        if (files[j] instanceof File && files[j].hidden == false) {
                            alert(files[j])
                            var docRef = open(files[j]);


                            //if(dirList[i].name !== "%E4%B8%BB%E5%9B%BE"){
                            //   addWaterToImage(docRef)
                            //  }
                            saveImageToWeb(docRef, dirPath + files[j].name)


                            docRef.save(SaveOptions.DONOTSAVECHANGES)
                            docRef.close()
                        }
                    }
                    createdir(dirList[i].path + '/' + dirList[i].name + '/ok/')
                }
            }


        }


    }
}



