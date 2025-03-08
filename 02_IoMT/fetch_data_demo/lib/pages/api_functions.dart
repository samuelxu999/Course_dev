// Importing necessary libraries and packages
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<String> getHeartRate(String startdate, String enddate) async {
  // build url for AWS API gateway endpoint: getHeartRate
  final url=Uri.parse('https://9xgokmzozd.execute-api.us-east-2.amazonaws.com/test/getHeartRate');
  final response = await http.post(url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8'
    },
    body: jsonEncode(<String,String>{
      "startdate": startdate,
      "enddate": enddate
    })
  );
  if(response.statusCode == 200) {
    // parse response data from backend side and return fetch data for UI
    Map<String,dynamic> mapbody = jsonDecode(response.body);
    return mapbody['body'];  
  }
  else{
    throw Exception('Fail to get data.');
  }
}

Future<String> saveHeartRate(String collect_date) async {
  // build url for AWS API gateway endpoint: saveHeartRate
  final url=Uri.parse('https://9xgokmzozd.execute-api.us-east-2.amazonaws.com/test/saveHeartRate');
  final response = await http.post(url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8'
    },
    body: jsonEncode(<String,String>{
      "collect_date": collect_date
    })
  );
  if(response.statusCode == 200) {
    // parse response results from backend side. 
    Map<String,dynamic> mapbody = jsonDecode(response.body);
    return mapbody['body'];  
  }
  else{
    throw Exception('Fail to save Fitbit data.');
  }
}