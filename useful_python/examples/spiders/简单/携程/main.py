import requests
import json


if __name__ == "__main__":

    url = "https://flights.ctrip.com/itinerary/api/12808/products"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
        "Referer": "https://flights.ctrip.com/itinerary/oneway/BJS-CKG?date=2020-05-22",
        "Content-Type": "application/json"
    }
    body = {
        "flightWay": "Oneway",
        "classType": "ALL",
        "hasChild": False,
        "hasBaby": False,
        "searchIndex": 1,
        "date": "2020-05-22",
        "airportParams": [
            {
                "dcity": "BJS",
                "acity": "CKG",
                "dcityname": "北京",
                "acityname": "重庆",
                "date": "2020-05-22",
                "dcityid": 1,
                "acityid": 477
            }
        ],
    }
    ret = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
    json_content = json.loads(ret.text)
    lists = json_content.get('data', {}).get('routeList', [])

    print(len(lists))
    for item in lists:
        if len(item.get('legs')) >= 1:
            legs = item.get('legs')
            flight = legs[0].get('flight')
            # 航空名
            airline_name = "航空名: "+flight.get('airlineName')
            # 航线代码
            flight_number = "航线代码: "+flight.get('flightNumber')
            # 离开日期
            departure_date = "离开日期: "+flight.get('departureDate')
            # 到达日期
            arrival_date = "到达日期: "+flight.get('arrivalDate')
            # 离开站
            de_air_name = "离开站: "+flight.get('departureAirportInfo').get('airportName')
            # 到达站
            ar_air_name = "到达站: "+flight.get('arrivalAirportInfo').get('airportName')

            price = "价格: " + str(legs[0].get('cabins')[0].get("price").get("salePrice"))

            results = [airline_name, flight_number, departure_date, arrival_date,  de_air_name, ar_air_name, price]
            print("\t".join(results))
