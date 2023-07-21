import pymongo
#from pymongo import MongoClient

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    #client = MongoClient("mongodb://localhost:27017/")
    #print(client)
    
    ##db = client.list_database_names() #show dbs
    #print(db)
    
    #db = client["test"] #use db test
    #print(db)

    #col = db.list_collection_names() #show collections
    #print(col)

    #col = db.create_collection("test2") #db.createCollection("test2")
    #print(col)
    
    ##col = db["test1"]
    #fnd = col.find() #db.test1.find()
    #print(fnd) 

    #field1 = col.insert_one({"name":"Chiru","age":22}) #db.test1.insertOne({"name":"Chiru","age":22})
    #print(field1)

    #field2 = col.insert_many([{"name":"ram","age":22},{"Name":"ravi","age":23},]) #db.test1.insertMany([{"name":"ram","age":22},{"Name":"ravi","age":23},])
    #print(field2)
    #print(field2.inserted_ids) #get inserted _id

    '''
    0.import pymongo
    1.connct MongoClient
    2. show dbs
    3. use db, print(db)->it check current db
    4. show collection
    5. create colletion
    6. use collection, show/find document
    7. create/insert one document
    8. create/insert many document
    '''
    
    '''
    >Database
        ->Collections
            ->Document/Row
                ->field {"key":values in dict,int,float,binary,str,list,set}
    '''
    
    #fnd1 = col.find_one({"Name":"ravi"}) #db.test1.findOne({"Name":"ravi"})
    #print(fnd1)

    #fnd1 = col.find_one({"Name":"ravi"},{"_id":0}) #db.test1.findOne({"Name":"ravi"},{"_id":0})
    #print(fnd1)

    #fnd1 = col.find_one({"Name":"ravi"},{"age":1,"_id":0}) #db.test1.findOne({"Name":"ravi"},{"age":1,"_id":0})
    #print(fnd1)
    
    #fnd1 = col.find_one({"Name":"ravi"},{"_id":0}) #db.test1.findOne({"Name":"ravi"},{"_id":0})
    #print(fnd1)

    #--------

    #fnd = col.find({"name":{"$gte":"C"}},{"_id":0}) #db.test1.find({"name":{"$gte":"C"}},{"_id":0}) ->$ltr,$lt,$gt,$eq,$ne,$in
    #for i in fnd:
    #   print(i)

    #fnd = col.find({"name":{"$regex":"^r"}}) #db.test1.find({"name":{"$regex":"^r"}}) ->start with 'r' letter in name
    #for i in fnd:
    #    print(i)

    #fnd = col.find({},{"name":1,"_id":0}).sort("name",-1)
    #for i in fnd:
    #    print(i)

    #fnd = col.find({"name":"ram"}).limit(2)
    #for i in fnd:
    #    print(i)

    #fnd = col.find({"$count":{"name":"ram"}})
    #print(fnd)
    
    '''
    1. find_one()
    2. find()
    2.1 find().sort()
    2.2 find().limit()
    2.3 $lt, $gt, $lte, $gte, $en, $ne, $in
    2.4 $regex
    2.5 $count()
    '''  
    
    #agg = col.aggregate([{"$match":{"age":{"$gt":20}}},{"$group":{"_id":"$age"}}]) ->$sum
    #for i in agg:
    #   print(i)

    '''
    1. $aggregate
    2. $match
    3. $group
    4. $sum
    '''

    #field_name_change = col.update_many({},{"$rename":{"age":"ages"}})
    #for i in col.find({},{"_id":0}):
    #    print(i)
    
    #incriments = col.update_many({},{"$inc":{"ages":100}})
    #print(incriments.modified_count)
    #for i in col.find({},{"_id":0}):
    #    print(i)

    #after_insertion = col.update_one({"name":"Chiru"},{"$set":{"age":20,"Branch":"EeE"}},upsert=True)
    #print(after_insertion.modified_count)

    #up_many = col.update_many({},{"$set":{"Branch":"EeE"}})
    #print(up_many.modified_count)

    #up_nd_delete_specfc_fild = col.update_many({},{"$unset":{"Branch":""}}) ->delete field
    #print(up_nd_delete_specfc_fild.modified_count)

    #c_date = col.update_one({"ages":100},{"$currentDate":{"datahora":{"$type":'date'}}},upsert=True)
    
    '''
    1. update_one
    2. update_many ->$set,$unset,$rename,$inc,$currentdate
    '''

    #-> delete field using $unset operation

    #-> delete document 
    ##db_col = client["test"]["test1"]
    #d_doc_one = db_col.delete_one({"name":"Chiru"})
    
    #d_doc_many = db_col.delete_many({"ages":{"$gt":122}})

    #d_all_doc = db_col.delete_many({})
    
    #->delete collection
    #d_col = db_col.drop() #db.test1.drop()

    #->delete database
    #client.drop_database('test') #db.dropDatabase()
    
    '''
    1. delete_one
    2. delete_many
    3. delete collection
    4. delete database
    '''
    
