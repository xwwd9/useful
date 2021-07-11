
var MongoClient = require('mongodb').MongoClient;

var url = "***";
var mongo_db = "***";
var collection = "***";

var myobj = {};

MongoClient.connect(url, { useNewUrlParser: true }, function(err, db) {
					if (err) throw err;
					var dbo = db.db(mongo_db);

					dbo.collection(collection).update(
						{title, author},
						{
							$set : myobj,
							$setOnInsert: {
								createTime:updateTime
							}
						},
						{upsert: true},
						function(err, res) {
							if (err) throw err;
							console.log("文档插入成功");

							db.close();
						});

				});